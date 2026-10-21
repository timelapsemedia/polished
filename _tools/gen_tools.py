# "Tools for bands": /tools/ + /de/tools/ and one page per Code Chaos Audio plugin (EN + DE).
# Executed from gen.py (shared namespace: page, sec, write, breadcrumb_html, ld helpers, BASE, PERSON ...).
#
# Facts come only from the product data in codechaos-store/products/<slug>/ (product.json, description.html)
# and, for Crucible, codechaos-seo/crucible.html + products/crucible-demo. Sales always stay on Gumroad
# (Code Chaos Audio). Frostfret, Hoarfell and both Black Metal Suite bundles went live on Gumroad on 2026-10-21
# (frostfret, frostfret-demo, hoarfell, hoarfell-demo, black-metal-suite, black-metal-suite-complete: HTTP 200).
# Frostfret/Hoarfell facts: products/<slug>/, plugins/<slug>/README.md, build/<slug>/loudness.json + make_demo.py.
# Assets: /assets/tools/<slug>-gui.{webp,jpg} (1200 px wide), <slug>-cover.jpg (OG image), demo MP3s (128 kbps),
# <bundle>-card.{webp,jpg} (800x450) and <bundle>-cover.jpg for the bundles.

TOOLS_TODAY = '2026-10-21'
GUMROAD = 'https://timberwolf688.gumroad.com/l/'
CCA = {"@type": "Organization", "@id": f"{BASE}/tools/#code-chaos-audio", "name": "Code Chaos Audio",
       "url": "https://codechaos-official.de/", "founder": PERSON}


def gum(permalink, campaign, lang):
    """Gumroad link with the UTM parameters agreed for polished.media (HTML-escaped for attributes)."""
    return html.escape(f'{GUMROAD}{permalink}?utm_source=polished&utm_medium=tools&utm_campaign={campaign}&utm_content={lang}')


def tool_path(slug, lang):
    return f'/de/tools/{slug}/' if lang == 'de' else f'/tools/{slug}/'


def eur(n, lang):
    if n == 0:
        return 'gratis' if lang == 'de' else 'free'
    return f'{n} €' if lang == 'de' else f'€{n}'


def mmss(s):
    s = int(round(s))
    return f'{s // 60}:{s % 60:02d}'


TT = {
    'en': dict(home='Home', hub='Tools for Bands', hub_path='/tools/', eyebrow='Tools for bands · Code Chaos Audio',
               demo='Free demo', free='Free download', buy='Buy on Gumroad', details='Details &amp; audio →',
               contact='/#contact', audit='Request an audio audit →',
               made='Made by <a href="/#engineer">Tim Borchert</a> under the label Code Chaos Audio · Sold on Gumroad · Updated October 2026',
               listen='Hear it', specs='At a <em>glance</em>', faq='{name} <em>FAQ</em>', related='More <em>tools</em>',
               master_h='Tool, mix or <em>master?</em>', spec_k='Detail', spec_v='{name}', shot='Screenshot',
               winmac='Windows 10/11 · macOS Apple Silicon', win='Windows 10/11 only', price_free='Free · pay what you want',
               checkout='Checkout, payment and any applicable taxes are handled by Gumroad. Polished only links to it.'),
    'de': dict(home='Startseite', hub='Tools für Bands', hub_path='/de/tools/', eyebrow='Tools für Bands · Code Chaos Audio',
               demo='Gratis-Demo', free='Gratis laden', buy='Auf Gumroad kaufen', details='Details &amp; Audio →',
               contact='/de/#kontakt', audit='Audio-Audit anfragen →',
               made='Entwickelt von <a href="/de/#tim">Tim Borchert</a> unter dem Label Code Chaos Audio · Verkauf über Gumroad · Stand: Oktober 2026',
               listen='Reinhören', specs='Auf einen <em>Blick</em>', faq='{name}: <em>FAQ</em>', related='Weitere <em>Tools</em>',
               master_h='Tool, Mix oder <em>Master?</em>', spec_k='Detail', spec_v='{name}', shot='Screenshot',
               winmac='Windows 10/11 · macOS Apple Silicon', win='Nur Windows 10/11', price_free='Gratis · Preis frei wählbar',
               checkout='Bestellung, Bezahlung und eventuell anfallende Steuern laufen komplett über Gumroad. Polished verlinkt nur dorthin.'),
}

# Plain system notes, identical wording on every page that has a macOS build (from description.html "Formats").
SYS_WINMAC = {
    'en': [('Windows', 'Windows 10/11: VST3 + Standalone'),
           ('macOS', 'Apple Silicon (arm64) only, no Intel build. VST3 + Standalone, <strong>not signed or notarized</strong>: macOS blocks it at first, allow it under System Settings → Privacy &amp; Security.'),
           ('AU / Logic Pro', 'No AU version, so Logic Pro is not supported.'),
           ('Copy protection', 'No licence server, no login, no online check.')],
    'de': [('Windows', 'Windows 10/11: VST3 + Standalone'),
           ('macOS', 'Nur Apple Silicon (arm64), kein Intel-Build. VST3 + Standalone, <strong>nicht signiert und nicht notarisiert</strong>: macOS blockiert das Plugin zuerst, freigeben unter Systemeinstellungen → Datenschutz &amp; Sicherheit.'),
           ('AU / Logic Pro', 'Keine AU-Version, Logic Pro wird daher nicht unterstützt.'),
           ('Kopierschutz', 'Kein Lizenzserver, kein Login, keine Online-Prüfung.')],
}
SYS_WIN = {
    'en': [('Windows', 'Windows 10/11: VST3 + Standalone'),
           ('macOS', 'No macOS build at the moment.')],
    'de': [('Windows', 'Windows 10/11: VST3 + Standalone'),
           ('macOS', 'Derzeit keine macOS-Version.')],
}

DEMO_NOTE = {
    'en': 'The free demo is the complete plugin; it plays a short noise burst every 45 seconds.',
    'de': 'Die Gratis-Demo ist das komplette Plugin; sie spielt alle 45 Sekunden einen kurzen Rauschstoß.',
}

# ---------------------------------------------------------------- TOOL DATA
TOOLS = {}

TOOLS['gravesaw'] = dict(
    slug='gravesaw', name='Gravesaw', permalink='gravesaw', demo='gravesaw-demo', price=19, os='winmac',
    category='Amp + cab plugin', category_de='Amp- und Cab-Plugin', genres=['black-metal-mastering', 'doom-gothic-mastering'],
    gui=('gravesaw', 1200, 624), cover=(1280, 720),
    audio=[('gravesaw-demo.mp3', {'en': 'Gravesaw demo: one DI riff at 170 BPM, six presets, then a full mix (26 s)',
                                  'de': 'Gravesaw-Demo: ein DI-Riff bei 170 BPM, sechs Presets, dann ein voller Mix (26 s)'})],
    chapters=[(0.0, 'DI guitar (dry, as recorded)', 'DI-Gitarre (trocken, wie aufgenommen)'),
              (2.824, 'Gravesaw: Cold Tremolo Lead', 'Gravesaw: Cold Tremolo Lead'),
              (5.647, 'Gravesaw: Carpathian Buzz', 'Gravesaw: Carpathian Buzz'),
              (8.471, 'Gravesaw: Frozen Wall Thick', 'Gravesaw: Frozen Wall Thick'),
              (11.294, 'Gravesaw: Raw Rehearsal Room', 'Gravesaw: Raw Rehearsal Room'),
              (14.118, 'Gravesaw: Tamed Fizz', 'Gravesaw: Tamed Fizz'),
              (16.941, 'Gravesaw: Four-Track Demo', 'Gravesaw: Four-Track Demo'),
              (19.765, 'Full mix: Wall Rhythm L/R double-track + Cold Tremolo Lead + Bass Grind + Black Metal Drum Kit',
               'Voller Mix: Wall Rhythm L/R als Doppelspur + Cold Tremolo Lead + Bass Grind + Black Metal Drum Kit')],
    related=['rimehall', 'frostfret', 'kick-bass-scope'], bundles=['black-metal-suite', 'black-metal-suite-complete'],
    en=dict(
        title='Gravesaw: Black Metal Amp + Cab Plugin (VST3) | Polished',
        og_title='Gravesaw: black metal amp + cab — Tools for bands',
        description='Gravesaw is a black metal amp with 19 built-in cabs for guitar and bass DI. How to prep a demo mix with it, real audio, honest system notes. €19.',
        card='Black metal amp with 19 built-in cabs for guitar and bass DI, from raw buzz to a thick wall.',
        h1='Gravesaw: <em>black metal amp and cab for DI guitar and bass</em>',
        lead='<strong>Gravesaw is a VST3 amp with the cab built in: plug in a guitar or bass DI and choose a voicing between raw buzz and a thick wall.</strong> It comes from Code Chaos Audio, the plugin label of Polished mastering engineer Tim Borchert, and it targets problems that show up again and again in black metal premasters: fizz that turns painful once the track gets louder, low end that clouds the tremolo, and noise between the riffs.',
        alt='Gravesaw plugin window: preamp section with Gate, Tight, Gain and Raw/Thick knobs, tone stack with Bass, Mid, Treble, Fizz and Presence, cab selector set to 4x12 Cold Bright, and input/output meters',
        caption='Gravesaw with the Carpathian Buzz preset. Gate, Tight and Gain sit before the distortion, the tone stack after it.',
        audio_note='Rendered with the plugin. The drums in the last section come from the Black Metal Drum Kit by Code Chaos Audio.',
        sections=[
            ('gs-demo-mix', 'Preparing a black metal demo mix <em>with Gravesaw and Rimehall</em>', '''    <p>This is the order that keeps a home recording easy to master. Everything happens in the mix, before anything goes to a mastering engineer.</p>
    <ol>
      <li><strong>Record two rhythm takes, not one.</strong> Start from the presets Wall Rhythm L and Wall Rhythm R, pan the takes hard left and right, and try the wide L/R cab pair that Gravesaw includes for double-tracked rhythm guitars.</li>
      <li><strong>Set the gate so the gaps stay silent.</strong> The gate sits in front of the amp (from -90 dBFS, which is off, up to -30 dBFS, with hold and hysteresis). Mastering compresses and limits, and any hiss between tremolo bursts comes up with it.</li>
      <li><strong>Use Tight before you reach for EQ.</strong> Tight is a high-pass in front of the distortion, adjustable from 20 to 400 Hz. Less low end into the gain stage means a tighter riff and more room for bass and kick. For a doom bottom, keep it low.</li>
      <li><strong>Decide on Fizz and the Tamed cabs on small speakers.</strong> Fizz shapes the top end above about 4 kHz. Six of the 19 cabs are harshness-tamed versions, for bright pickups and fizzy settings.</li>
      <li><strong>Run the bass DI through Gravesaw as well.</strong> The bass presets (Bass Grind, Bass Clank, Doom Bass Deep) and the three bass cabs give it grind. Low Blend mixes the clean DI low end back under the distortion, so the bottom stays solid.</li>
      <li><strong>Then add space.</strong> <a href="/tools/rimehall/">Rimehall</a> on the guitar bus puts the riff into a cold hall without burying it. Export the mix with 3 to 6 dB of headroom and no limiter on the master bus.</li>
    </ol>''', False),
            ('gs-mono', 'Why double-tracked guitars <em>have to survive mono</em>', '''    <p>Phones, Bluetooth speakers and many club and festival systems play your song in mono or close to it. Two separate performances panned left and right add up to a louder riff in the middle when they are summed. A single take that was copied, delayed or widened to fake a double can cancel parts of itself in mono, and the guitars suddenly sound thin and hollow.</p>
    <p>A master cannot repair that, because the problem sits inside the mix. That is why the audit at Polished checks the stereo image and phase of every mix before mastering. Recording real double-tracks with matching tones is the cheapest fix there is.</p>''', True),
        ],
        specs=[('Price', '€19 on Gumroad, free demo available'),
               ('Format', 'VST3 + Standalone, mono or stereo input'),
               ('Cabs', '19 built in: 10 guitar cabs, 6 harshness-tamed versions, 3 bass cabs. Synthesised from a model in code, not captured from real cabinets. Cab off for your own IR.'),
               ('Presets', '16 factory presets'),
               ('Gain stages', '4x oversampling with anti-aliased clipping'),
               ('Latency', '61 samples (1.4 ms at 44.1 kHz), reported to the DAW'),
               ('Output', 'Safety stage keeps peaks below -0.3 dBFS'),
               ('Testing', 'Automated checks on every preset. Not tried in every DAW yet.')],
        master='For rehearsal demos and pre-production, a Gravesaw tone in a rough mix is all you need. When the songs go to Bandcamp, streaming or a label, a separate mastering pass with fresh ears pays off: loudness for each platform, harshness under control, low end checked in mono. Polished starts every master with a written audio audit of your mix, so you know what to fix in the mix first. See <a href="/black-metal-mastering/">black metal mastering</a>.',
        faqs=[
            ('Does Gravesaw run on a Mac?', 'Yes, on Apple Silicon Macs (arm64) as VST3 and Standalone. There is no Intel build and no AU version, so Logic Pro is not supported. The macOS build is not signed or notarized: macOS blocks it at first, and you allow it under System Settings → Privacy &amp; Security.'),
            ('Can I use my own impulse responses?', 'Yes. Switch the cab off and load your own IR after Gravesaw. The 19 built-in cabs are the synthesised IRs of the Black Metal Tone Kit by Code Chaos Audio.'),
            ('Is there a free trial?', 'Yes. The Gravesaw demo on Gumroad is the full plugin with all 16 presets; it plays a short noise burst every 45 seconds.'),
            ('Does a good amp tone make mastering unnecessary?', 'No. Gravesaw shapes the guitar and bass inside your mix. Mastering works on the finished mix: loudness, tonal balance across the whole song, consistency across a release. A good tone makes that job easier, it does not replace it.'),
        ],
    ),
    de=dict(
        title='Gravesaw: Black-Metal-Amp + Cab als VST3 | Polished',
        og_title='Gravesaw: Black-Metal-Amp + Cab — Tools für Bands',
        description='Gravesaw ist ein Black-Metal-Amp mit 19 Cabs für Gitarre und Bass. So bereitest du damit einen Demo-Mix vor, mit echter Audio-Demo. 19 € auf Gumroad.',
        card='Black-Metal-Amp mit 19 eingebauten Cabs für Gitarren- und Bass-DI, von rohem Sägen bis zur dicken Wand.',
        h1='Gravesaw: <em>Black-Metal-Amp und Cab für DI-Gitarre und Bass</em>',
        lead='<strong>Gravesaw ist ein VST3-Amp mit eingebautem Cab: Gitarren- oder Bass-DI rein, dann die Färbung zwischen rohem Sägen und dicker Wand wählen.</strong> Er stammt von Code Chaos Audio, dem Plugin-Label von Polished-Mastering-Engineer Tim Borchert, und zielt auf Probleme, die in Black-Metal-Premastern immer wieder auftauchen: Fizz, der schmerzt, sobald der Track lauter wird, Bässe, die das Tremolo zumachen, und Rauschen zwischen den Riffs.',
        alt='Gravesaw-Pluginfenster: Preamp mit den Reglern Gate, Tight, Gain und Raw/Thick, Klangregelung mit Bass, Mid, Treble, Fizz und Presence, Cab-Auswahl auf 4x12 Cold Bright, Ein- und Ausgangsanzeigen',
        caption='Gravesaw mit dem Preset Carpathian Buzz. Gate, Tight und Gain sitzen vor der Verzerrung, die Klangregelung dahinter.',
        audio_note='Mit dem Plugin gerendert. Die Drums im letzten Abschnitt stammen aus dem Black Metal Drum Kit von Code Chaos Audio.',
        sections=[
            ('gs-demo-mix', 'Einen Black-Metal-Demo-Mix <em>mit Gravesaw und Rimehall vorbereiten</em>', '''    <p>In dieser Reihenfolge bleibt eine Heimaufnahme gut masterbar. Alles passiert im Mix, bevor irgendetwas zum Mastering geht.</p>
    <ol>
      <li><strong>Zwei Rhythmus-Takes aufnehmen, nicht einen.</strong> Mit den Presets Wall Rhythm L und Wall Rhythm R starten, die Takes hart links und rechts panen und das breite L/R-Cab-Paar ausprobieren, das Gravesaw für gedoppelte Rhythmusgitarren mitbringt.</li>
      <li><strong>Das Gate so setzen, dass die Pausen still bleiben.</strong> Das Gate sitzt vor dem Amp (von -90 dBFS, also aus, bis -30 dBFS, mit Hold und Hysterese). Beim Mastering wird komprimiert und limitiert, und jedes Rauschen zwischen den Tremolo-Phrasen kommt mit hoch.</li>
      <li><strong>Erst Tight, dann EQ.</strong> Tight ist ein Hochpass vor der Verzerrung, einstellbar von 20 bis 400 Hz. Weniger Bass in die Zerrstufe heißt ein strafferes Riff und mehr Platz für Bass und Kick. Für ein Doom-Fundament bleibt er tief.</li>
      <li><strong>Fizz und die Tamed-Cabs auf kleinen Lautsprechern entscheiden.</strong> Fizz formt die Höhen oberhalb von etwa 4 kHz. Sechs der 19 Cabs sind entschärfte Versionen für helle Tonabnehmer und fizzige Einstellungen.</li>
      <li><strong>Auch die Bass-DI durch Gravesaw schicken.</strong> Die Bass-Presets (Bass Grind, Bass Clank, Doom Bass Deep) und die drei Bass-Cabs geben ihm Biss. Low Blend mischt die saubere Tiefe der DI wieder unter die Verzerrung, damit das Fundament stabil bleibt.</li>
      <li><strong>Dann Raum dazu.</strong> <a href="/de/tools/rimehall/">Rimehall</a> auf dem Gitarrenbus setzt das Riff in eine kalte Halle, ohne es zu begraben. Den Mix mit 3 bis 6 dB Headroom und ohne Limiter auf der Summe exportieren.</li>
    </ol>''', False),
            ('gs-mono', 'Warum Doppelspuren <em>mono-kompatibel sein müssen</em>', '''    <p>Handys, Bluetooth-Boxen und viele Club- und Festival-Anlagen spielen deinen Song in Mono oder fast in Mono. Zwei getrennt eingespielte Takes, links und rechts gepannt, ergeben in Mono ein lauteres Riff in der Mitte. Ein einzelner Take, der kopiert, verzögert oder künstlich verbreitert wurde, löscht sich in Mono teilweise selbst aus, und die Gitarren klingen plötzlich dünn und hohl.</p>
    <p>Ein Master kann das nicht reparieren, weil das Problem im Mix sitzt. Deshalb prüft das Audit bei Polished vor jedem Master Stereobild und Phase. Echte Doppelspuren mit passendem Sound sind die günstigste Lösung, die es gibt.</p>''', True),
        ],
        specs=[('Preis', '19 € auf Gumroad, Gratis-Demo verfügbar'),
               ('Format', 'VST3 + Standalone, Mono- oder Stereo-Eingang'),
               ('Cabs', '19 eingebaut: 10 Gitarren-Cabs, 6 entschärfte Versionen, 3 Bass-Cabs. Im Code aus einem Modell synthetisiert, nicht von echten Boxen abgenommen. Cab abschaltbar für eigene IRs.'),
               ('Presets', '16 Werks-Presets'),
               ('Zerrstufen', '4-fach-Oversampling mit Anti-Aliasing'),
               ('Latenz', '61 Samples (1,4 ms bei 44,1 kHz), wird an die DAW gemeldet'),
               ('Ausgang', 'Sicherheitsstufe hält Spitzen unter -0,3 dBFS'),
               ('Tests', 'Automatische Prüfungen für jedes Preset. Noch nicht in jeder DAW ausprobiert.')],
        master='Für Proberaum-Demos und Vorproduktion reicht ein Gravesaw-Sound im groben Mix völlig. Wenn die Songs auf Bandcamp, zu Streamingdiensten oder zu einem Label gehen, lohnt sich ein eigener Mastering-Durchgang mit frischen Ohren: Lautheit für jede Plattform, Schärfe unter Kontrolle, Low End in Mono geprüft. Bei Polished beginnt jeder Master mit einem schriftlichen Audio-Audit deines Mixes, damit du weißt, was du vorher im Mix ändern solltest. Mehr dazu: <a href="/de/black-metal-mastering/">Black Metal Mastering</a>.',
        faqs=[
            ('Läuft Gravesaw auf dem Mac?', 'Ja, auf Macs mit Apple Silicon (arm64) als VST3 und Standalone. Es gibt keinen Intel-Build und keine AU-Version, Logic Pro wird daher nicht unterstützt. Der macOS-Build ist nicht signiert und nicht notarisiert: macOS blockiert ihn zuerst, du gibst ihn unter Systemeinstellungen → Datenschutz &amp; Sicherheit frei.'),
            ('Kann ich eigene Impulsantworten nutzen?', 'Ja. Das Cab abschalten und die eigene IR hinter Gravesaw laden. Die 19 eingebauten Cabs sind die synthetisierten IRs aus dem Black Metal Tone Kit von Code Chaos Audio.'),
            ('Gibt es eine kostenlose Testversion?', 'Ja. Die Gravesaw-Demo auf Gumroad ist das volle Plugin mit allen 16 Presets; sie spielt alle 45 Sekunden einen kurzen Rauschstoß.'),
            ('Macht ein guter Amp-Sound das Mastering überflüssig?', 'Nein. Gravesaw formt Gitarre und Bass innerhalb deines Mixes. Mastering arbeitet am fertigen Mix: Lautheit, Klangbalance über den ganzen Song, Einheitlichkeit über ein Release. Ein guter Sound macht diese Arbeit leichter, ersetzt sie aber nicht.'),
        ],
    ),
)

