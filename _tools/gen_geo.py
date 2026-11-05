# GEO building blocks (SISTRIX "Citation Worthiness", 22.10.2026; see _tools/GEO-MERKMALE.md).
# Executed from gen.py (shared namespace). page(..., typ=...) calls geo_ergaenzen() for every generated page:
#   - table of contents "On this page" / "Auf dieser Seite" at the end of the hero, links to every H2 (ids added if missing)
#   - author box with Tim's real portrait at the end of <main>
#   - visible "Last updated" date (+ %%STAND%% token in hero meta lines) and dateModified in the schemas
#   - Article schema with author/publisher/dates on article pages (typ='article'); tool pages (typ='produkt')
#     keep SoftwareApplication/Product and only get author + dateModified
# The date is the real last content change: _tools/seitenstand.json stores per page a hash of the visible text
# (title, description, body without these blocks). Only when that hash changes does the date move to the build day.
# New pages are seeded from `git log` of the page file. Commit seitenstand.json together with the pages.
import datetime, hashlib, re, subprocess, unicodedata

STAND_DATEI = os.path.join(ROOT, '_tools', 'seitenstand.json')
HEUTE = datetime.date.today().isoformat()
MONATE_EN = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
             'November', 'December']
try:
    with open(STAND_DATEI, encoding='utf-8') as _f:
        SEITENSTAND = json.load(_f)
except FileNotFoundError:
    SEITENSTAND = {}

PERSON_TIM = {"@type": "Person", "@id": f"{BASE}/#tim-borchert", "name": "Tim Borchert",
              "jobTitle": "Mastering Engineer", "image": f"{BASE}/tim-borchert-portrait.jpg"}
PUBLISHER = {"@type": "Organization", "@id": f"{BASE}/#business", "name": "Polished Mastering",
             "url": f"{BASE}/", "logo": f"{BASE}/assets/icon-512.png"}


def person_tim(lang):
    return dict(PERSON_TIM, url=f"{BASE}/de/#tim" if lang == 'de' else f"{BASE}/#engineer")


def _datei(path):
    rel = path.strip('/')
    return (rel + '/index.html') if path.endswith('/') else rel


def git_datum(path, erst=False):
    """Commit date (YYYY-MM-DD) of the last (or first) commit touching the page file; None without git/history."""
    args = ['git', '-C', ROOT, 'log', '--format=%cs', '--', _datei(path)]
    if not erst:
        args.insert(4, '-1')
    try:
        out = subprocess.run(args, capture_output=True, text=True, timeout=30).stdout.split()
    except (OSError, subprocess.SubprocessError):
        return None
    return (out[-1] if erst else out[0]) if out else None


def inhalt_hash(title, description, body):
    text = html.unescape(re.sub(r'<[^>]+>', ' ', title + ' ' + description + ' ' + body))
    return hashlib.sha1(' '.join(text.split()).encode('utf-8')).hexdigest()[:16]


def seitenstand(path, title, description, body):
    """(datePublished, dateModified) for a page; moves dateModified only on a real text change."""
    h = inhalt_hash(title, description, body)
    e = SEITENSTAND.get(path)
    if e is None:
        mod = git_datum(path) or HEUTE
        e = {'veroeffentlicht': git_datum(path, erst=True) or mod, 'geaendert': mod, 'hash': h}
    elif e['hash'] != h:
        e = dict(e, geaendert=HEUTE, hash=h)
    if SEITENSTAND.get(path) != e:
        SEITENSTAND[path] = e
        with open(STAND_DATEI, 'w', encoding='utf-8') as f:
            json.dump(dict(sorted(SEITENSTAND.items())), f, ensure_ascii=False, indent=1)
            f.write('\n')
    return e['veroeffentlicht'], e['geaendert']


def datum_text(iso, lang):
    j, m, t = (int(x) for x in iso.split('-'))
    return f'{t:02d}.{m:02d}.{j}' if lang == 'de' else f'{t} {MONATE_EN[m - 1]} {j}'


def slug(text):
    t = text.lower().replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')
    t = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '-', t).strip('-')[:60] or 'abschnitt'


