---
url: /de/metal-lautheit-daten/
title: "Metal & Gothic Lautheit 2026: LUFS und DR echter Releases | Polished"
description: "Gemessen statt geschätzt: Black Metal liegt im Median bei etwa −8 LUFS, DSBM bei −12,7, Doom und Gothic bei −7,5. Mediane, Spannen und Methode aus 64 Releases."
h1: "Was Metal- und Gothic-Releases wirklich messen"
typ: article
schema: Article + Dataset + FAQPage
hreflang_en: /metal-loudness-data/
---

Die meisten Lautheitstipps für Metal sind Spannen, an die sich jemand erinnert. Diese Seite ist das Gegenteil: Messwerte veröffentlichter Platten, mit offengelegter Methode zum Nachprüfen. Derselbe Korpus ist die Referenz für jedes Polished-Master und jeden Mix-Audit.

**Kurz:** In unseren Messungen liegt das mittlere Black-Metal-Release bei etwa −8 LUFS integriert, Depressive Black Metal (DSBM) deutlich leiser bei etwa −12,7 LUFS, Doom, Gothic und Dark Wave bei etwa −7,5 LUFS und moderner bzw. Industrial Metal bei etwa −7 LUFS. Das ist, was Platten tun, nicht, was deine tun muss.

<!-- TABELLEN: tabellen_polished_de.md hier einsetzen -->

## So liest du die Werte

- **Integrierte Lautheit (LUFS):** mittlere Lautheit des ganzen Tracks nach ITU-R BS.1770. In Klammern steht die mittlere Hälfte der Releases (25. bis 75. Perzentil). Ein Viertel der Platten ist leiser als der erste Wert, ein Viertel lauter als der zweite.
- **DR:** Dynamikwert nach der Methode der DR-Datenbank (zweithöchster Spitzenwert gegen die lautesten 20 % der RMS-Blöcke, je Kanal, gemittelt). Höher heißt mehr Abstand zwischen Spitzen und Körper.
- **LRA:** Lautheitsumfang in LU, also wie stark sich die Lautheit zwischen leisen und lauten Passagen bewegt.
- **PLR:** Verhältnis von Spitze zu Lautheit, True Peak minus integrierte Lautheit. Niedrige Werte heißen: Der Limiter arbeitet viel.
- **Side/Mid:** Energie des Seitensignals gegen das Mittensignal. Je näher an 0 dB, desto breiter.
- **Korrelation unter 150 Hz:** 1,00 ist komplett monofones Low End. Werte deutlich unter 0,9 können auf Mono-Anlagen und Handylautsprechern Bass kosten.
- **Tonale Balance:** Pegel jedes Bandes relativ zum 1-kHz-Band im mittleren Release. Sie zeigt die Form des Spektrums, keine Zielkurve.

## Was auffällt

- **DSBM ist das leise Genre.** Im Median etwa 5 dB unter Black Metal, mit einem DR um 10. Das passt zum langsamen, getragenen Material: Ein neunminütiges Klagelied gewinnt nichts durch harten Limiter.
- **Black Metal behält mehr Dynamik als Doom und Gothic.** DR 7,5 gegen 5,6, bei ähnlicher Lautheit. Doom- und Gothic-Platten sind meist dichter und in den unteren Mitten stärker komprimiert.
- **Doom, Gothic und Dark Wave haben das meiste Low End.** +17 dB unter 125 Hz relativ zu 1 kHz, gegen +15 bei Black Metal und +10 bei DSBM.
- **Die Höhen im Black Metal sind dunkler, als viele denken.** Das Höhenband (6,3 bis 12,5 kHz) liegt im Median etwa 18 dB unter 1 kHz. Die Härte, die man mit dem Genre verbindet, sitzt in den oberen Mitten der Gitarren, nicht in einem hellen Master.
- **Niemand mastert Metal auf −14 LUFS.** Streamingdienste regeln ohnehin alles auf etwa −14 herunter. Die gewählte Lautheit entscheidet über Dichte und Transienten, nicht über die Wiedergabelautstärke.

## So wurden die Daten erhoben

