# Measured loudness data pages (Grok #72, 12.11.2026): /metal-loudness-data/ + /de/metal-lautheit-daten/.
# Executed from gen.py (shared namespace). Text and tables: _tools/daten/*.md (see daten.py), never edited by hand here.

DATA_EN = '/metal-loudness-data/'
DATA_DE = '/de/metal-lautheit-daten/'
DATA_PAIR = {'en': DATA_EN, 'de': DATA_DE}

DATA_UI = {
    'en': dict(home='Home', guide=('Loudness Guide', '/metal-mastering-loudness/'),
               crumb='Metal Loudness Data', eyebrow='Data · Loudness',
               meta='By <a href="/#engineer">Tim Borchert</a>, mastering engineer, Systematic Musicology and Media Studies student (University of Hamburg) · Last updated: %%STAND%%',
               answer='Short answer', cta='Request Audio Audit →', contact='/#contact',
               variables=[('Integrated loudness', 'LUFS', 'ITU-R BS.1770 integrated loudness per track; median and 25th to 75th percentile per genre'),
                          ('Dynamic range (DR)', 'dB', 'DR database method: second-highest peak against the loudest 20 % of RMS blocks, per channel, averaged'),
                          ('Loudness range (LRA)', 'LU', 'EBU R 128 loudness range'),
                          ('Peak-to-loudness ratio (PLR)', 'dB', 'true peak minus integrated loudness'),
                          ('Side/mid ratio', 'dB', 'energy of the side signal against the mid signal'),
                          ('Correlation below 150 Hz', None, 'phase correlation of the low end, 1.00 = mono'),
                          ('Tonal balance relative to 1 kHz', 'dB', 'third-octave spectrum, grouped into five bands, relative to the 1 kHz band')],
               keywords=['metal mastering', 'LUFS', 'loudness', 'dynamic range', 'black metal', 'DSBM', 'doom metal', 'gothic', 'industrial metal']),
    'de': dict(home='Startseite', guide=('Lautstärke-Guide', '/de/metal-mastering-lautstaerke/'),
               crumb='Metal-Lautheit: Messdaten', eyebrow='Daten · Lautheit',
               meta='Von <a href="/de/#tim">Tim Borchert</a>, Mastering Engineer, Student der Systematischen Musikwissenschaft und Medienwissenschaft (Universität Hamburg) · Zuletzt aktualisiert: %%STAND%%',
               answer='Kurze Antwort', cta='Audio-Audit anfragen →', contact='/de/#kontakt',
               variables=[('Integrierte Lautheit', 'LUFS', 'integrierte Lautheit nach ITU-R BS.1770 je Track; Median und 25. bis 75. Perzentil je Genre'),
                          ('Dynamikwert (DR)', 'dB', 'Methode der DR-Datenbank: zweithöchster Spitzenwert gegen die lautesten 20 % der RMS-Blöcke, je Kanal, gemittelt'),
                          ('Lautheitsumfang (LRA)', 'LU', 'Loudness Range nach EBU R 128'),
                          ('Peak-to-Loudness-Ratio (PLR)', 'dB', 'True Peak minus integrierte Lautheit'),
                          ('Side/Mid-Verhältnis', 'dB', 'Energie des Seitensignals gegen das Mittensignal'),
                          ('Korrelation unter 150 Hz', None, 'Phasenkorrelation im Low End, 1,00 = mono'),
                          ('Tonale Balance relativ zu 1 kHz', 'dB', 'Terzspektrum, in fünf Bänder gruppiert, relativ zum 1-kHz-Band')],
               keywords=['Metal-Mastering', 'LUFS', 'Lautheit', 'Dynamik', 'Black Metal', 'DSBM', 'Doom Metal', 'Gothic', 'Industrial Metal']),
}
# The free mix audit only exists on branch conversion-2027 (not live on main): on main the texts point to the
# existing audio audit (included in every package) instead. No price or offer is added here. Each phrase must exist.
DATA_ERSATZ = {
    'en': [('the same one behind the free mix audit', 'the same one behind the Polished audio audit'),
           ('If you want those numbers for your own mix, the free mix audit measures it against this corpus and sends a written report. [Request a free mix audit](/#audit).',
            'If you want those numbers for your own mix, the audio audit in every Polished package measures it against this corpus, and you get a written report. [Request an audio audit](/#contact).')],
    'de': [('derselbe wie im kostenlosen Mix-Audit', 'derselbe wie im Polished-Audio-Audit'),
           ('Wenn du diese Werte für deinen eigenen Mix willst: Der kostenlose Mix-Audit misst ihn gegen diesen Korpus und schickt einen schriftlichen Bericht. [Kostenlosen Mix-Audit anfragen](/de/#audit).',
            'Wenn du diese Werte für deinen eigenen Mix willst: Das Audio-Audit in jedem Polished-Paket misst ihn gegen diesen Korpus, und du bekommst einen schriftlichen Bericht. [Audio-Audit anfragen](/de/#kontakt).')],
}
# Titles shortened to <= 60 characters (Tim's SEO rule); the frontmatter titles of the sources were 72-78 characters.
DATA_TITEL = {'en': 'Metal Loudness Data 2026: LUFS & DR of Real Releases',
              'de': 'Metal-Lautheit 2026: LUFS und DR echter Releases'}
