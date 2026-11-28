# Suno Mastering – Begründung, Preise, Messungen (Stand 28.11.2026)

Auftrag Tim, 28.11.2026: eigener Reiter „Suno Mastering“ auf polished.media neben Polished Auto, ein KI-Mastering-Abo für Suno- und andere KI-Tracks. Das KI-Campus-Zertifikat gehört hierher und nicht auf die Handmastering-Seiten. Bis 31.12.2026 gilt die Angebots-Sperre: nur Ankündigung und Warteliste.

Seiten: `/suno-mastering/` und `/de/suno-mastering/`, erzeugt von `_tools/gen_suno.py`, das `gen.py` aufruft.
Schalter: `_tools/suno_status.json`. Die Live-Fassung mit Tarifen, Preisen, Start-Link, Reiter in der Navigation und Offer-Schema erscheint nur, wenn **beides** gilt: Build-Datum ab 01.01.2027 **und** `live: true`. Sonst erscheinen Ankündigung und Warteliste. Das ist fail-closed: Fehlt die Datei oder ist sie kaputt, bleibt die Warteliste.
Vorschau der Live-Fassung außerhalb des Repos: `SUNO_VORSCHAU_DIR=<ordner> python _tools/gen.py`. `seitenstand.json` bleibt dabei unverändert.

## 1. Marktlage (belegt)

| Befund | Quelle | Stufe |
|---|---|---|
| Fast 75.000 vollständig KI-generierte Tracks pro Tag, rund 44 % der täglichen Uploads. Im Juni 2026 lag die Spitze über 50 %, im Juli 2026 waren es fast 90.000 am Tag. | Deezer-Pressemitteilung, 20.04.2026, Zahlen aktualisiert bis Juli 2026: https://newsroom-deezer.com/2026/04/ai-generated-tracks-represent-44-of-new-uploaded-music/ (am 28.11. selbst geöffnet) | C (Anbieterdaten) |
| Nur 1–3 % aller Streams. 2025 waren bis zu 85 % der Streams voll KI-generierter Tracks betrügerisch (an anderer Stelle derselben Seite: „up to 70 %“). KI-Tracks fliegen aus den algorithmischen Empfehlungen und den redaktionellen Playlists. | dieselbe Quelle | C |
| Nachfrage nach Suno-Mastering: Gesuche auf Upwork, viele Angebote auf Fiverr, airgigs mit 28 Angeboten (25–200 $, Median 75 $). Ein Umsatzbeleg fehlt. | Einnahmen-Scout 17.11. und 22.11.2026 (`C:/grok-bruecke/repo/einnahmen/berichte/`), Beleg 2/5 | D (anekdotisch) |
| Wettbewerb: SoundBoost.ai mit 35.133 $ MRR und 2.994 Abos, ab 16 $ im Monat unbegrenzt. OneMaster 9,90 $ pro Song (erster Song 4,90 $). HyFi ab 0,99 $ pro Track (0,33–0,50 $ pro Minute). aimusicmastering 1,99 $ für 5 Songs, nennt Suno ausdrücklich. Masterchannel Artist 15 € im Monat bei Jahreszahlung (am 28.11. geöffnet, Monatspreis auf der Seite unklar). **Kein geprüfter Anbieter nennt Metal-, Dark- oder Psy-Profile.** | Scout-Berichte (selbst geprüft), master.channel/pricing am 28.11. | C/E |
| Suno selbst: Pro 10 $ im Monat (20 Downloads), Premier 30 $ (60 Downloads), also 0,40–0,50 $ pro Track | Preisvergleichsseiten (costbench, gptprompts u. a.), nicht suno.com selbst | E |

