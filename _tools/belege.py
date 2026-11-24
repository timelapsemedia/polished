# Citable evidence for the loudness guide (EN + DE). Loaded by gen.py via exec, shares its globals (sec, gi_genre, gi_wert).
#
# Why: Aggarwal et al. 2024, "GEO: Generative Engine Optimization" (KDD, DOI 10.1145/3637528.3671900): source citations,
# verbatim quotations and statistics raise visibility in generative answers by 30-40 %.
#
# Rules:
#   - Every quotation is verbatim from the linked source (read on 24 Nov 2026). Do not reword quotations.
#   - Measured values come from genre_index.json via gi_genre(); nothing is typed in by hand.
#   - No prices and no buy links in these blocks (offer freeze December 2026).

LG_SPOTIFY = dict(name="Loudness normalization", autor="Spotify for Artists", jahr="retrieved 2026-11-24",
                  url="https://support.spotify.com/us/artists/article/loudness-normalization/")
LG_ITU = dict(name="Recommendation ITU-R BS.1770-5: Algorithms to measure audio programme loudness and true-peak audio level",
              autor="International Telecommunication Union", jahr="2023", url="https://www.itu.int/rec/R-REC-BS.1770")
LG_EBU = dict(name="EBU R 128: Loudness normalisation and permitted maximum level of audio signals (version 5.0)",
              autor="European Broadcasting Union", jahr="2023", url="https://tech.ebu.ch/publications/r128")
LG_KR = dict(name="Dynamic Range Across Music Genres and the Perception of Dynamic Compression in Hearing-Impaired Listeners",
             autor="Martin Kirchberger and Frank Russo", jahr="2016", url="https://doi.org/10.1177/2331216516630549",
             quelle="Trends in Hearing 20")
LG_QUELLEN = [LG_SPOTIFY, LG_ITU, LG_EBU, LG_KR]
LG_ZITAT = "We adjust tracks to -14 dB LUFS, according to the ITU 1770 standard."   # verbatim, Spotify for Artists
LG_SPOTIFY_REF = -14.0

LG_T = {
 'en': dict(
    id='lg-numbers', titel='Metal loudness <em>in numbers</em>',
    intro='The figures most often asked about, each with its source. Measured values are our own analysis of released records (<a href="/metal-loudness-data/">method and full tables</a>).',
    kopf=('Figure', 'Value', 'Source'),
    genres=[('black', 'Black metal releases'), ('dsbm', 'Depressive black metal (DSBM) releases'), ('doom_gothic', 'Doom / gothic releases'), ('modern_metal', 'Modern and industrial metal releases')],
    med='median {m} LUFS ({n} releases)', eigen='own measurement',
    zeilen_vor=[('Spotify playback reference', '−14 LUFS (Loud −11, Quiet −19)', 'Spotify for Artists'),
                ('Measurement standard for LUFS and true peak', 'ITU-R BS.1770-5 (November 2023)', 'ITU'),
                ('Broadcast target, for comparison', '−23 LUFS', 'EBU R 128')],
    runter='How far Spotify turns a median black metal master down', runter_wert='about {d} dB', runter_q='calculated: {m} LUFS to −14 LUFS',
    peak=('True-peak ceiling', '−1 dBTP, or −2 dBTP for masters louder than −14 LUFS', 'Spotify for Artists'),
    zitat_label='In Spotify\'s own words', zitat_quelle='Spotify for Artists, Loudness normalization',
    studie='Dense masters are not unique to metal. An acoustic analysis of recorded music found that samples from popular genres such as rock or rap generally have a smaller dynamic range than samples from classical genres (<a href="https://doi.org/10.1177/2331216516630549" rel="noopener" target="_blank">Kirchberger &amp; Russo 2016</a>, Trends in Hearing).',
    q_id='lg-sources', q_titel='Sources', q_intro='Platform values, standards and measurements on this page are based on:',
    q_eigen='Polished: <a href="/metal-loudness-data/">metal loudness data</a>, own measurement of 16 releases per genre after ITU-R BS.1770.'),
 'de': dict(
    id='lgd-numbers', titel='Metal-Lautheit <em>in Zahlen</em>',
    intro='Die am häufigsten gefragten Werte, jeweils mit Quelle. Die Messwerte stammen aus unserer eigenen Analyse veröffentlichter Platten (<a href="/de/metal-lautheit-daten/">Methode und alle Tabellen</a>).',
    kopf=('Kennzahl', 'Wert', 'Quelle'),
    genres=[('black', 'Black-Metal-Releases'), ('dsbm', 'Depressive-Black-Metal-Releases (DSBM)'), ('doom_gothic', 'Doom- und Gothic-Releases'), ('modern_metal', 'Modern- und Industrial-Metal-Releases')],
    med='Median {m} LUFS ({n} Releases)', eigen='eigene Messung',
    zeilen_vor=[('Wiedergabe-Referenz bei Spotify', '−14 LUFS (Laut −11, Leise −19)', 'Spotify for Artists'),
                ('Messnorm für LUFS und True Peak', 'ITU-R BS.1770-5 (November 2023)', 'ITU'),
                ('Zielwert im Rundfunk, zum Vergleich', '−23 LUFS', 'EBU R 128')],
    runter='So weit dreht Spotify einen mittleren Black-Metal-Master herunter', runter_wert='etwa {d} dB', runter_q='berechnet: {m} LUFS auf −14 LUFS',
    peak=('True-Peak-Obergrenze', '−1 dBTP, bei Mastern lauter als −14 LUFS −2 dBTP', 'Spotify for Artists'),
    zitat_label='Spotify im Wortlaut (englisches Original)', zitat_quelle='Spotify for Artists, Loudness normalization',
    studie='Sinngemäß: Spotify gleicht Tracks nach der Norm ITU 1770 auf −14 LUFS an. Dichte Master sind keine Eigenheit von Metal. Eine akustische Analyse von Musikaufnahmen ergab, dass Ausschnitte aus populären Genres wie Rock oder Rap in der Regel einen kleineren Dynamikumfang haben als Ausschnitte aus klassischen Genres (<a href="https://doi.org/10.1177/2331216516630549" rel="noopener" target="_blank">Kirchberger &amp; Russo 2016</a>, Trends in Hearing).',
    q_id='lgd-sources', q_titel='Quellen', q_intro='Plattformwerte, Normen und Messwerte auf dieser Seite stützen sich auf:',
    q_eigen='Polished: <a href="/de/metal-lautheit-daten/">Lautheitsdaten für Metal</a>, eigene Messung von 16 Releases je Genre nach ITU-R BS.1770.'),
}


