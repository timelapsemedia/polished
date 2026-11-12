# polished.media – GEO-Merkmale für die SEO-/GEO-Läufe

Gilt für jeden Lauf, der die Generatoren in `_tools/` bearbeitet (auch „Weekly run“).

**SEO-Arbeitsliste aus GSC (Pos. 8–30, CTR):** [`SEO-ARBEITSLISTE.md`](SEO-ARBEITSLISTE.md). Der Weekly run arbeitet zuerst deren offene Punkte ab, statt selbst neu zu suchen (Grok #72). Messwerte der Datenseiten nur aus `daten/genre_index.json` (erzeugt von `C:/traffic/seiten/genre_index.py`), nie von Hand.

## GEO-Merkmale (fester Arbeitsvorrat, seit 05.11.2026)

Grundlage: SISTRIX-Studie „Citation Worthiness“ vom 22.10.2026. Ausgewertet wurden 96.418 URLs aus ChatGPT, Google AI Mode und AI Overviews, jeweils zitierte gegen nicht zitierte Seiten derselben Domain. Es entscheidet also die einzelne Seite, nicht die Marke. Quelle: https://www.sistrix.de/news/geo-mythen-im-datencheck/. Die Werte sind Korrelationen, keine Kausalität.

Der Faktor gibt an, wie viel öfter eine Seite mit dem Merkmal zitiert wird. Seiten mit vielen der elf Merkmale werden etwa 2,1× so oft zitiert wie kaum optimierte.

| Prio | Merkmal | Faktor | Umsetzung |
|---|---|---|---|
| 1 | Sichtbares Inhaltsverzeichnis mit Sprungmarken | 1,7 | Kasten „Auf dieser Seite / On this page“ unter der H1, Links auf die H2-IDs |
| 2 | Article-Schema | 1,6 | Ratgeber- und Genre-Seiten bekommen `Article` mit `author`, `datePublished`, `dateModified`; Produktseiten behalten `Product`/`SoftwareApplication` (AI Overviews zitieren Produktseiten seltener, dort kein Article erzwingen) |
| 2 | Mindestens 5 klare H2 | 1,6 | Jede H2 beantwortet eine Frage |
| 3 | FAQ mit echten Fragen (FAQPage) | 1,4–1,5 | Fragen aus GSC/Bing-Suchanfragen, keine erfundenen |
| 3 | Tabelle mit Kopfzeile (`<th>`) | 1,4–1,5 | Vergleiche, Preise, technische Werte als echte Tabelle |
| 3 | Autorenbox mit Foto | 1,4 | „Tim Borchert“ mit echtem Foto, 1–2 Sätze, Link auf die Über-mich-Seite; `author` im Schema |
| 4 | Sichtbares Datum „Zuletzt aktualisiert“ | 1,3 | Aus dem Build-Datum der Seite, nur bei echter inhaltlicher Änderung erhöhen |
| 4 | Mindestens 1.000 Wörter | 1,5 | Nur mit echtem Inhalt für die Suchabsicht, nie Füllstoff |

**Umsetzung seit 05.11.2026 (`_tools/gen_geo.py`, automatisch über `page(..., typ=...)`):**
- `typ='article'` (Genre-, Ratgeber-, Preis-, Stem- und Label-Seiten): Inhaltsverzeichnis am Ende des Hero mit Links auf alle H2, `Article`-Schema (headline, author Tim Borchert, publisher, datePublished, dateModified, inLanguage), Autorenbox mit Foto, sichtbares „Last updated / Zuletzt aktualisiert“.
- `typ='produkt'` (/tools/*): wie oben, aber kein `Article`; `SoftwareApplication`/`Product` bekommen `author` und `dateModified`.
- `typ='home'` (/de/): Autorenbox und Datum, kein Inhaltsverzeichnis. index.html ist handgepflegt: nur der Block zwischen `<!-- geo:pakete -->` wird aus `PAKETE` neu geschrieben.
- Datum = letzte echte Textänderung: `_tools/seitenstand.json` hält je Seite einen Hash des sichtbaren Texts. Ändert sich der Text, springt das Datum auf den Build-Tag, sonst bleibt es. `seitenstand.json` immer mit den Seiten committen. `sitemap.xml` lastmod wird daraus gesetzt.
- Im Hero-Text steht das Datum als Platzhalter `%%STAND%%`.
- Tabellen: `laut_tabelle()` (Genre-Seiten, Werte aus dem Lautstärke-Guide), `paket_tabelle()` (/ und /de/, Werte wie die Preiskarten).
- Prüfen lokal: `python _tools/geo_merkmale.py https://polished.media --lokal .`

**Kaum Wirkung:** llms.txt, eine Ziel-Wortzahl als Selbstzweck, Lesbarkeitswerte sowie Breadcrumb-, HowTo- und QAPage-Schema. Diese nicht als GEO-Hebel verkaufen.

**Ablauf:**
1. Jede Routine misst live mit dem Prüfwerkzeug, welche Seiten welche Merkmale nicht haben:
   - codechaos-official.de: `python3 _build/geo_merkmale.py https://codechaos-official.de`
   - polished.media: `python3 _tools/geo_merkmale.py https://polished.media`
2. Die fehlenden Merkmale kommen **zentral in den Generator**, nicht als Handarbeit pro Seite:
   - codechaos: `_build/build_pages.py`
   - polished: `_tools/gen*.py`
3. Reihenfolge nach Prio: zuerst Inhaltsverzeichnis, dann Article-Schema mit Autor und Datum plus Autorenbox, dann Tabellen.
4. Pro Lauf eine Merkmal-Gruppe umsetzen, bauen, live prüfen (seo-werkstatt `seite_pruefen`) und IndexNow anstoßen.
5. Wirkung frühestens nach 4–8 Wochen bewerten: KI-Zitate über den SISTRIX-AI-Index, falls verfügbar, sonst über die Grok-Aufgabe T18 (KI-Sichtbarkeit) und GSC.
6. Messstand 05.11.2026 (Prüfwerkzeug, Anzahl Seiten ohne das Merkmal):
   - **codechaos-official.de, 21 Seiten:** AUTOR 21, DATUM 18, TOC 11, ART 7, WORTE 7, TAB 1, FAQ 1.
   - **polished.media, 36 Seiten:** AUTOR 36, DATUM 35, TOC 33, ART 28, WORTE 12, TAB 10, H2 3.