def h2_mit_ids(body):
    """Gives every <h2> a stable id (slug of its text if it has none). Returns (body, [(id, plain text)])."""
    vergeben = set(re.findall(r'\sid="([^"]+)"', body))
    eintraege = []

    def ersetze(m):
        attrs, inner = m.group(1) or '', m.group(2)
        text = ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', inner)).split())
        mid = re.search(r'\sid="([^"]+)"', attrs)
        if mid:
            hid = mid.group(1)
        else:
            basis = hid = slug(text)
            n = 2
            while hid in vergeben:
                hid, n = f'{basis}-{n}', n + 1
            vergeben.add(hid)
            attrs = f' id="{hid}"' + attrs
        eintraege.append((hid, text))
        return f'<h2{attrs}>{inner}</h2>'

    body = re.sub(r'<h2(\s[^>]*)?>(.*?)</h2>', ersetze, body, flags=re.S)
    return body, eintraege


def toc_html(eintraege, lang):
    titel = 'Auf dieser Seite' if lang == 'de' else 'On this page'
    lis = '\n'.join(f'        <li><a href="#{hid}">{html.escape(text, quote=False)}</a></li>' for hid, text in eintraege)
    return f'''    <nav class="toc" aria-label="{titel}">
      <p class="toc-title">{titel}</p>
      <ol>
{lis}
      </ol>
    </nav>'''


AUTOR_TEXT = {
    'en': dict(article='Written by', produkt='Made by', home='Mastered by', link='/#engineer', mehr='More about Tim',
               stand='Last updated', alt='Portrait of Tim Borchert, mastering engineer at Polished',
               bio='Tim Borchert masters every track at Polished personally. He studies Systematic Musicology and Media Studies '
                   'at the University of Hamburg. Before that he trained for two years as an event technician, mixed a rock band '
                   'live and released his own music on labels in Mexico, India and Turkey.',
               tools='Under the label Code Chaos Audio he also builds production tools for bands.'),
    'de': dict(article='Geschrieben von', produkt='Entwickelt von', home='Gemastert von', link='/de/#tim', mehr='Mehr über Tim',
               stand='Zuletzt aktualisiert', alt='Porträt von Tim Borchert, Mastering Engineer bei Polished',
               bio='Tim Borchert mastert jeden Track bei Polished persönlich. Er studiert Systematische Musikwissenschaft und '
                   'Medienwissenschaft an der Universität Hamburg. Davor hat er zwei Jahre eine Ausbildung zur Fachkraft für '
                   'Veranstaltungstechnik gemacht, eine Rockband live abgemischt und eigene Musik auf Labels in Mexiko, Indien '
                   'und der Türkei veröffentlicht.',
               tools='Unter dem Label Code Chaos Audio baut er außerdem Produktions-Tools für Bands.'),
}


def autorbox_html(lang, typ, geaendert):
    a = AUTOR_TEXT[lang]
    bio = a['bio'] + (' ' + a['tools'] if typ == 'produkt' else '')
    return f'''<section class="author-section" aria-label="{a[typ]} Tim Borchert">
  <div class="wrap">
    <aside class="author-box">
      <picture><source srcset="/assets/tim-borchert-160.webp" type="image/webp"><img src="/assets/tim-borchert-160.jpg" alt="{a['alt']}" width="80" height="80" loading="lazy" decoding="async"></picture>
      <div>
        <p class="author-label">{a[typ]}</p>
        <p class="author-name"><a href="{a['link']}">Tim Borchert</a></p>
        <p class="author-bio">{bio} <a href="{a['link']}">{a['mehr']} →</a></p>
        <p class="author-meta">{a['stand']}: <time datetime="{geaendert}">{datum_text(geaendert, lang)}</time></p>
      </div>
    </aside>
  </div>
</section>'''


def _typen(s):
    t = s.get('@type')
    return set(t) if isinstance(t, list) else {t}


def geo_ergaenzen(path, lang, title, description, body, schemas, typ, og_src):
    """Adds TOC, author box, dates and Article/author schema. typ: 'article' | 'produkt' | 'home'."""
    veroeffentlicht, geaendert = seitenstand(path, title, description, body)
    body = body.replace('%%STAND%%', f'<time datetime="{geaendert}">{datum_text(geaendert, lang)}</time>')
    body, eintraege = h2_mit_ids(body)
    if typ in ('article', 'produkt'):
        m = re.search(r'</h1>.*?(\n  </div>\n</header>)', body, re.S)
        assert m and len(eintraege) >= 3, f'{path}: hero end or H2s not found for the table of contents'
        body = body[:m.start(1)] + '\n' + toc_html(eintraege, lang) + body[m.start(1):]
    body += '\n' + autorbox_html(lang, typ, geaendert)
    schemas = [dict(s) for s in schemas]
    for s in schemas:
        typen = _typen(s)
        if 'dateModified' in s or typen & {'WebPage', 'CollectionPage', 'Article'}:
            s['dateModified'] = geaendert
        if 'Article' in typen:
            s.setdefault('datePublished', veroeffentlicht)
            s['author'] = person_tim(lang)
            s['publisher'] = PUBLISHER
        if 'SoftwareApplication' in typen:
            s['author'] = person_tim(lang)
            s['dateModified'] = geaendert
    if typ == 'article' and not any('Article' in _typen(s) for s in schemas):
        h1 = re.search(r'<h1[^>]*>(.*?)</h1>', body, re.S).group(1)
        schemas.append({"@context": "https://schema.org", "@type": "Article", "@id": f"{BASE}{path}#article",
                        "headline": ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', h1)).split()),
                        "description": description, "inLanguage": lang, "image": f"{BASE}{og_src}",
                        "datePublished": veroeffentlicht, "dateModified": geaendert,
                        "author": person_tim(lang), "publisher": PUBLISHER,
                        "mainEntityOfPage": {"@id": f"{BASE}{path}#webpage"}})
    return body, schemas


