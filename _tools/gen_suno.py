# Suno Mastering (EN + DE): automatic mastering subscription for Suno and other AI-generated tracks.
# Executed from gen.py (shared namespace). Tim, 28.11.2026: own tab "Suno Mastering" next to Polished Auto,
# the KI-Campus certificate belongs here (not on the hand-mastering pages: AI-label devaluation, Bellaiche et al. 2023).
#
# Two modes, chosen fail-closed by gen.py (SUNO_LIVE):
#   December 2026 / not ready  -> announcement + waitlist only: no prices, no plans, no sign-up link
#                                 (Angebots-Sperre 01.-31.12.2026, C:/kunden-kreislauf/angebots_sperre.py)
#   live (>= 2027-01-01 AND _tools/suno_status.json live=true) -> plans, prices, start link, Offer schema
# Preview of the live mode without touching the repo:  SUNO_VORSCHAU_DIR=<dir> python _tools/gen.py
# Reasons for positioning, plans and prices (sources, evidence levels): _tools/SUNO-BEGRUENDUNG.md

SUNO_EN = '/suno-mastering/'
SUNO_DE = '/de/suno-mastering/'
SUNO_PAIR = {'en': SUNO_EN, 'de': SUNO_DE}
DEEZER = 'https://newsroom-deezer.com/2026/04/ai-generated-tracks-represent-44-of-new-uploaded-music/'
KFA1 = 'https://ki-campus.org/lernangebote/kurse/ki-fuer-alle-1'

# Plans (live mode only). Economic-value reasoning in SUNO-BEGRUENDUNG.md; prices are final prices.
SUNO_PLANS = [  # (plan id, name, price, masters per month)
    ('suno_starter', 'Suno Starter', '9.90', 10),
    ('suno_pro', 'Suno Pro', '19.90', 30),
]

# Genre profiles of the Polished Auto engine (C:/polished-auto/pauto/genres.py), same list as /auto/
# Section order (measured as variants, see SUNO-BEGRUENDUNG.md)
SUNO_REIHENFOLGE = os.environ.get('SUNO_REIHENFOLGE', 'wie,profile,schluss,markt,nicht,wege,wer,faq').split(',')
NL = chr(10)

SUNO_PROFILE = ['Black Metal (atmospheric / post)', 'Depressive / raw Black Metal', 'Melodic Death Metal',
                'Brutal Death / Grind', 'Doom / Gothic Metal', 'Modern / Industrial Metal, NDH, Nu Metal', 'Psytrance',
                'Hitech / Psycore / Darkpsy', 'Dubstep / Bass Music', 'Hardcore / Hardstyle']


def _eur(p, lang):
    return f'{p.replace(".", ",")} €' if lang == 'de' else f'€{p}'


def suno_credential(lang):
    """KI-Campus statement of achievement as schema (same facts as codechaos-official.de/bio/, PR codechaos-seo#137)."""
    return {"@type": "EducationalOccupationalCredential", "@id": f"{BASE}{SUNO_PAIR[lang]}#ki-campus-kfa1",
            "name": "KI für Alle 1: Einführung in die Künstliche Intelligenz (Leistungsnachweis)",
            "alternateName": "AI for Everyone 1: Introduction to Artificial Intelligence (statement of achievement)",
            "credentialCategory": "Leistungsnachweis Onlinekurs / statement of achievement (online course)",
            "url": KFA1, "image": f"{BASE}/assets/weiterbildung/ki-campus-kfa1-1600.webp",
            "dateCreated": "2026-11-28", "educationalLevel": "Beginner",
            "recognizedBy": [{"@type": "Organization", "name": "KI-Campus (Stifterverband)", "url": "https://ki-campus.org/"},
                             {"@type": "CollegeOrUniversity", "name": "Heinrich-Heine-Universität Düsseldorf",
                              "url": "https://www.hhu.de/"}]}


def suno_figur(lang):
    alt = ('Leistungsnachweis KI für Alle 1: Einführung in die Künstliche Intelligenz, KI-Campus und Heinrich-Heine-'
           'Universität Düsseldorf, Tim Borchert, 28. November 2026' if lang == 'de' else
           'Statement of achievement: KI für Alle 1 (AI for Everyone 1: Introduction to Artificial Intelligence), KI-Campus '
           'and Heinrich Heine University Düsseldorf, Tim Borchert, 28 November 2026')
    cap = ('Zertifikat ansehen · über KI-Campus überprüfbar' if lang == 'de'
           else 'View certificate · verifiable via KI-Campus')
    return f'''    <figure class="cred-figure">
      <a href="/assets/weiterbildung/ki-campus-kfa1-1600.webp" target="_blank" rel="noopener" data-track="suno-zertifikat-{lang}">
        <picture><source type="image/webp" srcset="/assets/weiterbildung/ki-campus-kfa1-480.webp 1x, /assets/weiterbildung/ki-campus-kfa1-960.webp 2x"><img src="/assets/weiterbildung/ki-campus-kfa1-480.jpg" width="240" height="339" loading="lazy" decoding="async" alt="{alt}"></picture>
      </a>
      <figcaption>{cap}</figcaption>
    </figure>'''


