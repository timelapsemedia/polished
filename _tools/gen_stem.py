# Stem mastering guide (DE + EN). Executed from gen.py (shared namespace).

STEM_DE = '/de/stem-mastering/'
STEM_EN = '/stem-mastering/'
STEM_PAIR = {'en': STEM_EN, 'de': STEM_DE}

# ---------------------------------------------------------------- DE
SD_TITLE = 'Stem-Mastering: Vorteile, Kosten & Stem-Export | Polished'
SD_FAQS = [
    ('Was ist Stem-Mastering?', 'Beim Stem-Mastering wird nicht eine fertige Stereo-Datei gemastert, sondern mehrere Spurgruppen (Stems) wie Drums, Bass, Gitarren und Vocals. Jede Gruppe kann einzeln bearbeitet werden, bevor alles zum finalen Master zusammengeführt wird. Das gibt mehr Kontrolle, wenn sich Instrumente im Mix gegenseitig verdecken.'),
    ('Wann lohnt sich Stem-Mastering?', 'Stem-Mastering lohnt sich, wenn einzelne Elemente im Mix kollidieren, etwa Kick und Bass im Low End, Gitarren, die Vocals verdecken, oder Becken, die bei Blastbeats die Snare verschlucken. Bei einem gut ausbalancierten Mix reicht Stereo-Mastering. Das Audio-Audit von Polished sagt dir, was für deinen Mix sinnvoll ist.'),
    ('Was kostet Stem-Mastering?', 'Bei Polished kostet Stem-Mastering 129 € pro Track mit bis zu 6 Stems, die Stem-EP mit bis zu 5 Tracks 549 € (96 € günstiger als 5 Stem-Singles). Labels mit Partnerpreis zahlen 103 € pro Stem-Single. Alle Preise sind Endpreise inkl. 19 % USt. und enthalten das schriftliche Audio-Audit und unbegrenzte Revisionen.'),
    ('Wie viele Stems brauche ich?', 'Meist reichen 4 bis 6 Stems: Drums, Bass, Gitarren, Vocals, dazu bei Bedarf Keys/Synths und FX. Mehr Stems bedeuten nicht automatisch ein besseres Ergebnis; wichtig ist, dass zusammengehörige Spuren in einer Gruppe liegen und die Stems zusammen exakt deinen Mix ergeben.'),
    ('Ist Stem-Mastering dasselbe wie Mixing?', 'Nein. Beim Stem-Mastering bleibt dein Mix in seinen Grundzügen erhalten; es werden nur ganze Spurgruppen klanglich angepasst, zum Beispiel Bass leicht entschärft oder Vocals etwas nach vorne geholt. Lautstärkeverhältnisse einzelner Spuren, Arrangement oder Effekte innerhalb einer Gruppe werden nicht neu gemischt.'),
]
sd_body = f'''{breadcrumb_html([('Startseite', f'{BASE}/de/'), ('Stem-Mastering', f'{BASE}{STEM_DE}')], 'Brotkrumen')}
<header class="page-hero">
  <div class="wrap">
    <div class="eyebrow">Ratgeber · Stem-Mastering</div>
    <h1>Stem-Mastering: <em>mehr Kontrolle für deinen Mix</em></h1>
    <p class="lead"><strong>Beim Stem-Mastering werden statt einer Stereo-Datei mehrere Spurgruppen gemastert, zum Beispiel Drums, Bass, Gitarren und Vocals.</strong> Das hilft, wenn sich Instrumente im Mix verdecken. Bei Polished kostet Stem-Mastering 129 € pro Track inkl. USt., mit schriftlichem Audio-Audit und unbegrenzten Revisionen.</p>
    <div class="cta-row">
      <a href="/de/#kontakt" class="cta-btn" data-track="de-stem-hero">Stem-Mastering anfragen →</a>
      <a href="#export" class="cta-btn outline">Stems richtig exportieren</a>
    </div>
    <p class="meta-line">Von <a href="/de/#tim">Tim Borchert</a>, Mastering Engineer · Stand: Oktober 2026</p>
  </div>
</header>
{sec('sd-vs', 'Stereo- oder Stem-Mastering: <em>der Unterschied</em>', """    <div class="table-wrap">
      <table>
        <thead><tr><th></th><th>Stereo-Mastering</th><th>Stem-Mastering</th></tr></thead>
        <tbody>
          <tr><td>Ausgangsmaterial</td><td>eine fertige Stereo-Datei</td><td>4–6 Spurgruppen (Stems)</td></tr>
          <tr><td>Eingriffe</td><td>wirken immer auf den ganzen Mix</td><td>gezielt pro Gruppe möglich</td></tr>
          <tr><td>Ideal wenn</td><td>der Mix gut ausbalanciert ist</td><td>Elemente kollidieren oder einzelne Gruppen zu laut/leise sind</td></tr>
          <tr><td>Preis bei Polished</td><td>79 € pro Track</td><td>129 € pro Track</td></tr>
        </tbody>
      </table>
    </div>
    <p>Im Metal sind die typischen Fälle für Stems: Kick und Bass streiten sich unter 100 Hz, Gitarrenwände verdecken die Vocals, Becken überdecken bei Blastbeats die Snare, oder Sub-Drops fressen im Breakdown den Headroom. Im Stereo-Master lässt sich das nur mit Kompromissen lösen, mit Stems gezielt.</p>""")}
<section class="content-section alt" id="export" aria-labelledby="sd-export">
  <div class="wrap prose-wrap prose">
    <h2 id="sd-export">Stems richtig <em>exportieren</em></h2>
    <ol>
      <li><strong>Gruppen bilden:</strong> meist Drums, Bass, Gitarren, Vocals, dazu bei Bedarf Keys/Synths und FX (Hall- und Delay-Returns).</li>
      <li><strong>Gleicher Startpunkt, gleiche Länge:</strong> Alle Stems beginnen bei 0:00 bzw. Takt 1 und enden gleichzeitig, auch wenn eine Gruppe erst später einsetzt.</li>
      <li><strong>Format:</strong> 24- oder 32-Bit WAV in der Original-Samplerate deiner Session.</li>
      <li><strong>Summen-Test:</strong> Alle Stems zusammen bei 0 dB müssen exakt deinen Mix ergeben. Prüf das kurz in der DAW.</li>
      <li><strong>Keine Bearbeitung auf der Summe:</strong> Limiter, Clipper und Summenkompressor ausschalten. Gruppen-Bearbeitung, die zum Sound gehört, darf drinbleiben.</li>
      <li><strong>Effekte:</strong> Hall und Delay entweder in den jeweiligen Stem rendern oder als eigenen FX-Stem exportieren, aber nicht doppelt.</li>
      <li><strong>Headroom:</strong> Keine Clips; die Summe sollte mit etwa 3–6 dB Luft unter 0 dBFS bleiben.</li>
      <li><strong>Benennung:</strong> zum Beispiel <code>Songtitel_Drums.wav</code>, <code>Songtitel_Bass.wav</code>.</li>
    </ol>
    <p>Dazu am besten den Stereo-Mix als Referenz und ein bis zwei Referenztracks aus deinem Subgenre mitschicken. Das Audit prüft dann auch, ob die Stems korrekt zusammenpassen.</p>
  </div>
</section>
{sec('sd-kosten', 'Was kostet <em>Stem-Mastering?</em>', """    <div class="table-wrap">
      <table>
        <thead><tr><th>Paket</th><th>Preis inkl. USt.</th><th>Umfang</th></tr></thead>
        <tbody>
          <tr><td>Stem-Single</td><td>129 €</td><td>1 Track, bis zu 6 Stems, Audio-Audit, 48–72 Std.</td></tr>
          <tr><td>Stem-EP</td><td>549 €</td><td>bis 5 Tracks, 96 € günstiger als 5 Stem-Singles, 5–7 Tage</td></tr>
          <tr><td>Label-Partner Stem-Single</td><td>103 €</td><td>ab 4 Releases pro Jahr</td></tr>
        </tbody>
      </table>
    </div>
    <p>Ein Preisvergleich mit anderen Anbietern steht unter <a href="/de/mastering-kosten/">Was kostet Mastering?</a> Wenn du unsicher bist, ob Stems sich für deinen Mix lohnen: Schick den Stereo-Mix, das Audit sagt es dir.</p>
    <div class="cta-row" style="margin-top: 24px;"><a href="/de/#kontakt" class="cta-btn" data-track="de-stem-cta">Stem-Mastering anfragen →</a></div>""", alt=True)}
<section class="content-section" aria-labelledby="sd-faq">
  <div class="wrap prose-wrap">
    <h2 id="sd-faq">Stem-Mastering: <em>FAQ</em></h2>
{faq_html(SD_FAQS)}
  </div>
</section>'''
sd_schemas = [
    webpage_schema(STEM_DE, SD_TITLE, lang='de'),
    breadcrumb_schema([('Startseite', f'{BASE}/de/'), ('Stem-Mastering', f'{BASE}{STEM_DE}')]),
    {"@context": "https://schema.org", "@type": "Article", "@id": f"{BASE}{STEM_DE}#article",
     "headline": "Stem-Mastering: Was es ist, wann es sich lohnt und wie man Stems exportiert", "inLanguage": "de",
     "image": f"{BASE}/assets/og-image.jpg", "datePublished": TODAY, "dateModified": TODAY,
     "author": {"@type": "Person", "@id": f"{BASE}/#tim-borchert", "name": "Tim Borchert", "url": f"{BASE}/de/#tim"},
     "publisher": BIZ, "mainEntityOfPage": {"@id": f"{BASE}{STEM_DE}#webpage"}},
    {"@context": "https://schema.org", "@type": "HowTo", "name": "Stems für das Stem-Mastering exportieren", "inLanguage": "de",
     "step": [{"@type": "HowToStep", "position": i + 1, "text": t} for i, t in enumerate([
         'Spuren in 4–6 Gruppen zusammenfassen: Drums, Bass, Gitarren, Vocals, bei Bedarf Keys/Synths und FX.',
         'Alle Stems ab 0:00 bzw. Takt 1 mit gleicher Länge exportieren.',
         'Als 24- oder 32-Bit WAV in der Original-Samplerate rendern.',
         'Prüfen, dass alle Stems zusammen bei 0 dB exakt den Mix ergeben.',
         'Limiter, Clipper und Summenkompressor vor dem Export ausschalten.',
         'Hall und Delay in den Stem rendern oder als eigenen FX-Stem exportieren.',
         'Etwa 3–6 dB Headroom lassen und Dateien eindeutig benennen.'])]},
    faq_schema(SD_FAQS),
]
write(STEM_DE, page(path=STEM_DE, lang='de', title=SD_TITLE,
      description='Was ist Stem-Mastering, wann lohnt es sich und wie exportierst du Stems richtig? Mit Checkliste und Preisen: Stem-Mastering ab 129 € inkl. USt.',
      og_title='Stem-Mastering — Polished', body=sd_body, schemas=sd_schemas, counterpart=STEM_PAIR))

