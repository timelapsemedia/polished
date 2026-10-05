# German genre pages + German loudness guide. Executed from gen.py (shares its namespace).

PRICES_DE = '''      <div class="price-grid">
        <div class="price"><div class="name">Single · Stereo</div><div class="amount">79<span style="margin-left:4px;">€</span></div><p>Ein Track, vollständiges Audio-Audit, Streaming- und Bandcamp-Exporte, 48–72 Std.</p></div>
        <div class="price"><div class="name">Single · Stems</div><div class="amount">129<span style="margin-left:4px;">€</span></div><p>Bis zu 6 Stems für maximale Kontrolle pro Element, 48–72 Std.</p></div>
        <div class="price"><div class="name">EP · bis 5 Tracks</div><div class="amount">349<span style="margin-left:4px;">€</span></div><p>46 € gespart gegenüber 5 Singles. Audit pro Track, einheitliche Lautheit über das Release, 5–7 Tage.</p></div>
        <div class="price"><div class="name">Album · bis 10 Tracks</div><div class="amount">629<span style="margin-left:4px;">€</span></div><p>161 € gespart gegenüber 10 Singles. Audit pro Track plus Album-Audit, klangliche Konsistenz, Vinyl-Master auf Anfrage, 7–14 Tage.</p></div>
      </div>
      <p class="meta-line">Alle Preise sind Endpreise inkl. 19 % USt. <strong>Keine Vorkasse nötig: Zahlung wahlweise auf Rechnung nach Lieferung oder vorab.</strong> Jedes Paket enthält das schriftliche Audio-Audit und unbegrenzte Revisionen. <a href="/de/#preise">Alle Pakete im Überblick</a> · <a href="/de/mastering-kosten/">Preisvergleich</a> · <a href="/de/stem-mastering/">Stereo oder Stems?</a></p>'''

AUDIT_STEPS_DE = '''    <ol>
      <li><strong>Premaster schicken:</strong> 24/32-Bit WAV oder AIFF in der Original-Samplerate, 3–6 dB Headroom, kein Limiter auf der Summe, dazu ein oder zwei Referenztracks.</li>
      <li><strong>Schriftliches Audio-Audit:</strong> Frequenzspektrum, Dynamik und Lautheit, Stereobild und Phase sowie eine klangliche Einordnung gegenüber deinem Subgenre und deinen Referenzen.</li>
      <li><strong>Mastering-Plan:</strong> Jeder Schritt wird mit Begründung festgehalten, bevor irgendetwas bearbeitet wird.</li>
      <li><strong>Master und Exporte:</strong> 24-Bit WAV, 16-Bit AIFF, 320 kbps MP3 sowie eigene Versionen für Streaming und Bandcamp.</li>
      <li><strong>Revisionen:</strong> unbegrenzt, bis der Master so klingt, wie du ihn im Kopf hast.</li>
    </ol>'''

GUIDE_DE = '/de/metal-mastering-lautstaerke/'