TOOLS['rimehall'] = dict(
    slug='rimehall', name='Rimehall', permalink='rimehall', demo='rimehall-demo', price=19, os='winmac',
    category='Reverb plugin', category_de='Hall-Plugin', genres=['black-metal-mastering', 'doom-gothic-mastering'],
    gui=('rimehall', 1200, 734), cover=(1280, 720),
    audio=[('rimehall-demo.mp3', {'en': 'Rimehall demo: a dry riff at 170 BPM, six presets, then a full mix (69 s)',
                                  'de': 'Rimehall-Demo: ein trockenes Riff bei 170 BPM, sechs Presets, dann ein voller Mix (69 s)'})],
    chapters=[(0.0, 'Dry: synthetic tremolo riff (Black Metal Tone Kit DI + amp + cab IRs)', 'Trocken: synthetisches Tremolo-Riff (DI, Amp und Cab-IRs aus dem Black Metal Tone Kit)'),
              (7.85, 'Rimehall: Frozen Forest', 'Rimehall: Frozen Forest'),
              (15.69, 'Rimehall: Moonlit Tremolo Bus', 'Rimehall: Moonlit Tremolo Bus'),
              (23.54, 'Rimehall: Cassette Cathedral', 'Rimehall: Cassette Cathedral'),
              (31.39, 'Rimehall: Ice Shimmer Choir', 'Rimehall: Ice Shimmer Choir'),
              (39.24, 'Rimehall: Grim Rehearsal Tape', 'Rimehall: Grim Rehearsal Tape'),
              (47.08, 'Rimehall: Northern Void', 'Rimehall: Northern Void'),
              (54.93, 'Full mix: guitars through Moonlit Tremolo Bus, bass + Black Metal Drum Kit dry', 'Voller Mix: Gitarren durch Moonlit Tremolo Bus, Bass und Black Metal Drum Kit trocken')],
    related=['gravesaw', 'hoarfell', 'kick-bass-scope'], bundles=['black-metal-suite', 'black-metal-suite-complete'],
    en=dict(
        title='Rimehall: Black Metal Reverb & Tape Plugin | Polished',
        og_title='Rimehall: cold reverb, shimmer & tape — Tools for bands',
        description='Rimehall puts a cold hall, octave shimmer and tape grit on one bus and ducks the reverb while the riff plays. Mix tips for mastering, real audio. €19.',
        card='Cold hall, octave shimmer and tape grit on one bus, with ducking so fast riffs stay clear.',
        h1='Rimehall: <em>cold reverb, shimmer and tape for black metal</em>',
        lead='<strong>Rimehall puts a dark hall, an octave shimmer and a tape stage on one bus, and ducks the reverb while the dry signal plays.</strong> It is part 2 of the Code Chaos Black Metal Suite by Tim Borchert, who also masters at Polished. Use it on tremolo guitars, keys or vocals to push them into the distance without washing out the riff.',
        alt='Rimehall plugin window: estimated decay graph for low, mid and high frequencies, level meters, Cold Hall knobs (pre-delay, size, decay, damping, Frost, modulation), Shimmer and Space section, Tape/Lo-fi section and output',
        caption='Rimehall with the Frozen Forest preset. The graph shows the estimated decay for lows, mids and highs.',
        audio_note='The dry riff is synthesised; the demo was rendered with the plugin code itself, no third-party samples.',
        sections=[
            ('rh-master', 'Reverb that still works <em>after mastering</em>', '''    <p>A limiter lowers the peaks and brings up everything quieter, and reverb tails are quieter than the riff. That is why a mix that sounds perfectly balanced often sounds wetter after mastering. Rimehall has four controls that help you plan for that:</p>
    <ul>
      <li><strong>Ducking</strong> pulls the reverb down by up to 18 dB while the dry signal plays and lets it bloom in the gaps. Blast beats and fast tremolo stay readable, and the hall still fills every pause.</li>
      <li><strong>Frost</strong> sets the character of the hall in one knob: up gives thinner, colder lows and a little more air, down gives a darker and fuller hall. Reverb with a lot of low end eats headroom that the master needs for kick and bass.</li>
      <li><strong>Width</strong> controls the stereo spread of the effect. Check the mix in mono before you export: very wide reverbs can shrink or collapse in mono, and the <a href="/black-metal-mastering/">black metal audit</a> lists that among the most common findings.</li>
      <li><strong>Hiss</strong> in the tape stage is optional. Use it on purpose, because limiting will lift it. You can also choose whether the tape colours only the reverb or the whole bus.</li>
    </ul>
    <p>One more habit that saves a mastering session: export with the full tail. Decays go up to 30 seconds, so leave enough silence at the end of the song and let the mastering engineer handle the fade.</p>''', False),
            ('rh-stems', 'Rimehall and <em>stem mastering</em>', '''    <p>If you send stems, print Rimehall into the stem it belongs to, or give the reverb its own FX stem. Then the reverb level can still be adjusted in mastering without touching the dry guitars. How to export stems correctly is explained in the <a href="/stem-mastering/">stem mastering guide</a>.</p>''', True),
        ],
        specs=[('Price', '€19 on Gumroad, free demo available'),
               ('Format', 'VST3 + Standalone'),
               ('Hall', '8-line feedback delay network, pre-delay up to 250 ms, decay 0.3 to 30 s, damping 1 to 18 kHz'),
               ('Shimmer', 'Octave up inside the feedback loop, 0 to 100 %, band-limited before the pitch shift'),
               ('Tape / lo-fi', 'Wow, flutter, asymmetric saturation, tape tone 2 to 20 kHz, optional hiss'),
               ('Ducking', 'Up to 18 dB'),
               ('Presets', '14 factory presets'),
               ('Latency', 'Constant 4 ms, reported to the host'),
               ('Testing', 'Automated checks on every preset, including extreme settings. Not tried in every DAW yet.')],
        master='Reverb decisions are mix decisions, and they are hard to judge on the same speakers you tracked on. If you are unsure whether the hall is too big, the written audio audit at Polished tells you before mastering starts, including whether the mix holds up in mono.',
        faqs=[
            ('Does Rimehall run on a Mac?', 'Yes, on Apple Silicon Macs (arm64) as VST3 and Standalone. There is no Intel build and no AU version, so Logic Pro is not supported. The macOS build is not signed or notarized, so you allow it once under System Settings → Privacy &amp; Security.'),
            ('Is there a free trial?', 'Yes. The Rimehall demo on Gumroad is the complete plugin; it plays a short burst of quiet noise every 45 seconds.'),
            ('Is Rimehall only for black metal?', 'It is built for black metal and dark ambient, and the presets are named that way (Frozen Forest, Cassette Cathedral, Northern Void). The controls themselves work on any bus where you want a dark, long reverb that steps back while the instrument plays.'),
        ],
    ),
    de=dict(
        title='Rimehall: Black-Metal-Hall & Tape-Plugin | Polished',
        og_title='Rimehall: kalter Hall, Shimmer & Tape — Tools für Bands',
        description='Rimehall vereint kalten Hall, Oktav-Shimmer und Tape auf einem Bus und duckt den Hall, solange das Riff spielt. Mix-Tipps fürs Mastering, echte Demo. 19 €.',
        card='Kalter Hall, Oktav-Shimmer und Tape-Dreck auf einem Bus, mit Ducking, damit schnelle Riffs klar bleiben.',
        h1='Rimehall: <em>kalter Hall, Shimmer und Tape für Black Metal</em>',
        lead='<strong>Rimehall vereint eine dunkle Halle, einen Oktav-Shimmer und eine Tape-Stufe auf einem Bus und duckt den Hall, solange das trockene Signal spielt.</strong> Es ist Teil 2 der Code Chaos Black Metal Suite von Tim Borchert, der auch bei Polished mastert. Auf Tremolo-Gitarren, Keys oder Vocals schiebt es Spuren in die Ferne, ohne das Riff zu verwaschen.',
        alt='Rimehall-Pluginfenster: Grafik der geschätzten Nachhallzeit für Tiefen, Mitten und Höhen, Pegelanzeigen, Regler der Cold-Hall-Sektion (Pre-Delay, Size, Decay, Damping, Frost, Modulation), Shimmer- und Space-Sektion, Tape/Lo-Fi-Sektion und Ausgang',
        caption='Rimehall mit dem Preset Frozen Forest. Die Grafik zeigt die geschätzte Nachhallzeit für Tiefen, Mitten und Höhen.',
        audio_note='Das trockene Riff ist synthetisiert; die Demo wurde mit dem Plugin-Code selbst gerendert, ohne fremde Samples.',
        sections=[
            ('rh-master', 'Hall, der auch <em>nach dem Mastering</em> passt', '''    <p>Ein Limiter senkt die Spitzen und hebt alles Leisere an, und Hallfahnen sind leiser als das Riff. Deshalb klingt ein Mix, der perfekt ausbalanciert wirkt, nach dem Mastering oft halliger. Rimehall hat vier Regler, mit denen du das einplanen kannst:</p>
    <ul>
      <li><strong>Ducking</strong> senkt den Hall um bis zu 18 dB, solange das trockene Signal spielt, und lässt ihn in den Pausen aufblühen. Blastbeats und schnelles Tremolo bleiben lesbar, und der Raum füllt trotzdem jede Lücke.</li>
      <li><strong>Frost</strong> stellt den Charakter der Halle mit einem Regler ein: nach oben dünnere, kältere Tiefen und etwas mehr Luft, nach unten eine dunklere, vollere Halle. Hall mit viel Bassanteil frisst Headroom, den der Master für Kick und Bass braucht.</li>
      <li><strong>Width</strong> regelt die Stereobreite des Effekts. Prüf den Mix vor dem Export in Mono: Sehr breite Hallräume können in Mono schrumpfen oder zusammenfallen, und das <a href="/de/black-metal-mastering/">Black-Metal-Audit</a> zählt das zu den häufigsten Befunden.</li>
      <li><strong>Hiss</strong> in der Tape-Stufe ist optional. Setz es bewusst ein, denn Limiting hebt es an. Außerdem wählst du, ob das Tape nur den Hall oder den ganzen Bus färbt.</li>
    </ul>
    <p>Noch eine Gewohnheit, die Zeit im Mastering spart: mit vollständiger Hallfahne exportieren. Die Nachhallzeit reicht bis 30 Sekunden, also am Songende genug Stille lassen und den Fade dem Mastering überlassen.</p>''', False),
            ('rh-stems', 'Rimehall und <em>Stem-Mastering</em>', '''    <p>Wenn du Stems schickst, rendere Rimehall in den Stem, zu dem er gehört, oder gib dem Hall einen eigenen FX-Stem. Dann lässt sich der Hallanteil im Mastering noch anpassen, ohne die trockenen Gitarren anzufassen. Wie man Stems richtig exportiert, steht im <a href="/de/stem-mastering/">Stem-Mastering-Ratgeber</a>.</p>''', True),
        ],
        specs=[('Preis', '19 € auf Gumroad, Gratis-Demo verfügbar'),
               ('Format', 'VST3 + Standalone'),
               ('Halle', 'Feedback-Delay-Netzwerk mit 8 Leitungen, Pre-Delay bis 250 ms, Nachhall 0,3 bis 30 s, Dämpfung 1 bis 18 kHz'),
               ('Shimmer', 'Oktave aufwärts in der Rückkopplungsschleife, 0 bis 100 %, vor dem Pitch-Shift bandbegrenzt'),
               ('Tape / Lo-Fi', 'Wow, Flutter, asymmetrische Sättigung, Tape-Ton 2 bis 20 kHz, optionales Rauschen'),
               ('Ducking', 'Bis 18 dB'),
               ('Presets', '14 Werks-Presets'),
               ('Latenz', 'Konstant 4 ms, wird an den Host gemeldet'),
               ('Tests', 'Automatische Prüfungen für jedes Preset, auch mit Extremwerten. Noch nicht in jeder DAW ausprobiert.')],
        master='Hall-Entscheidungen sind Mix-Entscheidungen, und auf denselben Boxen, auf denen du aufgenommen hast, sind sie schwer zu beurteilen. Wenn du unsicher bist, ob die Halle zu groß ist, sagt dir das schriftliche Audio-Audit bei Polished das vor dem Mastering, einschließlich der Frage, ob der Mix in Mono hält.',
        faqs=[
            ('Läuft Rimehall auf dem Mac?', 'Ja, auf Macs mit Apple Silicon (arm64) als VST3 und Standalone. Es gibt keinen Intel-Build und keine AU-Version, Logic Pro wird daher nicht unterstützt. Der macOS-Build ist nicht signiert und nicht notarisiert, du gibst ihn einmal unter Systemeinstellungen → Datenschutz &amp; Sicherheit frei.'),
            ('Gibt es eine kostenlose Testversion?', 'Ja. Die Rimehall-Demo auf Gumroad ist das komplette Plugin; sie spielt alle 45 Sekunden einen kurzen, leisen Rauschstoß.'),
            ('Ist Rimehall nur für Black Metal?', 'Es ist für Black Metal und Dark Ambient gebaut, und die Presets heißen entsprechend (Frozen Forest, Cassette Cathedral, Northern Void). Die Regler selbst funktionieren auf jedem Bus, auf dem du einen dunklen, langen Hall willst, der zurücktritt, solange das Instrument spielt.'),
        ],
    ),
)