SUNO_TEXT = {
    'en': dict(
        title='Suno Mastering: automatic mastering for AI tracks | Polished',
        desc_dez='Automatic mastering for Suno and other AI-generated tracks, measured against real metal, dark and '
                 'electronic releases, with a PDF report. Starts January 2027; join the waitlist.',
        desc_live='Automatic mastering for Suno and other AI-generated tracks, measured against real metal, dark and '
                  'electronic releases, with a PDF report. From €9.90 a month for 10 masters.',
        og='Suno Mastering — Polished', home='Home', crumb='Suno Mastering',
        eyebrow_dez='Suno Mastering · from January 2027', eyebrow_live='Suno Mastering · automatic',
        h1='Suno Mastering: <em>your AI track, measured against real releases</em>',
        lead='<strong>Suno Mastering is an automatic mastering subscription for songs made with Suno, Udio and other AI '
             'music tools.</strong> Every master is measured against released records of your genre, comes with a PDF '
             'report, and it\'s only delivered if it passes the quality checks.',
        lead_dez=' It starts in January 2027. Until then, you can join the waitlist.',
        lead_live=' {p1} a month for {n1} masters.',
        cta_dez='Join the waitlist →', cta_live='Start Suno Mastering →', cta2='What it does',
        meta='Built by <a href="/#engineer">Tim Borchert</a>, mastering engineer · Last updated: %%STAND%%',
        markt_h='AI music in 2026: <em>the numbers</em>',
        markt_p1='Deezer receives almost 75,000 fully AI-generated tracks a day, about 44% of all daily uploads '
                 '(<a href="{d}" rel="noopener" target="_blank">Deezer press release, 20 April 2026</a>). In June 2026 the '
                 'share passed 50% at its peak. Yet AI tracks are only between 1 and 3% of all streams on Deezer, and in 2025 up to 85% '
                 'of the streams of fully AI-generated tracks were fraudulent. Deezer tags these tracks and removes them '
                 'from algorithmic recommendations.',
        markt_rows=[('Fully AI-generated uploads per day', 'almost 75,000 (July 2026: nearly 90,000)'),
                    ('Share of daily uploads', 'about 44% (June 2026 peak: over 50%)'),
                    ('Share of all streams', 'between 1 and 3%'),
                    ('Fraudulent streams of fully AI tracks (2025)', 'up to 85%'),
                    ('Algorithmic recommendations', 'AI-tagged tracks removed')],
        markt_th=('Deezer figure', 'Value'),
        markt_quelle='Source: Deezer newsroom, 20 April 2026, figures updated to July 2026.',
        markt_p2='What this means for your song: mastering doesn\'t change how a platform classifies it, and we never try '
                 'to hide where a track comes from. What a master can change is how your song holds up next to everything '
                 'else in a playlist: level, harshness, low end and stereo image.',
        wie_h='How Suno Mastering <em>works</em>',
        wie_dez_intro='Here\'s how it\'ll work from January 2027:',
        wie=['<strong>Your file:</strong> a WAV, AIFF or FLAC export of your song (44.1–96 kHz). You confirm that your plan '
             'on the AI tool allows commercial use.',
             '<strong>Your genre:</strong> you pick the profile closest to your song. Each profile is the measured spread '
             'of released records: tonal balance, loudness, dynamics, stereo width and harshness.',
             '<strong>The master:</strong> clipped peaks rebuilt, rumble removed, tonal balance moved into the genre range '
             '(only what lies outside it), low end centred, level set by dynamics with a true-peak ceiling of -1 dBTP.',
             '<strong>Quality checks:</strong> every master is measured again for true peak, clipping, dynamics, tonal '
             'balance, harshness and mono compatibility. A master that fails a check isn\'t delivered.',
             '<strong>Delivery:</strong> WAV at 16 bit / 44.1 kHz (the format distributors ask for), MP3 and a PDF report '
             'with the numbers before and after.'],
        profile_h='Genre profiles: <em>metal, dark and electronic</em>',
        profile_p='We measured the profiles from released records, with the same measurement we run on your file:',
        profile_p2='Pop, hip-hop and singer-songwriter songs don\'t have a profile yet. We\'d rather tell you that than guess.',
        nicht_h='What Suno Mastering <em>doesn\'t do</em>',
        nicht=['It doesn\'t listen. It measures and follows rules from real releases; the taste is yours.',
               'It doesn\'t fix the song itself: a buried vocal, smeared cymbals or a muddy arrangement stay the way they '
               'are. The report names these problems, so you can regenerate or edit those parts.',
               'It doesn\'t hide AI origin, and it won\'t change how Deezer, Spotify or anyone else detects or labels your '
               'track.',
               'No stems, no vinyl master, no album matching and no reference track of your own.'],
        wege_h='Three ways to get mastered <em>at Polished</em>',
        wege_th=('', 'Suno Mastering', 'Polished Auto', 'Polished by Tim'),
        wege=[('For', 'songs from Suno, Udio and other AI tools', 'your band\'s own mix', 'releases that need decisions by ear'),
              ('Who does the work', 'automatic, measured against genre releases', 'automatic, measured against genre releases', 'Tim, mastering engineer'),
              ('Delivery', '16-bit WAV + MP3 + PDF report', '24-bit master + streaming version + PDF report', 'all formats, written plan, revisions'),
              ('Starts', 'January 2027', 'January 2027', 'now')],
        wege_live_start=('Starts', 'now', 'now', 'now'),
        wege_link='<a href="/#packages">Polished by Tim: the hand-mastering packages</a>',
        wer_h='Who <em>builds it</em>',
        wer_p='Suno Mastering runs on the same engine as Polished Auto. Tim Borchert built and tuned it: mastering engineer '
              'for metal and gothic at Polished, student of Systematic Musicology and Media Studies at the University of '
              'Hamburg.',
        cred_kicker='Training',
        cred_titel='AI fundamentals · KI-Campus / Heinrich Heine University Düsseldorf',
        cred_p='In November 2026 Tim finished the online course “KI für Alle 1: Einführung in die Künstliche Intelligenz” '
               '(AI for Everyone 1: Introduction to Artificial Intelligence) with a statement of achievement. 45 hours of '
               'machine learning basics, data preparation and analysis, Python, and the ethical and legal side of AI.',
        cred_meta='Statement of achievement · 45 h · November 2026 · <a href="{k}" rel="noopener" target="_blank">course page</a>',
        wl_h='Join the <em>waitlist</em>',
        wl_p='Leave your email and we\'ll send you one message when Suno Mastering opens in January 2027. No payment, no '
             'obligation, no newsletter.',
        wl_name='Name', wl_name_ph='Your name or artist name', wl_email='Email',
        wl_tracks='Songs per month (roughly)', wl_tracks_opts=['1–2', '3–10', '11–30', 'more than 30'],
        wl_genre='Genre', wl_genre_opts=['Metal', 'Gothic / dark', 'Psytrance / Hitech', 'Other electronic', 'Other'],
        wl_choose='Choose', wl_msg='Suno Mastering waitlist (January 2027)',
        wl_consent='I have read the <a href="/datenschutz/">privacy policy</a> and agree that my details are used to '
                   'contact me about Suno Mastering.',
        wl_btn='Join the waitlist →', wl_hp='Leave this field empty',
        plans_h='Plans', plans_th=('Plan', 'Per month', 'Masters a month', 'Per master'),
        plans_note='All prices are final prices. The seller at checkout is our reseller Lemon Squeezy, who charges and pays '
                   'any VAT that applies. Plans renew monthly, and you can cancel anytime to the end of the month. '
                   'Unused masters don\'t roll over.',
        faq_h='Suno Mastering <em>FAQ</em>',
    ),
    'de': dict(
        title='Suno-Mastering: automatisches Mastering für KI-Songs | Polished',
        desc_dez='Automatisches Mastering für Suno- und andere KI-Songs, gemessen an echten Metal-, Dark- und '
                 'Elektronik-Veröffentlichungen, mit PDF-Bericht. Start Januar 2027, Warteliste offen.',
        desc_live='Automatisches Mastering für Suno- und andere KI-Songs, gemessen an echten Metal-, Dark- und '
                  'Elektronik-Veröffentlichungen, mit PDF-Bericht. Ab 9,90 € im Monat für 10 Master.',
        og='Suno-Mastering — Polished', home='Startseite', crumb='Suno-Mastering',
        eyebrow_dez='Suno-Mastering · ab Januar 2027', eyebrow_live='Suno-Mastering · automatisch',
        h1='Suno-Mastering: <em>dein KI-Song, gemessen an echten Veröffentlichungen</em>',
        lead='<strong>Suno-Mastering ist ein automatisches Mastering-Abo für Songs aus Suno, Udio und anderen KI-'
             'Musikwerkzeugen.</strong> Jeder Master wird an veröffentlichten Platten deines Genres gemessen, kommt mit '
             'PDF-Bericht und wird nur geliefert, wenn er die Qualitätsprüfung besteht.',
        lead_dez=' Los geht es im Januar 2027. Bis dahin kannst du dich auf die Warteliste setzen.',
        lead_live=' {p1} im Monat für {n1} Master.',
        cta_dez='Auf die Warteliste →', cta_live='Suno-Mastering starten →', cta2='So funktioniert es',
        meta='Entwickelt von <a href="/de/#tim">Tim Borchert</a>, Mastering Engineer · Zuletzt aktualisiert: %%STAND%%',
        markt_h='KI-Musik 2026: <em>die Zahlen</em>',
        markt_p1='Deezer bekommt fast 75.000 vollständig KI-generierte Tracks am Tag, rund 44 % aller täglichen Uploads '
                 '(<a href="{d}" rel="noopener" target="_blank">Deezer-Pressemitteilung vom 20.04.2026</a>). Im Juni 2026 '
                 'lag der Anteil in der Spitze über 50 %. Trotzdem machen KI-Tracks nur zwischen 1 und 3 % aller Streams auf Deezer aus, '
                 'und 2025 waren bis zu 85 % der Streams vollständig KI-generierter Tracks Betrug. Deezer kennzeichnet '
                 'diese Tracks und nimmt sie aus den algorithmischen Empfehlungen.',
        markt_rows=[('Vollständig KI-generierte Uploads pro Tag', 'fast 75.000 (Juli 2026: fast 90.000)'),
                    ('Anteil an den täglichen Uploads', 'rund 44 % (Spitze Juni 2026: über 50 %)'),
                    ('Anteil an allen Streams', 'zwischen 1 und 3 %'),
                    ('Betrügerische Streams vollständiger KI-Tracks (2025)', 'bis zu 85 %'),
                    ('Algorithmische Empfehlungen', 'KI-gekennzeichnete Tracks entfernt')],
        markt_th=('Kennzahl Deezer', 'Wert'),
        markt_quelle='Quelle: Deezer Newsroom, 20.04.2026, Zahlen aktualisiert bis Juli 2026.',
        markt_p2='Was das für deinen Song heißt: Mastering ändert nicht, wie eine Plattform ihn einordnet, und '
                 'Suno-Mastering versucht nie zu verschleiern, woher ein Track kommt. Ein Master kann aber ändern, wie '
                 'der Song neben allem anderen in einer Playlist besteht: Pegel, Härte, Tiefbass und Stereobild.',
        wie_h='So funktioniert <em>Suno-Mastering</em>',
        wie_dez_intro='So wird es ab Januar 2027 laufen:',
        wie=['<strong>Deine Datei:</strong> ein WAV-, AIFF- oder FLAC-Export deines Songs (44,1–96 kHz). Du bestätigst, '
             'dass dein Tarif beim KI-Werkzeug die kommerzielle Nutzung erlaubt.',
             '<strong>Dein Genre:</strong> Du wählst das passende Profil. Jedes Profil ist die gemessene Bandbreite '
             'veröffentlichter Platten: Klangbalance, Lautheit, Dynamik, Stereobreite und Härte.',
             '<strong>Der Master:</strong> geclippte Spitzen rekonstruiert, Rumpeln entfernt, Klangbalance in den '
             'Genrebereich gebracht (nur was außerhalb liegt), Tiefbass zentriert, Pegel nach Dynamik mit True-Peak-'
             'Grenze bei -1 dBTP.',
             '<strong>Qualitätsprüfung:</strong> Jeder Master wird erneut gemessen: True Peak, Clipping, Dynamik, '
             'Klangbalance, Härte und Mono-Kompatibilität. Fällt er durch, wird er nicht geliefert.',
             '<strong>Lieferung:</strong> WAV mit 16 Bit / 44,1 kHz (das Format, das Vertriebe verlangen), MP3 und ein '
             'PDF-Bericht mit den Werten vorher und nachher.'],
        profile_h='Genreprofile: <em>Metal, Dark und Elektronik</em>',
        profile_p='Die Profile sind an veröffentlichten Platten gemessen, mit derselben Messung wie deine Datei:',
        profile_p2='Für Pop, Hip-Hop oder Singer-Songwriter gibt es noch kein Profil. Das sagen wir lieber offen, als zu raten.',
        nicht_h='Was Suno-Mastering <em>nicht macht</em>',
        nicht=['Es hört nicht zu. Es misst und folgt Regeln aus echten Veröffentlichungen; der Geschmack bleibt bei dir.',
               'Es repariert nicht den Song selbst: Eine versteckte Stimme, verwaschene Becken oder ein matschiges '
               'Arrangement bleiben, wie sie sind. Der Bericht nennt solche Probleme, damit du Teile neu erzeugen oder '
               'bearbeiten kannst.',
               'Es verschleiert keine KI-Herkunft und ändert nicht, wie Deezer, Spotify oder andere den Track erkennen '
               'oder kennzeichnen.',
               'Keine Stems, kein Vinyl-Master, kein Album-Angleich, kein eigener Referenztrack.'],
        wege_h='Drei Wege zum Master <em>bei Polished</em>',
        wege_th=('', 'Suno-Mastering', 'Polished Auto', 'Polished by Tim'),
        wege=[('Für', 'Songs aus Suno, Udio und anderen KI-Werkzeugen', 'den eigenen Mix deiner Band', 'Veröffentlichungen, die Entscheidungen nach Gehör brauchen'),
              ('Wer arbeitet', 'automatisch, gemessen an Genre-Veröffentlichungen', 'automatisch, gemessen an Genre-Veröffentlichungen', 'Tim, Mastering Engineer'),
              ('Lieferung', '16-Bit-WAV + MP3 + PDF-Bericht', '24-Bit-Master + Streaming-Version + PDF-Bericht', 'alle Formate, schriftlicher Plan, Revisionen'),
              ('Start', 'Januar 2027', 'Januar 2027', 'jetzt')],
        wege_live_start=('Start', 'jetzt', 'jetzt', 'jetzt'),
        wege_link='<a href="/de/#preise">Polished by Tim: die Pakete für Handmastering</a>',
        wer_h='Wer <em>dahintersteht</em>',
        wer_p='Suno-Mastering läuft auf derselben Engine wie Polished Auto. Gebaut und abgestimmt hat sie Tim Borchert, '
              'Mastering Engineer für Metal und Gothic bei Polished und Student der Systematischen Musikwissenschaft und '
              'Medienwissenschaft an der Universität Hamburg.',
        cred_kicker='Weiterbildung',
        cred_titel='KI-Grundlagen · KI-Campus / Heinrich-Heine-Universität Düsseldorf',
        cred_p='Im November 2026 hat Tim den Onlinekurs „KI für Alle 1: Einführung in die Künstliche Intelligenz“ mit '
               'Leistungsnachweis abgeschlossen. 45 Stunden: Grundlagen des maschinellen Lernens, Datenaufbereitung und '
               '-analyse, Python sowie ethische und rechtliche Fragen rund um KI.',
        cred_meta='Leistungsnachweis · 45 Std. · November 2026 · <a href="{k}" rel="noopener" target="_blank">Kursseite</a>',
        wl_h='Auf die <em>Warteliste</em>',
        wl_p='Trag deine E-Mail ein, dann bekommst du eine Nachricht, sobald Suno-Mastering im Januar 2027 startet. '
             'Keine Zahlung, keine Verpflichtung, kein Newsletter.',
        wl_name='Name', wl_name_ph='Dein Name oder Künstlername', wl_email='E-Mail',
        wl_tracks='Songs pro Monat (ungefähr)', wl_tracks_opts=['1–2', '3–10', '11–30', 'mehr als 30'],
        wl_genre='Genre', wl_genre_opts=['Metal', 'Gothic / Dark', 'Psytrance / Hitech', 'Andere Elektronik', 'Anderes'],
        wl_choose='– wählen –', wl_msg='Warteliste Suno-Mastering (Januar 2027)',
        wl_consent='Ich habe die <a href="/datenschutz/">Datenschutzerklärung</a> gelesen und bin einverstanden, dass '
                   'meine Angaben genutzt werden, um mich zu Suno-Mastering zu kontaktieren.',
        wl_btn='Auf die Warteliste →', wl_hp='Dieses Feld leer lassen',
        plans_h='Tarife', plans_th=('Tarif', 'Pro Monat', 'Master pro Monat', 'Pro Master'),
        plans_note='Alle Preise sind Endpreise. Verkäufer im Bestellvorgang ist unser Wiederverkäufer Lemon Squeezy, der '
                   'eine anfallende Umsatzsteuer berechnet und abführt. Tarife verlängern sich monatlich und sind jederzeit '
                   'zum Monatsende kündbar. Nicht genutzte Master verfallen am Monatsende.',
        faq_h='Suno-Mastering: <em>FAQ</em>',
    ),
}