**Folgerung Positionierung:** Der Markt für KI-Songs ist riesig, aber die Songs bringen kaum Streams, und die Plattformen sortieren sie aus. Wer damit Geld verdienen will, bekommt das nicht über ein „klingt menschlich“-Versprechen. Das wäre falsch und nach § 5 UWG riskant. Es bleibt die ehrliche Lücke: **gemessene Genreprofile für Metal, Dark und Elektronik mit PDF-Bericht**. Kein geprüfter Wettbewerber bietet das an, und Polished ist genau dort zu Hause. Nischen-Framing wirkt (Tucker & Zhang 2011, Management Science, DOI 10.1287/mnsc.1110.1312, Stufe B). Deshalb sagt die Seite offen, was das Mastering nicht kann: KI-Herkunft verschleiern, den Song reparieren oder Pop- und Hip-Hop-Profile liefern.

**KI-Etikett:** Hörer bewerten Musik schlechter, wenn sie sie für KI-gemacht halten (Ansani et al. 2025, Empirical Studies of the Arts, DOI 10.1177/02762374241308807, Stufe B, N = 120; Label-Bias in drei präregistrierten Studien bei Rego 2026, Masterarbeit NOVA, http://hdl.handle.net/10362/203560, Stufe D). Bei Bildern zeigt Bellaiche et al. 2023 dasselbe (DOI 10.1186/s41235-023-00499-6, Stufe B). Folge: Das Wort „AI mastering“ steht nicht auf den Handmastering-Seiten. Hier ist der Song selbst KI-generiert, deshalb heißt der Dienst „automatic mastering for AI tracks“. Die Engine ist gemessene DSP und keine KI. Ein „AI-powered“ wäre deshalb eine unbelegte Werbeaussage.

## 2. Preise (Live-Fassung ab Januar, Economic Value nach Nagle & Müller, Stufe C)

| Tarif | Preis | Master/Monat | pro Master | Auszahlung nach Lemon Squeezy (DE-Kunde, 19 % USt., 5 % + 0,50 $ ≈ 0,46 €) |
|---|---|---|---|---|
| Suno Starter | 9,90 € | 10 | 0,99 € | ≈ 7,36 € |
| Suno Pro | 19,90 € | 30 | 0,66 € | ≈ 15,27 € |

Rechenkosten pro Master: 0,0008–0,0014 $ (gemessen, `C:/polished-auto/testberichte/kosten_pro_track.md`). Damit trägt jede Stufe.

**Economic-Value-Rechnung, Starter (Creator mit ca. 10 Songs im Monat, Metal/Dark/Elektronik):**
- Referenzwert der nächstbesten Alternative: SoundBoost ab 16 $ (≈ 15 €) im Monat unbegrenzt, oder HyFi pro Minute bei 10 × 3,5 min ≈ 11,6–17,5 $ (≈ 11–16 €). **Referenz ≈ 11–16 €.**
- Positiver Differenzierungswert: Genreprofile für Metal, Dark und Elektronik, die kein Wettbewerber hat, dazu PDF-Bericht mit Vorher/Nachher und Qualitätsgate (ein Master, der eine Prüfung nicht besteht, wird nicht geliefert). Geschätzt +2–5 €, **Stufe E, unbelegt**.
- Negativer Differenzierungswert: gedeckelt statt unbegrenzt, keine Pop- oder Hip-Hop-Profile. Geschätzt −1–3 €.
- **Economic Value ≈ 12–18 €. Preis 9,90 € liegt unter der Untergrenze, der wahrgenommene Wert liegt also über dem Preis** (Tims Regel vom 24.11.; Zeithaml 1988: Wert = Nutzen gegen Opfer).
- Anker: Der Suno-Pro-Tarif kostet 10 $ im Monat. Das Mastering-Abo kostet so viel wie das Abo des Werkzeugs selbst. Verwandte Anker wirken am stärksten (Schley & Weingarten 2026, Management Science, DOI 10.1287/mnsc.2023.03238, Stufe A, g = 0,825).

**Suno Pro (30 Master):** Die Referenz reicht von SoundBoost (≈ 15 €, unbegrenzt) bis HyFi (30 × ≈ 1,4 $ ≈ 39 €). Der Economic Value liegt damit bei ≈ 16–41 €. 19,90 € liegt über SoundBoost und ist nur durch die Genreprofile und den Bericht gedeckt. **Risiko:** Vielnutzer ohne Metal- oder Elektronik-Bezug wandern zu SoundBoost ab. Gemessen wird die Quote Pro/Starter ab Januar.

**Nur zwei Stufen, kein Einzelkauf auf dieser Seite:** Bei unsicheren Käufern schadet zu viel Auswahl (Chernev, Böckenholt & Goodman 2014, DOI 10.1016/j.jcps.2014.08.002, Stufe A, Moderatoren). Ein Festpreis neben nutzungsbasierten Preisen ist bei Transaktionskosten profitabler (Sundararajan 2004, Management Science, DOI 10.1287/mnsc.1040.0291, Stufe D, Modell). Den Einzelmaster gibt es bei Polished Auto für 6,90 €.

**Abgrenzung zu Polished Auto (12,90 € für 4 Master):** Suno-Tarife liefern 16-Bit-WAV, MP3 und Bericht. Polished Auto liefert einen 24-Bit-Master plus Streaming-Version und rechnet die Zahlungen auf einen Auftrag bei Tim an. Das ist eine Versionierung über das Lieferformat. Bands, die für Bandcamp oder Vinyl 24 Bit brauchen, bleiben damit bei Auto. Die Wirkung dieser Abgrenzung ist **Stufe E, unbelegt**. Ab Januar wird geprüft, ob Bands in den Suno-Tarif wechseln (Genre im Upload gegen Tarif).

**Preisendung ,90:** Sie passt zu Polished Auto. Der Effekt von 9er-Endungen ist klein (Troll u. a. 2023, g = 0,13, Stufe A).

## 3. Zertifikat (KI-Campus, „KI für Alle 1“)

- Muster ist Code Chaos /bio/ (PR timelapsemedia/codechaos-seo#137): Text-Abzeichen ohne fremde Logos, darunter das Zertifikat als Bild **ohne Punktzahl**. Bilder unverändert aus dem Branch `feature/weiterbildung-ki-campus` (Commit da0fa9a, Zeile „Gesamtergebnis“ entfernt) nach `assets/weiterbildung/`. Vorschau 240 px lazy (480 JPG/WebP, 960 WebP für 2x), Vollbild 1600 WebP.
- Ort: Abschnitt „Who builds it“ / „Wer dahintersteht“, weit unten (Handy 8,2 Bildschirmhöhen) und nicht im Hero. Ein Kurszertifikat ist ein Nebenbeleg: besser als kein Nachweis, schwächer als jeder Abschluss (Rivas, Baker & Evans 2020, AERA Open, DOI 10.1177/2332858420973577, Stufe B). Die Expertise der Quelle wirkt auf Glaubwürdigkeit und Kaufabsicht (Ismagilova et al. 2020, DOI 10.1016/j.jretconser.2019.01.005, Stufe A).
- Schema: `Person` (@id `/#tim-borchert`) mit `hasCredential` als `EducationalOccupationalCredential` (Name DE/EN, Kategorie, Kurs-URL, Bild, `recognizedBy` KI-Campus und HHU).
- Auf den Handmastering-Seiten bleibt es weg, wegen der Abwertung durch das KI-Etikett (Bellaiche et al. 2023, Stufe B).
- Wortlaut ohne „certified“, „zertifiziert“ oder „KI-Experte“, weil ein 45-Stunden-Einstiegskurs keine Zertifizierung ist (§ 5 UWG).

## 4. Varianten und Messungen (28.11.2026, lokal, http.server, Chrome-Bereich)

**Reihenfolge der Abschnitte, gemessen an der Formularposition auf dem Handy (390 × 844, in Bildschirmhöhen).** Kriterium: Formular innerhalb von ≤ 4 Bildschirmhöhen. Die Aufmerksamkeit liegt zu 74 % in den ersten zwei Höhen (Fessenden 2018, NN/g, Stufe D). Außerdem soll „So funktioniert es“ vor dem Formular stehen, der Nutzen also vor der Bitte (Dodds, Monroe & Grewal 1991, Stufe B, übertragen).

| Variante | Reihenfolge | Formular EN | Formular DE | Kriterium |
|---|---|---|---|---|
| A | Zahlen, So geht's, Profile, Nicht, Wege, Wer, Warteliste, FAQ | 8,46 | 8,64 | nein |
| **B (gewählt)** | So geht's, Profile, **Warteliste**, Zahlen, Nicht, Wege, Wer, FAQ | **3,88** | **3,96** | **ja** |
| C | So geht's, Zahlen, Warteliste, Profile, … | 4,31 | 4,42 | nein |

Desktop 1366 × 850: Formular bei 3,22 Höhen.

**Text (ig-human, `detect.py`):**

| Fassung | Ergebnis |
|---|---|
| EN v1 (sachlich, ohne Kurzformen) | 66,1 REVIEW, Schwachstelle VOICE 37,5, 4 Gedankenstriche |
| **EN v2 (Kurzformen, Ansprache, ohne Gedankenstriche)** | **80,0 PASS** (VOICE 62,0, FINGERPRINT 97,7) |
| EN live (Januar) | 76,4 PASS |

**Weitere Prüfungen:**
- Angebots-Gate `python C:/kunden-kreislauf/angebots_sperre.py --pruefe <text> --termin 2026-12-10` auf dem sichtbaren Text (Titel, Beschreibung, `<main>`): EN Exit 0, DE Exit 0. Der erste Lauf schlug an, weil „1–3 %“ als Rabatt „−3 %“ gelesen wurde (Fehlalarm). Jetzt steht dort „between 1 and 3%“ bzw. „zwischen 1 und 3 %“. Gegenprobe Live-Fassung: am 10.12. Exit 1 (gesperrt, richtig), am 02.01.2027 Exit 0.
- Schema: Alle 5 Blöcke (WebPage, Service, Person + hasCredential, FAQPage, BreadcrumbList) in Dezember- und Live-Fassung gegen das schema.org-Vokabular geprüft (Typ vorhanden, Eigenschaft vorhanden, Domain passt). Ergebnis: gültig. `inLanguage` an `Service` war ungültig und ist entfernt.
- Handy 390 px: kein horizontaler Überlauf, Tabellen scrollen in ihrem eigenen Rahmen, Fließtext ≥ 14 px (kleiner sind nur die seitenweiten Mono-Labels mit 11–12 px), Zertifikatsbild lädt (240 px).
- Keine `{{…}}`-Platzhalter und keine Heart Warrior UG im HTML: Die Fußzeile der Suno-Seiten ist ersetzt durch „© 2026 Polished Mastering · Imprint/Impressum“ (Assert in `suno_page`).

## 5. Offen (vor `live: true` in `suno_status.json`)

- [ ] Polished Auto live (`/auto/` existiert, Branch `polished-auto-2027` gepusht); vorher zeigt der Link `/auto/app/?plan=…` ins Leere. Darum hängt die Live-Fassung am Schalter.
- [ ] Tarife `suno_starter` und `suno_pro` in `C:/polished-auto/server/config.py` (PLANS) und als Varianten in Lemon Squeezy anlegen.
- [ ] Engine: Lieferformat 16 Bit / 44,1 kHz mit Dither plus MP3; an echten Suno-Exporten pro Genreprofil testen (MCP `suno` vorhanden, verbraucht Suno-Credits). Danach die Aussagen auf der Seite gegen die Messwerte prüfen.
- [ ] AGB und Kündigungsseite von Polished Auto um die Suno-Tarife ergänzen; Anbieterangaben ausfüllen (kein `{{ANBIETER_NAME}}` mehr).
- [ ] Ab Januar messen: Wartelisten-Einträge (Feld „Songs pro Monat“ prüft die Stufen-Annahme 10/30), Quote Starter/Pro, Abwanderung Monat 1, Bands im Suno-Tarif. Die GA4-Ereignisse `cta_click` (data-track `suno-*`) und `generate_lead` liefert site.js bereits.
- [ ] Seitenweite Navigation zeigt im Dezember weiter „Request Audit →“. Das ist nicht Teil dieser Seite; `hw_ende.py` blendet dafür den Dezember-Hinweis ein.