TOOLS['kick-bass-scope'] = dict(
    slug='kick-bass-scope', name='Kick/Bass Scope', permalink='kick-bass-scope', demo=None, price=0, os='winmac',
    category='Analyzer plugin', category_de='Analyse-Plugin', genres=['death-metal-mastering', 'metalcore-djent-mastering'],
    gui=('kick-bass-scope', 1200, 768), gui2=('kick-bass-scope-out-of-phase', 1200, 768), cover=(1280, 720),
    audio=[], chapters=[],
    related=['crucible', 'gravesaw', 'shardstep'],
    en=dict(
        title='Kick/Bass Scope: Free Kick & Bass Phase Check | Polished',
        og_title='Kick/Bass Scope: free kick & bass phase check — Tools for bands',
        description='Free VST3 that lays kick and bass on top of each other, beat-synced, and warns when they cancel. Why kick/bass phase matters before mastering.',
        card='Free analyzer that lays kick and bass on top of each other and warns you when they cancel.',
        h1='Kick/Bass Scope: <em>see whether kick and bass cancel, for free</em>',
        lead='<strong>Kick/Bass Scope is a free VST3 analyzer that draws your kick and your bass on top of each other, locked to your DAW\'s beat, and shows whether they add up or cancel each other.</strong> Tim Borchert built it under his Code Chaos Audio label for fast electronic music. The problem it shows is the same in a death metal or metalcore mix: two low-end sources fighting over the same moment.',
        alt='Kick/Bass Scope window with kick waveform in orange, bass in blue and their sum in grey over half a bar at 145 BPM, peak meters for kick, bass and sum, and a kick/bass correlation of +0.32 marked as in phase',
        alt2='The same groove out of phase: correlation of -0.32 and the red warning that kick and bass cancel each other, suggesting to flip the bass polarity or shift the bass notes',
        caption='In phase: kick and bass add up where they overlap (correlation +0.32).',
        caption2='Out of phase: same groove, the correlation drops to -0.32 and the scope warns you.',
        audio_note='',
        sections=[
            ('kb-why', 'Why kick/bass phase matters <em>before mastering</em>', '''    <p>Kick and bass share the lowest octave of a metal mix. Where they overlap, their waves either add up or partly cancel, and both cases change what the master can do:</p>
    <ul>
      <li><strong>Cancelling:</strong> the low end loses energy exactly on the beat. Mastering EQ can only raise kick and bass together, which also raises everything that was already fine. The fix belongs in the mix: flip the bass polarity, shift the bass notes or adjust the kick sample. The scope's warning text suggests exactly that.</li>
      <li><strong>Adding up:</strong> the sum gets louder than either part, and in mastering the limiter grabs those moments first. The scope shows the peak of kick, bass and sum per window in dBFS against an adjustable clip line, so you see how much headroom the low end really takes.</li>
    </ul>
    <p>In metal the relationship changes every time the chain changes: a new kick sample, a different bass amp or cab, an extra filter. Check again after each of those, not only once at the start of the mix.</p>''', False),
            ('kb-routing', 'Routing in <em>two minutes</em>', '''    <ol>
      <li>Put the scope on the bass track.</li>
      <li>Send the kick to its sidechain input.</li>
      <li>If your DAW cannot feed a sidechain into an effect, switch Input to <em>Single input</em>: route the kick panned hard left and the bass hard right to one bus and put the scope there.</li>
      <li>Pick a window of 1/4, 1/2, 1 bar or 2 bars. It follows the host tempo and bar position, and keeps running freely when the transport is stopped.</li>
    </ol>
    <p>Your audio passes through untouched: the output is bit-for-bit identical to the input. That is why there is no audio demo on this page, there is nothing to hear. The two screenshots show what it measures.</p>''', True),
        ],
        specs=[('Price', 'Free on Gumroad, pay what you want'),
               ('Format', 'VST3 + Standalone'),
               ('Display', 'Kick and bass in two colours, optional sum curve, ghost of the previous window, zoom up to +24 dB'),
               ('Readouts', 'Peak per window in dBFS for kick, bass and sum, overlap time in ms'),
               ('Clip line', 'Adjustable from -12 to 0 dBFS, default -0.3 dBFS'),
               ('Correlation', '-1 to +1, measured where both actually play, with a plain warning when they are out of phase'),
               ('Presets', '13 factory presets (named for psytrance tempos, the windows work at any tempo your DAW sends)'),
               ('Audio path', 'Bit-for-bit pass-through, checked in automated tests')],
        master='The scope tells you whether kick and bass work together. It does not tell you how the whole mix translates to earbuds, car speakers and streaming normalisation. That is what the written audio audit at Polished covers, including phase between kick, bass and guitars. See <a href="/death-metal-mastering/">death metal mastering</a> and <a href="/metalcore-djent-mastering/">metalcore and djent mastering</a>.',
        faqs=[
            ('Is Kick/Bass Scope really free?', 'Yes. It is a pay-what-you-want product on Gumroad; you can enter 0 € and download it.'),
            ('Does it run on a Mac?', 'Yes, on Apple Silicon Macs (arm64) as VST3 and Standalone. There is no Intel build and no AU version, so Logic Pro is not supported. The macOS build is not signed or notarized, so you allow it once under System Settings → Privacy &amp; Security.'),
            ('My DAW cannot route a sidechain into an effect. Can I still use it?', 'Yes. Set Input to Single input, pan the kick hard left and the bass hard right on one bus and put the scope on that bus.'),
        ],
    ),
    de=dict(
        title='Kick/Bass Scope: Phase von Kick & Bass prüfen | Polished',
        og_title='Kick/Bass Scope: Kick und Bass gratis prüfen — Tools für Bands',
        description='Gratis-VST3, das Kick und Bass taktsynchron übereinanderlegt und warnt, wenn sie sich auslöschen. Warum die Phase vor dem Mastering zählt.',
        card='Gratis-Analyzer, der Kick und Bass übereinanderlegt und warnt, wenn sie sich gegenseitig auslöschen.',
        h1='Kick/Bass Scope: <em>sehen, ob sich Kick und Bass auslöschen, gratis</em>',
        lead='<strong>Kick/Bass Scope ist ein kostenloser VST3-Analyzer, der Kick und Bass übereinander zeichnet, synchron zum Takt deiner DAW, und zeigt, ob sie sich addieren oder gegenseitig auslöschen.</strong> Tim Borchert hat ihn unter seinem Label Code Chaos Audio für schnelle elektronische Musik gebaut. Das Problem, das er sichtbar macht, ist in einem Death-Metal- oder Metalcore-Mix dasselbe: zwei Bassquellen, die sich um denselben Moment streiten.',
        alt='Fenster von Kick/Bass Scope mit der Kick-Wellenform in Orange, dem Bass in Blau und der Summe in Grau über einen halben Takt bei 145 BPM, Spitzenanzeigen für Kick, Bass und Summe und eine Kick/Bass-Korrelation von +0,32, als phasengleich markiert',
        alt2='Derselbe Groove gegenphasig: Korrelation -0,32 und die rote Warnung, dass sich Kick und Bass auslöschen, mit dem Vorschlag, die Bass-Polarität zu drehen oder die Bassnoten zu verschieben',
        caption='Phasengleich: Wo sich Kick und Bass überlappen, addieren sie sich (Korrelation +0,32).',
        caption2='Gegenphasig: derselbe Groove, die Korrelation fällt auf -0,32 und der Scope warnt.',
        audio_note='',
        sections=[
            ('kb-why', 'Warum die Phase von Kick und Bass <em>vor dem Mastering</em> zählt', '''    <p>Kick und Bass teilen sich die tiefste Oktave eines Metal-Mixes. Wo sie sich überlappen, addieren sich ihre Wellen oder löschen sich teilweise aus, und beides verändert, was der Master leisten kann:</p>
    <ul>
      <li><strong>Auslöschung:</strong> Das Low End verliert genau auf dem Schlag Energie. Ein Mastering-EQ kann Kick und Bass nur gemeinsam anheben und hebt damit auch alles an, was schon gepasst hat. Die Lösung gehört in den Mix: Bass-Polarität drehen, Bassnoten verschieben oder das Kick-Sample anpassen. Genau das schlägt auch der Warnhinweis im Scope vor.</li>
      <li><strong>Addition:</strong> Die Summe wird lauter als jeder Teil allein, und im Mastering greift der Limiter genau diese Momente zuerst. Der Scope zeigt pro Fenster die Spitzen von Kick, Bass und Summe in dBFS gegen eine einstellbare Clip-Linie, damit du siehst, wie viel Headroom das Low End wirklich braucht.</li>
    </ul>
    <p>Im Metal ändert sich das Verhältnis mit jeder Änderung der Kette: ein neues Kick-Sample, ein anderer Bass-Amp oder ein anderes Cab, ein zusätzlicher Filter. Prüf nach jeder dieser Änderungen neu, nicht nur einmal zu Beginn des Mixes.</p>''', False),
            ('kb-routing', 'Routing in <em>zwei Minuten</em>', '''    <ol>
      <li>Den Scope auf die Bassspur legen.</li>
      <li>Die Kick auf seinen Sidechain-Eingang schicken.</li>
      <li>Wenn deine DAW keinen Sidechain in einen Effekt führen kann: Input auf <em>Single input</em> stellen, die Kick hart links und den Bass hart rechts auf einen gemeinsamen Bus routen und den Scope dort einsetzen.</li>
      <li>Ein Fenster von 1/4, 1/2, 1 Takt oder 2 Takten wählen. Es folgt Tempo und Taktposition des Hosts und läuft bei gestopptem Transport frei weiter.</li>
    </ol>
    <p>Dein Audio läuft unverändert durch: Der Ausgang ist Bit für Bit identisch mit dem Eingang. Deshalb gibt es hier keine Audio-Demo, es gibt nichts zu hören. Die beiden Screenshots zeigen, was er misst.</p>''', True),
        ],
        specs=[('Preis', 'Gratis auf Gumroad, Preis frei wählbar'),
               ('Format', 'VST3 + Standalone'),
               ('Anzeige', 'Kick und Bass in zwei Farben, optionale Summenkurve, Nachbild des vorigen Fensters, Zoom bis +24 dB'),
               ('Messwerte', 'Spitzenwert pro Fenster in dBFS für Kick, Bass und Summe, Überlappungszeit in ms'),
               ('Clip-Linie', 'Einstellbar von -12 bis 0 dBFS, Standard -0,3 dBFS'),
               ('Korrelation', '-1 bis +1, gemessen dort, wo beide wirklich spielen, mit klarer Warnung bei Gegenphase'),
               ('Presets', '13 Werks-Presets (nach Psytrance-Tempi benannt, die Fenster funktionieren bei jedem Tempo, das die DAW liefert)'),
               ('Signalweg', 'Bit-genaues Durchreichen, in automatischen Tests geprüft')],
        master='Der Scope sagt dir, ob Kick und Bass zusammenarbeiten. Er sagt dir nicht, wie der ganze Mix auf Earbuds, im Auto und mit der Lautheitsnormalisierung der Streamingdienste funktioniert. Das deckt das schriftliche Audio-Audit bei Polished ab, inklusive der Phase zwischen Kick, Bass und Gitarren. Siehe <a href="/de/death-metal-mastering/">Death Metal Mastering</a> und <a href="/de/metalcore-djent-mastering/">Metalcore &amp; Djent Mastering</a>.',
        faqs=[
            ('Ist Kick/Bass Scope wirklich kostenlos?', 'Ja. Es ist ein Pay-what-you-want-Produkt auf Gumroad; du kannst 0 € eingeben und es herunterladen.'),
            ('Läuft es auf dem Mac?', 'Ja, auf Macs mit Apple Silicon (arm64) als VST3 und Standalone. Es gibt keinen Intel-Build und keine AU-Version, Logic Pro wird daher nicht unterstützt. Der macOS-Build ist nicht signiert und nicht notarisiert, du gibst ihn einmal unter Systemeinstellungen → Datenschutz &amp; Sicherheit frei.'),
            ('Meine DAW kann keinen Sidechain in einen Effekt führen. Geht es trotzdem?', 'Ja. Input auf Single input stellen, die Kick hart links und den Bass hart rechts auf einen Bus legen und den Scope auf diesem Bus einsetzen.'),
        ],
    ),
)

TOOLS['crucible'] = dict(
    slug='crucible', name='Crucible', permalink='crucible', demo='crucible-demo', price=19, os='win',
    category='Saturation plugin', category_de='Sättigungs-Plugin', genres=['death-metal-mastering', 'metalcore-djent-mastering'],
    gui=('crucible', 1200, 764), cover=(1200, 630),
    audio=[('crucible-dry.mp3', {'en': 'A · Dry: a 190 BPM loop without Crucible (10 s)', 'de': 'A · Trocken: ein Loop mit 190 BPM ohne Crucible (10 s)'}),
           ('crucible-wet.mp3', {'en': 'B · Crucible: the same loop with Crucible (10 s)', 'de': 'B · Crucible: derselbe Loop mit Crucible (10 s)'})],
    chapters=[],
    related=['kick-bass-scope', 'gravesaw', 'chaos-fm'],
    en=dict(
        title='Crucible: 3-Band Saturation Plugin (VST3) | Polished',
        og_title='Crucible: 3-band saturation — Tools for bands',
        description='Crucible saturates low, mid and high separately with five types per band. A split-band approach to metal bass, real A/B audio, Windows VST3. €19.',
        card='3-band saturation with five types per band, for grinding bass mids while the low end stays solid.',
        h1='Crucible: <em>3-band saturation for bass, drums and buses</em>',
        lead='<strong>Crucible splits your signal into low, mid and high and saturates each band on its own, with five types per band: Hard Clip, Wavefolder, Tube, Diode and Tape.</strong> Tim Borchert built it under Code Chaos Audio for psytrance production. The same split solves a classic metal problem: a bass that needs grind in the mids while the lowest octave stays clean and solid.',
        alt='Crucible plugin window with three bands, Low set to Hard Clip, Mid to Tube and High to Tape, each with Drive, Mix and Gain knobs, Mute and Solo, level meters, oversampling set to 4x and a crossover bar at 120 Hz and 4000 Hz',
        caption='Crucible with the crossovers at 120 Hz and 4 kHz. Each band has its own saturation type, drive, mix and gain.',
        audio_note='The same 190 BPM psy loop without and with Crucible. Both files measure about -16.5 LUFS integrated, so you hear density and tone, not just volume.',
        sections=[
            ('cr-bass', 'Split-band saturation <em>for a metal bass</em>', '''    <p>Distorting a whole bass signal is the quickest way to lose the low end: the lowest notes turn into fuzz, and the mix gets muddy under the guitars. With three bands you can treat each register for what it has to do.</p>
    <ul>
      <li><strong>Low band:</strong> little or no drive. Keep it clean and steady, so kick and bass still work together. Check it with the free <a href="/tools/kick-bass-scope/">Kick/Bass Scope</a>.</li>
      <li><strong>Mid band:</strong> this is where the grind lives that cuts through rhythm guitars on small speakers. Diode or Hard Clip add bite, Tube is rounder.</li>
      <li><strong>High band:</strong> Tape softens string noise and fret clank, more drive brings it forward.</li>
    </ul>
    <p>The two crossovers are adjustable, and every band has its own Drive, Mix, Gain, Mute and Solo. For heavy settings, raise the oversampling (Off, 2x, 4x or 8x) to keep aliasing down.</p>''', False),
            ('cr-bus', 'Saturation on the mix bus <em>before mastering?</em>', '''    <p>Saturation lowers the difference between peaks and average level. Once it is printed into the mix, it cannot be undone in mastering, and an over-squashed premaster leaves the master with less room to work. If you like Crucible on your mix bus, send two versions to mastering: one with it and one without, and say which one you prefer. The audit at Polished flags over-limited and over-saturated premasters before anything is processed.</p>''', True),
        ],
        specs=[('Price', '€19 on Gumroad, free demo available'),
               ('Format', 'VST3 + Standalone'),
               ('Bands', '3 (Linkwitz-Riley crossover), two adjustable crossover points'),
               ('Saturation types', 'Hard Clip, Wavefolder, Tube, Diode, Tape, selectable per band'),
               ('Per band', 'Drive, Mix, Gain, Mute, Solo'),
               ('Oversampling', 'Off, 2x, 4x or 8x'),
               ('License', 'Single-user, perpetual')],
        master='Crucible helps you shape single instruments and buses. A balanced, loud and consistent release is still the job of a mastering pass. Polished starts every master with a written audio audit, so you know whether the saturation in your mix helps or costs headroom.',
        faqs=[
            ('Does Crucible run on a Mac?', 'Not at the moment. Crucible is a Windows 10/11 plugin (VST3 and Standalone).'),
            ('Is there a free trial?', 'Yes. The Crucible demo on Gumroad is the complete plugin with every band, every saturation type and oversampling up to 8x; it plays a short burst of quiet noise every 45 seconds.'),
            ('Should I put Crucible on my master bus before sending the mix to mastering?', 'Only if it is part of the sound you want. Send a second version without it as well, so the mastering engineer can choose. Saturation that is printed into the mix cannot be removed later.'),
        ],
    ),
    de=dict(
        title='Crucible: 3-Band-Sättigung als VST3 | Polished',
        og_title='Crucible: 3-Band-Sättigung — Tools für Bands',
        description='Crucible sättigt Tiefen, Mitten und Höhen getrennt, mit fünf Typen pro Band. Ein Weg zu mehr Biss im Metal-Bass, A/B-Demo, Windows-VST3. 19 €.',
        card='3-Band-Sättigung mit fünf Typen pro Band: Biss in den Bass-Mitten, während das Fundament sauber bleibt.',
        h1='Crucible: <em>3-Band-Sättigung für Bass, Drums und Busse</em>',
        lead='<strong>Crucible teilt dein Signal in Tiefen, Mitten und Höhen und sättigt jedes Band für sich, mit fünf Typen pro Band: Hard Clip, Wavefolder, Tube, Diode und Tape.</strong> Tim Borchert hat es unter Code Chaos Audio für Psytrance-Produktionen gebaut. Dieselbe Aufteilung löst ein klassisches Metal-Problem: einen Bass, der in den Mitten Biss braucht, während die tiefste Oktave sauber und stabil bleibt.',
        alt='Crucible-Pluginfenster mit drei Bändern, Low auf Hard Clip, Mid auf Tube und High auf Tape, jeweils mit Drive-, Mix- und Gain-Reglern, Mute und Solo, Pegelanzeigen, Oversampling auf 4x und einer Crossover-Leiste bei 120 Hz und 4000 Hz',
        caption='Crucible mit Trennfrequenzen bei 120 Hz und 4 kHz. Jedes Band hat eigenen Sättigungstyp, Drive, Mix und Gain.',
        audio_note='Derselbe Psy-Loop mit 190 BPM ohne und mit Crucible. Beide Dateien messen etwa -16,5 LUFS integriert, du hörst also Dichte und Klang, nicht nur Lautstärke.',
        sections=[
            ('cr-bass', 'Mehrband-Sättigung <em>für einen Metal-Bass</em>', '''    <p>Ein komplettes Basssignal zu verzerren ist der schnellste Weg, das Fundament zu verlieren: Die tiefsten Töne werden zu Matsch, und unter den Gitarren wird es dumpf. Mit drei Bändern behandelst du jedes Register nach seiner Aufgabe.</p>
    <ul>
      <li><strong>Tiefes Band:</strong> wenig oder kein Drive. Sauber und stabil halten, damit Kick und Bass weiter zusammenarbeiten. Prüfen kannst du das mit dem kostenlosen <a href="/de/tools/kick-bass-scope/">Kick/Bass Scope</a>.</li>
      <li><strong>Mittleres Band:</strong> Hier sitzt der Biss, der auf kleinen Lautsprechern durch die Rhythmusgitarren kommt. Diode oder Hard Clip machen ihn bissiger, Tube runder.</li>
      <li><strong>Hohes Band:</strong> Tape glättet Saitengeräusche und Bundklappern, mehr Drive holt sie nach vorn.</li>
    </ul>
    <p>Die beiden Trennfrequenzen sind einstellbar, und jedes Band hat eigene Regler für Drive, Mix, Gain, Mute und Solo. Bei starker Sättigung das Oversampling erhöhen (Aus, 2x, 4x oder 8x), damit Aliasing gering bleibt.</p>''', False),
            ('cr-bus', 'Sättigung auf der Summe <em>vor dem Mastering?</em>', '''    <p>Sättigung verringert den Abstand zwischen Spitzen und Durchschnittspegel. Ist sie einmal in den Mix gerendert, lässt sie sich im Mastering nicht mehr zurücknehmen, und ein zu stark verdichteter Premaster lässt dem Master weniger Spielraum. Wenn dir Crucible auf der Summe gefällt, schick zwei Versionen zum Mastering: eine mit und eine ohne, und sag dazu, welche du bevorzugst. Das Audit bei Polished weist auf überlimitierte und übersättigte Premaster hin, bevor irgendetwas bearbeitet wird.</p>''', True),
        ],
        specs=[('Preis', '19 € auf Gumroad, Gratis-Demo verfügbar'),
               ('Format', 'VST3 + Standalone'),
               ('Bänder', '3 (Linkwitz-Riley-Weiche), zwei einstellbare Trennfrequenzen'),
               ('Sättigungstypen', 'Hard Clip, Wavefolder, Tube, Diode, Tape, pro Band wählbar'),
               ('Pro Band', 'Drive, Mix, Gain, Mute, Solo'),
               ('Oversampling', 'Aus, 2x, 4x oder 8x'),
               ('Lizenz', 'Einzelplatz, unbefristet')],
        master='Crucible hilft dir, einzelne Instrumente und Busse zu formen. Ein ausgewogenes, lautes und einheitliches Release bleibt die Aufgabe eines Mastering-Durchgangs. Bei Polished beginnt jeder Master mit einem schriftlichen Audio-Audit, damit du weißt, ob die Sättigung in deinem Mix hilft oder Headroom kostet.',
        faqs=[
            ('Läuft Crucible auf dem Mac?', 'Derzeit nicht. Crucible ist ein Plugin für Windows 10/11 (VST3 und Standalone).'),
            ('Gibt es eine kostenlose Testversion?', 'Ja. Die Crucible-Demo auf Gumroad ist das komplette Plugin mit allen Bändern, allen Sättigungstypen und Oversampling bis 8x; sie spielt alle 45 Sekunden einen kurzen, leisen Rauschstoß.'),
            ('Soll ich Crucible vor dem Mastering auf die Summe legen?', 'Nur, wenn es Teil des Sounds ist, den du willst. Schick zusätzlich eine Version ohne, damit beim Mastering gewählt werden kann. Einmal in den Mix gerenderte Sättigung lässt sich später nicht mehr entfernen.'),
        ],
    ),
)