SUNO_FAQ = {
    'en': [
        ('What is Suno mastering?',
         'Suno mastering is the final step for a song made with Suno or another AI music tool before release: level, '
         'tonal balance, low end, stereo image and peaks are brought in line with released records of the genre. Suno '
         'Mastering at Polished does this automatically and measures every master against real releases.'),
        ('Does mastering make my AI track pass as human-made?',
         'No. Mastering changes level and tone, not where a song comes from. Deezer tags fully AI-generated tracks and '
         'removes them from algorithmic recommendations, and Suno Mastering doesn\'t try to get around that.'),
        ('Which genres work best?',
         'Metal, gothic and dark music, psytrance, hitech and other electronic styles, because we measured the genre '
         'profiles from released records in those genres. Pop, hip-hop and singer-songwriter songs don\'t have a profile yet.'),
        ('Do I need the rights to my Suno song?',
         'Yes. You confirm that your plan on the AI tool allows commercial use of the song. Free plans of AI music tools '
         'are often limited to personal use, so check your tool\'s terms.'),
        ('When does Suno Mastering start?',
         'In January 2027, together with Polished Auto. If you\'re on the waitlist, you\'ll get one message when it opens.'),
    ],
    'de': [
        ('Was ist Suno-Mastering?',
         'Suno-Mastering ist der letzte Schritt für einen Song aus Suno oder einem anderen KI-Musikwerkzeug vor der '
         'Veröffentlichung: Pegel, Klangbalance, Tiefbass, Stereobild und Spitzen werden an veröffentlichte Platten des '
         'Genres angepasst. Suno-Mastering bei Polished macht das automatisch und misst jeden Master an echten '
         'Veröffentlichungen.'),
        ('Klingt mein KI-Track nach dem Mastering wie von Menschen gemacht?',
         'Nein. Mastering ändert Pegel und Klang, nicht die Herkunft eines Songs. Deezer kennzeichnet vollständig '
         'KI-generierte Tracks und nimmt sie aus den algorithmischen Empfehlungen; Suno-Mastering versucht nicht, das zu '
         'umgehen.'),
        ('Welche Genres passen am besten?',
         'Metal, Gothic und düstere Musik, Psytrance, Hitech und andere elektronische Stile, weil die Genreprofile an '
         'veröffentlichten Platten dieser Genres gemessen sind. Für Pop, Hip-Hop und Singer-Songwriter gibt es noch kein '
         'Profil.'),
        ('Brauche ich die Rechte an meinem Suno-Song?',
         'Ja. Du bestätigst, dass dein Tarif beim KI-Werkzeug die kommerzielle Nutzung des Songs erlaubt. Gratis-Tarife '
         'von KI-Musikwerkzeugen sind oft nur für die private Nutzung freigegeben; prüf die Bedingungen deines Werkzeugs.'),
        ('Wann startet Suno-Mastering?',
         'Im Januar 2027, zusammen mit Polished Auto. Wer auf der Warteliste steht, bekommt beim Start eine Nachricht.'),
    ],
}
SUNO_FAQ_LIVE = {
    'en': ('What does Suno Mastering cost?',
           'Suno Starter costs €9.90 a month for 10 masters (€0.99 per master), Suno Pro €19.90 a month for 30 masters '
           '(€0.66 per master). Plans renew monthly and can be cancelled to the end of any month.'),
    'de': ('Was kostet Suno-Mastering?',
           'Suno Starter kostet 9,90 € im Monat für 10 Master (0,99 € pro Master), Suno Pro 19,90 € im Monat für 30 Master '
           '(0,66 € pro Master). Die Tarife verlängern sich monatlich und sind zum Monatsende kündbar.'),
}


