# Price / cost landing pages (DE primary, EN counterpart). Executed from gen.py (shared namespace).

COST_DE = '/de/mastering-kosten/'
COST_EN = '/mastering-cost/'
COST_PAIR = {'en': COST_EN, 'de': COST_DE}

# ---------------------------------------------------------------- DE
CD_TITLE = 'Mastering Kosten & Preise 2026: Was kostet Mastering? | Polished'
CD_FAQS = [
    ('Was kostet professionelles Mastering?', 'Professionelles Mastering kostet in Deutschland grob zwischen 50 und 150 € pro Track, bei renommierten Studios auch 200 € und mehr. Automatische KI-Dienste sind deutlich günstiger, liefern aber keine individuelle Analyse. Bei Polished kostet Stereo-Mastering 79 € pro Track inkl. 19 % USt., inklusive schriftlichem Audio-Audit und unbegrenzten Revisionen.'),
    ('Was kostet es, einen Song mastern zu lassen?', 'Für einen einzelnen Song (Stereo-Mastering) zahlst du bei Polished 79 € inkl. USt., mit Stems 129 €. Darin enthalten sind ein schriftliches Audio-Audit, Exporte für Streaming und Bandcamp, Lieferung in 48–72 Stunden und unbegrenzte Revisionen. Wer drei Singles zusammen bucht, zahlt 73 € pro Single.'),
    ('Was kostet Mastering für eine EP oder ein Album?', 'Bei Polished kostet eine EP mit bis zu 5 Tracks 349 € (46 € günstiger als 5 Singles) und ein Album mit bis zu 10 Tracks 629 € (161 € günstiger als 10 Singles). Beide Pakete enthalten ein Audit pro Track und einen Konsistenz-Durchgang, damit das Release wie aus einem Guss klingt.'),
    ('Was kostet Stem-Mastering?', 'Stem-Mastering ist aufwendiger als Stereo-Mastering, weil mehrere Spurgruppen (z. B. Drums, Bass, Gitarren, Vocals) einzeln bearbeitet werden. Bei Polished kostet es 129 € pro Track mit bis zu 6 Stems, die Stem-EP mit bis zu 5 Tracks 549 €. Wie du Stems richtig exportierst, steht im <a href="/de/stem-mastering/">Ratgeber Stem-Mastering</a>.'),
    ('Was kostet Vinyl-Mastering?', 'Vinyl braucht eine eigene Fassung mit mehr Dynamik, monokompatiblem Bass und kontrollierten Zischlauten. Viele Studios berechnen dafür einen Aufpreis pro Seite oder Track. Bei Polished ist ein Vinyl-Master für Album-Projekte auf Anfrage möglich; sprich es bei der Anfrage an, dann ist es im Angebot enthalten.'),
    ('Was kosten Mix und Mastering zusammen?', 'Mixing ist deutlich aufwendiger als Mastering und kostet bei Studios grob 100 bis 300 € pro Song, je nach Spurenzahl und Studio. Zusammen mit dem Mastering liegst du für einen Song also meist bei etwa 150 bis 450 €. Polished bietet nur Mastering an (79 € pro Song inkl. USt.); das Audio-Audit zeigt vorher, ob dein Mix bereit fürs Mastering ist.'),
    ('Sind Revisionen im Preis enthalten?', 'Bei vielen Anbietern sind nur ein oder zwei Korrekturrunden enthalten, weitere kosten extra. Bei Polished sind Revisionen in jedem Paket unbegrenzt und ohne Zeitlimit enthalten.'),
    ('Lohnt sich KI-Mastering statt eines Engineers?', 'KI-Mastering ist günstig und schnell, wendet aber ein Standard-Profil auf deinen Mix an, ohne zu verstehen, was dein Genre braucht oder was im Mix nicht stimmt. Für Demos kann das reichen. Für ein Release, das neben anderen Veröffentlichungen bestehen soll, lohnt sich ein Engineer, der deinen Mix analysiert und Rückfragen beantwortet.'),
    ('Bietet Polished auch Mixing an?', 'Nein. Polished ist auf Mastering spezialisiert. Wenn das Audio-Audit zeigt, dass der Mix selbst noch Arbeit braucht, bekommst du einen ehrlichen Hinweis und auf Wunsch eine Empfehlung für einen Mixing-Engineer.'),
]
cd_body = f'''{breadcrumb_html([('Startseite', f'{BASE}/de/'), ('Mastering Kosten', f'{BASE}{COST_DE}')], 'Brotkrumen')}
<header class="page-hero">
  <div class="wrap">
    <div class="eyebrow">Preise · Kosten · Vergleich</div>
    <h1>Was kostet <em>Mastering?</em></h1>
    <p class="lead"><strong>Kurze Antwort: Professionelles Mastering kostet in Deutschland meist zwischen 50 und 150 € pro Track.</strong> KI-Dienste sind günstiger, renommierte Studios teurer. Bei Polished kostet ein Song 79 € inkl. USt., eine EP 349 € und ein Album 629 €, jeweils mit schriftlichem Audio-Audit und unbegrenzten Revisionen.</p>
    <div class="cta-row">
      <a href="/de/#kontakt" class="cta-btn" data-track="de-cost-hero">Festpreis-Angebot anfragen →</a>
      <a href="#preise-polished" class="cta-btn outline">Preise ansehen</a>
    </div>
    <p class="meta-line">Von <a href="/de/#tim">Tim Borchert</a>, Mastering Engineer · Stand: Oktober 2026 · Alle Preise Endpreise inkl. 19 % USt.</p>
  </div>
</header>
{sec('cd-markt', 'Mastering-Preise <em>im Vergleich</em>', """    <p>Die Spanne ist groß, weil sehr unterschiedliche Leistungen unter „Mastering“ verkauft werden. Grobe Richtwerte pro Track:</p>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Anbieter</th><th>Typischer Preis pro Track</th><th>Was du bekommst</th></tr></thead>
        <tbody>
          <tr><td>KI- / Automatik-Mastering</td><td>wenige Euro oder Monatsabo</td><td>Algorithmus wendet Lautheit und EQ an, keine Analyse deines Mixes, keine Rückfragen</td></tr>
          <tr><td>Freelancer-Plattformen</td><td>etwa 15–60 €</td><td>Stark schwankende Qualität, oft ohne Spezialisierung auf dein Genre</td></tr>
          <tr><td>Spezialisierte Mastering-Studios</td><td>etwa 50–150 €</td><td>Persönlicher Engineer, Revisionen, Erfahrung mit deinem Genre</td></tr>
          <tr><td>Renommierte Studios</td><td>etwa 100–300 € und mehr</td><td>Bekannte Namen und Räume, oft Aufpreis für Stems, Vinyl und Express</td></tr>
        </tbody>
      </table>
    </div>
    <p class="table-note">Richtwerte nach öffentlich einsehbaren Preislisten, Stand Oktober 2026. Einzelne Anbieter weichen ab.</p>
    <p>Der günstigste Weg ist nicht automatisch der billigste: Ein Master, der auf Spotify verzerrt oder neben anderen Releases dünn klingt, kostet dich am Ende mehr als ein sauberer Master.</p>""")}
<section class="content-section alt" id="preise-polished" aria-labelledby="cd-polished">
  <div class="wrap">
    <h2 id="cd-polished">Mastering-Preise <em>bei Polished</em></h2>
{PRICES_DE}
    <div class="table-wrap" style="margin-top: 32px;">
      <table>
        <thead><tr><th>Bundle / Rate</th><th>Preis</th><th>Ersparnis</th></tr></thead>
        <tbody>
          <tr><td>Single-Serie (3 Singles)</td><td>73 € pro Single</td><td>18 € gegenüber 3 Einzel-Singles</td></tr>
          <tr><td>Stem-EP (bis 5 Tracks)</td><td>549 €</td><td>96 € gegenüber 5 Stem-Singles</td></tr>
          <tr><td>Label-Partner (ab 4 Releases/Jahr)</td><td>Single 63 € · Stem-Single 103 € · EP 279 € · Album 499 €</td><td>feste Partnerpreise</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>
{sec('cd-faktoren', 'Was den Preis <em>beeinflusst</em>', """    <ul>
      <li><strong>Stereo oder Stems:</strong> Stem-Mastering bearbeitet mehrere Spurgruppen einzeln und ist deshalb teurer als ein Stereo-Master.</li>
      <li><strong>Anzahl der Tracks:</strong> EP- und Album-Pakete sind pro Track günstiger und enthalten einen Konsistenz-Durchgang über das ganze Release.</li>
      <li><strong>Formate:</strong> Streaming, Bandcamp, CD und Vinyl brauchen teils eigene Fassungen. Bei Polished sind Streaming- und Bandcamp-Exporte immer enthalten.</li>
      <li><strong>Revisionen:</strong> Viele Anbieter begrenzen Korrekturrunden oder berechnen sie extra. Bei Polished sind Revisionen unbegrenzt.</li>
      <li><strong>Lieferzeit:</strong> Express-Lieferung kostet bei vielen Studios Aufpreis. Bei Polished ist eine Single in 48–72 Stunden fertig, schneller auf Anfrage.</li>
      <li><strong>Analyse:</strong> Bei Polished ist ein schriftliches Audio-Audit deines Mixes im Preis enthalten. Woanders ist eine Mix-Analyse oft gar nicht Teil der Leistung.</li>
    </ul>""")}
{sec('cd-mix', 'Mix und Mastering: <em>was kostet beides?</em>', """    <p>Mixing und Mastering sind zwei verschiedene Arbeitsschritte. Beim <strong>Mixing</strong> werden alle Einzelspuren zu einem Stereo-Mix zusammengefügt: Lautstärkeverhältnisse, EQ, Kompression, Effekte. Beim <strong>Mastering</strong> wird dieser fertige Mix für die Veröffentlichung optimiert: Klangbalance, Lautheit, Formate.</p>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Leistung</th><th>Typischer Preis pro Song</th><th>Hinweis</th></tr></thead>
        <tbody>
          <tr><td>Mixing</td><td>etwa 100–300 €</td><td>abhängig von Spurenzahl, Aufwand und Studio</td></tr>
          <tr><td>Mastering</td><td>etwa 50–150 €</td><td>bei Polished 79 € inkl. USt.</td></tr>
          <tr><td>Mix + Mastering</td><td>etwa 150–450 €</td><td>bei getrennten Anbietern einzeln buchbar</td></tr>
        </tbody>
      </table>
    </div>
    <p class="table-note">Richtwerte nach öffentlich einsehbaren Preislisten, Stand Oktober 2026.</p>
    <p>Polished ist bewusst auf Mastering spezialisiert. Wenn das Audio-Audit zeigt, dass der Mix selbst noch Arbeit braucht, bekommst du das ehrlich gesagt, statt es im Mastering zu verstecken.</p>""", alt=True)}
{sec('cd-analog', 'Analog oder digital: <em>Unterschied im Preis</em>', """    <p>Analoges Mastering über Hardware wie Röhren-EQs und Kompressoren ist meist teurer als digitales Mastering, weil Geräte, Wartung und die Arbeit in Echtzeit mehr kosten. Am Markt liegt der Aufpreis häufig bei etwa 30–50 % pro Track.</p>
    <p>Teurer heißt nicht automatisch besser. Entscheidend ist, dass der Engineer weiß, was dein Mix und dein Genre brauchen. Ein gezielter Eingriff nach einer Analyse bringt mehr als teures Equipment ohne Plan.</p>""")}
{sec('cd-spartipps', 'So sparst du <em>beim Mastering</em>', """    <ol>
      <li><strong>Sauberer Mix mit Headroom:</strong> 3–6 dB Luft und kein Limiter auf der Summe. Dann reicht oft Stereo-Mastering statt Stems.</li>
      <li><strong>Mehrere Songs zusammen buchen:</strong> Bei Polished sparst du mit der EP 46 € gegenüber 5 Singles, mit dem Album 161 € gegenüber 10 Singles, mit der Single-Serie 18 € bei 3 Singles.</li>
      <li><strong>Stereo statt Stems, wenn möglich:</strong> Stems lohnen sich nur, wenn Elemente im Mix kollidieren. Das <a href="/de/stem-mastering/">Audit klärt das vorab</a>.</li>
      <li><strong>Referenztracks mitschicken:</strong> Je klarer das Ziel, desto weniger Revisionsschleifen.</li>
      <li><strong>Release-Termin früh nennen:</strong> So vermeidest du Express-Aufschläge.</li>
    </ol>""", alt=True)}
{sec('cd-lohnt', 'Lohnt sich <em>professionelles Mastering?</em>', """    <p>Für ein Release, das auf Spotify, Apple Music oder Bandcamp neben anderen Veröffentlichungen bestehen soll: ja. Ein professioneller Master sorgt dafür, dass dein Song auf Kopfhörern, im Auto und auf dem Handy ausgewogen klingt, die Lautheit zu den Plattformen passt und es nach der Kodierung keine Verzerrungen gibt. Für Demos und Skizzen kann KI-Mastering reichen.</p>
    <p>Wie laut Metal für Streaming gemastert werden sollte, steht im <a href="/de/metal-mastering-lautstaerke/">Lautstärke-Guide</a>.</p>""")}
{sec('cd-versteckt', 'Versteckte Kosten <em>vermeiden</em>', """    <p>Achte beim Vergleich darauf, ob der genannte Preis ein <strong>Endpreis inkl. Umsatzsteuer</strong> ist und was er enthält. Typische Aufpreise sind zusätzliche Revisionen, Stems, Vinyl- oder CD-Fassungen, Express-Lieferung und Abo-Gebühren.</p>
    <p>Bei Polished gibt es kein Abo, keine Bearbeitungsgebühr und keine Aufpreise für Revisionen oder Streaming-Exporte. Bezahlt wird nach Wahl vorab oder auf Rechnung nach Lieferung. Spezialisiert ist Polished auf <a href="/de/black-metal-mastering/">Black Metal</a>, <a href="/de/death-metal-mastering/">Death Metal</a>, <a href="/de/doom-gothic-mastering/">Doom &amp; Gothic</a> und <a href="/de/metalcore-djent-mastering/">Metalcore &amp; Djent</a>.</p>
    <div class="cta-row" style="margin-top: 24px;"><a href="/de/#kontakt" class="cta-btn" data-track="de-cost-cta">Festpreis-Angebot anfragen →</a></div>""", alt=True)}
<section class="content-section" aria-labelledby="cd-faq">
  <div class="wrap prose-wrap">
    <h2 id="cd-faq">Mastering-Kosten: <em>FAQ</em></h2>
{faq_html(CD_FAQS)}
  </div>
</section>'''
cd_schemas = [
    webpage_schema(COST_DE, CD_TITLE, lang='de'),
    breadcrumb_schema([('Startseite', f'{BASE}/de/'), ('Mastering Kosten', f'{BASE}{COST_DE}')]),
    {"@context": "https://schema.org", "@type": "Article", "@id": f"{BASE}{COST_DE}#article",
     "headline": "Was kostet Mastering? Preise und Kosten 2026 im Überblick", "inLanguage": "de",
     "image": f"{BASE}/assets/og-image.jpg", "datePublished": TODAY, "dateModified": TODAY,
     "author": {"@type": "Person", "@id": f"{BASE}/#tim-borchert", "name": "Tim Borchert", "url": f"{BASE}/de/#tim"},
     "publisher": BIZ, "mainEntityOfPage": {"@id": f"{BASE}{COST_DE}#webpage"}},
    faq_schema(CD_FAQS),
]
write(COST_DE, page(path=COST_DE, lang='de', title=CD_TITLE,
      description='Was kostet Mastering? Preisvergleich von KI-Mastering bis Studio, Kosten für Song, EP, Album, Stems und Vinyl. Polished: ab 79 € inkl. USt. mit Audio-Audit.',
      og_title='Was kostet Mastering? — Polished', body=cd_body, schemas=cd_schemas, counterpart=COST_PAIR))