TOOLS['shardstep'] = dict(
    slug='shardstep', name='Shardstep', permalink='shardstep', demo='shardstep-demo', price=15, os='winmac',
    category='Stutter and glitch plugin', category_de='Stutter- und Glitch-Plugin', genres=['metalcore-djent-mastering'],
    gui=('shardstep', 1200, 720), cover=(1280, 720),
    audio=[('shardstep-dry.mp3', {'en': 'A · Dry: the demo loop without Shardstep (38 s)', 'de': 'A · Trocken: der Demo-Loop ohne Shardstep (38 s)'}),
           ('shardstep-wet.mp3', {'en': 'B · Shardstep: the same loop with Shardstep (38 s)', 'de': 'B · Shardstep: derselbe Loop mit Shardstep (38 s)'})],
    chapters=[],
    related=['chaos-fm', 'crucible', 'kick-bass-scope'],
    en=dict(
        title='Shardstep: Stutter & Glitch Plugin for 200+ BPM | Polished',
        og_title='Shardstep: tempo-synced stutter & glitch — Tools for bands',
        description='Shardstep chops, repeats, reverses and tape-stops audio in time with your DAW, click-free at 200 to 300 BPM. Glitch fills that survive mastering. €15.',
        card='Tempo-synced stutter, tape stop and glitch fills for 200 to 300 BPM, click-free at every slice.',
        h1='Shardstep: <em>tempo-synced stutter and glitch for 200+ BPM</em>',
        lead='<strong>Shardstep chops, repeats, reverses and tape-stops audio in time with your DAW, with a short crossfade on every slice edge so nothing clicks.</strong> Tim Borchert\'s label Code Chaos Audio made it for hitech and psycore at 200 to 300 BPM. For bands it fits industrial and electronic crossover songs, breakdown fills and transitions where a guitar or drum bus should stutter on the grid.',
        alt='Shardstep plugin window: a 16-step pattern over one bar with steps set to 1/32, Tie, Reverse, 1/16, Gate, 1/32T and Tape, sound controls for Mix, Repeat Pitch, Slice Fade, Crush Bits and Downsample, and the MIDI trigger key map',
        caption='Shardstep at 200 BPM, synced to the host: one bar of 16 steps, each with its own effect.',
        audio_note='The same loop without and with Shardstep. The version with Shardstep measures about 0.6 LU louder (integrated), so keep that in mind when you compare.',
        sections=[
            ('sh-clicks', 'Glitch edits that <em>survive mastering</em>', '''    <p>At 250 BPM a 1/32 repeat lasts 30 ms and a 1/64 only 15 ms. Cut audio that short without a fade and every slice edge clicks. In the mix those clicks are easy to miss; after mastering, when the limiter has raised everything, they become audible and they eat headroom like extra transients.</p>
    <ul>
      <li><strong>Slice Fade</strong> puts a raised-cosine crossfade from 0.5 to 8 ms on every slice edge and every retrigger. Longer fades are smoother, shorter ones snappier.</li>
      <li><strong>Untouched when idle:</strong> when nothing plays (transport stopped, empty pattern, mix at 0 % or a bar the pattern skips), the audio passes through bit for bit. The rest of the song keeps its sound.</li>
      <li><strong>Zero latency:</strong> repeats replay audio that has already arrived, so the track stays in time with the rest of the mix.</li>
    </ul>
    <p>One practical habit: render or freeze the stutter track before you send stems or a mix to anyone. A pattern that depends on the DAW transport and bar position is easy to change by accident.</p>''', False),
            ('sh-band', 'Using it in a <em>band mix</em>', '''    <p>Patterns play every bar or only on the last bar of 2, 4 or 8, which is how fills and drops work. Hold a MIDI note to fire an effect by hand (C = 1/8 up to A# = Crush, any octave); a held note overrides the pattern and also works with the transport stopped. Among the 15 factory patterns is one called Bar 8 Breakdown Drop.</p>
    <p>Short repeats of a kick (1/64) are shorter than one cycle of the kick and can sit slightly off centre while they play. The signal returns to your untouched audio as soon as the effect ends.</p>''', True),
        ],
        specs=[('Price', '€15 on Gumroad, free demo available'),
               ('Format', 'VST3 + Standalone (the Standalone has no transport, so you play the effects with MIDI notes there)'),
               ('Pattern', '16 steps, one bar of sixteenths, synced to host tempo and bar position'),
               ('Effects per step', 'Repeat 1/8, 1/16, 1/32, 1/64, 1/8T, 1/16T, 1/32T, Reverse, Tape Stop, Gate, Crush, Tie'),
               ('Repeat Pitch', '-24 to +12 semitones'),
               ('Tape stop, gate, crush', 'Tape stop 1/16 to one bar; gate 1/16, 1/32 or 1/64; bitcrush 3 to 16 bit with 1 to 32x downsampling'),
               ('Presets', '15 factory patterns'),
               ('Testing', 'Automated checks on every pattern at 150, 200 and 260 BPM, including tempo ramps and transport stops. Not tried in every DAW yet.')],
        master='Effects like these are the moments a mastering engineer listens to twice: drops, stops and fills are where clicks, level jumps and limiter pumping show up first. The written audio audit at Polished lists them with timestamps before the master is made.',
        faqs=[
            ('Does Shardstep run on a Mac?', 'Yes, on Apple Silicon Macs (arm64) as VST3 and Standalone. There is no Intel build and no AU version, so Logic Pro is not supported. The macOS build is not signed or notarized, so you allow it once under System Settings → Privacy &amp; Security.'),
            ('Is there a free trial?', 'Yes. The Shardstep demo on Gumroad is the full plugin with a short noise burst every 45 seconds.'),
            ('Does Shardstep work below 200 BPM?', 'Yes. The pattern follows whatever tempo your DAW sends; the automated tests also run at 150 BPM. It was designed with very fast tempos in mind, where clicks are the biggest problem.'),
        ],
    ),
    de=dict(
        title='Shardstep: Stutter & Glitch für 200+ BPM | Polished',
        og_title='Shardstep: taktsynchroner Stutter & Glitch — Tools für Bands',
        description='Shardstep zerhackt, wiederholt, dreht um und stoppt Audio im DAW-Takt, klickfrei bei 200 bis 300 BPM. Glitch-Fills, die das Mastering überstehen. 15 €.',
        card='Taktsynchroner Stutter, Tape-Stop und Glitch-Fills für 200 bis 300 BPM, klickfrei an jeder Schnittkante.',
        h1='Shardstep: <em>taktsynchroner Stutter und Glitch für 200+ BPM</em>',
        lead='<strong>Shardstep zerhackt, wiederholt, dreht um und stoppt Audio im Takt deiner DAW, mit einer kurzen Überblendung an jeder Schnittkante, damit nichts klickt.</strong> Tim Borcherts Label Code Chaos Audio hat es für Hitech und Psycore mit 200 bis 300 BPM gebaut. Für Bands passt es zu Industrial- und Electronic-Crossover-Songs, Breakdown-Fills und Übergängen, in denen ein Gitarren- oder Drumbus im Raster stottern soll.',
        alt='Shardstep-Pluginfenster: ein 16-Step-Pattern über einen Takt mit Steps auf 1/32, Tie, Reverse, 1/16, Gate, 1/32T und Tape, Klangregler für Mix, Repeat Pitch, Slice Fade, Crush Bits und Downsample sowie die Tastenbelegung für MIDI-Trigger',
        caption='Shardstep bei 200 BPM, synchron zum Host: ein Takt mit 16 Steps, jeder mit eigenem Effekt.',
        audio_note='Derselbe Loop ohne und mit Shardstep. Die Version mit Shardstep misst etwa 0,6 LU mehr (integriert), das beim Vergleichen bitte bedenken.',
        sections=[
            ('sh-clicks', 'Glitch-Edits, die <em>das Mastering überstehen</em>', '''    <p>Bei 250 BPM dauert eine 1/32-Wiederholung 30 ms und eine 1/64 nur 15 ms. Wer Audio so kurz ohne Fade schneidet, bekommt an jeder Schnittkante einen Klick. Im Mix gehen diese Klicks leicht unter; nach dem Mastering, wenn der Limiter alles angehoben hat, werden sie hörbar und fressen Headroom wie zusätzliche Transienten.</p>
    <ul>
      <li><strong>Slice Fade</strong> legt an jede Schnittkante und jeden Neustart eine Raised-Cosine-Überblendung von 0,5 bis 8 ms. Längere Fades klingen weicher, kürzere knackiger.</li>
      <li><strong>Unverändert im Leerlauf:</strong> Wenn nichts spielt (Transport gestoppt, leeres Pattern, Mix auf 0 % oder ein Takt, den das Pattern auslässt), läuft das Audio Bit für Bit durch. Der Rest des Songs behält seinen Klang.</li>
      <li><strong>Null Latenz:</strong> Wiederholungen spielen Audio ab, das schon angekommen ist, die Spur bleibt also im Timing mit dem restlichen Mix.</li>
    </ul>
    <p>Eine praktische Gewohnheit: Die Stutter-Spur rendern oder einfrieren, bevor du Stems oder einen Mix weitergibst. Ein Pattern, das am Transport und an der Taktposition der DAW hängt, verändert sich leicht aus Versehen.</p>''', False),
            ('sh-band', 'Im <em>Band-Mix</em> einsetzen', '''    <p>Patterns laufen in jedem Takt oder nur im letzten Takt von 2, 4 oder 8, so entstehen Fills und Drops. Mit einer gehaltenen MIDI-Note löst du einen Effekt von Hand aus (C = 1/8 bis A# = Crush, in jeder Oktave); eine gehaltene Note hat Vorrang vor dem Pattern und funktioniert auch bei gestopptem Transport. Unter den 15 Werks-Patterns ist eines namens Bar 8 Breakdown Drop.</p>
    <p>Kurze Wiederholungen einer Kick (1/64) sind kürzer als eine Schwingung der Kick und können während des Effekts leicht aus der Mitte rutschen. Sobald der Effekt endet, ist wieder dein unbearbeitetes Audio da.</p>''', True),
        ],
        specs=[('Preis', '15 € auf Gumroad, Gratis-Demo verfügbar'),
               ('Format', 'VST3 + Standalone (die Standalone-Version hat keinen Transport, dort spielst du die Effekte per MIDI-Note)'),
               ('Pattern', '16 Steps, ein Takt in Sechzehnteln, synchron zu Tempo und Taktposition des Hosts'),
               ('Effekte pro Step', 'Repeat 1/8, 1/16, 1/32, 1/64, 1/8T, 1/16T, 1/32T, Reverse, Tape Stop, Gate, Crush, Tie'),
               ('Repeat Pitch', '-24 bis +12 Halbtöne'),
               ('Tape-Stop, Gate, Crush', 'Tape-Stop 1/16 bis ein Takt; Gate 1/16, 1/32 oder 1/64; Bitcrush 3 bis 16 Bit mit 1- bis 32-fachem Downsampling'),
               ('Presets', '15 Werks-Patterns'),
               ('Tests', 'Automatische Prüfungen für jedes Pattern bei 150, 200 und 260 BPM, auch mit Tempoänderungen und Transport-Stopps. Noch nicht in jeder DAW ausprobiert.')],
        master='Solche Effekte sind die Stellen, die man sich beim Mastering zweimal anhört: Drops, Stopps und Fills zeigen Klicks, Pegelsprünge und Limiter-Pumpen zuerst. Das schriftliche Audio-Audit bei Polished listet sie mit Zeitangabe auf, bevor der Master entsteht.',
        faqs=[
            ('Läuft Shardstep auf dem Mac?', 'Ja, auf Macs mit Apple Silicon (arm64) als VST3 und Standalone. Es gibt keinen Intel-Build und keine AU-Version, Logic Pro wird daher nicht unterstützt. Der macOS-Build ist nicht signiert und nicht notarisiert, du gibst ihn einmal unter Systemeinstellungen → Datenschutz &amp; Sicherheit frei.'),
            ('Gibt es eine kostenlose Testversion?', 'Ja. Die Shardstep-Demo auf Gumroad ist das volle Plugin mit einem kurzen Rauschstoß alle 45 Sekunden.'),
            ('Funktioniert Shardstep auch unter 200 BPM?', 'Ja. Das Pattern folgt jedem Tempo, das deine DAW liefert; die automatischen Tests laufen auch bei 150 BPM. Gebaut wurde es für sehr schnelle Tempi, bei denen Klicks das größte Problem sind.'),
        ],
    ),
)

TOOLS['chaos-fm'] = dict(
    slug='chaos-fm', name='Chaos FM', permalink='chaos-fm', demo='chaos-fm-demo', price=19, os='win',
    category='Synthesizer plugin', category_de='Synthesizer-Plugin', genres=['metalcore-djent-mastering'],
    gui=('chaos-fm', 1200, 791), cover=(1280, 720),
    audio=[], chapters=[],
    related=['shardstep', 'crucible', 'kick-bass-scope'],
    en=dict(
        title='Chaos FM: 3-Operator FM Synth (VST3, Windows) | Polished',
        og_title='Chaos FM: 3-operator FM synth — Tools for bands',
        description='Chaos FM is a 3-operator FM synth with a GENERATE button for leads, basses and stabs. How to fit FM synths into a guitar mix. Windows VST3, €19.',
        card='3-operator FM synth with a GENERATE button for metallic leads, bass layers and stabs.',
        h1='Chaos FM: <em>3-operator FM synth for electronic layers</em>',
        lead='<strong>Chaos FM is a three-operator FM synth with a GENERATE button that rolls a new, playable patch for the category you pick: lead, bass, acid, stab, pluck or FX.</strong> Code Chaos Audio, Tim Borchert\'s plugin label, built it for hitech and psycore. For bands it is a quick source of metallic leads, synth bass layers and stabs in industrial or electronic crossover songs. Windows only.',
        alt='Chaos FM plugin window with three operator sections (A carrier, B modulator, C modulator with feedback), each with ratio, fine, level and ADSR, plus algorithm, filter and voice controls, the preset Hitech Scream Lead and a GENERATE button',
        caption='Chaos FM with the preset Hitech Scream Lead. Every operator has its own ratio, level and envelope.',
        audio_note='',
        sections=[
            ('fm-mix', 'FM synths in a guitar mix, <em>before mastering</em>', '''    <p>FM sounds are bright and dense by nature, and in a metal mix they compete with cymbals and guitar fizz for the same upper range. A few habits keep them from becoming the harshest part of the master:</p>
    <ul>
      <li><strong>Use the filter.</strong> Chaos FM has a zero-delay lowpass with envelope amount and drive. Closing it a little takes the edge off before any EQ is needed.</li>
      <li><strong>Check unison in mono.</strong> Up to four unison voices with stereo spread sound wide on headphones; detuned voices can thin out when the mix is summed to mono.</li>
      <li><strong>Keep synth bass and kick apart.</strong> In mono/legato mode with glide, a synth bass can follow the bass guitar. Check its relationship to the kick with the free <a href="/tools/kick-bass-scope/">Kick/Bass Scope</a>.</li>
      <li><strong>Save what GENERATE gives you.</strong> A rolled patch is gone once you roll again. Save it or print the part to audio before the mix goes out.</li>
    </ul>''', False),
            ('fm-try', 'How to <em>hear it first</em>', '''    <p>There is no separate audio demo on this page. The quickest way to hear Chaos FM in your own song is the free demo on Gumroad: the full synth, with a short noise burst every 45 seconds. It runs on Windows only.</p>''', True),
        ],
        specs=[('Price', '€19 on Gumroad, free demo available'),
               ('Format', 'VST3 + Standalone'),
               ('Operators', '3 (carrier + 2 modulators), each with ratio, fine, level and full ADSR'),
               ('Algorithms', '3, feedback on operator C'),
               ('Filter', 'Zero-delay lowpass with envelope amount and drive'),
               ('Voices', 'Up to 4-voice unison with stereo spread, mono/legato with glide'),
               ('Presets', '12 factory presets plus GENERATE for Lead, Bass, Acid, Stab, Pluck and FX')],
        master='Synth layers change the balance of a band mix more than one might expect, especially in the top end. If you are unsure whether they sit right, the written audio audit at Polished checks the frequency balance before the master is made.',
        faqs=[
            ('Does Chaos FM run on a Mac?', 'No. Chaos FM is a Windows 10/11 plugin (VST3 and Standalone).'),
            ('Is there a free trial?', 'Yes. The Chaos FM demo on Gumroad is the full synth with presets and GENERATE; it plays a short noise burst every 45 seconds.'),
            ('What does the GENERATE button do?', 'It creates a new patch for the category you pick (Lead, Bass, Acid, Stab, Pluck or FX), built to stay musically usable instead of random noise.'),
        ],
    ),
    de=dict(
        title='Chaos FM: 3-Operator-FM-Synth (VST3, Windows) | Polished',
        og_title='Chaos FM: 3-Operator-FM-Synth — Tools für Bands',
        description='Chaos FM ist ein 3-Operator-FM-Synth mit GENERATE-Button für Leads, Bässe und Stabs. So passen FM-Synths in einen Gitarrenmix. Windows-VST3, 19 €.',
        card='3-Operator-FM-Synth mit GENERATE-Button für metallische Leads, Synth-Bässe und Stabs.',
        h1='Chaos FM: <em>3-Operator-FM-Synth für elektronische Layer</em>',
        lead='<strong>Chaos FM ist ein FM-Synth mit drei Operatoren und einem GENERATE-Button, der für die gewählte Kategorie einen neuen, spielbaren Sound würfelt: Lead, Bass, Acid, Stab, Pluck oder FX.</strong> Code Chaos Audio, das Plugin-Label von Tim Borchert, hat ihn für Hitech und Psycore gebaut. Für Bands ist er eine schnelle Quelle für metallische Leads, Synth-Bass-Layer und Stabs in Industrial- oder Electronic-Crossover-Songs. Nur für Windows.',
        alt='Chaos-FM-Pluginfenster mit drei Operator-Sektionen (A Träger, B Modulator, C Modulator mit Feedback), jeweils mit Ratio, Fine, Level und ADSR, dazu Regler für Algorithmus, Filter und Stimmen, das Preset Hitech Scream Lead und ein GENERATE-Button',
        caption='Chaos FM mit dem Preset Hitech Scream Lead. Jeder Operator hat eigene Ratio, eigenen Pegel und eigene Hüllkurve.',
        audio_note='',
        sections=[
            ('fm-mix', 'FM-Synths im Gitarrenmix, <em>vor dem Mastering</em>', '''    <p>FM-Sounds sind von Natur aus hell und dicht, und im Metal-Mix konkurrieren sie mit Becken und Gitarren-Fizz um denselben oberen Bereich. Ein paar Gewohnheiten verhindern, dass sie zum schärfsten Teil des Masters werden:</p>
    <ul>
      <li><strong>Den Filter nutzen.</strong> Chaos FM hat einen Zero-Delay-Tiefpass mit Hüllkurvenanteil und Drive. Ein wenig zudrehen nimmt die Schärfe, bevor überhaupt ein EQ nötig ist.</li>
      <li><strong>Unison in Mono prüfen.</strong> Bis zu vier Unison-Stimmen mit Stereobreite klingen auf Kopfhörern breit; verstimmte Stimmen können dünn werden, wenn der Mix in Mono summiert wird.</li>
      <li><strong>Synth-Bass und Kick trennen.</strong> Im Mono/Legato-Modus mit Glide kann ein Synth-Bass dem E-Bass folgen. Das Verhältnis zur Kick prüfst du mit dem kostenlosen <a href="/de/tools/kick-bass-scope/">Kick/Bass Scope</a>.</li>
      <li><strong>Speichern, was GENERATE liefert.</strong> Ein gewürfelter Sound ist weg, sobald du neu würfelst. Speichern oder die Spur als Audio rendern, bevor der Mix rausgeht.</li>
    </ul>''', False),
            ('fm-try', 'So hörst du <em>ihn zuerst</em>', '''    <p>Auf dieser Seite gibt es keine eigene Audio-Demo. Am schnellsten hörst du Chaos FM in deinem eigenen Song mit der Gratis-Demo auf Gumroad: der volle Synth, mit einem kurzen Rauschstoß alle 45 Sekunden. Er läuft nur unter Windows.</p>''', True),
        ],
        specs=[('Preis', '19 € auf Gumroad, Gratis-Demo verfügbar'),
               ('Format', 'VST3 + Standalone'),
               ('Operatoren', '3 (Träger + 2 Modulatoren), jeweils mit Ratio, Fine, Level und voller ADSR-Hüllkurve'),
               ('Algorithmen', '3, Feedback auf Operator C'),
               ('Filter', 'Zero-Delay-Tiefpass mit Hüllkurvenanteil und Drive'),
               ('Stimmen', 'Bis zu 4-fach-Unison mit Stereobreite, Mono/Legato mit Glide'),
               ('Presets', '12 Werks-Presets plus GENERATE für Lead, Bass, Acid, Stab, Pluck und FX')],
        master='Synth-Layer verschieben die Balance eines Band-Mixes stärker als gedacht, vor allem in den Höhen. Wenn du unsicher bist, ob sie richtig sitzen, prüft das schriftliche Audio-Audit bei Polished die Frequenzbalance, bevor der Master entsteht.',
        faqs=[
            ('Läuft Chaos FM auf dem Mac?', 'Nein. Chaos FM ist ein Plugin für Windows 10/11 (VST3 und Standalone).'),
            ('Gibt es eine kostenlose Testversion?', 'Ja. Die Chaos-FM-Demo auf Gumroad ist der volle Synth mit Presets und GENERATE; sie spielt alle 45 Sekunden einen kurzen Rauschstoß.'),
            ('Was macht der GENERATE-Button?', 'Er erzeugt einen neuen Sound für die gewählte Kategorie (Lead, Bass, Acid, Stab, Pluck oder FX), so gebaut, dass er musikalisch brauchbar bleibt statt zufälliges Rauschen zu liefern.'),
        ],
    ),
)

