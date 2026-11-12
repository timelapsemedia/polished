---
url: /metal-loudness-data/
title: "Metal & Gothic Loudness Data 2026: LUFS and DR of Real Releases | Polished"
description: "Measured, not guessed: black metal releases sit at about -8 LUFS, DSBM near -12.7, doom and gothic at -7.5. Medians, ranges and method from 64 releases."
h1: "What metal and gothic releases actually measure"
typ: article
schema: Article + Dataset + FAQPage
hreflang_de: /de/metal-lautheit-daten/
---

Most loudness advice for metal is a range somebody remembers. This page is the other thing: numbers measured from released records, with the method written down so you can check it. We've used the same corpus as the reference for every Polished master and every mix audit.

**Short answer:** in our measurements the median black metal release sits at about −8 LUFS integrated, depressive black metal (DSBM) much quieter at about −12.7 LUFS, doom, gothic and dark wave at about −7.5 LUFS, and modern and industrial metal at about −7 LUFS. That's what records do. It isn't what yours has to do.

<!-- TABELLEN: tabellen_polished_en.md hier einsetzen -->

## How to read these numbers

- **Integrated loudness (LUFS):** the average loudness of the whole track after the ITU-R BS.1770 weighting. The value in brackets is the middle half of the releases (25th to 75th percentile). So a quarter of the records you'd find is quieter than the first number, and a quarter is louder than the second.
- **DR:** the dynamic range figure as the DR database computes it (second-highest peak against the loudest 20 % of RMS blocks, per channel, averaged). Higher means there's more distance between peaks and body.
- **LRA:** loudness range in LU, how much the loudness moves between quiet and loud passages.
- **PLR:** peak-to-loudness ratio, true peak minus integrated loudness. Low values mean the limiter is doing a lot of the work.
- **Side/mid:** energy of the side signal against the mid signal. Closer to 0 dB means a wider mix.
- **Correlation below 150 Hz:** 1.00 is fully mono low end. Values well under 0.9 can lose bass on mono club systems and phone speakers.
- **Tonal balance:** each band's level relative to the 1 kHz band in the median release. It's the shape of the spectrum, not a target curve.

## What stands out

- **DSBM is the quiet one.** About 5 dB below black metal in the median, with a DR around 10. That fits the genre's slow, sustained material: there's little reason to push a 9-minute dirge into a limiter.
- **Black metal keeps more dynamics than doom and gothic.** DR 7.5 against 5.6, even though the loudness is similar. Doom and gothic records tend to be denser and more compressed in the low mids.
- **Doom, gothic and dark wave carry the most low end.** +17 dB below 125 Hz relative to 1 kHz, against +15 in black metal and +10 in DSBM.
- **Black metal top end is darker than you'd expect.** The air band (6.3 to 12.5 kHz) sits about 18 dB under 1 kHz in the median. The harsh sound most people associate with the genre lives in the guitars' upper mids, not in a bright master.
- **Nobody masters metal to −14 LUFS.** Streaming platforms turn everything down to about −14 anyway, so the loudness you choose decides density and transient detail, not playback volume.

## How the data was collected

- **Corpus:** 16 commercially released tracks per genre from 8 to 12 different artists. No artist contributes more than 2 of the 16 tracks.
- **Sources:** lossless files where we have them, otherwise high-bitrate lossy files. The table shows how many of the 16 were lossless. Where at least five lossless files exist, the dynamics values (DR, LRA, PLR, true peak) come only from those. Where they don't, we've marked the value with an asterisk. We measured how much MP3 shifts the numbers on our own reference files: DR reads about 1 dB high, loudness about 0.3 LU low.
- **Top end:** bands above 12.5 kHz only count files that actually contain full-band audio, because 128 kbit/s encoders cut there.
- **Software:** our own measuring core (the same one behind the free mix audit), loudness after BS.1770, DR after the DR-database method, true peak with 4× oversampling.
- **What we don't publish:** values of single tracks or artists. The page shows only medians and ranges.
- **Sample size:** 16 per genre is enough for a median and a rough range, not for fine distinctions. Melodic death metal (6 releases) and grindcore (7 releases from 3 artists) are left out until there is enough material. The corpus keeps growing, and we update this page with the date below.

## What this means for your master

A number in this table describes the genre. It's not a quality score. Being close to the median says your record is typical, not that it is good. A DSBM album mastered at −8 LUFS is not wrong because the median is −12.7, but it will sound denser than most of its neighbours on a playlist, and it gives up the slow swells that make the style work.

Here's what we actually check in a master or a mix audit:

1. Where the loudness sits in the genre range, and what it costs in that specific mix.
2. Whether the tonal balance falls outside the typical range in a band that matters (for black metal: low mids under the guitars, presence of the snare).
3. Low-end correlation and mono compatibility.
4. True peak headroom for streaming encoders.

If you want those numbers for your own mix, the free mix audit measures it against this corpus and sends a written report. [Request a free mix audit](/#audit).

## Metal loudness FAQ

**How loud should a metal master be?**
There isn't one value. Our measured medians run from about −12.7 LUFS (DSBM) to about −7 LUFS (modern and industrial metal). Pick the level your mix can hold before the cymbals and blast beats start to smear, then check true peak.

**How loud should a metal mix be before mastering?**
Mix loudness doesn't matter much as long as nothing clips and the mix bus isn't limited. Leave a few dB of headroom (peaks around −6 to −3 dBFS) so the master has room to work.

**What LUFS should black metal be mastered to?**
The middle half of the black metal releases we measured sits between −9.6 and −6.9 LUFS, median −8.0. Atmospheric and depressive black metal usually sits lower.

**Will Spotify turn my loud metal master down?**
Yes. With normalization on, Spotify plays everything at about −14 LUFS, so a −7 LUFS master is turned down by about 7 dB. It doesn't get louder than other tracks, only denser.

**Why is DSBM mastered quieter than other black metal?**
In our data the median DSBM release is about 5 dB quieter with clearly more dynamic range. Long, slow, sustained material gains little from heavy limiting and loses its swells.

**Can I use these numbers as a target?**
Use them as a map, not a target. They tell you where released records sit. Whether your record should sit in the middle or at the edge depends on the mix and on what you want it to sound like.

Related: [How loud should metal be mastered? LUFS guide](/metal-mastering-loudness/) | [Black metal mastering](/black-metal-mastering/) | [Doom & gothic mastering](/doom-gothic-mastering/)