def suno_body(lang, live):
    t = SUNO_TEXT[lang]
    home = f'{BASE}/de/' if lang == 'de' else f'{BASE}/'
    p1, n1 = _eur(SUNO_PLANS[0][2], lang), SUNO_PLANS[0][3]
    app = SUNO_STATUS.get('app_url', '/auto/app/?plan={plan}').format(plan=SUNO_PLANS[0][0])
    cta = (f'<a href="{app}" class="cta-btn" data-track="suno-start-{lang}">{t["cta_live"]}</a>' if live else
           f'<a href="#warteliste" class="cta-btn" data-track="suno-warteliste-hero-{lang}">{t["cta_dez"]}</a>')
    lead = t['lead'] + (t['lead_live'].format(p1=p1, n1=n1) if live else t['lead_dez'])
    rows = ''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in t['markt_rows'])
    wie = ''.join(f'\n      <li>{x}</li>' for x in t['wie'])
    nicht = ''.join(f'\n      <li>{x}</li>' for x in t['nicht'])
    profile = ''.join(f'\n      <li>{x}</li>' for x in SUNO_PROFILE)
    wege = t['wege'][:3] + [t['wege_live_start'] if live else t['wege'][3]]
    wege_rows = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in wege)
    wege_th = ''.join(f'<th>{c}</th>' for c in t['wege_th'])

    if live:
        plan_rows = ''.join(
            f'<tr><td>{name}</td><td>{_eur(preis, lang)}</td><td>{n}</td>'
            f'<td>{_eur(f"{float(preis) / n:.2f}", lang)}</td></tr>' for _pid, name, preis, n in SUNO_PLANS)
        plan_cta = ' '.join(
            f'<a href="{SUNO_STATUS.get("app_url", "/auto/app/?plan={plan}").format(plan=pid)}" class="cta-btn{"" if i == 0 else " outline"}" '
            f'data-track="suno-plan-{pid}-{lang}">{name} →</a>' for i, (pid, name, _p, _n) in enumerate(SUNO_PLANS))
        schluss = f'''<section class="content-section alt" id="tarife" aria-labelledby="suno-tarife-{lang}">
  <div class="wrap prose-wrap prose">
    <h2 id="suno-tarife-{lang}">{t["plans_h"]}</h2>
    <div class="table-wrap">
      <table>
        <thead><tr>{"".join(f"<th>{c}</th>" for c in t["plans_th"])}</tr></thead>
        <tbody>{plan_rows}</tbody>
      </table>
    </div>
    <p class="table-note">{t["plans_note"]}</p>
    <div class="cta-row">{plan_cta}</div>
  </div>
</section>'''
    else:
        tr = ''.join(f'<option value="{o}">{o}</option>' for o in t['wl_tracks_opts'])
        ge = ''.join(f'<option value="{o}">{o}</option>' for o in t['wl_genre_opts'])
        schluss = f'''<section class="content-section alt" id="warteliste" aria-labelledby="suno-wl-{lang}">
  <div class="wrap prose-wrap prose">
    <h2 id="suno-wl-{lang}">{t["wl_h"]}</h2>
    <p>{t["wl_p"]}</p>
    <form class="inquiry-form suno-waitlist" data-formsubmit data-lang="{lang}" novalidate>
      <input type="hidden" name="service" value="{t["wl_msg"]}">
      <input type="hidden" name="message" value="{t["wl_msg"]}">
      <div class="form-row">
        <div class="form-group"><label for="s-name-{lang}">{t["wl_name"]} <span class="req" aria-hidden="true">*</span></label><input type="text" id="s-name-{lang}" name="name" required autocomplete="name" placeholder="{t["wl_name_ph"]}"></div>
        <div class="form-group"><label for="s-email-{lang}">{t["wl_email"]} <span class="req" aria-hidden="true">*</span></label><input type="email" id="s-email-{lang}" name="email" required autocomplete="email" placeholder="you@email.com"></div>
      </div>
      <div class="form-row">
        <div class="form-group"><label for="s-tracks-{lang}">{t["wl_tracks"]}</label><select id="s-tracks-{lang}" name="tracks"><option value="">{t["wl_choose"]}</option>{tr}</select></div>
        <div class="form-group"><label for="s-genre-{lang}">{t["wl_genre"]}</label><select id="s-genre-{lang}" name="genre"><option value="">{t["wl_choose"]}</option>{ge}</select></div>
      </div>
      <div class="hp" aria-hidden="true"><label for="s-website-{lang}">{t["wl_hp"]}</label><input type="text" id="s-website-{lang}" name="_honey" tabindex="-1" autocomplete="off"></div>
      <div class="consent-row"><input type="checkbox" id="s-consent-{lang}" name="consent" required><label for="s-consent-{lang}">{t["wl_consent"]} <span class="req" aria-hidden="true">*</span></label></div>
      <button type="submit" class="cta-btn form-submit" data-track="suno-warteliste-form-{lang}">{t["wl_btn"]}</button>
      <div class="form-status" role="status" aria-live="polite"></div>
    </form>
  </div>
</section>'''

    faqs = SUNO_FAQ[lang][:-1] + [SUNO_FAQ_LIVE[lang]] if live else SUNO_FAQ[lang]
    kopf = f'''{breadcrumb_html([(t["home"], home), (t["crumb"], f"{BASE}{SUNO_PAIR[lang]}")], "Brotkrumen" if lang == "de" else "Breadcrumb")}
<header class="page-hero">
  <div class="wrap">
    <div class="eyebrow">{t["eyebrow_live" if live else "eyebrow_dez"]}</div>
    <h1>{t["h1"]}</h1>
    <p class="lead">{lead}</p>
    <div class="cta-row">
      {cta}
      <a href="#so-gehts" class="cta-btn outline">{t["cta2"]}</a>
    </div>
    <p class="meta-line">{t["meta"]}</p>
  </div>
</header>'''
    teile = {
        'markt': f'''{sec(f"suno-markt-{lang}", t["markt_h"], f"""    <p>{t["markt_p1"].format(d=DEEZER)}</p>
    <div class="table-wrap">
      <table>
        <thead><tr><th>{t["markt_th"][0]}</th><th>{t["markt_th"][1]}</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
    <p class="table-note">{t["markt_quelle"]}</p>
    <p>{t["markt_p2"]}</p>""")}''',
        'wie': f'''<section class="content-section alt" id="so-gehts" aria-labelledby="suno-wie-{lang}">
  <div class="wrap prose-wrap prose">
    <h2 id="suno-wie-{lang}">{t["wie_h"]}</h2>
    {"" if live else f"<p>{t['wie_dez_intro']}</p>"}
    <ol>{wie}
    </ol>
  </div>
</section>''',
        'profile': f'''{sec(f"suno-profile-{lang}", t["profile_h"], f"""    <p>{t["profile_p"]}</p>
    <ul>{profile}
    </ul>
    <p>{t["profile_p2"]}</p>""")}''',
        'nicht': f'''{sec(f"suno-nicht-{lang}", t["nicht_h"], f"""    <ul>{nicht}
    </ul>""", alt=True)}''',
        'wege': f'''{sec(f"suno-wege-{lang}", t["wege_h"], f"""    <div class="table-wrap">
      <table>
        <thead><tr>{wege_th}</tr></thead>
        <tbody>{wege_rows}</tbody>
      </table>
    </div>
    <p>{t["wege_link"]}</p>""")}''',
        'wer': f'''<section class="content-section alt" id="wer" aria-labelledby="suno-wer-{lang}">
  <div class="wrap prose-wrap prose">
    <h2 id="suno-wer-{lang}">{t["wer_h"]}</h2>
    <p>{t["wer_p"]}</p>
    <aside class="cred" id="ki-campus" aria-label="{t["cred_kicker"]}">
      <p class="cred-kicker">{t["cred_kicker"]}</p>
      <p class="cred-titel">{t["cred_titel"]}</p>
      <p>{t["cred_p"]}</p>
      <p class="cred-meta">{t["cred_meta"].format(k=KFA1)}</p>
{suno_figur(lang)}
    </aside>
  </div>
</section>''',
        'schluss': f'''{schluss}''',
        'faq': f'''<section class="content-section" aria-labelledby="suno-faq-{lang}">
  <div class="wrap prose-wrap">
    <h2 id="suno-faq-{lang}">{t["faq_h"]}</h2>
{faq_html(faqs)}
  </div>
</section>''',
    }
    body = kopf + NL + NL.join(teile[n] for n in SUNO_REIHENFOLGE)
    return body, faqs