BLACK_DE = dict(
    slug='black-metal-mastering', name='Black Metal Mastering', eyebrow='Genre · Black Metal',
    title='Black Metal Mastering online – mit Audio-Audit | Polished',
    og_title='Black Metal Mastering — Polished',
    description='Black-Metal-Mastering, das die kalte, rohe Atmosphäre erhält und das Low End kontrolliert. Schriftliches Audio-Audit vor jedem Master. Ab 79 € inkl. USt.',
    audience='Black-Metal-Bands, Ein-Personen-Projekte, Produzenten und Labels',
    h1='Black Metal Mastering, <em>das die Kälte behält.</em>',
    lead='<strong>Black-Metal-Mastering ist der letzte Schritt, der Tremolo-Wände, Blastbeats und Screams auf jedem Abhörsystem funktionieren lässt, ohne den rohen, kalten Charakter des Genres glattzuschleifen.</strong> Bei Polished beginnt jeder Black-Metal-Master mit einem schriftlichen Audio-Audit deines Mixes. Lautheit, Höhen und Low End werden gemessen und begründet entschieden, nicht per Preset. Ab 79 € pro Track, persönlich gemastert von Tim Borchert.',
    cta_h='Schick deinen <em>Black-Metal</em>-Mix.',
    sections=[
        sec('bm-needs', 'Was Black Metal <em>vom Master braucht</em>', '''    <p>Black Metal bricht die meisten Regeln, auf denen Standard-Mastering-Vorlagen aufbauen. Helligkeit, Rauschen und Dichte gehören zur Ästhetik. Wer sie „repariert“ wie bei einer Pop-Produktion, nimmt der Platte genau das, was sie ausmacht. Die Aufgabe ist, den Charakter zu erhalten und nur zu entfernen, was die Übertragung auf andere Systeme verhindert.</p>
''' + cards([
            ('Raw &amp; Lo-Fi', 'Rauschen, Dreck und Boxigkeit sind oft gewollt. Der Master schützt diese Textur und zähmt nur, was auf Earbuds schmerzt oder auf Handy-Lautsprechern zusammenbricht.'),
            ('Atmospheric &amp; Post-Black', 'Lange Hallfahnen und geschichtete Gitarren brauchen eine Breite, die auch in Mono funktioniert. Die Dynamik bleibt offen, damit Steigerungen noch wirken.'),
            ('Melodic &amp; Symphonic', 'Keys, Chöre und Leadgitarren konkurrieren in denselben oberen Mitten. Das Audit zeigt, wo sie sich maskieren, damit der Master Platz für die Melodie schafft.'),
            ('DSBM &amp; Depressive', 'Vocals sind oft absichtlich weit hinten. Der Master erhält diese Distanz und sorgt trotzdem dafür, dass der Track neben anderen Releases nicht einfach nur leise wirkt.'),
        ])),
        sec('bm-problems', 'Was das Audit <em>in Black-Metal-Mixen</em> typischerweise findet', '''    <ul>
      <li><strong>Schärfe zwischen 2 und 5 kHz</strong> durch gestapelte Tremolo-Gitarren und Becken, die anstrengend wird, sobald der Track lauter gemacht wird.</li>
      <li><strong>Beckenteppich bei Blastbeats</strong>, der die Snare verschluckt und schnelle Passagen zu Rauschen statt Intensität macht.</li>
      <li><strong>Bassdrums, die verschwinden</strong> unter der Gitarrenwand, oder getriggerte Kicks, die nach dem Limiting zu stark klicken.</li>
      <li><strong>Sub-Bass-Rumpeln und Phasenprobleme</strong> durch tiefgestimmte Gitarren und breite Hallräume, die Headroom fressen und in Mono zusammenfallen.</li>
      <li><strong>Zu stark limitierte Premaster</strong>, die keinen Spielraum lassen, den Track ohne Verzerrung konkurrenzfähig zu machen.</li>
    </ul>
    <p>Jeder Befund steht mit konkreter Lösung im schriftlichen Bericht. Wenn sich ein Problem im Mastering nicht sauber lösen lässt, steht das ebenfalls drin, damit du entscheiden kannst, ob du den Mix vorher anpasst.</p>''', alt=True),
        sec('bm-process', 'So entsteht <em>ein Black-Metal-Master</em>', AUDIT_STEPS_DE + f'''
    <p>Black Metal muss nicht plattgedrückt werden, um bösartig zu klingen. Streaming-Dienste drehen laute Master ohnehin leiser. Das Ziel ergibt sich daraus, wie viel dein Mix verträgt, bevor Becken und Blasts auseinanderfallen. Mehr dazu im <a href="{GUIDE_DE}">Guide zur Lautstärke beim Metal-Mastering</a>.</p>'''),
    ],
    faqs=[
        ('Kannst du rohen oder Lo-Fi-Black-Metal mastern, ohne dass er clean klingt?', 'Ja. Raw Black Metal wird so gemastert, dass er überall funktioniert, nicht so, dass er sauber wird. Das Audit trennt gewollte Textur wie Rauschen, Dreck und Boxigkeit von echten Problemen wie schmerzhaften Resonanzen, Rumpeln im Bass oder Phasenauslöschung. Nur die Probleme werden bearbeitet. Wenn die Platte hässlich bleiben soll, schreib das in dein Briefing und schick eine Referenz mit.'),
        ('Wie laut sollte ein Black-Metal-Master sein?', 'Es gibt keinen festen Wert. Streaming-Dienste normalisieren auf etwa -14 LUFS (Apple Music etwa -16 LUFS), extreme Lautheit kostet also vor allem Klarheit bei Blastbeats und Becken. Viele Black-Metal-Releases liegen grob zwischen -10 und -7 LUFS integriert. Das Ziel für deinen Track wird im Audit festgelegt, je nachdem, wie weit sich der Mix treiben lässt, bevor er zusammenbricht.'),
        ('Masterst du auch Ein-Personen-Projekte?', 'Ja. Soloprojekte sind ein großer Teil der Szene und werden genauso behandelt wie Band-Releases: gleiches Audit, gleicher Preis, gleiche unbegrenzte Revisionen. Programmierte Drums sind kein Problem. Das Audit prüft, ob getriggerte oder gesampelte Kicks nach dem Limiting noch klar durchkommen.'),
        ('Kann ich Stems statt eines Stereo-Mixes schicken?', 'Ja. Stem-Mastering (129 € pro Track inkl. USt., bis zu 6 Stems) lohnt sich bei Black Metal, wenn Gitarren und Becken im selben Bereich kämpfen oder die Kick unter der Wand verschwindet. Typische Stems sind Drums, Bass, Gitarren, Vocals, Keys/Synths und FX. Das Audit sagt dir, ob Stems für deinen Mix sinnvoll sind.'),
    ],
)