TOOLS['frostfret'] = dict(
    slug='frostfret', name='Frostfret', permalink='frostfret', demo='frostfret-demo', price=29, os='winmac', instrument=True,
    category='Virtual instrument (modelled guitar and bass)', category_de='Virtuelles Instrument (modellierte Gitarre und Bass)',
    genres=['black-metal-mastering', 'doom-gothic-mastering'],
    gui=('frostfret', 1200, 832), cover=(1280, 720),
    # Timings from plugins/frostfret/tools/make_demo.py (170 BPM: 1 bar = 1.412 s; acoustic switch at 12.6 s; clean/crunch at 11.41 s).
    audio=[('frostfret-blackmetal.mp3',
            {'en': 'Black metal: double-tracked tremolo guitars and bass through the built-in amp, 170 BPM, E phrygian (25 s)',
             'de': 'Black Metal: gedoppelte Tremolo-Gitarren und Bass durch den eingebauten Amp, 170 BPM, E-Phrygisch (25 s)'},
            [(0.0, 'Intro: tremolo on the open E (Wall of Ice, Double Track)', 'Intro: Tremolo auf dem leeren E (Wall of Ice, Double Track)'),
             (2.824, 'Riff A: tremolo picking with bass (Bass Pick Grind)', 'Riff A: Tremolo-Picking mit Bass (Bass Pick Grind)'),
             (11.294, 'Palm-muted gallop', 'Abgedämpfter Galopp (Palm Mute)'),
             (14.118, 'Riff B, an octave higher', 'Riff B, eine Oktave höher'),
             (21.176, 'Ringing chord to the end', 'Ausklingender Akkord')]),
           ('frostfret-acoustic.mp3',
            {'en': 'Acoustic: a strummed steel-string, then a fingerpicked nylon guitar, 100 BPM (26 s)',
             'de': 'Akustik: eine geschlagene Westerngitarre, dann eine gezupfte Nylongitarre, 100 BPM (26 s)'},
            [(0.0, 'Steel Strummer: strummed chords in E minor', 'Steel Strummer: geschlagene Akkorde in e-Moll'),
             (12.6, 'Nylon Nocturne: fingerpicked in A minor', 'Nylon Nocturne: gezupft in a-Moll')]),
           ('frostfret-clean-crunch.mp3',
            {'en': 'Clean and crunch: a clean arpeggio, then a crunch riff, 110 BPM (23 s)',
             'de': 'Clean und Crunch: ein cleanes Arpeggio, dann ein Crunch-Riff, 110 BPM (23 s)'},
            [(0.0, 'Clean Neck Arpeggio v1 (version 1 sound; clean is the most synthetic-sounding part)', 'Clean Neck Arpeggio v1 (Klang der Version 1; Clean ist der am deutlichsten synthetische Teil)'),
             (11.41, 'Cold Crunch Rhythm v1', 'Cold Crunch Rhythm v1')])],
    chapters=[],
    related=['gravesaw', 'hoarfell', 'rimehall'], bundles=['black-metal-suite-complete'],
    en=dict(
        title='Frostfret: Modelled Guitar VST3 Instrument | Polished',
        og_title='Frostfret: modelled guitar and bass from MIDI — Tools for bands',
        description='Frostfret plays guitar and bass from MIDI with modelled strings, no samples. Riff demos without a guitarist, mono-safe doubles, DI out. €29.',
        card='Modelled guitar and bass you play from MIDI: tremolo, palm mute, double tracking, amp built in or DI out.',
        h1='Frostfret: <em>a guitar you play from MIDI, for demos and pre-production</em>',
        lead='<strong>Frostfret is a VST3 instrument that plays electric, steel-string and nylon guitar and electric bass from MIDI, with modelled strings instead of samples.</strong> It belongs to the Code Chaos Black Metal Suite by Tim Borchert, who masters at Polished. It is made for the moment a song exists only in someone\'s head or in a MIDI file: the riff can be heard as a guitar part with tremolo picking, palm mutes and a double-tracked wall before anyone picks up a real guitar.',
        alt='Frostfret plugin window with the Wall of Ice preset: electric guitar section with type, tuning, pickup, attack and voicing menus and string knobs, performance section with tremolo picking, power chord and palm mute settings and a Double Track switch, amp section with High-Gain amp and cab, output section and a keyboard',
        caption='Frostfret with the Wall of Ice (Double Track) preset. Strings and pickup on top, playing style in the middle, the built-in amp below.',
        audio_note='Every note was rendered from MIDI by the plugin code, through Frostfret\'s built-in amp. No external effects, no drums, no recorded guitar anywhere. The black metal clip is mixed to about -13 LUFS, the acoustic clip to about -16 LUFS, the clean/crunch clip to about -14 LUFS.',
        sections=[
            ('ff-honest', 'What Frostfret sounds like, <em>honestly</em>', '''    <p>Frostfret is a model. Every note is a simulated string that is picked, rings, beats against itself and decays; there are no recorded guitar notes inside. No synthesised guitar sounds exactly like a recorded one, and Frostfret does not either.</p>
    <ul>
      <li><strong>Closest to a recording:</strong> distorted guitars (crunch and high gain) and the steel-string and nylon acoustics. The electric bass is close as well.</li>
      <li><strong>Most clearly synthetic:</strong> the clean electric guitar. You hear it in the first half of the clean/crunch clip above.</li>
      <li><strong>Two voicings:</strong> <em>Natural</em> is the current model, <em>Classic (v1)</em> keeps the darker sound of version 1. The Air knob makes strings and mic brighter or softer.</li>
    </ul>
    <p>Code Chaos Audio checks every sound type with an automated listening model against real recordings, and the result above is what that check says. Listen to the three clips or load the free demo before you buy.</p>''', False),
            ('ff-demo', 'A guitar demo <em>without the guitarist</em>', '''    <p>Many songs start with one person who has the riff but not the time, the tone or the guitar player at hand. With Frostfret, the riff becomes a guitar part the band can rehearse to:</p>
    <ol>
      <li><strong>Write the part as MIDI.</strong> Hold a note and Frostfret picks it as tremolo in 1/16, 1/16 triplets or 1/32, synced to your DAW tempo, with alternating down- and upstrokes. One key plays a power chord. Tunings go from E standard down to B standard, including Drop D and Drop C.</li>
      <li><strong>Mark the mutes.</strong> Palm mute follows a velocity zone, the mod wheel or a keyswitch, and it is continuous. Gallops and chugs sound muted without a second track.</li>
      <li><strong>Send the demo, keep the MIDI.</strong> When the real guitars are recorded later, the MIDI part shows the exact riff and tempo, and the Frostfret track serves as a guide.</li>
    </ol>
    <p>For the final record, a real performance through <a href="/tools/gravesaw/">Gravesaw</a> or a real amp usually still sounds better. For writing, pre-production and rough mixes, Frostfret saves the session.</p>''', True),
            ('ff-mono', 'Double tracking that <em>survives mono</em>', '''    <p>Turn on Double Track and Frostfret plays the same MIDI part as two independent takes, hard left and hard right, each with its own timing and picking. That is how a real rhythm wall is recorded, and it is why the wall holds up when a phone or a club system sums it to mono.</p>
    <p>Below 160 Hz, Frostfret keeps the output mono (with Double Track up to about 250 Hz), so the low end cannot cancel. Every preset is tested for mono compatibility. In the black metal clip on this page, the two sides correlate at 0.97 below 200 Hz, and folding the whole mix to mono costs 1.7 dB. A copied and delayed single take, the usual shortcut, often loses much more and sounds hollow. A master cannot repair that afterwards, which is why the audit at Polished checks phase and mono before every master.</p>''', False),
            ('ff-di', 'DI Out into <em>Gravesaw</em>, or the amp built in', '''    <p>Frostfret contains the amp of <a href="/tools/gravesaw/">Gravesaw</a> in four modes (Clean, Crunch, Overdrive, High-Gain) with the same 19 synthesised cabs. For a quick demo that is enough. For a mix you may want more control:</p>
    <ul>
      <li><strong>Switch the amp to DI Out.</strong> Frostfret then sends a clean DI signal, and you put Gravesaw or any other amp plugin after it, exactly as with a recorded DI guitar.</li>
      <li><strong>Print the DI as its own track.</strong> Amp decisions stay open until the mix, and you can re-amp the part without playing the MIDI again.</li>
      <li><strong>Set the amp gate before it matters.</strong> The noise between riffs gets louder in mastering, so gate it in the mix, not in the master.</li>
    </ul>
    <p>Export the finished mix with 3 to 6 dB of headroom and no limiter on the master bus. The <a href="/black-metal-mastering/">black metal mastering</a> page explains what happens after that.</p>''', True),
        ],
        specs=[('Price', '€29 on Gumroad, free demo available'),
               ('Format', 'VST3 instrument + Standalone, played from MIDI'),
               ('Guitars', 'Electric (bridge and neck humbucker, three single coils, tone pot), steel-string and nylon acoustic with modelled bodies and mic positions (12th fret, soundhole, lower bout), piezo or mic + piezo'),
               ('Bass', 'Electric bass with finger, pick and light slap, three bass cabs or DI'),
               ('Tunings', 'E, Eb, D and C standard, Drop D, Drop C, B standard (7-string / 5-string)'),
               ('Playing', 'Tremolo picking synced to the host (1/16, 1/16 triplet, 1/32), power chords, palm mute, legato, slides, bends, vibrato, harmonics, dead notes, strumming, Humanize, Double Track'),
               ('Amp', 'Gravesaw amp DSP: Clean, Crunch, Overdrive, High-Gain, 19 synthesised cabs, or DI Out'),
               ('Sound source', 'Modelled strings and bodies, no samples. Closest to a recording: distorted and acoustic guitars. Most clearly synthetic: clean electric.'),
               ('Presets', '30: 10 electric, 6 acoustic, 4 brighter variants, 4 version 1 sounds, 6 bass'),
               ('Stereo', 'Width only from Double Track and the room; mono below 160 Hz'),
               ('Latency', '61 samples (1.4 ms at 44.1 kHz), reported to the DAW'),
               ('Testing', 'Automated checks on every preset at 44.1, 48 and 96 kHz (no clicks, no silence, peaks below -0.3 dBFS, mono check). Not tried in every DAW yet.')],
        master='A Frostfret demo is a sketch of the record. Once real guitars, bass and drums are recorded, the mix decides how the album sounds, and the master decides how it translates to earbuds, car speakers and streaming normalisation. Polished starts every master with a written audio audit of your mix, including phase and mono checks of the guitar wall. See <a href="/black-metal-mastering/">black metal mastering</a>.',
        faqs=[
            ('Does Frostfret sound like a real guitar?', 'Close, depending on the sound. Distorted and acoustic guitars come closest to a recording, the clean electric guitar sounds the most synthetic. Frostfret is modelled and uses no samples. Listen to the three demo clips on this page or try the free demo.'),
            ('Can Frostfret replace the guitarist on our album?', 'For demos, songwriting and pre-production it can stand in. For a release, recorded guitars usually still sound better, and the Frostfret MIDI part then serves as a guide for the real takes.'),
            ('Can I use my own amp plugin?', 'Yes. Set the amp to DI Out; Frostfret then sends a clean DI signal, and you put Gravesaw or any other amp after it.'),
            ('Does it run on a Mac?', 'Yes, on Apple Silicon Macs (arm64) as VST3 and Standalone. There is no Intel build and no AU version, so Logic Pro is not supported. The macOS build is not signed or notarized: macOS blocks it at first, and you allow it under System Settings → Privacy &amp; Security.'),
            ('Is there a free trial?', 'Yes. The Frostfret demo on Gumroad is the full instrument with all 30 presets; it plays a short noise burst every 45 seconds.'),
        ],
    ),
    de=dict(
        title='Frostfret: modellierte Gitarre als VST3 | Polished',
        og_title='Frostfret: Gitarre und Bass aus MIDI — Tools für Bands',
        description='Frostfret spielt Gitarre und Bass aus MIDI, mit modellierten Saiten statt Samples. Riff-Demos ohne Gitarristen, monotaugliche Doppelspur, DI-Out. 29 €.',
        card='Modellierte Gitarre und Bass, gespielt aus MIDI: Tremolo, Palm Mute, Doppelspur, Amp eingebaut oder DI-Out.',
        h1='Frostfret: <em>eine Gitarre aus MIDI, für Demos und Vorproduktion</em>',
        lead='<strong>Frostfret ist ein VST3-Instrument, das E-Gitarre, Westerngitarre, Nylongitarre und E-Bass aus MIDI spielt, mit modellierten Saiten statt Samples.</strong> Es gehört zur Code Chaos Black Metal Suite von Tim Borchert, der bei Polished mastert. Gebaut ist es für den Moment, in dem ein Song nur im Kopf oder als MIDI-Datei existiert: Das Riff wird als Gitarrenspur hörbar, mit Tremolo-Picking, Palm Mutes und gedoppelter Wand, bevor jemand eine echte Gitarre in die Hand nimmt.',
        alt='Frostfret-Pluginfenster mit dem Preset Wall of Ice: E-Gitarren-Sektion mit Menüs für Typ, Stimmung, Tonabnehmer, Anschlag und Voicing sowie Saiten-Reglern, Performance-Sektion mit Tremolo-Picking, Powerchord, Palm Mute und Double-Track-Schalter, Amp-Sektion mit High-Gain-Amp und Cab, Ausgang und Klaviatur',
        caption='Frostfret mit dem Preset Wall of Ice (Double Track). Oben Saiten und Tonabnehmer, in der Mitte die Spielweise, unten der eingebaute Amp.',
        audio_note='Jede Note wurde vom Plugin-Code aus MIDI gerendert, durch den eingebauten Amp von Frostfret. Keine externen Effekte, keine Drums, nirgends eine aufgenommene Gitarre. Der Black-Metal-Clip liegt bei etwa -13 LUFS, der Akustik-Clip bei etwa -16 LUFS, der Clean/Crunch-Clip bei etwa -14 LUFS.',
        sections=[
            ('ff-honest', 'Wie Frostfret klingt, <em>ehrlich gesagt</em>', '''    <p>Frostfret ist ein Modell. Jede Note ist eine simulierte Saite, die angeschlagen wird, klingt, mit sich selbst schwebt und ausklingt; aufgenommene Gitarrentöne stecken nicht darin. Keine synthetische Gitarre klingt genau wie eine aufgenommene, auch Frostfret nicht.</p>
    <ul>
      <li><strong>Am nächsten an einer Aufnahme:</strong> verzerrte Gitarren (Crunch und High Gain) sowie Western- und Nylongitarre. Auch der E-Bass kommt nah heran.</li>
      <li><strong>Am deutlichsten synthetisch:</strong> die cleane E-Gitarre. Du hörst das in der ersten Hälfte des Clean/Crunch-Clips oben.</li>
      <li><strong>Zwei Voicings:</strong> <em>Natural</em> ist das aktuelle Modell, <em>Classic (v1)</em> behält den dunkleren Klang von Version 1. Der Air-Regler macht Saiten und Mikrofon heller oder weicher.</li>
    </ul>
    <p>Code Chaos Audio prüft jede Klangart mit einem automatischen Hörmodell gegen echte Aufnahmen, und das Ergebnis oben ist das, was diese Prüfung sagt. Hör dir die drei Clips an oder lade die Gratis-Demo, bevor du kaufst.</p>''', False),
            ('ff-demo', 'Ein Gitarren-Demo <em>ohne Gitarristen</em>', '''    <p>Viele Songs beginnen bei einer Person, die das Riff hat, aber nicht die Zeit, den Sound oder den Gitarristen griffbereit. Mit Frostfret wird das Riff zu einer Gitarrenspur, zu der die Band proben kann:</p>
    <ol>
      <li><strong>Die Spur als MIDI schreiben.</strong> Eine gehaltene Note spielt Frostfret als Tremolo in 1/16, 1/16-Triolen oder 1/32, synchron zum DAW-Tempo, mit abwechselndem Ab- und Aufschlag. Eine Taste spielt einen Powerchord. Die Stimmungen reichen von E-Standard bis B-Standard, inklusive Drop D und Drop C.</li>
      <li><strong>Die Mutes markieren.</strong> Palm Mute folgt einer Velocity-Zone, dem Modulationsrad oder einem Keyswitch, und zwar stufenlos. Galopp und Chugs klingen abgedämpft, ohne zweite Spur.</li>
      <li><strong>Demo verschicken, MIDI behalten.</strong> Wenn die echten Gitarren später aufgenommen werden, zeigt die MIDI-Spur genau Riff und Tempo, und die Frostfret-Spur dient als Guide.</li>
    </ol>
    <p>Für die fertige Platte klingt eine echte Performance durch <a href="/de/tools/gravesaw/">Gravesaw</a> oder einen echten Amp meist trotzdem besser. Für Songwriting, Vorproduktion und Rohmixe spart Frostfret die Session.</p>''', True),
            ('ff-mono', 'Doppelspur, die <em>in Mono hält</em>', '''    <p>Mit Double Track spielt Frostfret dieselbe MIDI-Spur als zwei unabhängige Takes, hart links und hart rechts, jeweils mit eigenem Timing und Anschlag. So wird eine echte Rhythmuswand aufgenommen, und deshalb hält die Wand, wenn ein Handy oder eine Club-Anlage sie zu Mono zusammenfasst.</p>
    <p>Unterhalb von 160 Hz bleibt der Ausgang von Frostfret mono (mit Double Track bis etwa 250 Hz), damit sich das Low End nicht auslöschen kann. Jedes Preset wird auf Monokompatibilität getestet. Im Black-Metal-Clip auf dieser Seite korrelieren die beiden Seiten unter 200 Hz mit 0,97, und der ganze Mix verliert in Mono 1,7 dB. Ein kopierter und verzögerter Einzeltake, die übliche Abkürzung, verliert oft deutlich mehr und klingt hohl. Ein Master kann das nachträglich nicht reparieren, deshalb prüft das Audit bei Polished vor jedem Master Phase und Mono.</p>''', False),
            ('ff-di', 'DI-Out in <em>Gravesaw</em>, oder der eingebaute Amp', '''    <p>Frostfret enthält den Amp von <a href="/de/tools/gravesaw/">Gravesaw</a> in vier Modi (Clean, Crunch, Overdrive, High-Gain) mit denselben 19 synthetisierten Cabs. Für ein schnelles Demo reicht das. Für einen Mix willst du vielleicht mehr Kontrolle:</p>
    <ul>
      <li><strong>Den Amp auf DI Out stellen.</strong> Frostfret gibt dann ein sauberes DI-Signal aus, und du setzt Gravesaw oder ein anderes Amp-Plugin dahinter, genau wie bei einer aufgenommenen DI-Gitarre.</li>
      <li><strong>Die DI als eigene Spur rendern.</strong> Amp-Entscheidungen bleiben bis zum Mix offen, und du kannst die Spur reampen, ohne das MIDI neu abzuspielen.</li>
      <li><strong>Das Amp-Gate rechtzeitig setzen.</strong> Das Rauschen zwischen den Riffs wird im Mastering lauter, also im Mix gaten, nicht im Master.</li>
    </ul>
    <p>Den fertigen Mix mit 3 bis 6 dB Headroom und ohne Limiter auf der Summe exportieren. Was danach passiert, steht auf der Seite <a href="/de/black-metal-mastering/">Black Metal Mastering</a>.</p>''', True),
        ],
        specs=[('Preis', '29 € auf Gumroad, Gratis-Demo verfügbar'),
               ('Format', 'VST3-Instrument + Standalone, gespielt über MIDI'),
               ('Gitarren', 'E-Gitarre (Humbucker Steg und Hals, drei Single Coils, Tonpoti), Western- und Nylongitarre mit modellierten Korpussen und Mikrofonpositionen (12. Bund, Schallloch, unterer Bug), Piezo oder Mikrofon + Piezo'),
               ('Bass', 'E-Bass mit Finger, Plektrum und leichtem Slap, drei Bass-Cabs oder DI'),
               ('Stimmungen', 'E-, Eb-, D- und C-Standard, Drop D, Drop C, B-Standard (7-Saiter / 5-Saiter)'),
               ('Spielweisen', 'Tremolo-Picking synchron zum Host (1/16, 1/16-Triole, 1/32), Powerchords, Palm Mute, Legato, Slides, Bendings, Vibrato, Flageoletts, Dead Notes, Strumming, Humanize, Double Track'),
               ('Amp', 'Amp-DSP von Gravesaw: Clean, Crunch, Overdrive, High-Gain, 19 synthetisierte Cabs, oder DI Out'),
               ('Klangquelle', 'Modellierte Saiten und Korpusse, keine Samples. Am nächsten an einer Aufnahme: verzerrte und akustische Gitarren. Am deutlichsten synthetisch: cleane E-Gitarre.'),
               ('Presets', '30: 10 E-Gitarre, 6 Akustik, 4 hellere Varianten, 4 Sounds aus Version 1, 6 Bass'),
               ('Stereo', 'Breite nur durch Double Track und Raum; unter 160 Hz mono'),
               ('Latenz', '61 Samples (1,4 ms bei 44,1 kHz), wird an die DAW gemeldet'),
               ('Tests', 'Automatische Prüfungen für jedes Preset bei 44,1, 48 und 96 kHz (keine Klicks, keine Stille, Spitzen unter -0,3 dBFS, Monoprüfung). Noch nicht in jeder DAW ausprobiert.')],
        master='Ein Frostfret-Demo ist eine Skizze der Platte. Sind echte Gitarren, Bass und Drums aufgenommen, entscheidet der Mix, wie das Album klingt, und der Master, wie es auf Earbuds, im Auto und nach der Lautheitsnormalisierung der Streamingdienste ankommt. Bei Polished beginnt jeder Master mit einem schriftlichen Audio-Audit deines Mixes, inklusive Phasen- und Monoprüfung der Gitarrenwand. Mehr dazu: <a href="/de/black-metal-mastering/">Black Metal Mastering</a>.',
        faqs=[
            ('Klingt Frostfret wie eine echte Gitarre?', 'Je nach Sound nah dran. Verzerrte und akustische Gitarren kommen einer Aufnahme am nächsten, die cleane E-Gitarre klingt am deutlichsten synthetisch. Frostfret ist modelliert und nutzt keine Samples. Hör dir die drei Demo-Clips auf dieser Seite an oder teste die Gratis-Demo.'),
            ('Kann Frostfret den Gitarristen auf unserem Album ersetzen?', 'Für Demos, Songwriting und Vorproduktion kann es einspringen. Für ein Release klingen aufgenommene Gitarren meist noch besser, und die MIDI-Spur aus Frostfret dient dann als Guide für die echten Takes.'),
            ('Kann ich mein eigenes Amp-Plugin nutzen?', 'Ja. Den Amp auf DI Out stellen; Frostfret gibt dann ein sauberes DI-Signal aus, und du setzt Gravesaw oder einen anderen Amp dahinter.'),
            ('Läuft Frostfret auf dem Mac?', 'Ja, auf Macs mit Apple Silicon (arm64) als VST3 und Standalone. Es gibt keinen Intel-Build und keine AU-Version, Logic Pro wird daher nicht unterstützt. Der macOS-Build ist nicht signiert und nicht notarisiert: macOS blockiert ihn zuerst, du gibst ihn unter Systemeinstellungen → Datenschutz &amp; Sicherheit frei.'),
            ('Gibt es eine kostenlose Testversion?', 'Ja. Die Frostfret-Demo auf Gumroad ist das volle Instrument mit allen 30 Presets; sie spielt alle 45 Sekunden einen kurzen Rauschstoß.'),
        ],
    ),
)