# ---------------------------------------------------------------- EN
CE_TITLE = 'How Much Does Mastering Cost? Prices 2026 | Polished'
CE_FAQS = [
    ('How much does professional mastering cost?', 'Professional mastering typically costs roughly €50–150 per track, and €200 or more at well-known studios. Automated AI services are much cheaper but do not analyse your mix individually. At Polished, stereo mastering costs €79 per track incl. 19% VAT, including a written audio audit and unlimited revisions.'),
    ('How much does it cost to master one song?', 'At Polished, one song costs €79 incl. VAT for stereo mastering or €129 from stems, including a written audio audit, streaming and Bandcamp exports, 48–72h delivery and unlimited revisions. Booking three singles together costs €73 per single.'),
    ('How much does EP or album mastering cost?', 'At Polished, an EP of up to 5 tracks costs €349 (€46 less than 5 singles) and an album of up to 10 tracks costs €629 (€161 less than 10 singles), both with a per-track audit and a consistency pass across the release.'),
    ('How much do mixing and mastering cost together?', 'Mixing takes considerably more work than mastering and usually costs roughly €100–300 per song at studios, depending on track count and studio. Together with mastering, one song typically lands around €150–450. Polished offers mastering only (€79 per song incl. VAT); the audio audit shows beforehand whether your mix is ready for mastering.'),
    ('Are revisions included in the price?', 'Many providers include one or two revision rounds and charge for more. At Polished, revisions are unlimited and have no time limit in every package.'),
    ('How much does stem mastering cost?', 'Stem mastering costs more than stereo mastering because several track groups (e.g. drums, bass, guitars, vocals) are processed individually. At Polished it is €129 per track with up to 6 stems, and €549 for a Stem EP of up to 5 tracks. How to prepare stems: <a href="/stem-mastering/">stem mastering guide</a>.'),
]
ce_body = f'''{breadcrumb_html([('Home', f'{BASE}/'), ('Mastering Cost', f'{BASE}{COST_EN}')])}
<header class="page-hero">
  <div class="wrap">
    <div class="eyebrow">Prices · Cost · Comparison</div>
    <h1>How much does <em>mastering cost?</em></h1>
    <p class="lead"><strong>Short answer: professional mastering usually costs roughly €50–150 per track.</strong> AI services are cheaper, renowned studios more expensive. At Polished, one song is €79 incl. VAT, an EP €349 and an album €629, each with a written audio audit and unlimited revisions.</p>
    <div class="cta-row">
      <a href="/#contact" class="cta-btn" data-track="cost-hero">Get a fixed quote →</a>
      <a href="/#packages" class="cta-btn outline">See packages</a>
    </div>
    <p class="meta-line">By <a href="/#engineer">Tim Borchert</a>, mastering engineer · Updated October 2026 · All prices final incl. 19% VAT</p>
  </div>
</header>
{sec('ce-market', 'Mastering prices <em>compared</em>', """    <div class="table-wrap">
      <table>
        <thead><tr><th>Provider type</th><th>Typical price per track</th><th>What you get</th></tr></thead>
        <tbody>
          <tr><td>AI / automated mastering</td><td>a few euros or a subscription</td><td>An algorithm applies loudness and EQ; no analysis of your mix, no questions</td></tr>
          <tr><td>Freelance marketplaces</td><td>roughly €15–60</td><td>Very mixed quality, often not specialised in your genre</td></tr>
          <tr><td>Specialised mastering studios</td><td>roughly €50–150</td><td>A dedicated engineer, revisions, experience in your genre</td></tr>
          <tr><td>Renowned studios</td><td>roughly €100–300+</td><td>Big names and rooms, often surcharges for stems, vinyl and rush delivery</td></tr>
        </tbody>
      </table>
    </div>
    <p class="table-note">Indicative ranges based on publicly listed prices, October 2026.</p>""")}
<section class="content-section alt" aria-labelledby="ce-polished">
  <div class="wrap">
    <h2 id="ce-polished">Mastering prices <em>at Polished</em></h2>
{PRICES_EN}
    <p class="meta-line">Bundles: Single Series €73 per single (3 singles) · Stem EP €549 · Label Partner from €63 per single. <a href="/#bundles">Details</a>.</p>
  </div>
</section>
{sec('ce-factors', 'What affects <em>the price</em>', """    <ul>
      <li><strong>Stereo vs. stems:</strong> stem mastering processes several track groups individually and costs more.</li>
      <li><strong>Number of tracks:</strong> EP and album packages cost less per track and include a consistency pass.</li>
      <li><strong>Formats:</strong> streaming, Bandcamp, CD and vinyl may need separate versions. Streaming and Bandcamp exports are always included at Polished.</li>
      <li><strong>Revisions:</strong> many providers cap or charge for revisions. At Polished they are unlimited.</li>
      <li><strong>Analysis:</strong> a written audio audit of your mix is included at Polished; elsewhere a mix analysis is often not part of the service.</li>
    </ul>
    <p>Polished specialises in <a href="/black-metal-mastering/">Black Metal</a>, <a href="/death-metal-mastering/">Death Metal</a>, <a href="/doom-gothic-mastering/">Doom &amp; Gothic</a> and <a href="/metalcore-djent-mastering/">Metalcore &amp; Djent</a>. You can pay up front or on invoice after delivery.</p>
    <div class="cta-row" style="margin-top: 24px;"><a href="/#contact" class="cta-btn" data-track="cost-cta">Get a fixed quote →</a></div>""", alt=True)}
<section class="content-section" aria-labelledby="ce-faq">
  <div class="wrap prose-wrap">
    <h2 id="ce-faq">Mastering cost <em>FAQ</em></h2>
{faq_html(CE_FAQS)}
  </div>
</section>'''
ce_schemas = [
    webpage_schema(COST_EN, CE_TITLE),
    breadcrumb_schema([('Home', f'{BASE}/'), ('Mastering Cost', f'{BASE}{COST_EN}')]),
    {"@context": "https://schema.org", "@type": "Article", "@id": f"{BASE}{COST_EN}#article",
     "headline": "How much does mastering cost? Prices 2026 compared", "inLanguage": "en",
     "image": f"{BASE}/assets/og-image.jpg", "datePublished": TODAY, "dateModified": TODAY,
     "author": {"@type": "Person", "@id": f"{BASE}/#tim-borchert", "name": "Tim Borchert", "url": f"{BASE}/#engineer"},
     "publisher": BIZ, "mainEntityOfPage": {"@id": f"{BASE}{COST_EN}#webpage"}},
    faq_schema(CE_FAQS),
]
write(COST_EN, page(path=COST_EN, lang='en', title=CE_TITLE,
      description='How much does mastering cost? Price comparison from AI mastering to studios, costs for a song, EP, album and stems. Polished: from €79 incl. VAT with audio audit.',
      og_title='How much does mastering cost? — Polished', body=ce_body, schemas=ce_schemas, counterpart=COST_PAIR))