def suno_schemas(lang, live, faqs):
    t = SUNO_TEXT[lang]
    path = SUNO_PAIR[lang]
    home = f'{BASE}/de/' if lang == 'de' else f'{BASE}/'
    service = {"@context": "https://schema.org", "@type": "Service", "@id": f"{BASE}{path}#service",
               "name": t['crumb'], "serviceType": "Automatic audio mastering for AI-generated music",
               "description": t['desc_live' if live else 'desc_dez'], "url": f"{BASE}{path}",
               "provider": BIZ, "areaServed": "Worldwide",
               "audience": {"@type": "Audience", "audienceType": "Creators of AI-generated music (Suno, Udio)"}}
    if live:
        ziel = f"{BASE}{path}#tarife"
        service["offers"] = [{"@type": "Offer", "name": name, "price": preis, "priceCurrency": "EUR", "url": ziel,
                              "availability": "https://schema.org/InStock",
                              "priceSpecification": {"@type": "UnitPriceSpecification", "price": preis,
                                                     "priceCurrency": "EUR", "billingDuration": "P1M",
                                                     "valueAddedTaxIncluded": True}}
                             for _pid, name, preis, _n in SUNO_PLANS]
    person = {"@context": "https://schema.org", "@type": "Person", "@id": f"{BASE}/#tim-borchert", "name": "Tim Borchert",
              "jobTitle": "Mastering Engineer", "hasCredential": suno_credential(lang)}
    return [webpage_schema(path, t['title'], lang=lang), service, person, faq_schema(faqs),
            breadcrumb_schema([(t['home'], home), (t['crumb'], f'{BASE}{path}')])]