DEATH_DE = dict(
    slug='death-metal-mastering', name='Death Metal Mastering', eyebrow='Genre · Death Metal',
    title='Death Metal Mastering online – mit Audio-Audit | Polished',
    og_title='Death Metal Mastering — Polished',
    description='Death-Metal-Mastering mit echtem Gewicht im Low End und Blastbeats, die lesbar bleiben. Schriftliches Audio-Audit vor jedem Master. Ab 79 € inkl. USt.',
    audience='Death-Metal-, Technical-Death-, Brutal-Death- und Deathcore-Bands, Produzenten und Labels',
    h1='Death Metal Mastering <em>mit Gewicht und Klarheit.</em>',
    lead='<strong>Death-Metal-Mastering gibt Palm-Mutes echtes Gewicht, hält Blastbeats und schnelle Double-Bass lesbar und sorgt dafür, dass Growls sich auf jedem Abhörsystem durch die Gitarrenwand setzen.</strong> Bei Polished beginnt jeder Death-Metal-Master mit einem schriftlichen Audio-Audit deines Mixes. Low End und Lautheit werden gemessen, nicht geraten. Ab 79 € pro Track, persönlich gemastert von Tim Borchert.',
    cta_h='Schick deinen <em>Death-Metal</em>-Mix.',
    sections=[
        sec('dm-needs', 'Was Death Metal <em>vom Master braucht</em>', '''    <p>Death Metal ist absichtlich dicht: tiefgestimmte Gitarren, schnelle Double-Bass, tiefe Growls und oft ein Bass im selben Register wie die Gitarren. Lautheit wird erwartet, aber jedes dB Limiting kostet Transienten. Ein guter Death-Metal-Master findet den Punkt, an dem die Platte hart zuschlägt, ohne dass die Drums zu Brei werden.</p>
''' + cards([
            ('Old School Death Metal', 'Organisch, gesättigt, manchmal absichtlich dumpf. Der Master bringt Druck und Durchsetzung und erhält den höhlenartigen Charakter.'),
            ('Technical &amp; Progressive', 'Jeder Ton zählt. Der Master schützt die Artikulation in schnellen Läufen und hält Basslinien unter den Gitarren hörbar.'),
            ('Brutal &amp; Slam', 'Maximales Gewicht in den unteren Mitten. Das Audit beobachtet den Bereich zwischen 100 und 300 Hz genau, damit Slams knallen statt dröhnen.'),
            ('Melodic Death Metal', 'Leads und Harmonien brauchen Präsenz ohne Schärfe. Der Master balanciert Aggression und melodische Klarheit.'),
        ])),
        sec('dm-problems', 'Was das Audit <em>in Death-Metal-Mixen</em> typischerweise findet', '''    <ul>
      <li><strong>Überladene untere Mitten (150–400 Hz)</strong> durch Gitarren, Bass und Toms, die sich stapeln: Der Mix klingt groß, aber undefiniert.</li>
      <li><strong>Double-Bass, die verschwimmt</strong> bei hohen Tempi, entweder zu klickig nach dem Limiting oder unter dem Bass verloren.</li>
      <li><strong>Growls im Kampf mit den Gitarren</strong> im selben Frequenzbereich, sodass Text und Rhythmus untergehen.</li>
      <li><strong>Snare ohne Crack</strong>, sobald der Master lauter wird, weil der Limiter jeden Schlag zuerst erwischt.</li>
      <li><strong>Vorab limitierte Mixe</strong>, bei denen die Summe schon hart geclippt ist und kaum Platz für einen sauberen, lauten Master bleibt.</li>
    </ul>
    <p>Jedes Problem wird mit Messwert und geplanter Lösung dokumentiert. Wenn die sauberste Lösung eine Änderung im Mix ist, steht das im Bericht, statt es hinter mehr Bearbeitung zu verstecken.</p>''', alt=True),
        sec('dm-process', 'So entsteht <em>ein Death-Metal-Master</em>', AUDIT_STEPS_DE + f'''
    <p>Death Metal wird meist lauter gemastert als die Normalisierungsziele der Streaming-Dienste. Das ist in Ordnung, solange die Transienten überleben. Der True Peak bleibt niedrig genug, damit nach der verlustbehafteten Kodierung nichts verzerrt. Details im <a href="{GUIDE_DE}">Guide zur Lautstärke beim Metal-Mastering</a>.</p>'''),
    ],
    faqs=[
        ('Wie verhinderst du, dass Blastbeats zu Brei werden?', 'Indem vor dem Limiting gemessen wird. Das Audit betrachtet Crest-Faktor, das Transientenverhalten von Kick und Snare und wie stark Becken und Gitarren die Drums maskieren. Das Lautheitsziel wird dann so gesetzt, dass der Limiter nicht jeden Snare-Schlag plattmacht. Wenn die Drums schon im Mix begraben sind, wird Stem-Mastering oder eine kleine Mix-Änderung empfohlen, statt einfach härter zu drücken.'),
        ('Wie laut sollte ein Death-Metal-Master sein?', 'Death Metal wird häufig lauter gemastert als die Streaming-Ziele, oft grob zwischen -9 und -6 LUFS integriert, eine feste Regel gibt es aber nicht. Spotify, YouTube und Tidal spielen mit etwa -14 LUFS ab, ein lauterer Master wird also leiser gedreht. Ziel ist die lauteste Version, die den Crack der Snare und die Definition der Double-Bass behält, mit einem True Peak von höchstens -1 dBTP.'),
        ('Masterst du auch Deathcore und Technical Death Metal?', 'Ja. Deathcore, Technical, Progressive, Brutal, Slam und Melodic Death Metal gehören alle dazu. Jedes Subgenre hat andere Prioritäten, von der Artikulation im Tech Death bis zum Gewicht der unteren Mitten im Slam, und das Audit vergleicht mit Referenzen aus deinem Subgenre.'),
        ('Lohnt sich Stem-Mastering bei Death Metal?', 'Oft ja. Wenn Kick, Bass und Gitarren im Low End konkurrieren, lassen sich mit Stem-Mastering (129 € pro Track inkl. USt., bis zu 6 Stems) die Gruppen einzeln formen, bevor der finale Master entsteht. Bei einem gut ausbalancierten Mix reicht Stereo-Mastering für 79 €. Das Audit sagt dir, was passt.'),
    ],
)