TOOLS['hoarfell'] = dict(
    slug='hoarfell', name='Hoarfell', permalink='hoarfell', demo='hoarfell-demo', price=17, os='winmac', instrument=True,
    category='Virtual instrument (modelled drums, bass and atmosphere)', category_de='Virtuelles Instrument (modellierte Drums, Bass und Atmosphäre)',
    genres=['black-metal-mastering', 'doom-gothic-mastering'],
    gui=('hoarfell', 1200, 832), cover=(1280, 720),
    # Timings from plugins/hoarfell/tools/make_demo.py (150 BPM: 1 bar = 1.6 s; 180 BPM: 1 bar = 1.333 s).
    audio=[('hoarfell-suite.mp3',
            {'en': 'Hoarfell alone: choir and bell intro, a mid-tempo groove, then a blast, 150 BPM, E phrygian (29 s)',
             'de': 'Hoarfell allein: Intro mit Chor und Glocke, ein Groove im mittleren Tempo, dann ein Blast, 150 BPM, E-Phrygisch (29 s)'},
            [(0.0, 'Intro: Choir Ah - Frozen Hall and Cold Bell, a tom swell at the end', 'Intro: Choir Ah - Frozen Hall und Cold Bell, am Ende ein Tom-Anstieg'),
             (6.4, 'Groove: Studio Kit, Bass Finger Amp, Winter Strings Pad', 'Groove: Studio Kit, Bass Finger Amp, Winter Strings Pad'),
             (19.2, 'Blast: Raw Blast Kit, Bass Tremolo Gallop, Choir Oh - Monastery', 'Blast: Raw Blast Kit, Bass Tremolo Gallop, Choir Oh - Monastery')]),
           ('hoarfell-blackmetal.mp3',
            {'en': 'Full black metal mix: Hoarfell drums, bass and choir with double-tracked Frostfret guitars, 180 BPM (37 s)',
             'de': 'Voller Black-Metal-Mix: Drums, Bass und Chor aus Hoarfell mit gedoppelten Frostfret-Gitarren, 180 BPM (37 s)'},
            [(0.0, 'Intro: tremolo guitar on E with the choir, snare build-up', 'Intro: Tremolo-Gitarre auf E mit Chor, Snare-Aufbau'),
             (2.667, 'Riff A over a blast (Raw Blast Kit)', 'Riff A über einem Blast (Raw Blast Kit)'),
             (13.333, 'Half-time with a palm-muted gallop', 'Halftime mit abgedämpftem Galopp'),
             (18.667, 'Riff B, an octave higher, over a blast', 'Riff B, eine Oktave höher, über einem Blast'),
             (29.333, 'Outro: one ringing chord', 'Outro: ein ausklingender Akkord')])],
    chapters=[],
    related=['frostfret', 'rimehall', 'kick-bass-scope'], bundles=['black-metal-suite-complete'],
    en=dict(
        title='Hoarfell: Modelled Drums, Bass & Choir VST3 | Polished',
        og_title='Hoarfell: drums, bass and choir pad from MIDI — Tools for bands',
        description='Hoarfell plays drums, bass and a choir pad from MIDI, modelled with no samples. GM drum map, blast-ready at 250 BPM, for demos and pre-production. €17.',
        card='Modelled drums on the GM map, bass and a choir pad from MIDI, made for blast beats in demos and pre-production.',
        h1='Hoarfell: <em>drums, bass and a choir pad for demos and pre-production</em>',
        lead='<strong>Hoarfell is a VST3 instrument with three engines: a drum kit on the General MIDI map that keeps up with blast beats, a modelled electric bass, and a choir, organ, strings, bell and keys section with a long hall.</strong> Like its sister plugin Frostfret it is modelled, with no samples inside, and it comes from Tim Borchert, who masters at Polished. It is the quickest way to turn a riff and a drum MIDI file into a song the whole band can hear.',
        alt='Hoarfell plugin window with the Studio Kit preset: drum kit knobs for Tune, Decay, Kick Click, Snare Snap, Velocity Layers, Round Robin, Lo-Fi, Cymbals and Room, the General MIDI drum mapping, output section and a keyboard',
        caption='Hoarfell on the drum engine with the Studio Kit preset. The mapping panel lists the General MIDI notes.',
        audio_note='Rendered from MIDI by the plugin code, no external effects. In the full mix the guitars come from Frostfret through its built-in amp, and the choir sits low, as a pad behind the guitars.',
        sections=[
            ('hf-preprod', 'Drums for demos and <em>pre-production</em>', '''    <p>Hoarfell reads the General MIDI drum map: kick on 36, snare on 38, hats on 42, 44 and 46, toms, two crashes, two rides, bell and china. A groove programmed in any DAW, played on an e-kit or taken from the 30 MIDI grooves of the <a href="https://timberwolf688.gumroad.com/l/black-metal-drum-kit?utm_source=polished&amp;utm_medium=tools&amp;utm_campaign=hoarfell&amp;utm_content=en" rel="noopener" data-track="tools-black-metal-drum-kit-hoarfell">Black Metal Drum Kit</a> plays right away.</p>
    <ul>
      <li><strong>One engine per instance.</strong> Drums, bass and atmosphere each get their own track. That keeps the demo mixable and gives you clean stems if you want to send <a href="/stem-mastering/">stems to mastering</a>.</li>
      <li><strong>Close mics, overheads and room</strong> per kit, with each drum placed in the overhead pair. Six kits from studio to lo-fi rehearsal tape.</li>
      <li><strong>Keep the tempo map.</strong> When the real drums are recorded later, the drummer can play to the same tempo and arrangement the band rehearsed with.</li>
    </ul>
    <p>Hoarfell is built for writing, demos and pre-production. For a release, recorded drums or a dedicated drum production are usually the better choice, and that is how the plugin is meant: as the drummer who is always available while the songs take shape.</p>''', False),
            ('hf-blast', 'Built for <em>blast beats</em>', '''    <p>Fast sixteenths are where many drum plugins start to click or smear. In Hoarfell a re-triggered drum fades its previous hit over 3 ms, so 250 BPM sixteenths stay click-free in the automated tests. Round Robin varies every hit, and velocity changes contact time and brightness, so a blast does not sound like the same sample fired 16 times per bar.</p>
    <p>One thing to set in the mix, not in the master: the <strong>Cymbals</strong> control balances crashes, rides, china and bell against kick, snare, toms and hats. A cymbal wash that covers the guitars is one of the most common findings in black metal premasters, and mastering EQ cannot lower the cymbals without dulling everything else.</p>''', True),
            ('hf-choir', 'The choir belongs <em>behind the mix</em>', '''    <p>The atmosphere engine has a modelled choir of up to eight singers per note, each with its own voice, pitch, vibrato and entry. It sings vowels only (Ah, Oh, Uh), no words. On sustained chords, Ah and Oh come close to a recorded choir; the low Uh drone less so. Use it as a pad behind guitars and drums, not as a lead choir.</p>
    <p>Long pads and halls fill every gap in a mix, and a limiter in mastering brings quiet parts up. If the choir already sounds present in the rough mix, it will sound louder after mastering. Keep it a little lower than feels right, as in the full mix above, and check the song in mono: below 160 Hz, Hoarfell keeps its output mono so the low end cannot cancel. The section also has a drawbar organ, a strings pad, a cold bell, celesta and lo-fi keys.</p>''', False),
        ],
        specs=[('Price', '€17 on Gumroad, free demo available'),
               ('Format', 'VST3 instrument + Standalone, one engine (Drums, Bass or Atmos / Keys) per instance'),
               ('Drums', 'General MIDI map: kick, two snares, rim, six toms, closed / pedal / open hat with choke, two crashes, two rides, bell, china'),
               ('Kits and mics', '6 kits from studio to lo-fi rehearsal; close mics, overhead pair, room, lo-fi control'),
               ('Blast speed', '250 BPM sixteenths click-free in the automated tests'),
               ('Bass', 'Modelled electric bass, finger, pick or light slap, tremolo picking synced to the host, Gravesaw amp DSP with three bass cabs, or DI'),
               ('Atmos / Keys', 'Choir (Ah, Oh, Uh, up to 8 singers per note, vowels only), drawbar organ, strings pad, cold bell, celesta, lo-fi keys, long hall'),
               ('Sound source', 'Modelled, no samples. Drum hits are shaped after averaged measurements of real drums; no recorded audio is stored.'),
               ('Presets', '20: 6 drum kits, 6 bass, 8 atmos'),
               ('Latency', '61 samples (1.4 ms at 44.1 kHz), reported to the DAW'),
               ('Testing', 'Automated checks on every preset at 44.1, 48 and 96 kHz, including a 250 BPM blast and a mono check. Not tried in every DAW yet.')],
        master='Hoarfell gives a demo drums, bass and atmosphere in one evening. When the album is recorded and mixed, the master decides how it holds up on earbuds, in the car and after streaming normalisation. Polished starts every master with a written audio audit of your mix, including cymbal harshness, low end and mono. See <a href="/black-metal-mastering/">black metal mastering</a> and <a href="/doom-gothic-mastering/">doom &amp; gothic mastering</a>.',
        faqs=[
            ('Can I use my own drum MIDI with Hoarfell?', 'Yes. Hoarfell uses the General MIDI drum map, so grooves from your DAW, an e-kit or the Black Metal Drum Kit play without remapping.'),
            ('Does Hoarfell replace a drummer or a drum library for the album?', 'It is made for demos and pre-production. For a release, recorded drums or a dedicated drum production usually remain the better choice.'),
            ('Can the choir sing lyrics?', 'No. It sings the vowels Ah, Oh and Uh, so it works as a choir pad behind the mix, not as a lead choir.'),
            ('Do I need Frostfret as well?', 'No. Hoarfell runs on its own. The guitars are in Frostfret; both together are part of the Black Metal Suite Complete bundle.'),
            ('Does it run on a Mac?', 'Yes, on Apple Silicon Macs (arm64) as VST3 and Standalone. There is no Intel build and no AU version, so Logic Pro is not supported. The macOS build is not signed or notarized, so you allow it once under System Settings → Privacy &amp; Security.'),
            ('Is there a free trial?', 'Yes. The Hoarfell demo on Gumroad is the full instrument with all 20 presets; it plays a short noise burst every 45 seconds.'),
        ],
    ),
    de=dict(
        title='Hoarfell: Drums, Bass & Chor als VST3 | Polished',
        og_title='Hoarfell: Drums, Bass und Chor-Pad aus MIDI — Tools für Bands',
        description='Hoarfell spielt Drums, Bass und ein Chor-Pad aus MIDI, modelliert ohne Samples. GM-Drum-Map, Blasts bis 250 BPM, für Demos und Vorproduktion. 17 €.',
        card='Modellierte Drums auf der GM-Map, Bass und ein Chor-Pad aus MIDI, gebaut für Blastbeats in Demos und Vorproduktion.',
        h1='Hoarfell: <em>Drums, Bass und ein Chor-Pad für Demos und Vorproduktion</em>',
        lead='<strong>Hoarfell ist ein VST3-Instrument mit drei Engines: ein Drumkit auf der General-MIDI-Belegung, das bei Blastbeats mithält, ein modellierter E-Bass und eine Sektion mit Chor, Orgel, Streichern, Glocke und Keys samt langer Halle.</strong> Wie das Schwester-Plugin Frostfret ist es modelliert, ohne Samples, und stammt von Tim Borchert, der bei Polished mastert. Es ist der schnellste Weg, aus einem Riff und einer Drum-MIDI-Datei einen Song zu machen, den die ganze Band hören kann.',
        alt='Hoarfell-Pluginfenster mit dem Preset Studio Kit: Drumkit-Regler für Tune, Decay, Kick Click, Snare Snap, Velocity Layers, Round Robin, Lo-Fi, Cymbals und Room, die General-MIDI-Belegung, Ausgangssektion und Klaviatur',
        caption='Hoarfell auf der Drum-Engine mit dem Preset Studio Kit. Das Mapping-Feld listet die General-MIDI-Noten.',
        audio_note='Vom Plugin-Code aus MIDI gerendert, keine externen Effekte. Im vollen Mix stammen die Gitarren aus Frostfret mit dessen eingebautem Amp, und der Chor liegt leise als Pad hinter den Gitarren.',
        sections=[
            ('hf-preprod', 'Drums für Demos und <em>Vorproduktion</em>', '''    <p>Hoarfell liest die General-MIDI-Drum-Belegung: Kick auf 36, Snare auf 38, Hi-Hats auf 42, 44 und 46, Toms, zwei Crashes, zwei Rides, Glocke und China. Ein Groove, in einer beliebigen DAW programmiert, auf einem E-Drum eingespielt oder aus den 30 MIDI-Grooves des <a href="https://timberwolf688.gumroad.com/l/black-metal-drum-kit?utm_source=polished&amp;utm_medium=tools&amp;utm_campaign=hoarfell&amp;utm_content=de" rel="noopener" data-track="tools-black-metal-drum-kit-hoarfell">Black Metal Drum Kit</a>, spielt sofort.</p>
    <ul>
      <li><strong>Eine Engine pro Instanz.</strong> Drums, Bass und Atmosphäre bekommen je eine eigene Spur. So bleibt das Demo mischbar, und du hast saubere Stems, falls du <a href="/de/stem-mastering/">Stems zum Mastering</a> schicken willst.</li>
      <li><strong>Close-Mics, Overheads und Raum</strong> pro Kit, jede Trommel mit eigenem Platz im Overhead-Paar. Sechs Kits vom Studio bis zum Lo-Fi-Probenmitschnitt.</li>
      <li><strong>Die Tempo-Map behalten.</strong> Wenn später echte Drums aufgenommen werden, spielt der Drummer zu demselben Tempo und Arrangement, mit dem die Band geprobt hat.</li>
    </ul>
    <p>Hoarfell ist für Songwriting, Demos und Vorproduktion gebaut. Für ein Release sind aufgenommene Drums oder eine eigene Drum-Produktion meist die bessere Wahl, und so ist das Plugin gedacht: als Drummer, der immer Zeit hat, solange die Songs entstehen.</p>''', False),
            ('hf-blast', 'Gebaut für <em>Blastbeats</em>', '''    <p>Bei schnellen Sechzehnteln fangen viele Drum-Plugins an zu klicken oder zu verschmieren. In Hoarfell blendet eine erneut angeschlagene Trommel ihren vorherigen Schlag über 3 ms aus, deshalb bleiben Sechzehntel bei 250 BPM in den automatischen Tests klickfrei. Round Robin variiert jeden Schlag, und die Velocity ändert Kontaktzeit und Helligkeit, damit ein Blast nicht wie dasselbe Sample klingt, das 16-mal pro Takt abgefeuert wird.</p>
    <p>Eine Sache gehört in den Mix, nicht in den Master: Der Regler <strong>Cymbals</strong> stellt Crashes, Rides, China und Glocke gegen Kick, Snare, Toms und Hi-Hats ein. Ein Becken-Teppich, der die Gitarren zudeckt, gehört zu den häufigsten Befunden in Black-Metal-Premastern, und Mastering-EQ kann die Becken nicht absenken, ohne alles andere mit abzudunkeln.</p>''', True),
            ('hf-choir', 'Der Chor gehört <em>hinter den Mix</em>', '''    <p>Die Atmosphären-Engine hat einen modellierten Chor mit bis zu acht Stimmen pro Note, jede mit eigener Stimme, Tonhöhe, Vibrato und eigenem Einsatz. Er singt nur Vokale (Ah, Oh, Uh), keine Worte. Auf gehaltenen Akkorden kommen Ah und Oh einem aufgenommenen Chor nahe, der tiefe Uh-Drone weniger. Setz ihn als Pad hinter Gitarren und Drums ein, nicht als Lead-Chor.</p>
    <p>Lange Pads und Hallräume füllen jede Lücke im Mix, und ein Limiter im Mastering hebt leise Anteile an. Wenn der Chor im Rohmix schon präsent klingt, klingt er nach dem Mastering lauter. Lass ihn etwas leiser, als es sich richtig anfühlt, wie im vollen Mix oben, und prüf den Song in Mono: Unter 160 Hz bleibt der Ausgang von Hoarfell mono, damit sich das Low End nicht auslöschen kann. Dazu gibt es Zugriegelorgel, Streicher-Pad, kalte Glocke, Celesta und Lo-Fi-Keys.</p>''', False),
        ],
        specs=[('Preis', '17 € auf Gumroad, Gratis-Demo verfügbar'),
               ('Format', 'VST3-Instrument + Standalone, eine Engine (Drums, Bass oder Atmos / Keys) pro Instanz'),
               ('Drums', 'General-MIDI-Belegung: Kick, zwei Snares, Rim, sechs Toms, geschlossene / Pedal- / offene Hi-Hat mit Choke, zwei Crashes, zwei Rides, Glocke, China'),
               ('Kits und Mikrofone', '6 Kits vom Studio bis zum Lo-Fi-Probenraum; Close-Mics, Overhead-Paar, Raum, Lo-Fi-Regler'),
               ('Blast-Tempo', 'Sechzehntel bei 250 BPM in den automatischen Tests klickfrei'),
               ('Bass', 'Modellierter E-Bass, Finger, Plektrum oder leichter Slap, Tremolo-Picking synchron zum Host, Amp-DSP von Gravesaw mit drei Bass-Cabs, oder DI'),
               ('Atmos / Keys', 'Chor (Ah, Oh, Uh, bis zu 8 Stimmen pro Note, nur Vokale), Zugriegelorgel, Streicher-Pad, kalte Glocke, Celesta, Lo-Fi-Keys, lange Halle'),
               ('Klangquelle', 'Modelliert, keine Samples. Die Drum-Schläge sind nach gemittelten Messungen echter Trommeln geformt; es ist keine Aufnahme gespeichert.'),
               ('Presets', '20: 6 Drumkits, 6 Bass, 8 Atmos'),
               ('Latenz', '61 Samples (1,4 ms bei 44,1 kHz), wird an die DAW gemeldet'),
               ('Tests', 'Automatische Prüfungen für jedes Preset bei 44,1, 48 und 96 kHz, inklusive Blast bei 250 BPM und Monoprüfung. Noch nicht in jeder DAW ausprobiert.')],
        master='Hoarfell gibt einem Demo an einem Abend Drums, Bass und Atmosphäre. Wenn das Album aufgenommen und gemischt ist, entscheidet der Master, wie es auf Earbuds, im Auto und nach der Lautheitsnormalisierung der Streamingdienste besteht. Bei Polished beginnt jeder Master mit einem schriftlichen Audio-Audit deines Mixes, inklusive Beckenschärfe, Low End und Mono. Mehr dazu: <a href="/de/black-metal-mastering/">Black Metal Mastering</a> und <a href="/de/doom-gothic-mastering/">Doom &amp; Gothic Mastering</a>.',
        faqs=[
            ('Kann ich eigene Drum-MIDI-Dateien mit Hoarfell nutzen?', 'Ja. Hoarfell nutzt die General-MIDI-Drum-Belegung, Grooves aus deiner DAW, von einem E-Drum oder aus dem Black Metal Drum Kit spielen also ohne Umbelegen.'),
            ('Ersetzt Hoarfell einen Drummer oder eine Drum-Library fürs Album?', 'Es ist für Demos und Vorproduktion gemacht. Für ein Release bleiben aufgenommene Drums oder eine eigene Drum-Produktion meist die bessere Wahl.'),
            ('Kann der Chor Texte singen?', 'Nein. Er singt die Vokale Ah, Oh und Uh und funktioniert daher als Chor-Pad hinter dem Mix, nicht als Lead-Chor.'),
            ('Brauche ich zusätzlich Frostfret?', 'Nein. Hoarfell läuft für sich allein. Die Gitarren stecken in Frostfret; beide zusammen sind Teil des Bundles Black Metal Suite Complete.'),
            ('Läuft Hoarfell auf dem Mac?', 'Ja, auf Macs mit Apple Silicon (arm64) als VST3 und Standalone. Es gibt keinen Intel-Build und keine AU-Version, Logic Pro wird daher nicht unterstützt. Der macOS-Build ist nicht signiert und nicht notarisiert, du gibst ihn einmal unter Systemeinstellungen → Datenschutz &amp; Sicherheit frei.'),
            ('Gibt es eine kostenlose Testversion?', 'Ja. Die Hoarfell-Demo auf Gumroad ist das volle Instrument mit allen 20 Presets; sie spielt alle 45 Sekunden einen kurzen Rauschstoß.'),
        ],
    ),
)