def suno_page(lang, live):
    t = SUNO_TEXT[lang]
    body, faqs = suno_body(lang, live)
    out = page(path=SUNO_PAIR[lang], lang=lang, title=t['title'], description=t['desc_live' if live else 'desc_dez'],
               og_title=t['og'], body=body, schemas=suno_schemas(lang, live, faqs), counterpart=SUNO_PAIR, typ='auto')
    # This page belongs to the new business (from 2027): no Heart Warrior UG and no provider name in the HTML.
    # Provider details live in the imprint; a {{ANBIETER_NAME}} placeholder would block every push (pre-push hook).
    out = re.sub(r'(<div>© )\d{4}( Polished Mastering)[^<]*(</div>)', r'\g<1>' + HEUTE[:4] + r'\g<2> · <a href="/impressum/">'
                 + ('Impressum' if lang == 'de' else 'Imprint') + r'</a>\g<3>', out, count=1)
    assert 'Heart Warrior' not in out and not re.search(r'\{\{[A-Z_]+\}\}', out), SUNO_PAIR[lang]
    return out


for _l in ('en', 'de'):
    write(SUNO_PAIR[_l], suno_page(_l, SUNO_LIVE))

# Preview of the live mode outside the repo (never committed): SUNO_VORSCHAU_DIR=<dir>
if os.environ.get('SUNO_VORSCHAU_DIR'):
    # page() records content hashes in seitenstand.json; a preview must not move the real page dates
    with open(STAND_DATEI, encoding='utf-8') as _f:
        _stand_text = _f.read()
    _stand_alt = {k: dict(v) for k, v in SEITENSTAND.items()}
    for _l in ('en', 'de'):
        _ziel = os.path.join(os.environ['SUNO_VORSCHAU_DIR'], SUNO_PAIR[_l].strip('/'), 'index.html')
        os.makedirs(os.path.dirname(_ziel), exist_ok=True)
        with open(_ziel, 'w', encoding='utf-8') as _f:
            _f.write(suno_page(_l, True))
        print('preview', _ziel)
    SEITENSTAND.clear()
    SEITENSTAND.update(_stand_alt)
    with open(STAND_DATEI, 'w', encoding='utf-8') as _f:
        _f.write(_stand_text)