def lg_zahlen(lang, alt=False):
    """Key-figures section directly under the hero: table with sources, verbatim Spotify quotation, one study."""
    t = LG_T[lang]
    de = lang == 'de'
    rows = list(t['zeilen_vor'])
    for key, label in t['genres']:
        g = gi_genre('polished', key)
        rows.append((label, t['med'].format(m=gi_wert(g['lufs_int']['med'], de), n=g['n_lufs']), t['eigen']))
    med = gi_genre('polished', 'black')['lufs_int']['med']
    diff = f'{round(med - LG_SPOTIFY_REF):d}'
    rows.append((t['runter'], t['runter_wert'].format(d=diff), t['runter_q'].format(m=gi_wert(med, de))))
    rows.append(t['peak'])
    body = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in rows)
    k = t['kopf']
    inner = f"""    <p>{t['intro']}</p>
    <div class="table-wrap">
      <table>
        <thead><tr><th>{k[0]}</th><th>{k[1]}</th><th>{k[2]}</th></tr></thead>
        <tbody>{body}</tbody>
      </table>
    </div>
    <blockquote class="answer-box" cite="{LG_SPOTIFY['url']}" style="margin-left:0;margin-right:0"><div class="label">{t['zitat_label']}</div><p lang="en">“{LG_ZITAT}”</p><p class="table-note" style="margin:10px 0 0">{t['zitat_quelle']}: <a href="{LG_SPOTIFY['url']}" rel="noopener" target="_blank">support.spotify.com</a></p></blockquote>
    <p>{t['studie']}</p>"""
    return sec(t['id'], t['titel'], inner, alt=alt)


def lg_quellen(lang, alt=False):
    t = LG_T[lang]
    abruf = {'en': 'retrieved 24 November 2026', 'de': 'abgerufen am 24.11.2026'}[lang]
    lis = ''.join(f'<li>{q["autor"]} ({q["jahr"] if q["jahr"].isdigit() else abruf}): <a href="{q["url"]}" rel="noopener" target="_blank">{q["name"]}</a>{". " + q["quelle"] if q.get("quelle") else ""}.</li>' for q in LG_QUELLEN)
    inner = f"""    <p>{t['q_intro']}</p>
    <ol>{lis}<li>{t['q_eigen']}</li></ol>"""
    return sec(t['q_id'], t['q_titel'], inner, alt=alt)


def lg_citation():
    """schema.org citation for the Article object."""
    out = []
    for q in LG_QUELLEN:
        person = q is LG_KR
        autor = [{"@type": "Person", "name": n} for n in q["autor"].split(" and ")] if person else {"@type": "Organization", "name": q["autor"]}
        eintrag = {"@type": "ScholarlyArticle" if person else "CreativeWork", "name": q["name"], "author": autor, "url": q["url"]}
        if q["jahr"].isdigit():
            eintrag["datePublished"] = q["jahr"]
        out.append(eintrag)
    return out