# ---------------------------------------------------------------- EN
SE_TITLE = 'Stem Mastering: Benefits, Cost & How to Export Stems | Polished'
SE_FAQS = [
    ('What is stem mastering?', 'Stem mastering masters several track groups (stems) such as drums, bass, guitars and vocals instead of one finished stereo file. Each group can be processed individually before everything is combined into the final master, which gives more control when instruments mask each other in the mix.'),
    ('When is stem mastering worth it?', 'Stem mastering is worth it when elements in the mix collide, for example kick and bass in the low end, guitars masking the vocals, or cymbals swallowing the snare during blast beats. For a well-balanced mix, stereo mastering is enough. The Polished audio audit tells you which one suits your mix.'),
    ('How much does stem mastering cost?', 'At Polished, stem mastering costs €129 per track with up to 6 stems, and the Stem EP (up to 5 tracks) costs €549, €96 less than 5 stem singles. All prices include 19% VAT, the written audio audit and unlimited revisions.'),
    ('How many stems do I need?', 'Usually 4 to 6 stems: drums, bass, guitars, vocals, plus keys/synths and FX if needed. More stems are not automatically better; what matters is that related tracks share a group and that all stems together reproduce your mix exactly.'),
]
se_body = f'''{breadcrumb_html([('Home', f'{BASE}/'), ('Stem Mastering', f'{BASE}{STEM_EN}')])}
<header class="page-hero">
  <div class="wrap">
    <div class="eyebrow">Guide · Stem Mastering</div>
    <h1>Stem mastering: <em>more control over your mix</em></h1>
    <p class="lead"><strong>Stem mastering masters several track groups, such as drums, bass, guitars and vocals, instead of one stereo file.</strong> It helps when instruments mask each other in the mix. At Polished, stem mastering costs €129 per track incl. VAT, with a written audio audit and unlimited revisions.</p>
    <div class="cta-row">
      <a href="/#contact" class="cta-btn" data-track="stem-hero">Request stem mastering →</a>
      <a href="#export" class="cta-btn outline">How to export stems</a>
    </div>
    <p class="meta-line">By <a href="/#engineer">Tim Borchert</a>, mastering engineer · Updated October 2026</p>
  </div>
</header>
{sec('se-vs', 'Stereo vs. stem mastering', """    <div class="table-wrap">
      <table>
        <thead><tr><th></th><th>Stereo mastering</th><th>Stem mastering</th></tr></thead>
        <tbody>
          <tr><td>Source</td><td>one finished stereo file</td><td>4–6 track groups (stems)</td></tr>
          <tr><td>Processing</td><td>always affects the whole mix</td><td>targeted per group</td></tr>
          <tr><td>Best when</td><td>the mix is well balanced</td><td>elements collide or a group is too loud/quiet</td></tr>
          <tr><td>Price at Polished</td><td>€79 per track</td><td>€129 per track</td></tr>
        </tbody>
      </table>
    </div>
    <p>Typical metal cases for stems: kick and bass fighting below 100 Hz, guitar walls masking the vocals, cymbals covering the snare in blast beats, or sub drops eating the headroom in breakdowns.</p>""")}
<section class="content-section alt" id="export" aria-labelledby="se-export">
  <div class="wrap prose-wrap prose">
    <h2 id="se-export">How to <em>export stems</em></h2>
    <ol>
      <li><strong>Group tracks:</strong> usually drums, bass, guitars, vocals, plus keys/synths and FX (reverb and delay returns) if needed.</li>
      <li><strong>Same start, same length:</strong> every stem starts at 0:00 / bar 1 and ends at the same point.</li>
      <li><strong>Format:</strong> 24- or 32-bit WAV at your session's sample rate.</li>
      <li><strong>Null test:</strong> all stems together at 0 dB must reproduce your mix exactly.</li>
      <li><strong>No master-bus processing:</strong> turn off limiters, clippers and bus compression. Group processing that is part of the sound can stay.</li>
      <li><strong>Effects:</strong> render reverb and delay into the stem or export them as a separate FX stem, never both.</li>
      <li><strong>Headroom:</strong> no clipping; leave about 3–6 dB below 0 dBFS on the sum.</li>
      <li><strong>Naming:</strong> e.g. <code>SongTitle_Drums.wav</code>, <code>SongTitle_Bass.wav</code>.</li>
    </ol>
    <p>Include the stereo mix as a reference and one or two reference tracks from your subgenre. Pricing compared to other providers: <a href="/mastering-cost/">How much does mastering cost?</a></p>
    <div class="cta-row" style="margin-top: 24px;"><a href="/#contact" class="cta-btn" data-track="stem-cta">Request stem mastering →</a></div>
  </div>
</section>
<section class="content-section" aria-labelledby="se-faq">
  <div class="wrap prose-wrap">
    <h2 id="se-faq">Stem mastering <em>FAQ</em></h2>
{faq_html(SE_FAQS)}
  </div>
</section>'''
se_schemas = [
    webpage_schema(STEM_EN, SE_TITLE),
    breadcrumb_schema([('Home', f'{BASE}/'), ('Stem Mastering', f'{BASE}{STEM_EN}')]),
    {"@context": "https://schema.org", "@type": "Article", "@id": f"{BASE}{STEM_EN}#article",
     "headline": "Stem mastering: what it is, when it's worth it and how to export stems", "inLanguage": "en",
     "image": f"{BASE}/assets/og-image.jpg", "datePublished": TODAY, "dateModified": TODAY,
     "author": {"@type": "Person", "@id": f"{BASE}/#tim-borchert", "name": "Tim Borchert", "url": f"{BASE}/#engineer"},
     "publisher": BIZ, "mainEntityOfPage": {"@id": f"{BASE}{STEM_EN}#webpage"}},
    faq_schema(SE_FAQS),
]
write(STEM_EN, page(path=STEM_EN, lang='en', title=SE_TITLE,
      description='What is stem mastering, when is it worth it and how do you export stems correctly? Checklist and prices: stem mastering from €129 incl. VAT.',
      og_title='Stem mastering — Polished', body=se_body, schemas=se_schemas, counterpart=STEM_PAIR))