# ---------------------------------------------------------------- tables with real data (header row <th>)
# Loudness orientation per genre page: same values as the loudness guide tables (gen.py LG / gen_de.py LGD).
LAUT = {
    'en': {'black-metal-mastering': [('Black Metal', 'around -10 to -7 LUFS', 'Cymbal wash and harshness in blast sections')],
           'death-metal-mastering': [('Death Metal', 'around -9 to -6 LUFS', 'Snare crack and double-kick definition')],
           'doom-gothic-mastering': [('Doom / Sludge', 'around -11 to -8 LUFS', 'Sustained sub energy and loss of contrast'),
                                     ('Gothic Metal / Gothic Rock', 'around -12 to -8 LUFS', 'Dynamics between quiet and heavy sections')],
           'metalcore-djent-mastering': [('Metalcore / Djent', 'around -8 to -6 LUFS', 'Low end below 100 Hz eating headroom in breakdowns')]},
    'de': {'black-metal-mastering': [('Black Metal', 'etwa -10 bis -7 LUFS', 'Beckenteppich und Schärfe in Blast-Passagen')],
           'death-metal-mastering': [('Death Metal', 'etwa -9 bis -6 LUFS', 'Crack der Snare und Definition der Double-Bass')],
           'doom-gothic-mastering': [('Doom / Sludge', 'etwa -11 bis -8 LUFS', 'Stehende Sub-Energie und Verlust von Kontrast'),
                                     ('Gothic Metal / Gothic Rock', 'etwa -12 bis -8 LUFS', 'Dynamik zwischen leisen und schweren Teilen')],
           'metalcore-djent-mastering': [('Metalcore / Djent', 'etwa -8 bis -6 LUFS', 'Low End unter 100 Hz frisst in Breakdowns den Headroom')]},
}