TOOL_ORDER = ['gravesaw', 'rimehall', 'frostfret', 'hoarfell', 'kick-bass-scope', 'crucible', 'shardstep', 'chaos-fm']

# Packs (not plugins) that are live on Gumroad and fit the black metal pages.
PACKS = [
    dict(slug='black-metal-tone-kit', name='Black Metal Tone Kit', price=9,
         en='19 synthesised cab IRs (48 and 44.1 kHz) plus REAPER FX chains for guitar and bass. Works with NAM and any IR loader. The cabs inside Gravesaw are these IRs.',
         de='19 synthetisierte Cab-IRs (48 und 44,1 kHz) plus REAPER-FX-Ketten für Gitarre und Bass. Funktioniert mit NAM und jedem IR-Loader. Die Cabs in Gravesaw sind genau diese IRs.'),
    dict(slug='black-metal-drum-kit', name='Black Metal Drum Kit', price=12,
         en='47 synthesised drum samples and 30 MIDI grooves for blast beats, gallop and doom, from 60 to 230 BPM. The drums in the Gravesaw and Rimehall demos come from it.',
         de='47 synthetisierte Drum-Samples und 30 MIDI-Grooves für Blastbeats, Galopp und Doom, von 60 bis 230 BPM. Die Drums in den Demos von Gravesaw und Rimehall stammen daraus.'),
]
PACK = {p['slug']: p for p in PACKS}

# Bundles live on Gumroad since 2026-10-21 (products/black-metal-suite*/product.json). 'single' = sum of the parts.
BUNDLES = [
    dict(slug='black-metal-suite', name='Black Metal Suite Essentials', price=39,
         items=['gravesaw', 'rimehall', 'black-metal-tone-kit', 'black-metal-drum-kit'],
         en='Amp, reverb, cab IRs and drum samples with MIDI: the mixing side of a black metal record.',
         de='Amp, Hall, Cab-IRs und Drum-Samples mit MIDI: die Mix-Seite einer Black-Metal-Platte.'),
    dict(slug='black-metal-suite-complete', name='Black Metal Suite Complete', price=69,
         items=['frostfret', 'hoarfell', 'gravesaw', 'rimehall', 'black-metal-tone-kit', 'black-metal-drum-kit'],
         en='Everything in Essentials plus the two instruments: write, demo and mix a song without a sample library.',
         de='Alles aus Essentials plus die zwei Instrumente: einen Song schreiben, als Demo hören und mischen, ohne Sample-Library.'),
]
BUNDLE = {b['slug']: b for b in BUNDLES}


def item_name(s):
    return TOOLS[s]['name'] if s in TOOLS else PACK[s]['name']


def item_price(s):
    return TOOLS[s]['price'] if s in TOOLS else PACK[s]['price']


for _b in BUNDLES:
    _b['single'] = sum(item_price(s) for s in _b['items'])
    _b['save'] = _b['single'] - _b['price']
assert (BUNDLE['black-metal-suite']['single'], BUNDLE['black-metal-suite-complete']['single']) == (59, 105)


# ---------------------------------------------------------------- HTML helpers
def picture(key, w, h, alt, eager=False, cls=''):
    load = 'loading="eager" fetchpriority="high"' if eager else 'loading="lazy"'
    c = f' class="{cls}"' if cls else ''
    return (f'<picture><source srcset="/assets/tools/{key}-gui.webp" type="image/webp">'
            f'<img src="/assets/tools/{key}-gui.jpg" alt="{html.escape(alt)}" width="{w}" height="{h}" {load} decoding="async"{c}></picture>')


def cta_buttons(t, lang, where):
    u = TT[lang]
    out = []
    if t['demo']:
        out.append(f'<a href="{gum(t["demo"], t["slug"], lang)}" class="cta-btn" rel="noopener" data-track="tools-{t["slug"]}-demo-{where}">{u["demo"]} →</a>')
        out.append(f'<a href="{gum(t["permalink"], t["slug"], lang)}" class="cta-btn outline" rel="noopener" data-track="tools-{t["slug"]}-buy-{where}">{u["buy"]} · {eur(t["price"], lang)}</a>')
    else:
        out.append(f'<a href="{gum(t["permalink"], t["slug"], lang)}" class="cta-btn" rel="noopener" data-track="tools-{t["slug"]}-free-{where}">{u["free"]} →</a>')
    return '\n      '.join(out)


def os_line(t, lang):
    return TT[lang]['winmac'] if t['os'] == 'winmac' else TT[lang]['win']


def format_line(t, lang):
    if t.get('instrument'):
        return 'VST3 instrument + Standalone' if lang == 'en' else 'VST3-Instrument + Standalone'
    return 'VST3 + Standalone'


def bundle_offer(b):
    return {"@type": "Offer", "price": f'{b["price"]}.00', "priceCurrency": "EUR",
            "availability": "https://schema.org/InStock", "url": f'{GUMROAD}{b["slug"]}', "seller": {"@id": CCA["@id"]}}


def bundle_schema(b, lang, path):
    names = ', '.join(item_name(s) for s in b['items'])
    desc = (f'{b["en"]} Contains {names}. {eur(b["price"], "en")} instead of {eur(b["single"], "en")} bought separately.'
            if lang == 'en' else
            f'{b["de"]} Enthält {names}. {eur(b["price"], "de")} statt {eur(b["single"], "de")} einzeln.')
    return {"@context": "https://schema.org", "@type": "Product", "@id": f'{BASE}{path}#{b["slug"]}',
            "name": f'Code Chaos {b["name"]}', "description": desc, "url": f'{BASE}{path}#bundles',
            "image": f'{BASE}/assets/tools/{b["slug"]}-cover.jpg', "brand": {"@type": "Brand", "name": "Code Chaos Audio"},
            "offers": bundle_offer(b)}


def bundle_card(b, lang):
    def label(s):
        return f'<a href="{tool_path(s, lang)}">{item_name(s)}</a>' if s in TOOLS else item_name(s)
    lis = '\n'.join(f'            <li>{label(s)} <span>{eur(item_price(s), lang)}</span></li>' for s in b['items'])
    alt = f'Cover of the {b["name"]} bundle' if lang == 'en' else f'Cover des Bundles {b["name"]}'
    price = (f'<strong>{eur(b["price"], lang)}</strong> instead of <s>{eur(b["single"], lang)}</s> · you save {eur(b["save"], lang)}'
             if lang == 'en' else
             f'<strong>{eur(b["price"], lang)}</strong> statt <s>{eur(b["single"], lang)}</s> · du sparst {eur(b["save"], lang)}')
    btn = 'Buy the bundle on Gumroad' if lang == 'en' else 'Bundle auf Gumroad kaufen'
    return f'''      <article class="tool-card bundle-card" id="{b["slug"]}">
        <div class="tool-card-img"><picture><source srcset="/assets/tools/{b["slug"]}-card.webp" type="image/webp"><img src="/assets/tools/{b["slug"]}-card.jpg" alt="{html.escape(alt)}" width="800" height="450" loading="lazy" decoding="async"></picture></div>
        <h3>{b["name"]}</h3>
        <p>{b[lang]}</p>
        <p class="bundle-price">{price}</p>
        <ul class="bundle-list">
{lis}
        </ul>
        <div class="cta-row">
          <a href="{gum(b["slug"], b["slug"], lang)}" class="cta-btn" rel="noopener" data-track="tools-{b["slug"]}-buy-hub">{btn} · {eur(b["price"], lang)}</a>
        </div>
      </article>'''


def bundle_note(t, lang):
    """Short bundle hint on the black metal tool pages."""
    bs = [BUNDLE[s] for s in t.get('bundles', [])]
    if not bs:
        return ''
    sid = f'{t["slug"][:2]}-bundle'
    hub = TT[lang]['hub_path'] + '#bundles'
    lis = []
    for b in bs:
        parts = ', '.join(item_name(s) for s in b['items'])
        link = f'<a href="{gum(b["slug"], t["slug"], lang)}" rel="noopener" data-track="tools-{b["slug"]}-{t["slug"]}">{b["name"]}</a>'
        if lang == 'en':
            lis.append(f'      <li><strong>{link}</strong>: {eur(b["price"], lang)} instead of {eur(b["single"], lang)} (save {eur(b["save"], lang)}). Contains {parts}.</li>')
        else:
            lis.append(f'      <li><strong>{link}</strong>: {eur(b["price"], lang)} statt {eur(b["single"], lang)} (du sparst {eur(b["save"], lang)}). Enthält {parts}.</li>')
    if lang == 'en':
        h = f'Cheaper in <em>a bundle</em>'
        p = (f'{t["name"]} is part of the Code Chaos Black Metal Suite. ' +
             ('It is included in both bundles:' if len(bs) > 1 else 'It is included in the Complete bundle:'))
        more = f'<a href="{hub}">Compare the bundles</a>. Bought separately, {t["name"]} costs {eur(t["price"], lang)}.'
    else:
        h = f'Günstiger im <em>Bundle</em>'
        p = (f'{t["name"]} gehört zur Code Chaos Black Metal Suite. ' +
             ('Es steckt in beiden Bundles:' if len(bs) > 1 else 'Es steckt im Complete-Bundle:'))
        more = f'<a href="{hub}">Bundles vergleichen</a>. Einzeln kostet {t["name"]} {eur(t["price"], lang)}.'
    inner = f'    <p>{p}</p>\n    <ul>\n' + '\n'.join(lis) + f'\n    </ul>\n    <p>{more}</p>'
    return sec(sid, h, inner)


def price_line(t, lang):
    return TT[lang]['price_free'] if t['price'] == 0 else eur(t['price'], lang)


def tool_schema(t, lang, path):
    L = t[lang]
    offer = {"@type": "Offer", "price": f'{t["price"]}.00' if t['price'] else '0', "priceCurrency": "EUR",
             "availability": "https://schema.org/InStock", "url": f'{GUMROAD}{t["permalink"]}',
             "seller": {"@id": CCA["@id"]}}
    return {"@context": "https://schema.org", "@type": ["SoftwareApplication", "Product"],
            "@id": f'{BASE}{path}#software', "name": t['name'], "url": f'{BASE}{path}', "inLanguage": lang,
            "description": L['description'],
            "applicationCategory": "MultimediaApplication",
            "applicationSubCategory": t['category'] if lang == 'en' else t['category_de'],
            "operatingSystem": "Windows 10, Windows 11, macOS (Apple Silicon)" if t['os'] == 'winmac' else "Windows 10, Windows 11",
            "image": f'{BASE}/assets/tools/{t["slug"]}-cover.jpg',
            "screenshot": f'{BASE}/assets/tools/{t["gui"][0]}-gui.jpg',
            "brand": {"@type": "Brand", "name": "Code Chaos Audio"},
            "publisher": CCA, "offers": offer}


def specs_table(t, lang):
    u = TT[lang]
    rows = list(t[lang]['specs'])
    sysrows = SYS_WINMAC[lang] if t['os'] == 'winmac' else SYS_WIN[lang]
    rows = rows[:2] + sysrows + rows[2:]
    if t['demo']:
        rows.append(('Demo', DEMO_NOTE[lang]))
    body = '\n'.join(f'          <tr><td>{k}</td><td>{v}</td></tr>' for k, v in rows)
    return f'''    <div class="table-wrap">
      <table class="spec-table">
        <thead><tr><th scope="col">{u["spec_k"]}</th><th scope="col">{u["spec_v"].format(name=t["name"])}</th></tr></thead>
        <tbody>
{body}
        </tbody>
      </table>
    </div>
    <p class="table-note">{u["checkout"]}</p>'''


def audio_block(t, lang):
    if not t['audio']:
        return ''
    u = TT[lang]
    def chapter_list(aid, chs):
        lis = '\n'.join(f'      <li><button type="button" class="chapter-seek" data-audio="{aid}" data-seek="{s}">{mmss(s)}</button> {en if lang == "en" else de}</li>'
                        for s, en, de in chs)
        return f'\n    <ol class="chapters">\n{lis}\n    </ol>'

    players = []
    for i, entry in enumerate(t['audio']):
        f, labels = entry[0], entry[1]
        aid = f'{t["slug"]}-audio-{i}'
        player = f'''    <div class="audio-demo">
      <p class="audio-label" id="{aid}-label">{labels[lang]}</p>
      <audio id="{aid}" controls preload="metadata" aria-labelledby="{aid}-label" src="/assets/tools/{f}"></audio>
    </div>'''
        if len(entry) > 2 and entry[2]:          # chapters for this player
            player += chapter_list(aid, entry[2])
        players.append(player)
    chapters = chapter_list(f'{t["slug"]}-audio-0', t['chapters']) if t['chapters'] else ''
    note = f'\n    <p class="audio-note">{t[lang]["audio_note"]}</p>' if t[lang]['audio_note'] else ''
    return sec(f'{t["slug"][:2]}-listen', f'{u["listen"]}: <em>{t["name"]}</em>', '\n'.join(players) + chapters + note, alt=True)


def tool_page(t, lang):
    u = TT[lang]
    L = t[lang]
    slug = t['slug']
    path = tool_path(slug, lang)
    home = '/de/' if lang == 'de' else '/'
    crumbs = [(u['home'], f'{BASE}{home}'), (u['hub'], f'{BASE}{u["hub_path"]}'), (t['name'], f'{BASE}{path}')]
    w, h = t['gui'][1], t['gui'][2]
    figs = f'''    <figure class="tool-shot">
      {picture(t["gui"][0], w, h, L["alt"], eager=True)}
      <figcaption>{L["caption"]}</figcaption>
    </figure>'''
    if t.get('gui2'):
        figs += f'''
    <figure class="tool-shot">
      {picture(t["gui2"][0], t["gui2"][1], t["gui2"][2], L["alt2"])}
      <figcaption>{L["caption2"]}</figcaption>
    </figure>'''
    sections = '\n'.join(sec(i, title, inner, alt=a) for i, title, inner, a in L['sections'])
    rel = '\n'.join(f'        <a href="{tool_path(r, lang)}"><span>{price_line(TOOLS[r], lang)}</span>{TOOLS[r]["name"]}</a>' for r in t['related'])
    master_link = f'<a href="{u["contact"]}" data-track="{lang}-tools-{slug}-audit">{"Request an audio audit" if lang == "en" else "Audio-Audit anfragen"}</a>'
    prices = ('Mastering at Polished starts at €79 per track, all prices incl. 19% VAT, pay after delivery if you like.'
              if lang == 'en' else 'Mastering bei Polished gibt es ab 79 € pro Track inkl. 19 % USt., Zahlung auf Wunsch erst nach Lieferung.')
    try_h = (f'Try {t["name"]} <em>free.</em>' if lang == 'en' else f'{t["name"]} <em>gratis testen.</em>') if t['demo'] else \
            (f'Get {t["name"]} <em>free.</em>' if lang == 'en' else f'{t["name"]} <em>gratis laden.</em>')
    try_p = (DEMO_NOTE[lang] + (' Buying and downloading happens on Gumroad, under Code Chaos Audio.' if lang == 'en' else ' Kauf und Download laufen über Gumroad, unter Code Chaos Audio.')) if t['demo'] else \
            ('Pay what you want, including nothing. The download happens on Gumroad, under Code Chaos Audio.' if lang == 'en'
             else 'Zahl, was du willst, auch nichts. Der Download läuft über Gumroad, unter Code Chaos Audio.')
    master_inner = f'    <p>{L["master"]}</p>\n    <p>{prices} {master_link}.</p>'
    # keep the alternating section backgrounds when the bundle hint adds a section
    faq_alt, rel_alt = (' alt', '') if t.get('bundles') else ('', ' alt')
    bundle_block = ('\n' + bundle_note(t, lang)) if t.get('bundles') else ''
    body = f'''{breadcrumb_html(crumbs, 'Brotkrumen' if lang == 'de' else 'Breadcrumb')}
<header class="page-hero">
  <div class="wrap">
    <div class="eyebrow">{u["eyebrow"]}</div>
    <h1>{L["h1"]}</h1>
    <p class="lead">{L["lead"]}</p>
    <div class="cta-row">
      {cta_buttons(t, lang, "hero")}
    </div>
    <p class="meta-line">{price_line(t, lang)} · {os_line(t, lang)} · {format_line(t, lang)}<br>{u["made"]}</p>
  </div>
</header>
<section class="content-section tool-shots" aria-label="{u["shot"]}">
  <div class="wrap">
{figs}
  </div>
</section>
{audio_block(t, lang)}
{sections}
{sec(f"{slug[:2]}-specs", u["specs"], specs_table(t, lang))}
{sec(f"{slug[:2]}-master", u["master_h"], master_inner, alt=True)}{bundle_block}
<section class="content-section{faq_alt}" aria-labelledby="{slug[:2]}-faq">
  <div class="wrap prose-wrap">
    <h2 id="{slug[:2]}-faq">{u["faq"].format(name=t["name"])}</h2>
{faq_html(L["faqs"])}
  </div>
</section>
<section class="content-section{rel_alt}" aria-labelledby="{slug[:2]}-rel">
  <div class="wrap">
    <h2 id="{slug[:2]}-rel">{u["related"]}</h2>
    <div class="related">
{rel}
    </div>
    <p class="meta-line"><a href="{u["hub_path"]}">{"All tools for bands" if lang == "en" else "Alle Tools für Bands"} →</a></p>
  </div>
</section>
<section class="cta-band" aria-labelledby="{slug[:2]}-cta">
  <div class="wrap">
    <h2 id="{slug[:2]}-cta">{try_h}</h2>
    <p>{try_p}</p>
    <div class="cta-row">
      {cta_buttons(t, lang, "final")}
    </div>
  </div>
</section>'''
    webpage = {"@context": "https://schema.org", "@type": "WebPage", "@id": f"{BASE}{path}#webpage",
               "url": f"{BASE}{path}", "name": L['title'], "inLanguage": lang,
               "isPartOf": {"@id": f"{BASE}/#website"}, "about": {"@id": f'{BASE}{path}#software'},
               "primaryImageOfPage": f'{BASE}/assets/tools/{slug}-cover.jpg', "dateModified": TOOLS_TODAY}
    schemas = [webpage, breadcrumb_schema(crumbs), tool_schema(t, lang, path), faq_schema(L['faqs'])]
    cw, ch = t['cover']
    og_alt = html.escape(f'{t["name"]} by Code Chaos Audio' if lang == 'en' else f'{t["name"]} von Code Chaos Audio')
    return page(path=path, lang=lang, title=L['title'], description=L['description'], og_title=L['og_title'],
                body=body, schemas=schemas, counterpart={'en': tool_path(slug, 'en'), 'de': tool_path(slug, 'de')},
                og_image=(f'/assets/tools/{slug}-cover.jpg', cw, ch, og_alt))


