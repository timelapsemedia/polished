# Label partner landing page (EN + DE). Executed from gen.py (shared namespace).

LABEL_EN = '/mastering-for-labels/'
LABEL_DE = '/de/mastering-fuer-labels/'
LABEL_PAIR = {'en': LABEL_EN, 'de': LABEL_DE}
LABEL_DATE = '2026-10-21'
LABEL_MAIL_EN = 'mailto:polished.media@gmx.de?subject=Label%20partner%20rates'
LABEL_MAIL_DE = 'mailto:polished.media@gmx.de?subject=Label-Partnerpreise'


def label_offers(names):
    rows = [(names[0], 63), (names[1], 103), (names[2], 279), (names[3], 499)]
    return [{"@type": "Offer", "name": n, "price": str(p), "priceCurrency": "EUR",
             "priceSpecification": {"@type": "UnitPriceSpecification", "price": str(p), "priceCurrency": "EUR", "valueAddedTaxIncluded": True},
             "eligibleQuantity": {"@type": "QuantitativeValue", "minValue": 4, "unitText": "releases per year"}} for n, p in rows]


# ---------------------------------------------------------------- EN
LE_TITLE = 'Mastering for Record Labels: Fixed Partner Rates | Polished'
LE_FAQS = [
    ('Who gets label partner rates?', 'Independent labels with a release schedule of at least 4 releases per year. The rates are fixed: €63 per stereo single, €103 per stem single, €279 per EP (up to 5 tracks) and €499 per album (up to 10 tracks). All prices are final prices incl. 19% German VAT.'),
    ('How does payment work for labels?', 'Each release is either prepaid or invoiced after delivery, whichever suits your label. There is no subscription and no recurring fee; you pay per release at the partner rate.'),
    ('What if we release fewer than 4 records a year?', 'Then the regular packages apply: €79 per stereo single, €129 per stem single, €349 for an EP and €629 for an album. Artists with several singles can book a Single Series of 3 singles at €73 each. The audit and unlimited revisions are included either way.'),
    ('Do label releases get the same audit?', 'Yes. Every track gets the same written audio audit as a regular order: frequency balance against genre references, dynamics and loudness, stereo image and phase. Same process, same unlimited revisions, only the price per release is lower.'),
    ('Can you deliver vinyl and Bandcamp masters?', 'Yes. Every master comes as 24-bit WAV, 16-bit AIFF and 320 kbps MP3 with exports for Spotify, Apple Music and Bandcamp. A separate vinyl-ready master is available on request for album projects.'),
    ('Which genres do you master?', 'Black Metal, Death Metal, Doom and Gothic, plus Metalcore and Djent. Polished works only with heavy and dark music, so loudness and tone are judged against references from your subgenre, not against pop masters.'),
]
le_body = f'''{breadcrumb_html([('Home', f'{BASE}/'), ('Mastering for Labels', f'{BASE}{LABEL_EN}')])}
<header class="page-hero">
  <div class="wrap">
    <div class="eyebrow">For independent labels</div>
    <h1>Mastering for metal &amp; gothic <em>record labels</em></h1>
    <p class="lead"><strong>Independent labels with 4 or more releases a year get fixed mastering rates at Polished: €63 per single, €103 per stem single, €279 per EP and €499 per album, incl. VAT.</strong> Every track gets a written audio audit and unlimited revisions. Each release is prepaid or invoiced after delivery.</p>
    <div class="cta-row">
      <a href="{LABEL_MAIL_EN}" class="cta-btn" data-track="label-hero">Request label rates →</a>
      <a href="#lp-rates" class="cta-btn outline">See partner rates</a>
    </div>
    <p class="meta-line">By <a href="/#engineer">Tim Borchert</a>, mastering engineer · Updated October 2026</p>
  </div>
</header>
<section class="content-section" id="lp-rates" aria-labelledby="le-rates">
  <div class="wrap prose-wrap prose">
    <h2 id="le-rates">Label mastering rates: <em>fixed per release</em></h2>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Release</th><th>Label partner rate</th><th>Regular price</th><th>Delivery</th></tr></thead>
        <tbody>
          <tr><td>Single · stereo</td><td>€63</td><td>€79</td><td>48–72 h</td></tr>
          <tr><td>Single · stems (up to 6)</td><td>€103</td><td>€129</td><td>48–72 h</td></tr>
          <tr><td>EP · up to 5 tracks</td><td>€279 (€55.80 per track)</td><td>€349</td><td>5–7 days</td></tr>
          <tr><td>Album · up to 10 tracks</td><td>€499 (€49.90 per track)</td><td>€629</td><td>7–14 days</td></tr>
        </tbody>
      </table>
    </div>
    <p>All prices are final prices incl. 19% German VAT. Partner rates apply from 4 releases per year. There is no subscription: you pay per release, up front or on invoice after delivery. Full package details are on the <a href="/#bundles">pricing overview</a>, and a market comparison is in the <a href="/mastering-cost/">mastering cost guide</a>.</p>
  </div>
</section>
{sec('le-get', 'What your label and your bands <em>get</em>', """    <ul>
      <li><strong>A written audio audit per track:</strong> frequency balance against Black, Death, Doom and Gothic references, dynamics and loudness, stereo image and phase. Your bands see why each decision was made.</li>
      <li><strong>One consistent sound across your catalog:</strong> loudness and tone stay comparable from release to release, so a label sampler or playlist does not jump in level.</li>
      <li><strong>Album consistency:</strong> EPs and albums get loudness balance across tracks and optimized sequencing and transitions.</li>
      <li><strong>Every format:</strong> 24-bit WAV, 16-bit AIFF and 320 kbps MP3, with exports for Spotify, Apple Music and Bandcamp. Vinyl-ready master on request for albums.</li>
      <li><strong>Unlimited revisions:</strong> no extra cost, no time limit, on every release.</li>
    </ul>""", alt=True)}
{sec('le-how', 'How label mastering <em>works</em>', f"""    <ol>
      <li><strong>Tell us your release schedule.</strong> A short email with your label, genres and how many releases you plan per year is enough to unlock partner rates.</li>
      <li><strong>Send the mixes per release.</strong> Stereo mixdowns or stems, plus one or two reference tracks from the band's subgenre.</li>
      <li><strong>Audit, then master.</strong> Each track is analysed first; the written report and the master are delivered together.</li>
      <li><strong>Revise until it fits.</strong> The band or the label gives specific feedback, and the master is reworked until it is right.</li>
      <li><strong>Pay per release.</strong> Prepaid or on invoice after delivery.</li>
    </ol>
    <div class="cta-row" style="margin-top: 24px;"><a href="{LABEL_MAIL_EN}" class="cta-btn" data-track="label-how-cta">Request label rates →</a></div>""")}
{sec('le-genres', 'Genres for <em>label releases</em>', f"""    <p>Polished masters heavy and dark music only. Each genre has its own guide with typical mastering problems and loudness ranges:</p>
    <ul>
      {''.join(f'<li><a href="/{s}/">{n}</a></li>' for s, n in GENRES)}
    </ul>
    <p>How loud metal masters should be for streaming and Bandcamp is covered in the <a href="/metal-mastering-loudness/">loudness guide</a>; when stems make sense is in the <a href="/stem-mastering/">stem mastering guide</a>.</p>""", alt=True)}
<section class="content-section" aria-labelledby="le-faq">
  <div class="wrap prose-wrap">
    <h2 id="le-faq">Label mastering <em>FAQ</em></h2>
{faq_html(LE_FAQS)}
  </div>
</section>'''
le_schemas = [
    webpage_schema(LABEL_EN, LE_TITLE),
    breadcrumb_schema([('Home', f'{BASE}/'), ('Mastering for Labels', f'{BASE}{LABEL_EN}')]),
    {"@context": "https://schema.org", "@type": "Service", "@id": f"{BASE}{LABEL_EN}#service",
     "name": "Label partner mastering", "serviceType": "Audio mastering for record labels", "inLanguage": "en",
     "provider": BIZ, "areaServed": "Worldwide",
     "audience": {"@type": "BusinessAudience", "audienceType": "Independent record labels (from 4 releases per year)"},
     "offers": label_offers(['Label Partner – Stereo Single', 'Label Partner – Stem Single', 'Label Partner – EP (up to 5 tracks)', 'Label Partner – Album (up to 10 tracks)'])},
    faq_schema(LE_FAQS),
]
write(LABEL_EN, page(path=LABEL_EN, lang='en', title=LE_TITLE,
      description='Mastering for independent metal & gothic labels: fixed partner rates from 4 releases a year. €63 single, €279 EP, €499 album incl. VAT, audit included.',
      og_title='Mastering for record labels — Polished', body=le_body, schemas=le_schemas, counterpart=LABEL_PAIR))