DOOM_DE = dict(
    slug='doom-gothic-mastering', name='Doom & Gothic Mastering', eyebrow='Genre · Doom · Gothic',
    title='Doom & Gothic Metal Mastering online | Polished',
    og_title='Doom & Gothic Mastering — Polished',
    description='Mastering für Doom, Sludge und Gothic, das Dynamik und Raum erhält, während das Low End schwer bleibt. Schriftliches Audio-Audit vor jedem Master. Ab 79 €.',
    audience='Doom-Metal-, Funeral-Doom-, Sludge-, Stoner-, Gothic-Metal-, Gothic-Rock- und Darkwave-Bands, Produzenten und Labels',
    h1='Doom &amp; Gothic Mastering <em>mit Raum zum Atmen.</em>',
    lead='<strong>Beim Doom- und Gothic-Mastering geht es darum, Dynamik und Raum zu erhalten, damit langsame Steigerungen wirken, während das Low End dick bleibt, ohne Vocals, Keys und Atmosphäre zu verschlucken.</strong> Bei Polished beginnt jeder Doom- und Gothic-Master mit einem schriftlichen Audio-Audit deines Mixes. Die Lautheit wird bewusst gewählt, nicht standardmäßig maximiert. Ab 79 € pro Track, persönlich gemastert von Tim Borchert.',
    cta_h='Schick deinen <em>Doom- oder Gothic</em>-Mix.',
    sections=[
        sec('dg-needs', 'Was Doom und Gothic <em>vom Master brauchen</em>', '''    <p>Langsame Musik legt alles offen. Gehaltene Akkorde, lange Ausklänge und leise Passagen machen Überkompression hörbar, wo schnelle Genres sie verstecken. Doom- und Gothic-Platten verlieren den Großteil ihrer Wirkung, wenn jeder Teil auf dieselbe Lautheit gedrückt wird. Der Master muss Kontraste erhalten, das Low End schwer, aber kontrolliert halten und Platz für Vocals, Keys und Hallfahnen lassen.</p>
''' + cards([
            ('Doom &amp; Funeral Doom', 'Riesiges, langsames, stehendes Low End. Der Master hält es massiv, ohne dass die Sub-Energie den Headroom des ganzen Tracks frisst.'),
            ('Sludge &amp; Stoner', 'Fuzz und Sättigung sind der Sound. Das Audit trennt musikalische Verzerrung von Schärfe, die bei Lautstärke anstrengend wird.'),
            ('Gothic Metal', 'Klarer Gesang und Growls, Keys, Chöre und Gitarren brauchen alle ihren Platz. Der Master verbindet Gewicht mit Klarheit in den Mitten.'),
            ('Gothic Rock &amp; Darkwave', 'Bassgetrieben und atmosphärisch. Der Master hält die Basslinie vorne und den Hallraum tief, ohne dass es matschig wird.'),
        ])),
        sec('dg-problems', 'Was das Audit <em>in Doom- und Gothic-Mixen</em> typischerweise findet', '''    <ul>
      <li><strong>Überladener Sub- und unterer Mittenbereich</strong> durch gehaltene, tiefgestimmte Akkorde, der Vocals und Keys maskiert.</li>
      <li><strong>Überkompression</strong>, die den Kontrast zwischen leise und schwer plattmacht, von dem diese Genres leben.</li>
      <li><strong>Hallfahnen, die in Mono zusammenfallen</strong> oder den Mix auf kleinen Lautsprechern trüb machen.</li>
      <li><strong>Scharfer Fuzz in den oberen Mitten</strong>, der beim Aufdrehen schmerzt.</li>
      <li><strong>Uneinheitliche Pegel zwischen den Songs</strong> auf EPs und Alben mit sehr unterschiedlicher Dynamik.</li>
    </ul>
    <p>Bei kompletten Releases betrachtet das Audit auch die Platte als Ganzes, damit leise Interludes und schwere Songs zusammengehören statt nebeneinanderzustehen.</p>''', alt=True),
        sec('dg-process', 'So entsteht <em>ein Doom- oder Gothic-Master</em>', AUDIT_STEPS_DE + f'''
    <p>Doom- und Gothic-Master profitieren am meisten von der Lautheitsnormalisierung der Streaming-Dienste: Ein dynamischer Master wird nicht bestraft, er behält einfach seinen Punch. Vinyl-Master gibt es auf Anfrage für Album-Projekte. Mehr im <a href="{GUIDE_DE}">Guide zur Lautstärke beim Metal-Mastering</a>.</p>'''),
    ],
    faqs=[
        ('Klingt meine Doom-Platte dann zu leise neben anderen Releases?', 'Nicht auf Streaming-Plattformen. Spotify, YouTube und Tidal normalisieren auf etwa -14 LUFS, Apple Music auf etwa -16 LUFS. Ein dynamischerer Doom-Master wird dort ähnlich laut wahrgenommen und behält seine Kontraste. Auf Bandcamp gibt es keine Normalisierung, deshalb wird die Lautheit dort gezielt geplant. Das Audit legt das Ziel pro Track fest.'),
        ('Kann das Low End schwerer werden, ohne matschig zu klingen?', 'Meistens ja. Das Audit zeigt, wo die Energie im Bass tatsächlich sitzt: oft Sub-Energie unter 60 Hz, die Headroom frisst, im Gegensatz zu den unteren Mitten um 150–300 Hz, die Gewicht erzeugen. Der Master formt diese Bereiche getrennt. Wenn Kick und Bass schon im Mix kämpfen, gibt Stem-Mastering die meiste Kontrolle.'),
        ('Masterst du neben Gothic Metal auch Gothic Rock und Darkwave?', 'Ja. Gothic Rock, Darkwave, Deathrock und Gothic Metal gehören alle zum Schwerpunkt. Diese Stile sind oft bassgetrieben und atmosphärisch, deshalb hält der Master die Basslinie vorne und den Hallraum tief, ohne die Vocals zu vernebeln.'),
        ('Gibt es auch einen Vinyl-Master?', 'Ja. Ein Vinyl-Master ist für Album-Projekte auf Anfrage möglich. Vinyl profitiert von erhaltener Dynamik, einem monokompatiblen Low End und kontrollierten Zischlauten, was gut zu Doom und Gothic passt. Erwähne Vinyl im Briefing, dann wird es ab dem Audit mitgeplant.'),
    ],
)