def laut_tabelle(slug_, lang):
    if lang == 'de':
        h, kopf = 'Lautheit <em>im Überblick</em>', ('Stil', 'Übliche integrierte Lautheit', 'Was die Lautheit zuerst begrenzt')
        extra = [('Streaming-Wiedergabe', 'etwa -14 LUFS (Spotify, YouTube, Tidal, Amazon Music), etwa -16 LUFS (Apple Music), Bandcamp ohne Normalisierung', 'Lautere Master werden leiser gedreht'),
                 ('True Peak', 'unter -1 dBTP, bei Mastern lauter als -14 LUFS unter -2 dBTP', 'Spitzen steigen bei der Kodierung (Empfehlung von Spotify)')]
        note = 'Orientierungswerte aus der Mastering-Praxis, keine Zielwerte. Details und Quellen im <a href="/de/metal-mastering-lautstaerke/">Lautstärke-Guide</a>.'
    else:
        h, kopf = 'Loudness <em>at a glance</em>', ('Style', 'Common integrated loudness', 'What limits loudness first')
        extra = [('Streaming playback', 'about -14 LUFS (Spotify, YouTube, Tidal, Amazon Music), about -16 LUFS (Apple Music), no normalization on Bandcamp', 'Louder masters are turned down'),
                 ('True peak', 'below -1 dBTP, below -2 dBTP for masters louder than -14 LUFS', 'Peaks rise during lossy encoding (Spotify recommendation)')]
        note = 'Orientation values from mastering practice, not targets. Details and sources in the <a href="/metal-mastering-loudness/">loudness guide</a>.'
    rows = '\n'.join(f'          <tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in LAUT[lang][slug_] + extra)
    return f'''
    <h3>{h}</h3>
    <div class="table-wrap">
      <table>
        <thead><tr><th scope="col">{kopf[0]}</th><th scope="col">{kopf[1]}</th><th scope="col">{kopf[2]}</th></tr></thead>
        <tbody>
{rows}
        </tbody>
      </table>
    </div>
    <p class="table-note">{note}</p>'''


# Package overview (same figures as the price cards on / and /de/ and as ANGEBOTE in gen.py).
PAKETE = {
    'en': [('Single · stereo', '1 track', '€79', '48–72 h'),
           ('Single · stems', '1 track, up to 6 stems', '€129', '48–72 h'),
           ('EP', 'up to 5 tracks', '€349', '5–7 days'),
           ('Album', 'up to 10 tracks, vinyl master on request', '€629', '7–14 days'),
           ('Single Series', '3 singles, mastered as they are released over up to 12 months', '€73 per single', '48–72 h per single'),
           ('Stem EP', 'up to 5 tracks, up to 6 stems each', '€549', '5–7 days'),
           ('Label Partner', 'from 4 releases per year', 'single €63 · stem single €103 · EP €279 · album €499', 'as per release')],
    'de': [('Single · Stereo', '1 Track', '79 €', '48–72 Std.'),
           ('Single · Stems', '1 Track, bis zu 6 Stems', '129 €', '48–72 Std.'),
           ('EP', 'bis 5 Tracks', '349 €', '5–7 Tage'),
           ('Album', 'bis 10 Tracks, Vinyl-Master auf Anfrage', '629 €', '7–14 Tage'),
           ('Single-Serie', '3 Singles, gemastert, wenn sie erscheinen, über bis zu 12 Monate', '73 € pro Single', '48–72 Std. pro Single'),
           ('Stem-EP', 'bis 5 Tracks, bis zu 6 Stems pro Track', '549 €', '5–7 Tage'),
           ('Label-Partner', 'ab 4 Releases pro Jahr', 'Single 63 € · Stem-Single 103 € · EP 279 € · Album 499 €', 'je nach Release')],
}


def paket_tabelle(lang, cls='table-wrap'):
    kopf = ('Paket', 'Umfang', 'Preis inkl. 19 % USt.', 'Lieferzeit') if lang == 'de' else ('Package', 'Scope', 'Price incl. 19% VAT', 'Delivery')
    note = ('Jedes Paket enthält das schriftliche Audio-Audit, Exporte für Streaming und Bandcamp und unbegrenzte Revisionen.'
            if lang == 'de' else 'Every package includes the written audio audit, streaming and Bandcamp exports and unlimited revisions.')
    rows = '\n'.join(f'          <tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in PAKETE[lang])
    return f'''    <div class="{cls}">
      <table>
        <caption>{"Alle Pakete im Vergleich" if lang == "de" else "All packages compared"}</caption>
        <thead><tr>{"".join(f'<th scope="col">{k}</th>' for k in kopf)}</tr></thead>
        <tbody>
{rows}
        </tbody>
      </table>
    </div>
    <p class="table-note">{note}</p>'''


def startseite_tabelle():
    """index.html is hand-edited: only the block between the geo markers is (re)written from PAKETE['en']."""
    datei = os.path.join(ROOT, 'index.html')
    with open(datei, encoding='utf-8') as f:
        s = f.read()
    a, b = '<!-- geo:pakete -->', '<!-- /geo:pakete -->'
    assert s.count(a) == 1 and s.count(b) == 1, 'index.html: geo:pakete markers missing'
    neu = s[:s.index(a) + len(a)] + '\n' + paket_tabelle('en', 'table-wrap pkg-compare') + '\n    ' + s[s.index(b):]
    if neu != s:
        with open(datei, 'w', encoding='utf-8') as f:
            f.write(neu)
        print('wrote', datei)


def sitemap_lastmod():
    """sitemap.xml: lastmod of every generated page = its dateModified (seitenstand.json)."""
    datei = os.path.join(ROOT, 'sitemap.xml')
    with open(datei, encoding='utf-8') as f:
        s = f.read()

    def ersetze(m):
        e = SEITENSTAND.get(m.group(1).replace(BASE, '') or '/')
        return m.group(0) if not e else f'<loc>{m.group(1)}</loc>\n    <lastmod>{e["geaendert"]}</lastmod>'
    neu = re.sub(r'<loc>([^<]+)</loc>\s*<lastmod>[^<]*</lastmod>', ersetze, s)
    if neu != s:
        with open(datei, 'w', encoding='utf-8') as f:
            f.write(neu)
        print('wrote', datei)