- **Korpus:** 16 veröffentlichte Tracks je Genre von 8 bis 12 verschiedenen Künstlern. Kein Künstler steuert mehr als 2 der 16 Tracks bei.
- **Quellen:** verlustfreie Dateien, wo vorhanden, sonst verlustbehaftete Dateien mit hoher Bitrate. Die Tabelle zeigt, wie viele der 16 verlustfrei waren. Gibt es mindestens fünf verlustfreie Dateien, stammen die Dynamikwerte (DR, LRA, PLR, True Peak) nur aus diesen, sonst ist der Wert mit Sternchen markiert. Wie stark MP3 die Werte verschiebt, haben wir an eigenen Referenzdateien gemessen: DR liest etwa 1 dB zu hoch, die Lautheit etwa 0,3 LU zu niedrig.
- **Höhen:** Bänder über 12,5 kHz zählen nur Dateien mit echtem Vollband-Audio, weil 128-kbit/s-Encoder dort abschneiden.
- **Software:** unser eigener Messkern (derselbe wie im kostenlosen Mix-Audit), Lautheit nach BS.1770, DR nach der Methode der DR-Datenbank, True Peak mit 4-facher Überabtastung.
- **Was wir nicht veröffentlichen:** Werte einzelner Tracks oder Künstler. Die Seite zeigt nur Mediane und Spannen.
- **Stichprobe:** 16 je Genre reichen für einen Median und eine grobe Spanne, nicht für feine Unterschiede. Melodic Death Metal (6 Releases) und Grindcore (7 Releases von 3 Künstlern) fehlen, bis genug Material da ist. Der Korpus wächst, die Seite wird mit Datum aktualisiert.

## Was das für dein Master heißt

Ein Wert in dieser Tabelle beschreibt das Genre, er ist keine Qualitätsnote. Nah am Median heißt: typisch, nicht gut. Ein DSBM-Album auf −8 LUFS ist nicht falsch, weil der Median bei −12,7 liegt. Es klingt aber dichter als die meisten Nachbarn in einer Playlist und gibt die langsamen Steigerungen auf, von denen der Stil lebt.

Was wir in einem Master oder Mix-Audit tatsächlich prüfen:

1. Wo die Lautheit in der Genre-Spanne liegt und was sie in genau diesem Mix kostet.
2. Ob die tonale Balance in einem wichtigen Band außerhalb der typischen Spanne liegt (bei Black Metal: untere Mitten unter den Gitarren, Präsenz der Snare).
3. Korrelation und Monotauglichkeit im Low End.
4. True-Peak-Reserve für die Encoder der Streamingdienste.

Wenn du diese Werte für deinen eigenen Mix willst: Der kostenlose Mix-Audit misst ihn gegen diesen Korpus und schickt einen schriftlichen Bericht. [Kostenlosen Mix-Audit anfragen](/de/#audit).

## Häufige Fragen zur Metal-Lautheit

**Wie laut sollte ein Metal-Master sein?**
Einen festen Wert gibt es nicht. Unsere gemessenen Mediane reichen von etwa −12,7 LUFS (DSBM) bis etwa −7 LUFS (moderner und Industrial Metal). Nimm die Lautheit, die dein Mix hält, bevor Becken und Blastbeats verschmieren, und prüfe dann den True Peak.

**Wie laut sollte ein Metal-Mix vor dem Mastering sein?**
Die Mix-Lautheit spielt kaum eine Rolle, solange nichts clippt und auf dem Summenbus kein Limiter sitzt. Lass ein paar dB Reserve (Spitzen etwa bei −6 bis −3 dBFS), damit das Mastering Raum hat.

**Auf wie viel LUFS wird Black Metal gemastert?**
Die mittlere Hälfte der von uns gemessenen Black-Metal-Releases liegt zwischen −9,6 und −6,9 LUFS, Median −8,0. Atmosphärischer und depressiver Black Metal liegt meist darunter.

**Regelt Spotify mein lautes Metal-Master herunter?**
Ja. Mit aktivierter Normalisierung spielt Spotify alles bei etwa −14 LUFS, ein Master mit −7 LUFS wird also um etwa 7 dB leiser gestellt. Es wird nicht lauter als andere Tracks, nur dichter.

**Warum wird DSBM leiser gemastert als anderer Black Metal?**
In unseren Daten ist das mittlere DSBM-Release etwa 5 dB leiser und hat deutlich mehr Dynamik. Langes, langsames, getragenes Material gewinnt durch starkes Limiting wenig und verliert seine Steigerungen.

**Kann ich die Werte als Ziel nehmen?**
Nimm sie als Karte, nicht als Ziel. Sie zeigen, wo veröffentlichte Platten liegen. Ob deine Platte in der Mitte oder am Rand liegen sollte, hängt vom Mix ab und davon, wie sie klingen soll.

Siehe auch: [Metal-Mastering-Lautstärke: LUFS-Ratgeber](/de/metal-mastering-lautstaerke/) · [Black Metal Mastering](/de/black-metal-mastering/) · [Doom & Gothic Mastering](/de/doom-gothic-mastering/)