CORE_DE = dict(
    slug='metalcore-djent-mastering', name='Metalcore & Djent Mastering', eyebrow='Genre · Metalcore · Djent',
    title='Metalcore & Djent Mastering online | Polished',
    og_title='Metalcore & Djent Mastering — Polished',
    description='Metalcore- und Djent-Mastering mit straffem, kontrolliertem Low End, klaren Breakdowns und Vocals am richtigen Platz. Audio-Audit vor jedem Master. Ab 79 €.',
    audience='Metalcore-, Post-Hardcore-, Djent-, Progressive-Metal- und Deathcore-Bands, Produzenten und Labels',
    h1='Metalcore &amp; Djent Mastering <em>straff auf dem Grid.</em>',
    lead='<strong>Beim Metalcore- und Djent-Mastering geht es um ein präzises, kontrolliertes Low End für synkopierte Extended-Range-Riffs, Breakdowns mit Druck und Clean- wie Scream-Vocals, die genau dort sitzen, wo sie hingehören.</strong> Bei Polished beginnt jeder Metalcore- und Djent-Master mit einem schriftlichen Audio-Audit deines Mixes. Lautheit und Low End werden gemessen. Ab 79 € pro Track, persönlich gemastert von Tim Borchert.',
    cta_h='Schick deinen <em>Metalcore- oder Djent</em>-Mix.',
    sections=[
        sec('mc-needs', 'Was Metalcore und Djent <em>vom Master brauchen</em>', '''    <p>Moderner Metalcore und Djent wird straff, laut und poliert produziert, oft mit programmierten Drums, Extended-Range-Gitarren und Synth-Layern. Hörer vergleichen dein Release direkt mit großen Produktionen. Der Master muss diese moderne Lautheit und Politur liefern und gleichzeitig das Low End kontrollieren, wenn 7- und 8-Saiter, Bass und Kick alle unter 100 Hz zuhause sind.</p>
''' + cards([
            ('Metalcore &amp; Post-Hardcore', 'Große Refrains, klarer Gesang und schwere Breakdowns in einem Song. Der Master hält beide Hälften kraftvoll, ohne dass der Refrain untergeht.'),
            ('Djent &amp; Prog Metal', 'Synkopierte Low-End-Riffs brauchen Definition. Der Master hält jeden Palm-Mute-Chug einzeln hörbar statt als durchgehendes Grollen.'),
            ('Deathcore', 'Extremes Low End und extreme Vocals. Das Audit achtet genau auf den Headroom, damit Drops knallen, ohne zu verzerren.'),
            ('Electronic Hybrid', 'Synths, Sub-Drops und Samples über der Band. Der Master balanciert die Sub-Energie, damit sie den Gitarren nicht den Headroom stiehlt.'),
        ])),
        sec('mc-problems', 'Was das Audit <em>in Metalcore- und Djent-Mixen</em> typischerweise findet', '''    <ul>
      <li><strong>Kollisionen unter 100 Hz</strong> zwischen Extended-Range-Gitarren, Bass, Kick und Sub-Drops.</li>
      <li><strong>Breakdowns, die leiser werden</strong> nach dem Limiting, weil das Low End den gesamten Headroom frisst.</li>
      <li><strong>Clean-Vocals zu weit hinten</strong> im Refrain oder Screams zu scharf im Bereich 3–5 kHz.</li>
      <li><strong>Sub-Drops und 808s</strong>, die den Limiter überfahren und Pumpen erzeugen.</li>
      <li><strong>Phasenprobleme</strong> durch geschichtete Gitarren-DIs, Re-Amps und Stereo-Verbreiterung, die den Mix in Mono schwächen.</li>
    </ul>
    <p>Jeder Befund wird mit Messwerten und geplanter Lösung dokumentiert, inklusive eines ehrlichen Hinweises, wenn etwas zuerst im Mix geändert werden sollte.</p>''', alt=True),
        sec('mc-process', 'So entsteht <em>ein Metalcore- oder Djent-Master</em>', AUDIT_STEPS_DE + f'''
    <p>Metalcore gehört zu den am lautesten gemasterten Metal-Stilen. Das ist machbar, die saubersten Ergebnisse entstehen aber aus einem Mix mit Headroom und ohne Limiter auf der Summe. Ziele und True-Peak-Grenzen findest du im <a href="{GUIDE_DE}">Guide zur Lautstärke beim Metal-Mastering</a>.</p>'''),
    ],
    faqs=[
        ('Wird mein Metalcore-Master so laut wie große Releases?', 'Meistens nah dran, wenn der Mix es zulässt. Moderner Metalcore wird oft grob zwischen -8 und -6 LUFS integriert gemastert. Ob dein Mix das sauber erreicht, hängt davon ab, wie kontrolliert das Low End ist und wie viel Headroom der Premaster hat. Das Audit misst das zuerst und sagt dir ehrlich, welche Lautheit ohne Verzerrung oder Pumpen möglich ist.'),
        ('Wie gehst du mit dem Low End von 7- und 8-Saitern um?', 'Das Audit zeigt, wo sich Gitarre, Bass und Kick unter 100 Hz überlagern, und prüft die Phase zwischen ihnen. Der Master kontrolliert diesen Bereich dann so, dass Palm-Mute-Riffs einzeln hörbar bleiben. Wenn die Kollision tief im Mix steckt, lassen sich mit Stem-Mastering (129 € pro Track inkl. USt., bis zu 6 Stems) Gitarren und Bass getrennt formen.'),
        ('Bekommen Breakdowns und Sub-Drops besondere Aufmerksamkeit?', 'Ja. Genau an Breakdowns scheitern viele Master: Das Low End frisst den Headroom des Limiters, und der schwerste Moment wirkt am Ende kleiner. Das Audit markiert diese Stellen, und der Master wird gezielt an Breakdowns und Drops geprüft, nicht nur am lautesten Refrain.'),
        ('Arbeitest du mit programmierten Drums und Amp-Sims?', 'Ja. Programmierte Drums, Amp-Simulationen und reine In-the-Box-Produktionen sind im Metalcore und Djent Standard und werden genauso gemastert wie aufgenommenes Material. Das Audit prüft samplebasierte Kicks und Snares auf Klicks oder Schärfe nach dem Limiting.'),
    ],
)