DATA_TECHNIQUE = 'ITU-R BS.1770 integrated loudness, DR database method, third-octave spectrum'


def daten_seite(lang):
    u = DATA_UI[lang]
    meta, intro, sections = datenseite_lesen(f'seite_polished_{lang}.md', f'tabellen_polished_{lang}.md', DATA_ERSATZ[lang])
    path = meta['url']
    assert path == DATA_PAIR[lang], path
    home = '/de/' if lang == 'de' else '/'
    crumbs = [(u['home'], f'{BASE}{home}'), (u['guide'][0], f'{BASE}{u["guide"][1]}'), (u['crumb'], f'{BASE}{path}')]
    assert len(intro) == 2 and intro[1][1].startswith('**'), f'{path}: intro = lead + short answer expected'
    kurz = md_inline(intro[1][1])
    secs, faqs = [], []
    for i, (titel, bloecke) in enumerate(sections):
        if 'FAQ' in titel or 'Häufige Fragen' in titel:
            faqs, rest = md_faq(bloecke)
            assert len(faqs) >= 4, f'{path}: FAQ not found'
            weiter = '\n'.join(md_block_html(b) for b in rest)
            if lang == 'de':  # Arbeitsliste B: Datenseite -> /de/ mit Anker „Metal & Gothic Mastering“
                weiter = weiter.replace('</p>', ' · <a href="/de/">Metal &amp; Gothic Mastering</a></p>', 1)
            secs.append(f'''<section class="content-section{" alt" if i % 2 else ""}" aria-labelledby="{slug(titel)}">
  <div class="wrap prose-wrap">
    <h2 id="{slug(titel)}">{md_inline(titel)}</h2>
{faq_html(faqs)}
    <div class="prose">
{weiter}
    </div>
  </div>
</section>''')
        else:
            inner = '\n'.join(md_block_html(b) for b in bloecke)
            secs.append(sec(slug(titel), md_inline(titel), inner, alt=bool(i % 2)))
    body = f'''{breadcrumb_html(crumbs, 'Brotkrumen' if lang == 'de' else 'Breadcrumb')}
<header class="page-hero">
  <div class="wrap">
    <div class="eyebrow">{u["eyebrow"]}</div>
    <h1>{html.escape(meta["h1"], quote=False)}</h1>
    <p class="lead">{md_inline(intro[0][1])}</p>
    <div class="answer-box"><div class="label">{u["answer"]}</div><p>{kurz_ohne_label(kurz)}</p></div>
    <div class="cta-row">
      <a href="{u["contact"]}" class="cta-btn" data-track="{lang}-data-hero">{u["cta"]}</a>
    </div>
    <p class="meta-line">{u["meta"]}</p>
  </div>
</header>
''' + '\n'.join(secs)
    url = f'{BASE}{path}'
    dataset = {"@context": "https://schema.org", "@type": "Dataset", "@id": f"{url}#dataset",
               "name": meta['h1'], "description": meta['description'], "url": url, "inLanguage": lang,
               "creator": {"@type": "Person", "@id": f"{BASE}/#tim-borchert", "name": "Tim Borchert"},
               "publisher": BIZ, "copyrightHolder": BIZ,
               "license": {"@type": "CreativeWork", "name": "© Polished Mastering, all rights reserved"},
               "isAccessibleForFree": True, "keywords": u['keywords'],
               "measurementTechnique": DATA_TECHNIQUE, "temporalCoverage": "2026",
               "dateModified": TODAY,  # replaced by the real page date in geo_ergaenzen()
               "variableMeasured": [dict({"@type": "PropertyValue", "name": n, "description": d}, **({"unitText": e} if e else {}))
                                    for n, e, d in u['variables']],
               "isPartOf": {"@id": f"{url}#webpage"}}
    schemas = [webpage_schema(path, DATA_TITEL[lang], lang=lang), breadcrumb_schema(crumbs), dataset, faq_schema(faqs)]
    return page(path=path, lang=lang, title=DATA_TITEL[lang], description=meta['description'], og_title=meta['h1'],
                body=body, schemas=schemas, counterpart=DATA_PAIR, og_type='article', typ='article')


for _l in ('en', 'de'):
    write(DATA_PAIR[_l], daten_seite(_l))