# ---------------------------------------------------------------- DE
LD_TITLE = 'Mastering für Labels: feste Partnerpreise | Polished'
LD_FAQS = [
    ('Welche Labels bekommen Partnerpreise?', 'Unabhängige Labels mit mindestens 4 Releases pro Jahr. Die Preise sind fest: 63 € pro Stereo-Single, 103 € pro Stem-Single, 279 € pro EP (bis 5 Tracks) und 499 € pro Album (bis 10 Tracks). Alle Preise sind Endpreise inkl. 19 % USt.'),
    ('Wie wird bezahlt?', 'Jedes Release wird wahlweise vorab bezahlt oder nach Lieferung per Rechnung abgerechnet. Es gibt kein Abo und keine laufende Gebühr; bezahlt wird pro Release zum Partnerpreis.'),
    ('Was gilt bei weniger als 4 Releases im Jahr?', 'Dann gelten die regulären Pakete: 79 € pro Stereo-Single, 129 € pro Stem-Single, 349 € pro EP und 629 € pro Album. Für mehrere Singles gibt es die Single-Serie mit 3 Singles zu je 73 €. Audit und unbegrenzte Revisionen sind immer enthalten.'),
    ('Bekommen Label-Releases dasselbe Audit?', 'Ja. Jeder Track bekommt dasselbe schriftliche Audio-Audit wie ein regulärer Auftrag: Frequenzbalance im Vergleich zu Genre-Referenzen, Dynamik und Lautheit, Stereobild und Phase. Gleicher Ablauf, gleiche unbegrenzte Revisionen, nur der Preis pro Release ist niedriger.'),
    ('Liefert ihr auch Vinyl- und Bandcamp-Master?', 'Ja. Jeder Master kommt als 24-Bit-WAV, 16-Bit-AIFF und 320-kbps-MP3 mit Exporten für Spotify, Apple Music und Bandcamp. Ein eigener Vinyl-Master ist bei Album-Projekten auf Anfrage möglich.'),
    ('Welche Genres masterst du?', 'Black Metal, Death Metal, Doom und Gothic sowie Metalcore und Djent. Polished arbeitet nur mit harter und dunkler Musik; Lautheit und Klang werden an Referenzen aus dem jeweiligen Subgenre gemessen.'),
]
ld_body = f'''{breadcrumb_html([('Startseite', f'{BASE}/de/'), ('Mastering für Labels', f'{BASE}{LABEL_DE}')], 'Brotkrumen')}
<header class="page-hero">
  <div class="wrap">
    <div class="eyebrow">Für unabhängige Labels</div>
    <h1>Mastering für Metal- &amp; Gothic-<em>Labels</em></h1>
    <p class="lead"><strong>Unabhängige Labels mit mindestens 4 Releases im Jahr bekommen bei Polished feste Mastering-Preise: 63 € pro Single, 103 € pro Stem-Single, 279 € pro EP und 499 € pro Album, inkl. USt.</strong> Jeder Track bekommt ein schriftliches Audio-Audit und unbegrenzte Revisionen. Bezahlt wird pro Release, vorab oder auf Rechnung nach Lieferung.</p>
    <div class="cta-row">
      <a href="{LABEL_MAIL_DE}" class="cta-btn" data-track="de-label-hero">Label-Preise anfragen →</a>
      <a href="#lp-preise" class="cta-btn outline">Partnerpreise ansehen</a>
    </div>
    <p class="meta-line">Von <a href="/de/#tim">Tim Borchert</a>, Mastering Engineer · Stand: Oktober 2026</p>
  </div>
</header>
<section class="content-section" id="lp-preise" aria-labelledby="ld-preise">
  <div class="wrap prose-wrap prose">
    <h2 id="ld-preise">Label-Mastering Preise: <em>fest pro Release</em></h2>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Release</th><th>Label-Partnerpreis</th><th>Regulärer Preis</th><th>Lieferung</th></tr></thead>
        <tbody>
          <tr><td>Single · Stereo</td><td>63 €</td><td>79 €</td><td>48–72 Std.</td></tr>
          <tr><td>Single · Stems (bis 6)</td><td>103 €</td><td>129 €</td><td>48–72 Std.</td></tr>
          <tr><td>EP · bis 5 Tracks</td><td>279 € (55,80 € pro Track)</td><td>349 €</td><td>5–7 Tage</td></tr>
          <tr><td>Album · bis 10 Tracks</td><td>499 € (49,90 € pro Track)</td><td>629 €</td><td>7–14 Tage</td></tr>
        </tbody>
      </table>
    </div>
    <p>Alle Preise sind Endpreise inkl. 19 % USt. Die Partnerpreise gelten ab 4 Releases pro Jahr. Es gibt kein Abo: Bezahlt wird pro Release, vorab oder auf Rechnung nach Lieferung. Alle Pakete stehen in der <a href="/de/#preise">Preisübersicht</a>, ein Marktvergleich unter <a href="/de/mastering-kosten/">Was kostet Mastering?</a></p>
  </div>
</section>
{sec('ld-leistung', 'Was dein Label und deine Bands <em>bekommen</em>', """    <ul>
      <li><strong>Ein schriftliches Audio-Audit pro Track:</strong> Frequenzbalance im Vergleich zu Black-, Death-, Doom- und Gothic-Referenzen, Dynamik und Lautheit, Stereobild und Phase. Deine Bands sehen, warum welche Entscheidung getroffen wurde.</li>
      <li><strong>Ein einheitlicher Sound über den ganzen Katalog:</strong> Lautheit und Klang bleiben von Release zu Release vergleichbar, damit Label-Sampler und Playlists nicht im Pegel springen.</li>
      <li><strong>Album-Konsistenz:</strong> EPs und Alben bekommen eine abgestimmte Lautheit über alle Tracks und optimierte Übergänge.</li>
      <li><strong>Alle Formate:</strong> 24-Bit-WAV, 16-Bit-AIFF und 320-kbps-MP3 mit Exporten für Spotify, Apple Music und Bandcamp. Vinyl-Master für Alben auf Anfrage.</li>
      <li><strong>Unbegrenzte Revisionen:</strong> ohne Aufpreis und ohne Frist, bei jedem Release.</li>
    </ul>""", alt=True)}
{sec('ld-ablauf', 'So läuft Label-Mastering <em>ab</em>', f"""    <ol>
      <li><strong>Release-Plan schicken.</strong> Eine kurze Mail mit Label, Genres und geplanter Zahl an Releases pro Jahr reicht für die Partnerpreise.</li>
      <li><strong>Mixe pro Release senden.</strong> Stereo-Mixdowns oder Stems, dazu ein bis zwei Referenztracks aus dem Subgenre der Band.</li>
      <li><strong>Erst Audit, dann Master.</strong> Jeder Track wird zuerst analysiert; Bericht und Master kommen zusammen.</li>
      <li><strong>Revisionen, bis es passt.</strong> Band oder Label geben konkretes Feedback, der Master wird überarbeitet, bis er stimmt.</li>
      <li><strong>Bezahlung pro Release.</strong> Vorab oder auf Rechnung nach Lieferung.</li>
    </ol>
    <div class="cta-row" style="margin-top: 24px;"><a href="{LABEL_MAIL_DE}" class="cta-btn" data-track="de-label-how-cta">Label-Preise anfragen →</a></div>""")}
{sec('ld-genres', 'Genres für <em>Label-Releases</em>', f"""    <p>Polished mastert ausschließlich harte und dunkle Musik. Zu jedem Genre gibt es einen eigenen Ratgeber mit typischen Mastering-Problemen und Lautheitsbereichen:</p>
    <ul>
      {''.join(f'<li><a href="/de/{s}/">{n}</a></li>' for s, n in GENRES)}
    </ul>
    <p>Wie laut Metal für Streaming und Bandcamp gemastert werden sollte, steht im <a href="/de/metal-mastering-lautstaerke/">Lautstärke-Guide</a>; wann sich Stems lohnen, im <a href="/de/stem-mastering/">Ratgeber Stem-Mastering</a>.</p>""", alt=True)}
<section class="content-section" aria-labelledby="ld-faq">
  <div class="wrap prose-wrap">
    <h2 id="ld-faq">Mastering für Labels: <em>FAQ</em></h2>
{faq_html(LD_FAQS)}
  </div>
</section>'''
ld_schemas = [
    webpage_schema(LABEL_DE, LD_TITLE, lang='de'),
    breadcrumb_schema([('Startseite', f'{BASE}/de/'), ('Mastering für Labels', f'{BASE}{LABEL_DE}')]),
    {"@context": "https://schema.org", "@type": "Service", "@id": f"{BASE}{LABEL_DE}#service",
     "name": "Label-Partner-Mastering", "serviceType": "Audio-Mastering für Plattenlabels", "inLanguage": "de",
     "provider": BIZ, "areaServed": "Worldwide",
     "audience": {"@type": "BusinessAudience", "audienceType": "Unabhängige Plattenlabels (ab 4 Releases pro Jahr)"},
     "offers": label_offers(['Label-Partner – Stereo-Single', 'Label-Partner – Stem-Single', 'Label-Partner – EP (bis 5 Tracks)', 'Label-Partner – Album (bis 10 Tracks)'])},
    faq_schema(LD_FAQS),
]
write(LABEL_DE, page(path=LABEL_DE, lang='de', title=LD_TITLE,
      description='Mastering für unabhängige Metal- & Gothic-Labels: feste Partnerpreise ab 4 Releases im Jahr. 63 € Single, 279 € EP, 499 € Album inkl. USt., mit Audit.',
      og_title='Mastering für Labels — Polished', body=ld_body, schemas=ld_schemas, counterpart=LABEL_PAIR))