for _g in (BLACK_DE, DEATH_DE, DOOM_DE, CORE_DE):
    write(f'/de/{_g["slug"]}/', genre_page(_g, 'de'))

# ---------------------------------------------------------------- GERMAN LOUDNESS GUIDE
LGD_TITLE = 'Wie laut sollte Metal gemastert werden? LUFS-Guide | Polished'
LGD_FAQS = [
    ('Auf wie viel LUFS sollte man Metal mastern?', 'Es gibt keinen einzig richtigen Wert. Streaming-Dienste normalisieren die Wiedergabe auf etwa -14 LUFS integriert (Apple Music etwa -16 LUFS), lautere Master werden also leiser gedreht. Viele kommerzielle Metal-Releases liegen grob zwischen -10 und -6 LUFS integriert, weil Dichte und Sättigung zum Sound gehören. Das richtige Ziel ist der lauteste Pegel, den dein Mix erreicht, bevor Transienten, Becken und Low End zusammenbrechen.'),
    ('Dreht Spotify laute Metal-Master leiser?', 'Ja. Mit aktivierter Normalisierung (Standard) spielt Spotify Tracks mit etwa -14 LUFS integriert ab. Ein Master mit -8 LUFS wird um etwa 6 dB leiser gedreht. Zusätzlich gibt es die Einstellung „Laut“ mit -11 LUFS und „Leise“ mit -19 LUFS.'),
    ('Dreht Spotify leise Master lauter?', 'Nur teilweise. Spotify hebt leisere Tracks nur so weit an, wie ihr True Peak es zulässt, und lässt dabei etwa 1 dB Headroom. Spotifys eigenes Beispiel: Ein Track mit -20 LUFS und einem True Peak von -5 dBFS wird nur auf -16 LUFS angehoben. Ein sehr dynamischer Master mit hohen Spitzen kann deshalb etwas leiser wiedergegeben werden als lautere Master.'),
    ('Welchen True Peak sollte ein Metal-Master haben?', 'Spotify empfiehlt einen True Peak unter -1 dBTP und unter -2 dBTP, wenn der Master lauter als -14 LUFS integriert ist, weil verlustbehaftete Kodierung Spitzen anheben und Verzerrungen verursachen kann. Für laute Metal-Master ist -1 dBTP eine übliche Obergrenze, niedrigere Werte kommen zum Einsatz, wenn der Codec-Test Clipping zeigt.'),
    ('Sollte ich für Bandcamp anders mastern?', 'Bandcamp normalisiert nicht. Hörer hören deinen Master genau so, wie er geliefert wurde, und Pegelunterschiede zu anderen Releases sind hörbar. Viele Künstler nutzen überall denselben Master. Wenn dein Streaming-Master eher dynamisch ist, kann eine etwas lautere Bandcamp-Version sinnvoll sein.'),
]
lgd_body = f'''{breadcrumb_html([('Startseite', f'{BASE}/de/'), ('Lautstärke-Guide Metal-Mastering', f'{BASE}{GUIDE_DE}')], 'Brotkrumen')}
<header class="page-hero">
  <div class="wrap">
    <div class="eyebrow">Guide · Lautstärke</div>
    <h1>Wie laut sollte Metal <em>gemastert werden?</em></h1>
    <p class="lead"><strong>Kurze Antwort: Es gibt keinen einzig richtigen LUFS-Wert für Metal.</strong> Streaming-Dienste spielen alles mit etwa -14 LUFS ab (Apple Music etwa -16 LUFS), zusätzliche Lautheit wird also leiser gedreht. Das richtige Ziel ist der lauteste Pegel, den dein Mix erreicht, bevor Blastbeats, Becken und Low End zusammenbrechen.</p>
    <p class="meta-line">Von <a href="/de/#tim">Tim Borchert</a>, Mastering Engineer, Systematische Musikwissenschaft (Universität Hamburg) · Veröffentlicht am 5. Oktober 2026</p>
  </div>
</header>
{sec('lgd-what', 'Was LUFS bedeutet <em>und warum es zählt</em>', """    <div class="answer-box"><div class="label">Definition</div><p>LUFS (Loudness Units relative to Full Scale) misst die wahrgenommene Lautheit über die Zeit, gewichtet nach dem menschlichen Gehör. Integrated LUFS ist der Durchschnitt über den ganzen Track. Streaming-Plattformen nutzen diesen Wert, um alle Tracks ähnlich laut abzuspielen.</p></div>
    <p>Peak-Meter zeigen nur das höchste Sample. LUFS zeigt, wie laut sich ein Track tatsächlich anfühlt. Zwei Master können beide bei -1 dBFS spitzen und trotzdem 6 dB auseinanderliegen. Um genau diesen Unterschied ging es im Loudness War, und genau das hat die Normalisierung verändert.</p>
    <p>Drei Werte zählen, wenn ein Metal-Master für die Veröffentlichung bewertet wird:</p>
    <ul>
      <li><strong>Integrated LUFS:</strong> die durchschnittliche Lautheit über den Track. Darauf normalisieren die Plattformen.</li>
      <li><strong>True Peak (dBTP):</strong> der tatsächliche Spitzenpegel nach Digital-Analog-Wandlung und verlustbehafteter Kodierung. Er kann höher liegen als der Sample-Peak.</li>
      <li><strong>Crest-Faktor / Dynamikumfang:</strong> der Abstand zwischen Spitzen und Durchschnittspegel. Im Metal entscheidet er, ob die Snare noch knallt oder nur in der Wand sitzt.</li>
    </ul>""")}
{sec('lgd-platforms', 'Lautheitsziele <em>nach Plattform</em>', """    <div class="table-wrap">
      <table>
        <thead><tr><th>Plattform</th><th>Referenzpegel</th><th>Was mit einem lauten Metal-Master passiert</th></tr></thead>
        <tbody>
          <tr><td>Spotify</td><td>-14 LUFS (Normal) · -11 LUFS (Laut) · -19 LUFS (Leise)</td><td>Wird auf den gewählten Pegel leiser gedreht. Leise Tracks werden nur so weit angehoben, wie der True Peak es erlaubt.</td></tr>
          <tr><td>YouTube</td><td>etwa -14 LUFS</td><td>Wird leiser gedreht. Leisere Tracks werden nicht angehoben.</td></tr>
          <tr><td>Apple Music</td><td>etwa -16 LUFS (Sound Check)</td><td>Wird leiser gedreht, wenn Sound Check aktiv ist.</td></tr>
          <tr><td>Tidal</td><td>etwa -14 LUFS</td><td>Wird leiser gedreht.</td></tr>
          <tr><td>Amazon Music</td><td>etwa -14 LUFS</td><td>Wird leiser gedreht.</td></tr>
          <tr><td>Deezer</td><td>etwa -15 LUFS</td><td>Wird leiser gedreht.</td></tr>
          <tr><td>Bandcamp</td><td>keine Normalisierung</td><td>Wird genau so abgespielt, wie er geliefert wurde.</td></tr>
        </tbody>
      </table>
    </div>
    <p class="table-note">Werte nach Plattform-Dokumentation und verbreiteten Messungen, Stand Oktober 2026. Plattformen können ihre Referenzpegel ändern. Die Spotify-Werte stammen aus den <a href="https://support.spotify.com/de/artists/article/loudness-normalization/" rel="noopener" target="_blank">Richtlinien von Spotify zur Lautheitsnormalisierung</a>.</p>
    <p>Die praktische Folge: Auf Streaming-Plattformen landen ein Master mit -7 LUFS und einer mit -11 LUFS bei ungefähr derselben Wiedergabelautstärke. Der lautere gewinnt den Lautstärkewettbewerb nicht mehr. Er gibt nur Transienten-Details ab, es sei denn, genau diese Dichte ist der Sound, den du willst.</p>""", alt=True)}
{sec('lgd-metal', 'Typische Lautheit <em>nach Metal-Subgenre</em>', """    <p>Kommerzieller Metal wird meist lauter gemastert als die Streaming-Referenzen, und das ist legitim: Sättigung und Dichte gehören zum Sound des Genres. Diese Bereiche dienen der groben Orientierung, sie sind keine Zielwerte:</p>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Subgenre</th><th>Üblicher Integrated-Bereich</th><th>Was die Lautheit zuerst begrenzt</th></tr></thead>
        <tbody>
          <tr><td>Metalcore / Djent</td><td>etwa -8 bis -6 LUFS</td><td>Low End unter 100 Hz frisst in Breakdowns den Headroom</td></tr>
          <tr><td>Death Metal</td><td>etwa -9 bis -6 LUFS</td><td>Crack der Snare und Definition der Double-Bass</td></tr>
          <tr><td>Black Metal</td><td>etwa -10 bis -7 LUFS</td><td>Beckenteppich und Schärfe in Blast-Passagen</td></tr>
          <tr><td>Doom / Sludge</td><td>etwa -11 bis -8 LUFS</td><td>Stehende Sub-Energie und Verlust von Kontrast</td></tr>
          <tr><td>Gothic Metal / Gothic Rock</td><td>etwa -12 bis -8 LUFS</td><td>Dynamik zwischen leisen und schweren Teilen</td></tr>
        </tbody>
      </table>
    </div>
    <p class="table-note">Orientierungswerte aus der Mastering-Praxis. Einzelne Releases weichen stark ab, und der richtige Wert für deinen Track hängt vom Mix ab.</p>
    <p>Genre-spezifische Details: <a href="/de/black-metal-mastering/">Black Metal</a>, <a href="/de/death-metal-mastering/">Death Metal</a>, <a href="/de/doom-gothic-mastering/">Doom &amp; Gothic</a>, <a href="/de/metalcore-djent-mastering/">Metalcore &amp; Djent</a>.</p>""")}
{sec('lgd-peak', 'True Peak: <em>der Wert, der Verzerrung verursacht</em>', """    <p>Wenn ein WAV-Master für Streaming in Ogg Vorbis, AAC oder MP3 umgewandelt wird, können Spitzen über den ursprünglichen Pegel steigen. Ein auf 0 dBFS limitierter Master kann nach der Kodierung clippen, obwohl das WAV sauber aussieht. Laute, dichte Metal-Master sind besonders betroffen.</p>
    <ul>
      <li>Spotify empfiehlt einen True Peak <strong>unter -1 dBTP</strong>.</li>
      <li>Für Master, die lauter als -14 LUFS integriert sind, empfiehlt Spotify <strong>unter -2 dBTP</strong>.</li>
      <li>Ein Test über eine echte Codec-Vorschau zeigt Kodierungsverzerrungen schon vor dem Release.</li>
    </ul>""", alt=True)}
{sec('lgd-how', 'Wie die richtige Lautheit <em>festgelegt wird</em>', """    <p>Bei Polished ist Lautheit keine feste Einstellung. Sie ergibt sich aus dem Audio-Audit, das vor jedem Master läuft:</p>
    <ol>
      <li>Den Premaster messen: Integrated LUFS, True Peak, Crest-Faktor und die Kurzzeit-Lautheit der schwersten Passagen.</li>
      <li>Mit Referenzen aus deinem Subgenre vergleichen, die du auswählst oder die zu deinem Briefing passen.</li>
      <li>Die Schwelle finden, ab der mehr Lautheit den Crack der Snare, die Definition der Blastbeats oder die Kontrolle im Low End kostet.</li>
      <li>Das Ziel unterhalb dieser Schwelle setzen, den True Peak prüfen und eine Codec-Vorschau durchlaufen lassen.</li>
      <li>Den Master mit dokumentierten Messwerten liefern, damit du genau weißt, was du veröffentlichst.</li>
    </ol>
    <p>Wenn du deinen Track messen lassen willst, schick ihn rein. Das Audit ist in jedem Paket enthalten, ab 79 € pro Track inkl. USt.</p>
    <div class="cta-row" style="margin-top: 24px;"><a href="/de/#kontakt" class="cta-btn" data-track="de-guide-cta">Audio-Audit anfragen →</a><a href="/de/#preise" class="cta-btn outline">Preise ansehen</a></div>""")}
<section class="content-section alt" aria-labelledby="lgd-faq">
  <div class="wrap prose-wrap">
    <h2 id="lgd-faq">Metal-Lautheit: <em>FAQ</em></h2>
{faq_html(LGD_FAQS)}
  </div>
</section>'''
lgd_schemas = [
    webpage_schema(GUIDE_DE, LGD_TITLE, lang='de'),
    breadcrumb_schema([('Startseite', f'{BASE}/de/'), ('Lautstärke-Guide Metal-Mastering', f'{BASE}{GUIDE_DE}')]),
    {"@context": "https://schema.org", "@type": "Article", "@id": f"{BASE}{GUIDE_DE}#article",
     "headline": "Wie laut sollte Metal gemastert werden? LUFS, True Peak und Streaming-Normalisierung",
     "description": "Lautheitsziele für Metal-Master: Streaming-Normalisierung nach Plattform, typische LUFS-Bereiche nach Subgenre und True-Peak-Grenzen.",
     "image": f"{BASE}/assets/og-image.jpg", "inLanguage": "de",
     "datePublished": TODAY, "dateModified": TODAY,
     "author": {"@type": "Person", "@id": f"{BASE}/#tim-borchert", "name": "Tim Borchert", "url": f"{BASE}/de/#tim"},
     "publisher": BIZ, "mainEntityOfPage": {"@id": f"{BASE}{GUIDE_DE}#webpage"},
     "about": ["Audio-Mastering", "Lautheitsnormalisierung", "LUFS", "Metal"]},
    faq_schema(LGD_FAQS),
]
write(GUIDE_DE, page(path=GUIDE_DE, lang='de', title=LGD_TITLE,
      description='Wie laut sollte Metal gemastert werden? LUFS-Ziele der Streaming-Plattformen, typische Lautheit für Metalcore, Death, Black und Doom Metal und True-Peak-Grenzen.',
      og_title='Wie laut sollte Metal gemastert werden? — Polished', body=lgd_body, schemas=lgd_schemas,
      counterpart={'en': '/metal-mastering-loudness/', 'de': GUIDE_DE}))
