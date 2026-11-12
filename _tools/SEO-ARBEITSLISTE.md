# SEO-Arbeitsliste polished.media (Hebel 2, Stand 11.11.2026)

Quelle: Search Console sc-domain:polished.media, 14.10.–10.11.2026, gemessen mit `python C:/traffic/wirkung.py` (Rohdaten `C:/traffic/daten/letzter_stand.json`). Evidenz: eigene Daten (Stufe C, Beobachtung). Regel aus P6: zuerst Seiten mit Impressionen auf Position 8–30, Genre-Unterseiten nur bei belegtem Suchvolumen. Ergänzt #60 (dort Punkt 1 Kostenseite, Punkt 4 Lautheits-Guide mit eigenen Messwerten), dupliziert nichts.

## A. Sofort (CTR-Hebel, Seite steht schon gut)

| Seite | Impr. | Klicks | Pos. | Maßnahme |
|---|---|---|---|---|
| /metal-mastering-loudness/ | 249 | 2 | 6,8 | CTR 0,8 % bei Pos. 7 ist schwach. Title/Description mit gemessenen Zahlen: Title „How Loud Should Metal Be Mastered? Measured LUFS of Real Releases (2026)“, Description „Measured medians: black metal about −8 LUFS, DSBM −12.7, doom/gothic −7.5 (16 releases each). Streaming plays at −14. True-peak limits and how to choose.“ Subgenre-Tabelle: Werte für Black, DSBM, Doom/Gothic, Modern Metal aus der neuen Datenseite übernehmen und auf sie verlinken; „orientation ranges“ für die übrigen Genres lassen. |
| /de/metal-mastering-lautstaerke/ | 20 | 2 | 4,6 | Gleiches auf Deutsch, Link auf /de/metal-lautheit-daten/. |

## B. Position 8–30 (Inhaltstiefe, interne Links)

| Seite / Suchanfrage | Impr. | Pos. | Maßnahme |
|---|---|---|---|
| /tools/ ← „mix polishing plugin“ | 74 (Anfrage 49) | 17–18 | Einziger Pos.-8–30-Begriff mit Volumen. H2 + kurzer Absatz „Mix polishing plugins“: welche eigenen Tools welchen Polier-Schritt machen (Sättigung Crucible, Phase/Low End Kick/Bass Scope …), nur Fakten aus den Produktseiten. Title-Zusatz prüfen. |
| /de/ | 27 | 11,8 | Interne Links von Genre-Seiten und Datenseite auf /de/ mit Anker „Metal & Gothic Mastering“. |
| /de/death-metal-mastering/ | 10 | 12,3 | Inhaltstiefe (EN-Seite steht auf 3,2): DE an EN angleichen, Datenseite verlinken. |
| /de/tools/ + /de/tools/chaos-fm, crucible, frostfret | 9 / 5 / 2 / 5 | 7–11 | DE-Produktseiten an EN-Stand angleichen (EN jeweils besser platziert). |
| /de/stem-mastering/ ← „stem mastering preise“, „stems verkaufen“ | 8 | 20–32 | Preis-Absatz mit Stem-Preis (öffentliches Angebot) oben, FAQ „Was kostet Stem-Mastering?“. „stems verkaufen“ ist fremde Suchabsicht: nicht bedienen. |
| /de/mastering-fuer-labels/, /mastering-for-labels/ | 8 / 5 | 23 / 31 | Nur interne Links (Startseite, Kostenseite); kein Volumen für mehr Aufwand. |

## C. Großes Volumen außerhalb 8–30 (in #60 Punkt 1 schon beauftragt)

/de/mastering-kosten/: 722 Impressionen auf Pos. ~61 („mastering preise/kosten“, „online mastering preise“, „mixing mastering kosten“, je 55–100 Impr.). Bleibt bei #60; hier nur der Hinweis, dass es weiter das größte Volumen der Domain ist.

## D. Neue Seiten (Hebel 1, GEO)

- /metal-loudness-data/ + /de/metal-lautheit-daten/: Texte `C:/traffic/seiten/seite_polished_en.md` / `_de.md`, Tabellen `tabellen_polished_en.md` / `_de.md` (aus `genre_index.py`, nicht von Hand ändern). typ='article', Schema Article + Dataset (variableMeasured, measurementTechnique, temporalCoverage 2026, creator Tim Borchert, license „© Polished“) + FAQPage. In llms.txt / llms-full.txt, Sitemap, IndexNow; Links von Loudness-Guide, Black-/Doom-Gothic-Seiten.
- codechaos-official.de /en/psy-loudness-data/ + /psy-lautheit-daten/: Texte `seite_codechaos_en.md` / `_de.md`, Tabellen `tabellen_codechaos_*.md`. Links von /mastering/, /psycore/, /hitech-psytrance/, Kick/Bass-Scope-Seite; llms.txt.

## Messung

Wöchentlich montags über `C:/kunden-kreislauf/messen.py` → `C:/traffic/wirkung.py` (Bericht `C:/traffic/berichte/wirkung_<datum>.md`). Erfolgskriterium nach 4 Wochen (Messdatum 09.12.2026): Klicks auf /metal-mastering-loudness/ > 2 je 28 T bei ähnlichen Impressionen; Pos.-8–30-Paare rücken nach oben; KI-Sitzungen ≥ 16.

## Umsetzungsstand (Website-Bau-Lauf Grok #72, 12.11.2026)

Der Weekly run arbeitet nur die offenen Punkte ab und misst die erledigten erst am 09.12.2026 (4 Wochen).

- [x] A /metal-mastering-loudness/ + /de/metal-mastering-lautstaerke/: Title (auf ≤ 60 Zeichen gekürzt), Description, Subgenre-Tabelle mit Messwerten aus `daten/genre_index.json` (Black, DSBM, Doom/Gothic/Dark Wave, Modern/Industrial), übrige Zeilen als Orientierung, Links auf die Datenseite.
- [x] B /tools/: Abschnitt „Mix polishing plugins“ (Crucible, Kick/Bass Scope, Rimehall) + DE, EN-Title „Tools for Bands: Mix Polishing Plugins for Metal“.
- [x] B /de/: Anker „Metal & Gothic Mastering“ von allen DE-Genre-Seiten (Lautheitstabelle) und von der DE-Datenseite.
- [x] B /de/death-metal-mastering/, /de/tools/*: geprüft, schon auf EN-Stand (gleiche H2/FAQ-Zahl, 92–96 % der EN-Wortzahl); Link auf die Datenseite über die Lautheitstabelle.
- [x] B /de/stem-mastering/: Preis steht schon in Title, H1 und Lead, FAQ „Was kostet Stem-Mastering?“ vorhanden; nichts geändert.
- [x] B Labels: Link von /de/ ergänzt (/ und Kostenseiten hatten ihn schon).
- [x] D Datenseiten /metal-loudness-data/ + /de/metal-lautheit-daten/ (`gen_daten.py`, Quellen `daten/`).
- [ ] C /de/mastering-kosten/ bleibt bei #60.