# ---------------------------------------------------------------- OVERVIEW /tools/
HUB = {
    'en': dict(
        title='Tools for Bands: Plugins for Metal Mixes | Polished',
        og_title='Tools for bands — Polished',
        description='Plugins from the mastering desk: Gravesaw amp, Rimehall reverb, Frostfret guitar, Hoarfell drums, a free phase scope and two bundles. Real demo audio.',
        h1='Tools for bands, <em>built next to the mastering desk.</em>',
        lead='<strong>Many problems a mastering engineer finds start much earlier: a fizzy amp tone, a reverb that collapses in mono, a kick and bass that cancel each other.</strong> Tim Borchert, who masters every track at Polished, also builds audio plugins under the label Code Chaos Audio. Here they are with screenshots, real demo audio and plain system requirements. Everything is sold on Gumroad, and most plugins have a free demo.',
        workflow_h='Where each tool <em>fits</em>',
        workflow=[('Writing and demos', 'Frostfret plays guitar and bass from MIDI, Hoarfell plays drums, bass and a choir pad. Both are modelled, with no samples, and made for demos and pre-production.'),
                  ('Tone', 'Gravesaw turns guitar and bass DIs into a black metal amp and cab sound, with 19 built-in cabs.'),
                  ('Space', 'Rimehall adds a cold hall, shimmer and tape, and ducks the reverb while the riff plays.'),
                  ('Low end', 'Kick/Bass Scope shows whether kick and bass add up or cancel. It is free.'),
                  ('Saturation', 'Crucible saturates bass, drums and buses in three bands with five saturation types per band.'),
                  ('Electronic layers', 'Shardstep adds tempo-synced stutter and glitch fills, Chaos FM generates FM leads, basses and stabs.')],
        grid_h='All <em>plugins</em>',
        packs_h='Also for black metal: <em>sample and IR packs</em>',
        packs_p='Not plugins, but from the same workshop and live on Gumroad. Both packs are also included in both bundles above.',
        bundles_h='Black Metal Suite: <em>two bundles</em>',
        bundles_p='The black metal tools are also sold together as the Code Chaos Black Metal Suite, in two sizes. Every plugin inside runs on Windows 10/11 and on Apple Silicon Macs (unsigned, no AU). Buying happens on Gumroad.',
        sys_h='System requirements <em>at a glance</em>',
        sys_cols=('Plugin', 'Price', 'Windows', 'macOS', 'Free demo'),
        yes='Yes', no='No', mac_yes='Apple Silicon only, unsigned', mac_no='No',
        sys_note='No AU versions, so Logic Pro is not supported. The macOS builds are not signed or notarized; macOS blocks them at first and you allow them under System Settings → Privacy &amp; Security. Every plugin was tested with automated checks but has not been tried in every DAW yet.',
        master_h='Tools don\'t replace <em>a master</em>',
        master_p='These plugins help you get a mix ready. A release that sounds right on earbuds, in the car and after streaming normalisation still needs a mastering pass with fresh ears. At Polished every master starts with a written audio audit of your mix, from €79 per track incl. VAT, unlimited revisions.',
        faqs=[('Who makes these plugins?', 'Tim Borchert, the mastering engineer behind Polished, builds them under the label Code Chaos Audio. Polished links to them; buying and downloading happens on Gumroad.'),
              ('Do the plugins run on a Mac?', 'Gravesaw, Rimehall, Frostfret, Hoarfell, Shardstep and Kick/Bass Scope run on Apple Silicon Macs as VST3 and Standalone. There are no Intel builds and no AU versions, and the macOS builds are not signed or notarized. Crucible and Chaos FM are Windows only.'),
              ('Can I try them before buying?', 'Yes. Gravesaw, Rimehall, Frostfret, Hoarfell, Shardstep, Crucible and Chaos FM each have a free demo on Gumroad: the full plugin with a short noise burst every 45 seconds. Kick/Bass Scope is free.'),
              ('Do Frostfret and Hoarfell sound like real recordings?', 'They are modelled, with no samples. Distorted and acoustic guitars come closest to a recording, the clean electric guitar sounds the most synthetic. The drums are made for demos and pre-production, and the choir sings vowels only, as a pad behind the mix. Each page has demo audio to judge for yourself.'),
              ('Is there a bundle?', 'Yes, two. Black Metal Suite Essentials (Gravesaw, Rimehall, Tone Kit, Drum Kit) costs €39 instead of €59. Black Metal Suite Complete adds Frostfret and Hoarfell and costs €69 instead of €105.')],
    ),
    'de': dict(
        title='Tools für Bands: Plugins für Metal-Mixe | Polished',
        og_title='Tools für Bands — Polished',
        description='Plugins vom Mastering-Platz: Gravesaw-Amp, Rimehall-Hall, Frostfret-Gitarre, Hoarfell-Drums, ein Gratis-Phasen-Scope und zwei Bundles. Echte Audio-Demos.',
        h1='Tools für Bands, <em>gebaut neben dem Mastering-Platz.</em>',
        lead='<strong>Viele Probleme, die beim Mastering auffallen, entstehen viel früher: ein fizziger Amp-Sound, ein Hall, der in Mono zusammenfällt, Kick und Bass, die sich gegenseitig auslöschen.</strong> Tim Borchert, der bei Polished jeden Track mastert, baut unter dem Label Code Chaos Audio auch Audio-Plugins. Hier findest du sie mit Screenshots, echter Audio-Demo und klaren Systemangaben. Verkauft wird alles über Gumroad, und für die meisten Plugins gibt es eine Gratis-Demo.',
        workflow_h='Wo welches Tool <em>hingehört</em>',
        workflow=[('Songwriting und Demos', 'Frostfret spielt Gitarre und Bass aus MIDI, Hoarfell spielt Drums, Bass und ein Chor-Pad. Beide sind modelliert, ohne Samples, und für Demos und Vorproduktion gemacht.'),
                  ('Sound', 'Gravesaw macht aus Gitarren- und Bass-DIs einen Black-Metal-Amp- und Cab-Sound, mit 19 eingebauten Cabs.'),
                  ('Raum', 'Rimehall bringt kalten Hall, Shimmer und Tape und duckt den Hall, solange das Riff spielt.'),
                  ('Low End', 'Kick/Bass Scope zeigt, ob sich Kick und Bass addieren oder auslöschen. Er ist kostenlos.'),
                  ('Sättigung', 'Crucible sättigt Bass, Drums und Busse in drei Bändern, mit fünf Sättigungstypen pro Band.'),
                  ('Elektronische Layer', 'Shardstep liefert taktsynchrone Stutter- und Glitch-Fills, Chaos FM erzeugt FM-Leads, -Bässe und -Stabs.')],
        grid_h='Alle <em>Plugins</em>',
        packs_h='Außerdem für Black Metal: <em>Sample- und IR-Pakete</em>',
        packs_p='Keine Plugins, aber aus derselben Werkstatt und auf Gumroad erhältlich. Beide Pakete stecken auch in beiden Bundles oben.',
        bundles_h='Black Metal Suite: <em>zwei Bundles</em>',
        bundles_p='Die Black-Metal-Tools gibt es auch zusammen als Code Chaos Black Metal Suite, in zwei Größen. Jedes enthaltene Plugin läuft unter Windows 10/11 und auf Macs mit Apple Silicon (unsigniert, kein AU). Gekauft wird über Gumroad.',
        sys_h='Systemanforderungen <em>auf einen Blick</em>',
        sys_cols=('Plugin', 'Preis', 'Windows', 'macOS', 'Gratis-Demo'),
        yes='Ja', no='Nein', mac_yes='Nur Apple Silicon, unsigniert', mac_no='Nein',
        sys_note='Keine AU-Versionen, Logic Pro wird daher nicht unterstützt. Die macOS-Builds sind nicht signiert und nicht notarisiert; macOS blockiert sie zuerst, du gibst sie unter Systemeinstellungen → Datenschutz &amp; Sicherheit frei. Alle Plugins wurden mit automatischen Prüfungen getestet, aber noch nicht in jeder DAW ausprobiert.',
        master_h='Tools ersetzen <em>keinen Master</em>',
        master_p='Diese Plugins helfen dir, einen Mix fertig zu machen. Ein Release, das auf Earbuds, im Auto und nach der Lautheitsnormalisierung der Streamingdienste stimmt, braucht trotzdem einen Mastering-Durchgang mit frischen Ohren. Bei Polished beginnt jeder Master mit einem schriftlichen Audio-Audit deines Mixes, ab 79 € pro Track inkl. USt., unbegrenzte Revisionen.',
        faqs=[('Wer entwickelt diese Plugins?', 'Tim Borchert, der Mastering Engineer hinter Polished, baut sie unter dem Label Code Chaos Audio. Polished verlinkt sie; Kauf und Download laufen über Gumroad.'),
              ('Laufen die Plugins auf dem Mac?', 'Gravesaw, Rimehall, Frostfret, Hoarfell, Shardstep und Kick/Bass Scope laufen auf Macs mit Apple Silicon als VST3 und Standalone. Es gibt keine Intel-Builds und keine AU-Versionen, und die macOS-Builds sind nicht signiert und nicht notarisiert. Crucible und Chaos FM gibt es nur für Windows.'),
              ('Kann ich sie vor dem Kauf testen?', 'Ja. Für Gravesaw, Rimehall, Frostfret, Hoarfell, Shardstep, Crucible und Chaos FM gibt es auf Gumroad jeweils eine Gratis-Demo: das volle Plugin mit einem kurzen Rauschstoß alle 45 Sekunden. Kick/Bass Scope ist kostenlos.'),
              ('Klingen Frostfret und Hoarfell wie echte Aufnahmen?', 'Sie sind modelliert, ohne Samples. Verzerrte und akustische Gitarren kommen einer Aufnahme am nächsten, die cleane E-Gitarre klingt am deutlichsten synthetisch. Die Drums sind für Demos und Vorproduktion gemacht, und der Chor singt nur Vokale, als Pad hinter dem Mix. Jede Seite hat Audio-Demos zum Selbstprüfen.'),
              ('Gibt es ein Bundle?', 'Ja, zwei. Black Metal Suite Essentials (Gravesaw, Rimehall, Tone Kit, Drum Kit) kostet 39 € statt 59 €. Black Metal Suite Complete enthält zusätzlich Frostfret und Hoarfell und kostet 69 € statt 105 €.')],
    ),
}


def tool_card(t, lang):
    u = TT[lang]
    path = tool_path(t['slug'], lang)
    w, h = t['gui'][1], t['gui'][2]
    return f'''      <article class="tool-card">
        <div class="tool-card-img">{picture(t["gui"][0], w, h, (t["name"] + " plugin window") if lang == "en" else ("Pluginfenster von " + t["name"]))}</div>
        <h3><a href="{path}">{t["name"]}</a></h3>
        <p>{t[lang]["card"]}</p>
        <p class="tool-meta">{price_line(t, lang)} · {os_line(t, lang)}</p>
        <div class="cta-row">
          {cta_buttons(t, lang, "hub")}
        </div>
        <a href="{path}" class="tool-more">{u["details"]}</a>
      </article>'''


def hub_page(lang):
    u = TT[lang]
    H = HUB[lang]
    path = u['hub_path']
    home = '/de/' if lang == 'de' else '/'
    crumbs = [(u['home'], f'{BASE}{home}'), (u['hub'], f'{BASE}{path}')]
    cards_html = '\n'.join(tool_card(TOOLS[s], lang) for s in TOOL_ORDER)
    bundles_html = '\n'.join(bundle_card(b, lang) for b in BUNDLES)
    # ninth tile, so the 3-column plugin grid has no empty cell: points to the bundle section
    lo = min(b['price'] for b in BUNDLES)
    if lang == 'en':
        bt = ('Black Metal Suite bundles', 'Gravesaw, Rimehall, Frostfret, Hoarfell and the two black metal packs, bundled in two sizes.',
              f'From {eur(lo, lang)} · save up to {eur(max(b["save"] for b in BUNDLES), lang)}', 'Compare the bundles')
    else:
        bt = ('Black-Metal-Suite-Bundles', 'Gravesaw, Rimehall, Frostfret, Hoarfell und die zwei Black-Metal-Pakete, gebündelt in zwei Größen.',
              f'Ab {eur(lo, lang)} · bis zu {eur(max(b["save"] for b in BUNDLES), lang)} gespart', 'Bundles vergleichen')
    cards_html += f'''
      <article class="tool-card">
        <div class="tool-card-img"><picture><source srcset="/assets/tools/black-metal-suite-complete-card.webp" type="image/webp"><img src="/assets/tools/black-metal-suite-complete-card.jpg" alt="{html.escape(bt[0])}" width="800" height="450" loading="lazy" decoding="async"></picture></div>
        <h3><a href="#bundles">{bt[0]}</a></h3>
        <p>{bt[1]}</p>
        <p class="tool-meta">{bt[2]}</p>
        <div class="cta-row">
          <a href="#bundles" class="cta-btn outline">{bt[3]} →</a>
        </div>
      </article>'''
    flow = cards(H['workflow'])
    packs = '\n'.join(f'      <li><strong><a href="{gum(p["slug"], p["slug"], lang)}" rel="noopener" data-track="tools-{p["slug"]}-hub">{p["name"]}</a></strong> ({eur(p["price"], lang)}): {p[lang]}</li>' for p in PACKS)
    rows = []
    for s in TOOL_ORDER:
        t = TOOLS[s]
        rows.append(f'          <tr><td><a href="{tool_path(s, lang)}">{t["name"]}</a></td><td>{price_line(t, lang)}</td><td>{H["yes"]}</td>'
                    f'<td>{H["mac_yes"] if t["os"] == "winmac" else H["mac_no"]}</td><td>{H["yes"] if t["demo"] else ("—" if t["price"] == 0 else H["no"])}</td></tr>')
    table = f'''    <div class="table-wrap">
      <table>
        <thead><tr>{"".join(f'<th scope="col">{c}</th>' for c in H["sys_cols"])}</tr></thead>
        <tbody>
{chr(10).join(rows)}
        </tbody>
      </table>
    </div>
    <p class="table-note">{H["sys_note"]} {u["checkout"]}</p>'''
    genre_links = ('<a href="/black-metal-mastering/">black metal</a>, <a href="/death-metal-mastering/">death metal</a>, <a href="/doom-gothic-mastering/">doom &amp; gothic</a> and <a href="/metalcore-djent-mastering/">metalcore &amp; djent</a>'
                   if lang == 'en' else
                   '<a href="/de/black-metal-mastering/">Black Metal</a>, <a href="/de/death-metal-mastering/">Death Metal</a>, <a href="/de/doom-gothic-mastering/">Doom &amp; Gothic</a> und <a href="/de/metalcore-djent-mastering/">Metalcore &amp; Djent</a>')
    master_extra = (f'Genre pages: {genre_links}.' if lang == 'en' else f'Genre-Seiten: {genre_links}.')
    packs_inner = f'    <p>{H["packs_p"]}</p>\n    <ul>\n{packs}\n    </ul>'
    master_inner = (f'    <p>{H["master_p"]} {master_extra}</p>\n    <div class="cta-row" style="margin-top: 24px;">'
                    f'<a href="{u["contact"]}" class="cta-btn" data-track="{lang}-tools-hub-audit">{u["audit"]}</a></div>')
    body = f'''{breadcrumb_html(crumbs, 'Brotkrumen' if lang == 'de' else 'Breadcrumb')}
<header class="page-hero">
  <div class="wrap">
    <div class="eyebrow">{u["eyebrow"]}</div>
    <h1>{H["h1"]}</h1>
    <p class="lead">{H["lead"]}</p>
    <div class="cta-row">
      <a href="#plugins" class="cta-btn">{"See all plugins" if lang == "en" else "Alle Plugins ansehen"} →</a>
      <a href="{gum("kick-bass-scope", "kick-bass-scope", lang)}" class="cta-btn outline" rel="noopener" data-track="tools-kick-bass-scope-free-hubhero">{"Free: Kick/Bass Scope" if lang == "en" else "Gratis: Kick/Bass Scope"}</a>
    </div>
    <p class="meta-line">{u["made"]}</p>
  </div>
</header>
<section class="content-section" aria-labelledby="tl-flow">
  <div class="wrap">
    <h2 id="tl-flow">{H["workflow_h"]}</h2>
{flow}
  </div>
</section>
<section class="content-section alt" id="plugins" aria-labelledby="tl-grid">
  <div class="wrap">
    <h2 id="tl-grid">{H["grid_h"]}</h2>
    <div class="tool-grid">
{cards_html}
    </div>
  </div>
</section>
<section class="content-section" id="bundles" aria-labelledby="tl-bundles">
  <div class="wrap">
    <div class="prose-wrap prose">
    <h2 id="tl-bundles">{H["bundles_h"]}</h2>
    <p>{H["bundles_p"]}</p>
    </div>
    <div class="tool-grid bundle-grid">
{bundles_html}
    </div>
    <div class="prose-wrap prose" style="margin-top: 48px;">
    <h3 id="tl-packs">{H["packs_h"]}</h3>
{packs_inner}
    </div>
  </div>
</section>
{sec("tl-sys", H["sys_h"], table, alt=True)}
{sec("tl-master", H["master_h"], master_inner)}
<section class="content-section alt" aria-labelledby="tl-faq">
  <div class="wrap prose-wrap">
    <h2 id="tl-faq">{"Tools for bands: <em>FAQ</em>" if lang == "en" else "Tools für Bands: <em>FAQ</em>"}</h2>
{faq_html(H["faqs"])}
  </div>
</section>'''
    itemlist = {"@context": "https://schema.org", "@type": "ItemList", "@id": f"{BASE}{path}#plugins",
                "name": u['hub'], "numberOfItems": len(TOOL_ORDER),
                "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": TOOLS[s]['name'],
                                     "url": f'{BASE}{tool_path(s, lang)}'} for i, s in enumerate(TOOL_ORDER)]}
    webpage = {"@context": "https://schema.org", "@type": "CollectionPage", "@id": f"{BASE}{path}#webpage",
               "url": f"{BASE}{path}", "name": H['title'], "inLanguage": lang,
               "isPartOf": {"@id": f"{BASE}/#website"}, "mainEntity": {"@id": f"{BASE}{path}#plugins"},
               "primaryImageOfPage": f'{BASE}/assets/tools/gravesaw-cover.jpg', "dateModified": TOOLS_TODAY}
    schemas = [webpage, breadcrumb_schema(crumbs), itemlist] + [bundle_schema(b, lang, path) for b in BUNDLES] + [faq_schema(H['faqs'])]
    og_alt = 'Gravesaw by Code Chaos Audio' if lang == 'en' else 'Gravesaw von Code Chaos Audio'
    return page(path=path, lang=lang, title=H['title'], description=H['description'], og_title=H['og_title'],
                body=body, schemas=schemas, counterpart={'en': '/tools/', 'de': '/de/tools/'},
                og_image=('/assets/tools/gravesaw-cover.jpg', 1280, 720, og_alt))


def tools_teaser(lang, sid, heading, intro, slugs, outro='', packs=(), bundles=False):
    """Short 'tools for bands' block for the genre pages (internal links to the plugin pages)."""
    def kind(t):
        if t.get('instrument'):
            return 'Instrument'
        return 'Plugin'
    links = [f'        <a href="{tool_path(s, lang)}"><span>{kind(TOOLS[s])} · {price_line(TOOLS[s], lang)}</span>{TOOLS[s]["name"]}</a>' for s in slugs]
    for ps in packs:
        p = next(x for x in PACKS if x['slug'] == ps)
        links.append(f'        <a href="{gum(p["slug"], p["slug"], lang)}" rel="noopener" data-track="tools-{p["slug"]}-{sid}"><span>{"Pack" if lang == "en" else "Paket"} · {eur(p["price"], lang)}</span>{p["name"]}</a>')
    if bundles:
        lo = min(b['price'] for b in BUNDLES)
        links.append(f'        <a href="{TT[lang]["hub_path"]}#bundles"><span>Bundle · {"from" if lang == "en" else "ab"} {eur(lo, lang)}</span>Black Metal Suite</a>')
    hub = TT[lang]['hub_path']
    more = 'All tools for bands' if lang == 'en' else 'Alle Tools für Bands'
    return f'''<section class="content-section" aria-labelledby="{sid}">
  <div class="wrap">
    <div class="prose-wrap prose">
    <h2 id="{sid}">{heading}</h2>
    <p>{intro}</p>
    </div>
    <div class="related">
{chr(10).join(links)}
    </div>
    <div class="prose-wrap prose" style="margin-top: 24px;">
    <p>{outro + " " if outro else ""}<a href="{hub}">{more} →</a></p>
    </div>
  </div>
</section>
'''


# ---------------------------------------------------------------- checks + write
for lang in ('en', 'de'):
    for s in TOOL_ORDER:
        L = TOOLS[s][lang]
        assert len(L['title']) <= 60, (s, lang, len(L['title']), L['title'])
        assert len(L['description']) <= 160, (s, lang, len(L['description']))
    assert len(HUB[lang]['title']) <= 60 and len(HUB[lang]['description']) <= 160, lang
    write(TT[lang]['hub_path'], hub_page(lang))
    for s in TOOL_ORDER:
        write(tool_path(s, lang), tool_page(TOOLS[s], lang))
