#!/usr/bin/env python3
"""Generates all polished.media subpages (genre pages, guides, cost pages, /de/, 404).

Run from anywhere:  python3 _tools/gen.py
- gen.py      shared layout, nav/footer, EN genre pages, loudness guide, /de/ home, 404
- gen_de.py   German genre pages + German loudness guide
- gen_cost.py mastering cost pages (DE + EN)
index.html (the homepage) is NOT generated; edit it directly.
_tools/ is not published by GitHub Pages (Jekyll skips folders starting with "_").
"""
import json, os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://polished.media'
TODAY = '2026-10-05'
FONTS = 'https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;1,9..144,300;1,9..144,400&family=JetBrains+Mono:wght@400;500;700&family=Manrope:wght@400;600;700&display=swap'

BIZ = {"@id": f"{BASE}/#business"}
PERSON = {"@id": f"{BASE}/#tim-borchert"}

GENRES = [
    ('black-metal-mastering', 'Black Metal Mastering'),
    ('death-metal-mastering', 'Death Metal Mastering'),
    ('doom-gothic-mastering', 'Doom & Gothic Mastering'),
    ('metalcore-djent-mastering', 'Metalcore & Djent Mastering'),
]


def ld(obj):
    return '<script type="application/ld+json">\n' + json.dumps(obj, ensure_ascii=False, indent=2) + '\n</script>'


def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in faqs]}


def strip_tags(s):
    import re
    return re.sub(r'<[^>]+>', '', s)


def faq_html(faqs):
    return '\n'.join(
        f'        <details class="faq-item">\n          <summary>{html.escape(q, quote=False)}</summary>\n          <div class="faq-answer">{a}</div>\n        </details>'
        for q, a in faqs)


def breadcrumb_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u}
                                for i, (n, u) in enumerate(items)]}


def breadcrumb_html(items, label='Breadcrumb'):
    lis = []
    for i, (n, u) in enumerate(items):
        if i == len(items) - 1:
            lis.append(f'<li aria-current="page">{html.escape(n, quote=False)}</li>')
        else:
            lis.append(f'<li><a href="{u.replace(BASE, "") or "/"}">{html.escape(n, quote=False)}</a></li>')
    return f'<nav class="breadcrumb wrap" aria-label="{label}"><ol>{"".join(lis)}</ol></nav>'


LANGS = [('en', 'EN', 'English', '/'), ('de', 'DE', 'Deutsch', '/de/')]


def lang_switch(lang, counterpart=None):
    """EN | DE switcher. Links to the translated version of the page, else to the other language's home page."""
    counterpart = counterpart or {}
    items = []
    for code, short, full, home in LANGS:
        href = counterpart.get(code, home)
        if code == lang:
            items.append(f'<span aria-current="true" lang="{code}" title="{full}">{short}</span>')
        else:
            items.append(f'<a href="{href}" hreflang="{code}" lang="{code}" title="{full}" data-track="lang-{code}">{short}</a>')
    label = 'Sprache' if lang == 'de' else 'Language'
    return f'<div class="lang-switch" role="group" aria-label="{label}">{"".join(items)}</div>'


def nav(lang='en', current='', counterpart=None):
    if lang == 'de':
        links = [('/de/#audit', 'Audit'), ('/de/#genres', 'Genres'), ('/de/#preise', 'Preise'),
                 ('/de/mastering-kosten/', 'Kosten-Vergleich'), ('/de/metal-mastering-lautstaerke/', 'Lautstärke-Guide')]
        cta = ('/de/#kontakt', 'Audit anfragen →', 'Anfragen →')
        toggle = 'Menü öffnen'
    else:
        links = [('/#audit', 'Audit'), ('/#genres', 'Genres'), ('/#packages', 'Packages'),
                 ('/mastering-cost/', 'Cost Guide'), ('/metal-mastering-loudness/', 'Loudness Guide')]
        cta = ('/#contact', 'Request Audit →', 'Audit →')
        toggle = 'Toggle menu'
    lis = []
    for href, label in links:
        extra = ' aria-current="page"' if href == current else ''
        if href == '/de/':
            extra += ' hreflang="de" lang="de"'
        if href == '/' and lang == 'de':
            extra += ' hreflang="en" lang="en"'
        lis.append(f'<li><a href="{href}"{extra}>{label}</a></li>')
    return f'''<a href="#main" class="skip-link">{"Zum Inhalt springen" if lang == "de" else "Skip to content"}</a>
<nav class="site-nav" aria-label="{"Hauptnavigation" if lang == "de" else "Main navigation"}">
  <div class="nav-inner">
    <a href="{"/de/" if lang == "de" else "/"}" class="logo">Polished<span class="dot">.</span></a>
    <ul class="nav-links" id="navLinks">
      {"".join(lis)}
    </ul>
    <div class="nav-actions">
      {lang_switch(lang, counterpart)}
      <button class="menu-toggle" id="menuToggle" aria-label="{toggle}" aria-controls="navLinks" aria-expanded="false"><span></span><span></span><span></span></button>
      <a href="{cta[0]}" class="cta-btn nav-cta" data-track="nav-cta"><span class="cta-full">{cta[1]}</span><span class="cta-short">{cta[2]}</span></a>
    </div>
  </div>
</nav>'''


def footer(lang='en'):
    if lang == 'de':
        return f'''<footer>
  <div class="wrap">
    <div class="footer-inner">
      <div class="footer-brand">
        <a href="/de/" class="logo">Polished<span class="dot">.</span></a>
        <p>Online-Mastering-Studio für Metal &amp; Gothic aus Niedersachsen. Schriftliches Audio-Audit vor jedem Master.</p>
      </div>
      <div class="footer-col">
        <p class="footer-title">Genres</p>
        <ul>
          {''.join(f'<li><a href="/de/{s}/">{n}</a></li>' for s, n in GENRES)}<li><a href="https://codechaos-official.de/mastering/">Psytrance, Psycore &amp; Hitech Mastering</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <p class="footer-title">Studio</p>
        <ul>
          <li><a href="/de/#audit">Audio-Audit</a></li>
          <li><a href="/de/#preise">Preise</a></li>
          <li><a href="/de/mastering-kosten/">Mastering-Kosten</a></li>
          <li><a href="/de/stem-mastering/">Stem-Mastering</a></li>
          <li><a href="/de/metal-mastering-lautstaerke/">Lautstärke-Guide</a></li>
          <li><a href="/de/#kontakt">Kontakt</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <p class="footer-title">Kontakt</p>
        <ul>
          <li><a href="mailto:polished.media@gmx.de">polished.media@gmx.de</a></li>
          <li><a href="https://instagram.com/polishedmetalmastering" rel="noopener" target="_blank">Instagram</a></li>
          <li><a href="https://www.tiktok.com/@polished.media" rel="noopener" target="_blank">TikTok</a></li>
          <li><a href="/" hreflang="en" lang="en">English</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div>© 2026 Polished Mastering · Heart Warrior – Business meets Spiritualität UG (haftungsbeschränkt)</div>
      <div><a href="/#legal-notice">Impressum</a> · <a href="/#privacy">Datenschutz</a> · <a href="/#terms">AGB</a> · <a href="#" class="cookie-settings-link">Cookie-Einstellungen</a></div>
    </div>
  </div>
</footer>'''
    return f'''<footer>
  <div class="wrap">
    <div class="footer-inner">
      <div class="footer-brand">
        <a href="/" class="logo">Polished<span class="dot">.</span></a>
        <p>Metal &amp; Gothic audio mastering studio, grounded in music science. Full audio audit before every master.</p>
      </div>
      <div class="footer-col">
        <p class="footer-title">Genres</p>
        <ul>
          {''.join(f'<li><a href="/{s}/">{n}</a></li>' for s, n in GENRES)}<li><a href="https://codechaos-official.de/en/mastering/" hreflang="en">Psytrance, Psycore &amp; Hitech Mastering</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <p class="footer-title">Studio</p>
        <ul>
          <li><a href="/#audit">Audit Process</a></li>
          <li><a href="/#packages">Packages &amp; Pricing</a></li>
          <li><a href="/mastering-cost/">Mastering Cost Guide</a></li>
          <li><a href="/stem-mastering/">Stem Mastering Guide</a></li>
          <li><a href="/metal-mastering-loudness/">Loudness Guide</a></li>
          <li><a href="/#engineer">About Tim</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <p class="footer-title">Contact</p>
        <ul>
          <li><a href="mailto:polished.media@gmx.de">polished.media@gmx.de</a></li>
          <li><a href="https://instagram.com/polishedmetalmastering" rel="noopener" target="_blank">Instagram</a></li>
          <li><a href="https://www.tiktok.com/@polished.media" rel="noopener" target="_blank">TikTok</a></li>
          <li><a href="/de/" hreflang="de" lang="de">Deutsch</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div>© 2026 Polished Mastering · Heart Warrior – Business meets Spiritualität UG (haftungsbeschränkt)</div>
      <div><a href="/#legal-notice">Legal Notice</a> · <a href="/#privacy">Privacy Policy</a> · <a href="/#terms">Terms</a> · <a href="#" class="cookie-settings-link">Cookie settings</a></div>
    </div>
  </div>
</footer>'''


def page(*, path, lang, title, description, og_title, body, schemas, alternates=None, counterpart=None, robots='index, follow, max-snippet:-1, max-image-preview:large', canonical=True):
    url = f'{BASE}{path}'
    if counterpart and not alternates:
        alternates = [(l, f'{BASE}{p}') for l, p in counterpart.items()] + [('x-default', f'{BASE}{counterpart["en"]}')]
    alt = ''
    if alternates:
        alt = '\n'.join(f'<link rel="alternate" hreflang="{hl}" href="{u}">' for hl, u in alternates) + '\n'
    canon = f'<link rel="canonical" href="{url}">\n' if canonical else ''
    og_locale = 'de_DE' if lang == 'de' else 'en_US'
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#0a0a0a">
<meta name="color-scheme" content="dark">
<title>{html.escape(title, quote=False)}</title>
<meta name="description" content="{html.escape(description)}">
<meta name="author" content="Tim Borchert · Polished Mastering">
<meta name="robots" content="{robots}">
{canon}{alt}<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta property="og:type" content="{"article" if ("loudness" in path or "lautstaerke" in path) else "website"}">
<meta property="og:site_name" content="Polished Mastering">
<meta property="og:locale" content="{og_locale}">
<meta property="og:title" content="{html.escape(og_title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/assets/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Polished — Metal &amp; Gothic Mastering, with mastering engineer Tim Borchert">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(og_title)}">
<meta name="twitter:description" content="{html.escape(description)}">
<meta name="twitter:image" content="{BASE}/assets/og-image.jpg">
<link rel="preload" href="/assets/fonts/manrope-normal-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/fraunces-normal-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css">
{chr(10).join(ld(s) for s in schemas)}
</head>
<body>
{nav(lang, path, counterpart)}
<main id="main">
{body}
</main>
{footer(lang)}
<script src="/assets/site.js" defer></script>
</body>
</html>
'''


def write(path, content):
    out = os.path.join(ROOT, path.strip('/'), 'index.html') if path.endswith('/') else os.path.join(ROOT, path.strip('/'))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(content)
    print('wrote', out)


PRICES_EN = '''      <div class="price-grid">
        <div class="price"><div class="name">Single · Stereo</div><div class="amount"><span>€</span>79</div><p>One track, full audio audit, streaming + Bandcamp exports, 48–72h.</p></div>
        <div class="price"><div class="name">Single · Stems</div><div class="amount"><span>€</span>129</div><p>Up to 6 stems for maximum control per element, 48–72h.</p></div>
        <div class="price"><div class="name">EP · up to 5</div><div class="amount"><span>€</span>349</div><p>Save €46 vs. 5 singles. Audit per track, consistent loudness across the release, 5–7 days.</p></div>
        <div class="price"><div class="name">Album · up to 10</div><div class="amount"><span>€</span>629</div><p>Save €161 vs. 10 singles. Per-track + album audit, tonal consistency, vinyl master on request, 7–14 days.</p></div>
      </div>
      <p class="meta-line">All prices are final prices incl. 19% VAT. <strong>No upfront payment required: pay on invoice after delivery, or up front if you prefer.</strong> Every package includes the written audio audit and unlimited revisions. <a href="/#packages">Full package details</a> · <a href="/mastering-cost/">Price comparison</a> · <a href="/stem-mastering/">Stereo or stems?</a></p>'''


def service_schema(name, path, desc, audience, lang='en'):
    return {"@context": "https://schema.org", "@type": "Service",
            "@id": f"{BASE}{path}#service", "inLanguage": lang,
            "name": name, "serviceType": name, "url": f"{BASE}{path}",
            "description": desc, "provider": BIZ, "areaServed": "Worldwide",
            "audience": {"@type": "Audience", "audienceType": audience},
            "offers": {"@type": "AggregateOffer", "priceCurrency": "EUR", "lowPrice": "79", "highPrice": "629",
                       "offerCount": "4", "url": f"{BASE}/de/#preise" if lang == 'de' else f"{BASE}/#packages",
                       "priceSpecification": {"@type": "PriceSpecification", "priceCurrency": "EUR", "valueAddedTaxIncluded": True}}}


def webpage_schema(path, name, lang='en', page_type='WebPage'):
    return {"@context": "https://schema.org", "@type": page_type, "@id": f"{BASE}{path}#webpage",
            "url": f"{BASE}{path}", "name": name, "inLanguage": lang,
            "isPartOf": {"@id": f"{BASE}/#website"}, "about": BIZ,
            "primaryImageOfPage": f"{BASE}/assets/og-image.jpg", "dateModified": TODAY}


UI = {
    'en': dict(home='Home', prefix='', cta='Request Audio Audit →', contact='/#contact', pricing='Pricing',
               meta='Mastered by <a href="/#engineer">Tim Borchert</a>, Systematic Musicology degree, University of Hamburg · Updated October 2026',
               pricing_h='{name} <em>pricing</em>', faq_h='{name} <em>FAQ</em>', related_h='Other <em>genres</em>',
               cta_p='Send your premaster and a reference track. You get a written audio audit and a mastering plan before anything is processed.',
               email='Email Tim', note='Replies within 24h · Pay after delivery · Limited slots per week'),
    'de': dict(home='Startseite', prefix='/de', cta='Audio-Audit anfragen →', contact='/de/#kontakt', pricing='Preise',
               meta='Gemastert von <a href="/de/#tim">Tim Borchert</a>, Abschluss in Systematischer Musikwissenschaft, Universität Hamburg · Aktualisiert Oktober 2026',
               pricing_h='{name}: <em>Preise</em>', faq_h='{name}: <em>FAQ</em>', related_h='Weitere <em>Genres</em>',
               cta_p='Schick deinen Premaster und einen Referenztrack. Du bekommst ein schriftliches Audio-Audit und einen Mastering-Plan, bevor irgendetwas bearbeitet wird.',
               email='E-Mail an Tim', note='Antwort meist innerhalb von 24 Std. · Zahlung auch nach Lieferung · Begrenzte Slots pro Woche'),
}


def related(current, lang='en'):
    prefix = UI[lang]['prefix']
    items = [(s, n) for s, n in GENRES if s != current][:3]
    return '\n'.join(f'        <a href="{prefix}/{s}/"><span>Genre</span>{n}</a>' for s, n in items)


def genre_page(g, lang='en'):
    u = UI[lang]
    slug = g['slug']
    path = f"{u['prefix']}/{slug}/"
    home = '/de/' if lang == 'de' else '/'
    crumbs = [(u['home'], f'{BASE}{home}'), (g['name'], f'{BASE}{path}')]
    sections = '\n'.join(g['sections'])
    body = f'''{breadcrumb_html(crumbs, 'Brotkrumen' if lang == 'de' else 'Breadcrumb')}
<header class="page-hero">
  <div class="wrap">
    <div class="eyebrow">{g["eyebrow"]}</div>
    <h1>{g["h1"]}</h1>
    <p class="lead">{g["lead"]}</p>
    <div class="cta-row">
      <a href="{u['contact']}" class="cta-btn" data-track="{lang}-{slug}-hero">{u['cta']}</a>
      <a href="#pricing" class="cta-btn outline">{u['pricing']}</a>
    </div>
    <p class="meta-line">{u['meta']}</p>
  </div>
</header>
{sections}
<section class="content-section alt" id="pricing" aria-labelledby="pricing-h">
  <div class="wrap">
    <h2 id="pricing-h">{u['pricing_h'].format(name=g["name"])}</h2>
{PRICES_DE if lang == 'de' else PRICES_EN}
  </div>
</section>
<section class="content-section" aria-labelledby="faq-h">
  <div class="wrap prose-wrap">
    <h2 id="faq-h">{u['faq_h'].format(name=g["name"])}</h2>
{faq_html(g["faqs"])}
  </div>
</section>
<section class="content-section alt" aria-labelledby="related-h">
  <div class="wrap">
    <h2 id="related-h">{u['related_h']}</h2>
    <div class="related">
{related(slug, lang)}
    </div>
  </div>
</section>
<section class="cta-band" aria-labelledby="cta-h">
  <div class="wrap">
    <h2 id="cta-h">{g["cta_h"]}</h2>
    <p>{u['cta_p']}</p>
    <div class="cta-row">
      <a href="{u['contact']}" class="cta-btn" data-track="{lang}-{slug}-final">{u['cta']}</a>
      <a href="mailto:polished.media@gmx.de" class="cta-btn outline" data-track="{lang}-{slug}-email">{u['email']}</a>
    </div>
    <div class="note">{u['note']}</div>
  </div>
</section>'''
    schemas = [webpage_schema(path, g['title'], lang=lang),
               breadcrumb_schema(crumbs),
               service_schema(g['name'], path, g['description'], g['audience'], lang),
               faq_schema(g['faqs'])]
    return page(path=path, lang=lang, title=g['title'], description=g['description'],
                og_title=g['og_title'], body=body, schemas=schemas,
                counterpart={'en': f'/{slug}/', 'de': f'/de/{slug}/'})


def sec(id_, title, inner, alt=False):
    return f'''<section class="content-section{" alt" if alt else ""}" aria-labelledby="{id_}">
  <div class="wrap prose-wrap prose">
    <h2 id="{id_}">{title}</h2>
{inner}
  </div>
</section>'''


def cards(items):
    return '    <div class="card-grid">\n' + '\n'.join(
        f'      <div class="card"><div class="num">/ {i+1:02d}</div><h3>{h}</h3><p>{p}</p></div>'
        for i, (h, p) in enumerate(items)) + '\n    </div>'


AUDIT_STEPS = '''    <ol>
      <li><strong>Premaster in:</strong> 24/32-bit WAV or AIFF at session sample rate, 3–6 dB headroom, no master-bus limiter, plus one or two reference tracks.</li>
      <li><strong>Written audio audit:</strong> frequency spectrum, dynamics and loudness, stereo image and phase, and a sonic assessment against your subgenre and references.</li>
      <li><strong>Mastering plan:</strong> every move is listed with the reason behind it before anything is processed.</li>
      <li><strong>Master + exports:</strong> 24-bit WAV, 16-bit AIFF, 320 kbps MP3, platform-specific versions for streaming and Bandcamp.</li>
      <li><strong>Revisions:</strong> unlimited, until it matches what you hear in your head.</li>
    </ol>'''

# ---------------------------------------------------------------- GENRE CONTENT
BLACK = dict(
    slug='black-metal-mastering', name='Black Metal Mastering', eyebrow='Genre · Black Metal',
    title='Black Metal Mastering Online – Audit-First | Polished',
    og_title='Black Metal Mastering — Polished',
    description='Black metal mastering that keeps the cold, raw atmosphere and controls the low end. Written audio audit before every master. From €79, unlimited revisions.',
    audience='Black Metal bands, one-person projects, producers and labels',
    h1='Black Metal Mastering <em>that keeps the frost.</em>',
    lead='<strong>Black metal mastering is the final stage that makes tremolo walls, blast beats and harsh vocals translate to every system without sanding off the raw, cold character of the genre.</strong> At Polished every black metal master starts with a written audio audit of your mix, so loudness, brightness and low end are decided by measurement, not by a generic preset. From €79 per track, mastered personally by Tim Borchert.',
    cta_h='Send your <em>black metal</em> mix.',
    sections=[
        sec('bm-needs', 'What black metal needs <em>from a master</em>', '''    <p>Black metal breaks most of the rules generic mastering templates are built on. Brightness, noise and density are part of the aesthetic, so "fixing" them the way a pop chain would can strip out exactly what makes the record work. The job is to keep the character and remove only what blocks translation.</p>
''' + cards([
            ('Raw &amp; lo-fi', 'Hiss, grit and boxiness are often intentional. The master protects that texture and only tames what becomes painful on earbuds or collapses on phone speakers.'),
            ('Atmospheric &amp; post-black', 'Long reverbs and layered guitars need width that survives mono playback. Dynamics are kept open so crescendos still land.'),
            ('Melodic &amp; symphonic', 'Keys, choirs and lead guitars compete in the same upper mids. The audit shows where they mask each other so the master can open space for the melody.'),
            ('DSBM &amp; depressive', 'Vocals are often buried on purpose. The master keeps that distance while making sure the track doesn\'t sound simply quiet next to other releases.'),
        ])),
        sec('bm-problems', 'What the audit typically finds <em>in black metal mixes</em>', '''    <ul>
      <li><strong>Harsh 2–5 kHz buildup</strong> from stacked tremolo guitars and cymbals, which turns fatiguing once the track is pushed louder.</li>
      <li><strong>Cymbal wash during blast beats</strong> that swallows the snare and turns fast sections into noise instead of intensity.</li>
      <li><strong>Kick drums that disappear</strong> under the guitar wall, or triggered kicks that click too hard after limiting.</li>
      <li><strong>Sub-bass rumble and phase issues</strong> from tuned-down guitars and wide reverbs, which eat headroom and collapse in mono.</li>
      <li><strong>Over-limited premasters</strong> that leave no room to make the track competitive without distortion.</li>
    </ul>
    <p>Each finding goes into the written report with a concrete fix. When a problem can't be solved properly in mastering, the report says so, so you can decide whether to adjust the mix first.</p>''', alt=True),
        sec('bm-process', 'How a black metal master <em>comes together</em>', AUDIT_STEPS + '''
    <p>For loudness, black metal doesn't have to be crushed to sound vicious. Streaming services turn loud masters down anyway, so the target is set by what your mix can take before cymbals and blasts fall apart. More on that in the <a href="/metal-mastering-loudness/">metal mastering loudness guide</a>.</p>'''),
    ],
    faqs=[
        ('Can you master raw or lo-fi black metal without making it sound clean?', 'Yes. Raw black metal is mastered to translate, not to be cleaned up. The audit separates intentional texture like hiss, grit and boxiness from actual problems like painful resonances, low-end rumble or phase cancellation, and only the problems are addressed. If you want the record to stay ugly, say so in your brief and include a reference.'),
        ('How loud should a black metal master be?', 'There is no fixed number. Streaming services normalize playback to around -14 LUFS (Apple Music around -16 LUFS), so extreme loudness mostly costs clarity in blast beats and cymbals. Many black metal releases sit roughly between -10 and -7 LUFS integrated, but the target for your track is set from the audit, based on how far the mix can be pushed before it collapses.'),
        ('Do you master one-person black metal projects?', 'Yes. Solo projects are a big part of the scene and are handled exactly like band releases: same audit, same price, same unlimited revisions. Programmed drums are fine. The audit checks whether triggered or sampled kicks will still read clearly after limiting.'),
        ('Can I send stems instead of a stereo mix?', 'Yes. Stem mastering (€129 per track, up to 6 stems) is useful in black metal when guitars and cymbals fight in the same range or the kick disappears under the wall. Typical stems are drums, bass, guitars, vocals, keys/synths and FX. The audit tells you whether stems are worth it for your mix.'),
    ],
)

DEATH = dict(
    slug='death-metal-mastering', name='Death Metal Mastering', eyebrow='Genre · Death Metal',
    title='Death Metal Mastering Online – Audit-First | Polished',
    og_title='Death Metal Mastering — Polished',
    description='Death metal mastering with real low-end weight and blast beats that stay readable. Written audio audit before every master. From €79, unlimited revisions.',
    audience='Death Metal, Technical Death Metal, Brutal Death Metal and Deathcore bands, producers and labels',
    h1='Death Metal Mastering <em>with weight and clarity.</em>',
    lead='<strong>Death metal mastering is the stage that gives palm-mutes real weight, keeps blast beats and fast double-kick readable, and makes growls cut through the guitar wall on every playback system.</strong> At Polished every death metal master starts with a written audio audit of your mix, so the low end and loudness are decided by measurement, not by guesswork. From €79 per track, mastered personally by Tim Borchert.',
    cta_h='Send your <em>death metal</em> mix.',
    sections=[
        sec('dm-needs', 'What death metal needs <em>from a master</em>', '''    <p>Death metal is dense by design: down-tuned guitars, fast double-kick, low growls and often bass playing in the same register as the guitars. Loudness is expected, but every dB of limiting costs transient definition. A good death metal master finds the point where the record hits hard without the drums turning into mush.</p>
''' + cards([
            ('Old-school death metal', 'Organic, saturated, sometimes murky by intent. The master adds punch and translation while keeping the cavernous character.'),
            ('Technical &amp; progressive', 'Every note matters. The master protects articulation in fast runs and keeps bass lines audible under the guitars.'),
            ('Brutal &amp; slam', 'Maximum weight in the low mids. The audit watches the 100–300 Hz region closely so slams hit instead of booming.'),
            ('Melodic death metal', 'Leads and harmonies need presence without harshness. The master balances aggression with melodic clarity.'),
        ])),
        sec('dm-problems', 'What the audit typically finds <em>in death metal mixes</em>', '''    <ul>
      <li><strong>Low-mid buildup (150–400 Hz)</strong> from guitars, bass and toms stacking up, which makes the mix sound big but undefined.</li>
      <li><strong>Double-kick that blurs</strong> at high tempos, either too clicky after limiting or lost under the bass.</li>
      <li><strong>Growls fighting the guitars</strong> in the same frequency range, so lyrics and rhythm get lost.</li>
      <li><strong>Snare losing crack</strong> when the master is pushed, because the limiter catches every hit first.</li>
      <li><strong>Pre-limited mixes</strong> where the mix bus is already clipped hard, leaving little room for a clean, loud master.</li>
    </ul>
    <p>Each issue is documented with the measured value and the planned fix. If the cleanest solution is a change in the mix, the report says so instead of hiding it behind more processing.</p>''', alt=True),
        sec('dm-process', 'How a death metal master <em>comes together</em>', AUDIT_STEPS + '''
    <p>Death metal is usually mastered louder than streaming normalization targets, which is fine as long as the transients survive. True peak is kept low enough to avoid distortion after lossy encoding. Details in the <a href="/metal-mastering-loudness/">metal mastering loudness guide</a>.</p>'''),
    ],
    faqs=[
        ('How do you keep blast beats from turning into mush?', 'By measuring before limiting. The audit looks at crest factor, transient behavior of kick and snare, and how much the cymbals and guitars mask the drums. The loudness target is then set so the limiter doesn\'t flatten every snare hit. If the drums are already buried in the mix, stem mastering or a small mix change is recommended instead of just pushing harder.'),
        ('How loud should a death metal master be?', 'Death metal is commonly mastered louder than streaming targets, often somewhere around -9 to -6 LUFS integrated, but there\'s no rule. Spotify, YouTube and Tidal play back at about -14 LUFS, so a louder master is turned down. The goal is the loudest version that still keeps snare crack and double-kick definition, with true peak at or below -1 dBTP.'),
        ('Do you master deathcore and technical death metal too?', 'Yes. Deathcore, technical, progressive, brutal, slam and melodic death metal are all covered. Each has different priorities, from articulation in tech death to low-mid weight in slam, and the audit is set against references from your specific subgenre.'),
        ('Is stem mastering worth it for death metal?', 'Often, yes. When kick, bass and guitars compete in the low end, stem mastering (€129 per track, up to 6 stems) allows each group to be shaped separately before the final master. For a well-balanced mix, stereo mastering at €79 is enough. The audit tells you which one fits.'),
    ],
)

DOOM = dict(
    slug='doom-gothic-mastering', name='Doom & Gothic Mastering', eyebrow='Genre · Doom · Gothic',
    title='Doom & Gothic Metal Mastering Online | Polished',
    og_title='Doom & Gothic Mastering — Polished',
    description='Doom, sludge and gothic mastering that keeps dynamics and space while the low end stays heavy. Written audio audit before every master. From €79.',
    audience='Doom Metal, Funeral Doom, Sludge, Stoner, Gothic Metal, Gothic Rock and Darkwave bands, producers and labels',
    h1='Doom &amp; Gothic Mastering <em>with room to breathe.</em>',
    lead='<strong>Doom and gothic mastering is about keeping dynamic range and space intact so slow builds still hit, while the low end stays thick without swallowing vocals, keys and atmosphere.</strong> At Polished every doom and gothic master starts with a written audio audit of your mix, so loudness is chosen deliberately instead of maximized by default. From €79 per track, mastered personally by Tim Borchert.',
    cta_h='Send your <em>doom or gothic</em> mix.',
    sections=[
        sec('dg-needs', 'What doom and gothic need <em>from a master</em>', '''    <p>Slow music exposes everything. Sustained chords, long decays and quiet passages make over-compression audible in a way fast genres can hide. Doom and gothic records lose most of their impact when every section is pushed to the same loudness. The master has to preserve contrast, keep the low end heavy but controlled, and leave space for vocals, keys and reverb tails.</p>
''' + cards([
            ('Doom &amp; funeral doom', 'Huge, slow, sustained low end. The master keeps it massive without letting sub energy eat the headroom of the whole track.'),
            ('Sludge &amp; stoner', 'Fuzz and saturation are the sound. The audit separates musical distortion from harshness that becomes fatiguing at volume.'),
            ('Gothic metal', 'Clean and harsh vocals, keys, choirs and guitars all need their place. The master balances weight with clarity in the mids.'),
            ('Gothic rock &amp; darkwave', 'Bass-driven and atmospheric. The master keeps the bass line forward and the reverb space deep without getting muddy.'),
        ])),
        sec('dg-problems', 'What the audit typically finds <em>in doom and gothic mixes</em>', '''    <ul>
      <li><strong>Sub and low-mid buildup</strong> from sustained, down-tuned chords that masks vocals and keys.</li>
      <li><strong>Over-compression</strong> that flattens the quiet-to-heavy contrast these genres depend on.</li>
      <li><strong>Reverb tails that collapse in mono</strong> or turn the mix murky on small speakers.</li>
      <li><strong>Harsh fuzz in the upper mids</strong> that becomes painful when the record is turned up.</li>
      <li><strong>Inconsistent levels between songs</strong> on EPs and albums with very different dynamics from track to track.</li>
    </ul>
    <p>For full releases the audit also covers the record as a whole, so quiet interludes and heavy songs feel connected instead of mismatched.</p>''', alt=True),
        sec('dg-process', 'How a doom or gothic master <em>comes together</em>', AUDIT_STEPS + '''
    <p>Doom and gothic masters benefit most from loudness normalization on streaming platforms: a dynamic master isn't penalized, it just keeps its punch. Vinyl masters are available on request for album projects. More in the <a href="/metal-mastering-loudness/">metal mastering loudness guide</a>.</p>'''),
    ],
    faqs=[
        ('Will my doom record sound too quiet next to other releases?', 'Not on streaming platforms. Spotify, YouTube and Tidal normalize playback to around -14 LUFS and Apple Music to around -16 LUFS, so a more dynamic doom master plays back at a similar perceived level while keeping its contrast. On Bandcamp there\'s no normalization, so the loudness there is planned explicitly. The audit sets the target per track.'),
        ('Can you make the low end heavier without making it muddy?', 'Usually, yes. The audit identifies where the low-end energy actually sits, often sub energy below 60 Hz that eats headroom versus low mids around 150–300 Hz that create weight. The master shapes those regions separately. If kick and bass are fighting in the mix itself, stem mastering gives the most control.'),
        ('Do you master gothic rock and darkwave as well as gothic metal?', 'Yes. Gothic rock, darkwave, deathrock and gothic metal are all part of the focus. These styles are often bass-driven and atmospheric, so the master keeps the bass line forward and the reverb space deep without clouding the vocals.'),
        ('Can you prepare a vinyl master?', 'Yes. A vinyl-ready master is available on request for album projects. Vinyl benefits from preserved dynamics, a mono-compatible low end and controlled sibilance, which suits doom and gothic material well. Mention vinyl in your brief so it\'s planned from the audit onward.'),
    ],
)

CORE = dict(
    slug='metalcore-djent-mastering', name='Metalcore & Djent Mastering', eyebrow='Genre · Metalcore · Djent',
    title='Metalcore & Djent Mastering Online | Polished',
    og_title='Metalcore & Djent Mastering — Polished',
    description='Metalcore and djent mastering with tight, controlled low end, clear breakdowns and vocals that sit right. Written audio audit before every master. From €79.',
    audience='Metalcore, Post-Hardcore, Djent, Progressive Metal and Deathcore bands, producers and labels',
    h1='Metalcore &amp; Djent Mastering <em>tight to the grid.</em>',
    lead='<strong>Metalcore and djent mastering is about precise, controlled low end for syncopated extended-range riffs, breakdowns that hit hard, and clean and screamed vocals that both sit exactly where they should.</strong> At Polished every metalcore and djent master starts with a written audio audit of your mix, so loudness and low end are set by measurement. From €79 per track, mastered personally by Tim Borchert.',
    cta_h='Send your <em>metalcore or djent</em> mix.',
    sections=[
        sec('mc-needs', 'What metalcore and djent need <em>from a master</em>', '''    <p>Modern metalcore and djent are produced tight, loud and polished, often with programmed drums, extended-range guitars and synth layers. Listeners compare your release directly to big-budget productions. The master has to deliver that modern loudness and polish while keeping the low end controlled when 7- and 8-string guitars, bass and kick all live below 100 Hz.</p>
''' + cards([
            ('Metalcore &amp; post-hardcore', 'Big choruses, clean vocals and heavy breakdowns in one song. The master keeps both halves powerful without the chorus getting lost.'),
            ('Djent &amp; prog metal', 'Syncopated low-end riffs need definition. The master keeps every palm-muted chug distinct instead of one continuous rumble.'),
            ('Deathcore', 'Extreme low end and extreme vocals. The audit watches headroom carefully so drops hit without distortion.'),
            ('Electronic-hybrid', 'Synths, sub drops and samples on top of the band. The master balances sub energy so it doesn\'t steal headroom from the guitars.'),
        ])),
        sec('mc-problems', 'What the audit typically finds <em>in metalcore and djent mixes</em>', '''    <ul>
      <li><strong>Low-end collisions below 100 Hz</strong> between extended-range guitars, bass, kick and sub drops.</li>
      <li><strong>Breakdowns that get quieter</strong> after limiting because the low end eats all the headroom.</li>
      <li><strong>Clean vocals too far back</strong> in choruses, or screams too harsh in the 3–5 kHz range.</li>
      <li><strong>Sub drops and 808s</strong> that overload the limiter and cause pumping.</li>
      <li><strong>Phase issues</strong> from layered guitar DIs, re-amps and stereo widening that weaken the mix in mono.</li>
    </ul>
    <p>Each finding is documented with measured values and a planned fix, including an honest note if something should be changed in the mix first.</p>''', alt=True),
        sec('mc-process', 'How a metalcore or djent master <em>comes together</em>', AUDIT_STEPS + '''
    <p>Metalcore is one of the loudest-mastered metal styles. That's achievable, but the cleanest results come from a mix with headroom and no master-bus limiter. See the <a href="/metal-mastering-loudness/">metal mastering loudness guide</a> for targets and true-peak limits.</p>'''),
    ],
    faqs=[
        ('Can you get my metalcore master as loud as major releases?', 'Usually close, if the mix allows it. Modern metalcore is often mastered somewhere around -8 to -6 LUFS integrated. Whether your mix can get there cleanly depends on how controlled the low end is and how much headroom the premaster has. The audit measures that first and tells you honestly what loudness is possible without distortion or pumping.'),
        ('How do you handle 7- and 8-string low end?', 'The audit looks at where guitar, bass and kick energy overlap below 100 Hz and checks phase between them. The master then controls that region so palm-muted riffs stay distinct. When the collision is deep in the mix, stem mastering (€129 per track, up to 6 stems) allows guitars and bass to be shaped separately.'),
        ('Do breakdowns and sub drops get special attention?', 'Yes. Breakdowns are often where masters fail: the low end eats the limiter\'s headroom and the heaviest moment ends up feeling smaller. The audit flags those sections, and the master is checked specifically on breakdowns and drops, not only on the loudest chorus.'),
        ('Do you work with programmed drums and amp sims?', 'Yes. Programmed drums, amp simulators and in-the-box productions are standard in metalcore and djent and are mastered exactly like tracked material. The audit checks sample-based kicks and snares for clicks or harshness after limiting.'),
    ],
)

for g in (BLACK, DEATH, DOOM, CORE):
    write(f'/{g["slug"]}/', genre_page(g))
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gen_de.py'), encoding='utf-8').read())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gen_cost.py'), encoding='utf-8').read())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gen_stem.py'), encoding='utf-8').read())

# ---------------------------------------------------------------- LOUDNESS GUIDE
LG_PATH = '/metal-mastering-loudness/'
LG_TITLE = 'How Loud Should Metal Be Mastered? LUFS Guide 2026 | Polished'
LG_FAQS = [
    ('What LUFS should metal be mastered to?', 'There is no single correct value. Streaming services normalize playback to about -14 LUFS integrated (Apple Music about -16 LUFS), so louder masters are turned down. Many commercial metal releases land roughly between -10 and -6 LUFS integrated because density and saturation are part of the sound. The right target is the loudest level your mix reaches before transients, cymbals and low end start to collapse.'),
    ('Does Spotify turn down loud metal masters?', 'Yes. With normalization on (the default), Spotify plays tracks at about -14 LUFS integrated. A master at -8 LUFS is turned down by about 6 dB. Spotify also offers a "Loud" setting at -11 LUFS and a "Quiet" setting at -19 LUFS.'),
    ('Does Spotify turn up quiet masters?', 'Only partly. Spotify raises quieter tracks only as far as their true peak allows, keeping about 1 dB of headroom. Its own example: a track at -20 LUFS with a true peak of -5 dBFS is only lifted to -16 LUFS. A very dynamic master with high peaks can therefore play back slightly quieter than louder masters.'),
    ('What true peak should a metal master have?', 'Spotify recommends keeping true peak below -1 dBTP, and below -2 dBTP if the master is louder than -14 LUFS integrated, because lossy encoding can push peaks higher and cause distortion. For loud metal masters, -1 dBTP is a common ceiling, with lower values used when the codec test shows clipping.'),
    ('Should I master differently for Bandcamp?', 'Bandcamp does not normalize loudness, so listeners hear your master exactly as delivered and level differences to other releases are audible. Many artists use the same master everywhere. If your streaming master is relatively dynamic, a slightly louder Bandcamp version can make sense.'),
]
lg_body = f'''{breadcrumb_html([('Home', f'{BASE}/'), ('Metal Mastering Loudness Guide', f'{BASE}{LG_PATH}')])}
<header class="page-hero">
  <div class="wrap">
    <div class="eyebrow">Guide · Loudness</div>
    <h1>How loud should metal <em>be mastered?</em></h1>
    <p class="lead"><strong>Short answer: there is no single correct LUFS value for metal.</strong> Streaming services play everything back at roughly -14 LUFS (Apple Music around -16 LUFS), so extra loudness is turned down. The right target is the loudest level your specific mix can reach before blast beats, cymbals and low end start to collapse.</p>
    <p class="meta-line">By <a href="/#engineer">Tim Borchert</a>, mastering engineer, Systematic Musicology (University of Hamburg) · Published October 5, 2026</p>
  </div>
</header>
{sec('lg-what', 'What LUFS means <em>and why it matters</em>', """    <div class="answer-box"><div class="label">Definition</div><p>LUFS (Loudness Units relative to Full Scale) measures perceived loudness over time, weighted the way human hearing works. Integrated LUFS is the average across a whole track. Streaming platforms use it to play every track at a similar level.</p></div>
    <p>Peak meters only show the highest sample. LUFS shows how loud a track actually feels. Two masters can both peak at -1 dBFS and still be 6 dB apart in perceived loudness. That difference is what the loudness war was about, and why normalization changed it.</p>
    <p>Three numbers matter when a metal master is judged for release:</p>
    <ul>
      <li><strong>Integrated LUFS</strong>: the average loudness across the track. This is what platforms normalize to.</li>
      <li><strong>True peak (dBTP)</strong>: the real peak level after digital-to-analog conversion and lossy encoding. It can be higher than the sample peak.</li>
      <li><strong>Crest factor / dynamic range</strong>: the difference between peaks and average level. In metal this decides whether the snare still cracks or just sits in the wall.</li>
    </ul>""")}
{sec('lg-platforms', 'Streaming loudness targets <em>by platform</em>', """    <div class="table-wrap">
      <table>
        <thead><tr><th>Platform</th><th>Playback reference</th><th>What happens to a loud metal master</th></tr></thead>
        <tbody>
          <tr><td>Spotify</td><td>-14 LUFS (Normal) · -11 LUFS (Loud) · -19 LUFS (Quiet)</td><td>Turned down to the selected level. Quiet tracks are only lifted as far as true peak allows.</td></tr>
          <tr><td>YouTube</td><td>about -14 LUFS</td><td>Turned down. Quieter tracks are not turned up.</td></tr>
          <tr><td>Apple Music</td><td>about -16 LUFS (Sound Check)</td><td>Turned down when Sound Check is enabled.</td></tr>
          <tr><td>Tidal</td><td>about -14 LUFS</td><td>Turned down.</td></tr>
          <tr><td>Amazon Music</td><td>about -14 LUFS</td><td>Turned down.</td></tr>
          <tr><td>Deezer</td><td>about -15 LUFS</td><td>Turned down.</td></tr>
          <tr><td>Bandcamp</td><td>no normalization</td><td>Played exactly as delivered.</td></tr>
        </tbody>
      </table>
    </div>
    <p class="table-note">Values reflect platform documentation and widely used measurements as of October 2026. Platforms can change their reference levels. Spotify values are taken from <a href="https://support.spotify.com/us/artists/article/loudness-normalization/" rel="noopener" target="_blank">Spotify's loudness normalization guidelines</a>.</p>
    <p>The practical consequence: on streaming platforms a -7 LUFS master and a -11 LUFS master end up at roughly the same playback level. The louder one doesn't win the volume contest anymore. It only gives up transient detail, unless that density is part of the sound you want.</p>""", alt=True)}
{sec('lg-metal', 'Typical loudness ranges <em>by metal subgenre</em>', """    <p>Commercial metal is usually mastered louder than streaming references, and that's legitimate: saturation and density are part of the genre's sound. These are rough orientation ranges, not targets:</p>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Subgenre</th><th>Common integrated range</th><th>What limits loudness first</th></tr></thead>
        <tbody>
          <tr><td>Metalcore / Djent</td><td>around -8 to -6 LUFS</td><td>Low end below 100 Hz eating headroom in breakdowns</td></tr>
          <tr><td>Death Metal</td><td>around -9 to -6 LUFS</td><td>Snare crack and double-kick definition</td></tr>
          <tr><td>Black Metal</td><td>around -10 to -7 LUFS</td><td>Cymbal wash and harshness in blast sections</td></tr>
          <tr><td>Doom / Sludge</td><td>around -11 to -8 LUFS</td><td>Sustained sub energy and loss of contrast</td></tr>
          <tr><td>Gothic Metal / Gothic Rock</td><td>around -12 to -8 LUFS</td><td>Dynamics between quiet and heavy sections</td></tr>
        </tbody>
      </table>
    </div>
    <p class="table-note">Orientation values from mastering practice. Individual releases vary widely, and the right value for your track depends on the mix.</p>
    <p>Genre-specific details: <a href="/black-metal-mastering/">black metal</a>, <a href="/death-metal-mastering/">death metal</a>, <a href="/doom-gothic-mastering/">doom &amp; gothic</a>, <a href="/metalcore-djent-mastering/">metalcore &amp; djent</a>.</p>""")}
{sec('lg-peak', 'True peak: <em>the number that causes distortion</em>', """    <p>When a WAV master is converted to Ogg Vorbis, AAC or MP3 for streaming, peaks can rise above the original level. A master limited to 0 dBFS can clip after encoding even though the WAV looks clean. Loud, dense metal masters are especially exposed.</p>
    <ul>
      <li>Spotify recommends a true peak <strong>below -1 dBTP</strong>.</li>
      <li>For masters louder than -14 LUFS integrated, Spotify recommends <strong>below -2 dBTP</strong>.</li>
      <li>Checking the master through an actual codec preview reveals encoding distortion before release.</li>
    </ul>""", alt=True)}
{sec('lg-how', 'How the right loudness <em>is chosen</em>', """    <p>At Polished, loudness isn't a fixed setting. It comes out of the audio audit that runs before every master:</p>
    <ol>
      <li>Measure the premaster: integrated LUFS, true peak, crest factor, short-term loudness of the heaviest sections.</li>
      <li>Compare against references from your subgenre that you choose or that fit your brief.</li>
      <li>Find the threshold where pushing further starts to cost snare crack, blast-beat definition or low-end control.</li>
      <li>Set the target below that threshold, check true peak and run a codec preview.</li>
      <li>Deliver the master with the measured values documented, so you know exactly what you're releasing.</li>
    </ol>
    <p>If you want your track measured, send it in. The audit is included in every package, from €79 per track.</p>
    <div class="cta-row" style="margin-top: 24px;"><a href="/#contact" class="cta-btn" data-track="guide-cta">Request Audio Audit →</a><a href="/#packages" class="cta-btn outline">Packages &amp; Pricing</a></div>""")}
<section class="content-section alt" aria-labelledby="lg-faq">
  <div class="wrap prose-wrap">
    <h2 id="lg-faq">Metal loudness <em>FAQ</em></h2>
{faq_html(LG_FAQS)}
  </div>
</section>'''
lg_schemas = [
    webpage_schema(LG_PATH, LG_TITLE),
    breadcrumb_schema([('Home', f'{BASE}/'), ('Metal Mastering Loudness Guide', f'{BASE}{LG_PATH}')]),
    {"@context": "https://schema.org", "@type": "Article", "@id": f"{BASE}{LG_PATH}#article",
     "headline": "How loud should metal be mastered? LUFS, true peak and streaming normalization",
     "description": "Loudness targets for metal masters: streaming normalization by platform, typical LUFS ranges by subgenre, and true-peak limits.",
     "image": f"{BASE}/assets/og-image.jpg", "inLanguage": "en",
     "datePublished": TODAY, "dateModified": TODAY,
     "author": {"@type": "Person", "@id": f"{BASE}/#tim-borchert", "name": "Tim Borchert", "url": f"{BASE}/#engineer"},
     "publisher": BIZ, "mainEntityOfPage": {"@id": f"{BASE}{LG_PATH}#webpage"},
     "about": ["Audio mastering", "Loudness normalization", "LUFS", "Metal music"]},
    faq_schema(LG_FAQS),
]
write(LG_PATH, page(path=LG_PATH, lang='en', title=LG_TITLE,
      description='How loud should metal be mastered? Streaming LUFS targets by platform, typical loudness for metalcore, death, black and doom metal, and true-peak limits.',
      og_title='How loud should metal be mastered? — Polished', body=lg_body, schemas=lg_schemas,
      counterpart={'en': LG_PATH, 'de': '/de/metal-mastering-lautstaerke/'}))

# ---------------------------------------------------------------- GERMAN LANDING PAGE
DE_PATH = '/de/'
DE_TITLE = 'Metal Mastering Studio Deutschland – online ab 79 € | Polished'
DE_FAQS = [
    ('Was kostet Mastering bei Polished?', 'Alle Preise sind Endpreise inklusive 19 % Umsatzsteuer. Stereo-Mastering kostet ab 79 € pro Track, Stem-Mastering ab 129 € pro Track. Das EP-Paket (bis 5 Tracks) kostet 349 €, das Album-Paket (bis 10 Tracks) 629 €, also 161 € weniger als 10 einzelne Singles. In jedem Paket sind das schriftliche Audio-Audit und unbegrenzte Revisionen enthalten. Es gibt kein Abo und keine versteckten Zusatzkosten. Bezahlt wird nach Wahl vorab oder auf Rechnung nach Lieferung. Einen Preisvergleich findest du unter <a href="/de/mastering-kosten/">Was kostet Mastering?</a>'),
    ('Gibt es Label-Raten oder Bundles?', 'Ja. Labels mit Release-Planung (ab 4 Releases pro Jahr) bekommen feste Partnerpreise: 63 € pro Stereo-Single, 103 € pro Stem-Single, 279 € pro EP und 499 € pro Album. Wer mehrere Singles veröffentlicht, bucht die Single-Serie: 3 Singles zu je 73 €, gemastert, wenn sie erscheinen, über bis zu 12 Monate. Die Stem-EP umfasst bis zu 5 Tracks aus Stems für 549 €. Bezahlt wird nach Wahl per Vorkasse oder auf Rechnung nach Fertigstellung. Alle Preise sind Endpreise inklusive 19 % Umsatzsteuer, Audit und unbegrenzte Revisionen sind immer enthalten.'),
    ('Was ist das Audio-Audit?', 'Das Audio-Audit ist eine vollständige technische und klangliche Analyse deines Mixes, bevor eine einzige Mastering-Entscheidung fällt: Frequenzspektrum, Dynamik und Lautheit, Stereobild und Phase sowie eine Einordnung im Genre-Kontext. Du bekommst einen schriftlichen Bericht mit konkreten Schwachstellen und einer Mastering-Strategie, die erklärt, welche Schritte gemacht werden und warum.'),
    ('Wie lange dauert das Mastering?', 'Eine Single ist in der Regel nach 48–72 Stunden fertig, inklusive Audit. Eine EP dauert etwa 5–7 Tage, ein Album etwa 7–14 Tage. Express-Lieferung in 24 Stunden ist auf Anfrage möglich. Wenn ein Release-Termin feststeht, sag es direkt dazu.'),
    ('Wie laut sollte ein Metal-Master sein?', 'Es gibt keinen festen Wert. Spotify, YouTube und Tidal spielen Musik mit etwa -14 LUFS ab, Apple Music mit etwa -16 LUFS. Lautere Master werden also leiser gedreht. Viele Metal-Releases liegen trotzdem grob zwischen -10 und -6 LUFS integriert. Das Audit misst, wie laut dein Mix werden kann, bevor Blastbeats, Becken und Low End zusammenbrechen. Mehr dazu im <a href="/de/metal-mastering-lautstaerke/">Lautstärke-Guide</a>.'),
    ('Arbeitet Polished nur online?', 'Ja. Polished ist ein Online-Mastering-Studio mit Sitz in Kirchlinteln (Niedersachsen). Dateien werden über WeTransfer, Dropbox oder Google Drive ausgetauscht, Kommunikation läuft per E-Mail oder Instagram-DM. Bands aus Deutschland, Österreich und der Schweiz werden genauso betreut wie internationale Projekte, auf Deutsch oder Englisch.'),
    ('Ist das KI-Mastering wie bei LANDR?', 'Nein. Jeder Track wird von Tim Borchert persönlich analysiert und gemastert. Ein Algorithmus kann Lautheit und EQ-Kurven anwenden, aber kein schriftliches Audit erstellen, deine künstlerische Absicht verstehen oder eine Strategie speziell für Black Metal, Death Metal, Doom oder Gothic entwickeln.'),
]
de_body = f'''<header class="page-hero">
  <div class="wrap">
    <div class="eyebrow">Metal &amp; Gothic Mastering Studio</div>
    <h1>Metal Mastering, <em>analysiert statt geraten.</em></h1>
    <p class="lead"><strong>Polished ist ein Mastering-Studio aus Deutschland, spezialisiert auf Black Metal, Death Metal, Doom, Gothic sowie Metalcore und Djent, und arbeitet komplett online.</strong> Jedes Projekt beginnt mit einem schriftlichen Audio-Audit deines Mixes, bevor ein Plugin angefasst wird. Gemastert persönlich von Tim Borchert, Systematische Musikwissenschaft an der Universität Hamburg. Ab 79 € pro Track, unbegrenzte Revisionen.</p>
    <div class="cta-row">
      <a href="#kontakt" class="cta-btn" data-track="de-hero">Audio-Audit anfragen →</a>
      <a href="#preise" class="cta-btn outline">Preise ansehen</a>
    </div>
    <p class="meta-line">Zahlung auch nach Lieferung · Antwort meist innerhalb von 24 Stunden · Begrenzte Slots pro Woche</p>
  </div>
</header>
<section class="content-section" id="audit" aria-labelledby="de-audit">
  <div class="wrap prose-wrap prose">
    <h2 id="de-audit">Vollständiges <em>Audio-Audit</em> vor jedem Master</h2>
    <div class="answer-box"><div class="label">Definition</div><p>Ein Audio-Audit ist eine vollständige technische und klangliche Analyse eines Mixes, die vor jeder Mastering-Entscheidung durchgeführt wird. Du bekommst einen schriftlichen Bericht mit den gefundenen Schwachstellen und einer konkreten Mastering-Strategie.</p></div>
    <ul>
      <li><strong>Frequenzspektrum:</strong> Resonanzen, Maskierung und Abweichungen vom Genre, abgeglichen mit Black-, Death-, Doom- und Gothic-Referenzen.</li>
      <li><strong>Dynamik &amp; Lautheit:</strong> Crest-Faktor, LUFS, True Peak und Kompatibilität mit den Streaming-Plattformen.</li>
      <li><strong>Stereobild &amp; Phase:</strong> Korrelation, Mono-Kompatibilität und Phasenprobleme im Bassbereich.</li>
      <li><strong>Klangliche Einordnung:</strong> Vergleich mit Referenztracks aus deinem Subgenre und daraus eine konkrete Strategie.</li>
    </ul>
    <p>Das Audit ist in jedem Paket enthalten. Wenn sich zeigt, dass der Mix selbst noch Arbeit braucht, steht das ehrlich im Bericht, statt es im Mastering zu verstecken.</p>
  </div>
</section>
<section class="content-section alt" id="genres" aria-labelledby="de-genres">
  <div class="wrap">
    <h2 id="de-genres">Metal &amp; Gothic, <em>sonst nichts.</em></h2>
    <p class="lead" style="margin-bottom: 0;">Kein Pop, kein Hip-Hop, keine Einheitsvorlage. Jedes Subgenre braucht andere Prioritäten im Master. Mehr dazu auf den Genre-Seiten:</p>
    <div class="card-grid">
      <div class="card"><div class="num">/ 01</div><h3><a href="/de/black-metal-mastering/">Black Metal Mastering</a></h3><p>Tremolo-Wände ohne Schärfe, kalte Höhen und Atmosphäre bleiben erhalten, das Low End bleibt kontrolliert.</p></div>
      <div class="card"><div class="num">/ 02</div><h3><a href="/de/death-metal-mastering/">Death Metal Mastering</a></h3><p>Palm-Mutes mit echtem Gewicht, Blastbeats, die lesbar bleiben, Growls, die sich durchsetzen.</p></div>
      <div class="card"><div class="num">/ 03</div><h3><a href="/de/doom-gothic-mastering/">Doom &amp; Gothic Mastering</a></h3><p>Dynamik und Raum für langsame Aufbauten, ein schweres Low End, das den Mix nicht verschluckt.</p></div>
      <div class="card"><div class="num">/ 04</div><h3><a href="/de/metalcore-djent-mastering/">Metalcore &amp; Djent Mastering</a></h3><p>Präzises Low End für Extended-Range-Riffs, Breakdowns mit Druck, Vocals am richtigen Platz.</p></div>
    </div>
  </div>
</section>
<section class="content-section" id="preise" aria-labelledby="de-preise">
  <div class="wrap">
    <h2 id="de-preise">Transparente Preise, <em>kein Abo.</em></h2>
    <div class="price-grid">
      <div class="price"><div class="name">Single · Stereo</div><div class="amount">79<span style="margin-left:4px;">€</span></div><p>Ein Track, vollständiges Audio-Audit, Streaming- und Bandcamp-Exporte, 48–72 Std.</p></div>
      <div class="price"><div class="name">Single · Stems</div><div class="amount">129<span style="margin-left:4px;">€</span></div><p>Bis zu 6 Stems für maximale Kontrolle pro Element, 48–72 Std.</p></div>
      <div class="price"><div class="name">EP · bis 5 Tracks</div><div class="amount">349<span style="margin-left:4px;">€</span></div><p>46 € gespart gegenüber 5 Singles. Audit pro Track, einheitliche Lautheit über das Release, 5–7 Tage.</p></div>
      <div class="price"><div class="name">Album · bis 10 Tracks</div><div class="amount">629<span style="margin-left:4px;">€</span></div><p>161 € gespart gegenüber 10 Singles. Audit pro Track plus Album-Audit, klangliche Konsistenz, Vinyl-Master auf Anfrage, 7–14 Tage.</p></div>
    </div>
    <p class="meta-line">Alle Preise sind Endpreise inkl. 19 % USt. <strong>Keine Vorkasse nötig: Zahlung wahlweise auf Rechnung nach Lieferung oder vorab.</strong> Jedes Paket enthält das schriftliche Audio-Audit und unbegrenzte Revisionen. Zahlung per Überweisung oder PayPal.</p>
    <h2 id="de-bundles" style="margin-top:72px;">Mehr Releases, <em>weniger pro Master.</em></h2>
    <div class="price-grid">
      <div class="price"><div class="name">Single-Serie · 3 Singles</div><div class="amount">73<span style="margin-left:4px;">€</span></div><p>Pro Single statt 79 €, 18 € gespart. Gemastert, wenn die Singles erscheinen, über bis zu 12 Monate. Bezahlung pro Single oder alle drei vorab.</p></div>
      <div class="price"><div class="name">Stem-EP · bis 5 Tracks</div><div class="amount">549<span style="margin-left:4px;">€</span></div><p>96 € gespart gegenüber 5 Stem-Singles. Bis zu 6 Stems pro Track, Audit pro Track, 5–7 Tage.</p></div>
      <div class="price"><div class="name">Label-Partner · ab 4 Releases pro Jahr</div><div class="amount">ab 63<span style="margin-left:4px;">€</span></div><p>Single 63 €, Stem-Single 103 €, EP 279 €, Album 499 €. Ein konsistenter Klang über euren Katalog, Vorkasse oder Rechnung pro Release.</p></div>
    </div>
    <p class="meta-line">Alle Preise sind Endpreise inkl. 19 % USt. Bezahlung nach Wahl: Vorkasse oder auf Rechnung nach Fertigstellung. <a href="/de/mastering-kosten/">Mastering-Preise im Vergleich</a>.</p>
  </div>
</section>
<section class="content-section alt" aria-labelledby="de-ablauf">
  <div class="wrap prose-wrap prose">
    <h2 id="de-ablauf">So entsteht <em>dein Master</em></h2>
    <ol>
      <li><strong>Premaster schicken:</strong> 24/32-Bit WAV oder AIFF in der Original-Samplerate, 3–6 dB Headroom, kein Limiter auf der Summe, dazu ein oder zwei Referenztracks.</li>
      <li><strong>Audio-Audit:</strong> schriftlicher Bericht mit Schwachstellen und Mastering-Plan.</li>
      <li><strong>Mastering:</strong> gezielte Bearbeitung nach Plan, geprüft auf mehreren Abhörsystemen.</li>
      <li><strong>Lieferung:</strong> 24-Bit WAV, 16-Bit AIFF, 320 kbps MP3 sowie Versionen für Streaming und Bandcamp.</li>
      <li><strong>Revisionen:</strong> unbegrenzt, ohne Zeitlimit, bis der Master passt.</li>
    </ol>
  </div>
</section>
<section class="content-section" id="tim" aria-labelledby="de-tim">
  <div class="wrap prose-wrap prose">
    <h2 id="de-tim">Dein Mastering Engineer: <em>Tim Borchert</em></h2>
    <p>Tim Borchert hat Systematische Musikwissenschaft an der Universität Hamburg studiert und mastert jeden Track bei Polished persönlich. Sein Ansatz: erst messen und vergleichen, dann gezielt bearbeiten, statt Plugin-Roulette. Polished wurde 2024 gegründet und arbeitet vollständig online aus Kirchlinteln in Niedersachsen, für Bands aus Deutschland, Österreich, der Schweiz und international.</p>
  </div>
</section>
<section class="content-section alt" aria-labelledby="de-faq">
  <div class="wrap prose-wrap">
    <h2 id="de-faq">Häufige <em>Fragen</em></h2>
{faq_html(DE_FAQS)}
  </div>
</section>
<section class="content-section contact-section" id="kontakt" aria-labelledby="de-cta">
  <div class="wrap contact-grid">
    <div>
      <div class="eyebrow">Kontakt</div>
      <h2 id="de-cta">Dein Track. <em>Polished.</em></h2>
      <p class="lead" style="font-size: 18px;">Schreib kurz, um welches Projekt es geht: Genre, Anzahl der Tracks, Referenzen und geplanter Release-Termin. Die Antwort kommt persönlich von Tim, meist innerhalb von 24 Stunden.</p>
      <ul class="contact-direct">
        <li><span>E-Mail</span><a href="mailto:polished.media@gmx.de?subject=Mastering-Anfrage" data-track="de-email">polished.media@gmx.de</a></li>
        <li><span>Instagram</span><a href="https://instagram.com/polishedmetalmastering" rel="noopener" target="_blank" data-track="de-instagram">@polishedmetalmastering</a></li>
      </ul>
    </div>
    <form class="inquiry-form" data-formsubmit data-lang="de" novalidate>
      <div class="form-row">
        <div class="form-group"><label for="f-name">Name <span class="req" aria-hidden="true">*</span></label><input type="text" id="f-name" name="name" required autocomplete="name" placeholder="Dein Name oder Bandname"></div>
        <div class="form-group"><label for="f-email">E-Mail <span class="req" aria-hidden="true">*</span></label><input type="email" id="f-email" name="email" required autocomplete="email" placeholder="du@email.de"></div>
      </div>
      <div class="form-row">
        <div class="form-group"><label for="f-genre">Genre</label>
          <select id="f-genre" name="genre"><option value="">– Genre wählen –</option><option>Black Metal</option><option>Death Metal</option><option value="Doom & Gothic">Doom &amp; Gothic</option><option value="Metalcore/Djent">Metalcore · Djent</option><option value="Other">Anderes Genre</option></select></div>
        <div class="form-group"><label for="f-service">Leistung</label>
          <select id="f-service" name="service"><option value="">– Leistung wählen –</option><option value="Audio Audit">Nur Audio-Audit (Beratung)</option><option value="Stereo Single">Single – Stereo-Mastering (79 € inkl. USt.)</option><option value="Stem Single">Single – Stem-Mastering (129 € inkl. USt.)</option><option value="EP Mastering">EP-Mastering (349 € inkl. USt.)</option><option value="Album Mastering">Album-Mastering (629 € inkl. USt.)</option><option value="Single Series">Single-Serie – 3 Singles (je 73 € inkl. USt.)</option><option value="Stem EP">Stem-EP – bis 5 Tracks (549 € inkl. USt.)</option><option value="Label Partner">Label-Partner-Raten (ab 63 € inkl. USt.)</option><option value="Unsure">Noch unsicher</option></select></div>
      </div>
      <div class="form-group"><label for="f-tracks">Anzahl Tracks</label><input type="text" id="f-tracks" name="tracks" placeholder="z. B. 1 Single, EP mit 4 Tracks, Album mit 9 Tracks"></div>
      <div class="form-group"><label for="f-files">Link zu den Dateien <span class="opt">(optional)</span></label><input type="url" id="f-files" name="files" inputmode="url" placeholder="WeTransfer-, Dropbox- oder Google-Drive-Link zum Premaster"></div>
      <div class="form-group"><label for="f-message">Nachricht <span class="req" aria-hidden="true">*</span></label><textarea id="f-message" name="message" required placeholder="Worum geht es? Vision, Referenztracks, geplanter Release-Termin?"></textarea></div>
      <div class="hp" aria-hidden="true"><label for="f-website">Dieses Feld leer lassen</label><input type="text" id="f-website" name="_honey" tabindex="-1" autocomplete="off"></div>
      <div class="consent-row"><input type="checkbox" id="f-consent" name="consent" required><label for="f-consent">Ich habe die <a href="/#privacy">Datenschutzerklärung</a> gelesen und bin einverstanden, dass meine Angaben zur Bearbeitung der Anfrage verarbeitet werden. <span class="req" aria-hidden="true">*</span></label></div>
      <button type="submit" class="cta-btn form-submit" data-track="de-form-submit">Anfrage senden →</button>
      <div class="form-status" role="status" aria-live="polite"></div>
    </form>
  </div>
</section>'''
de_schemas = [
    webpage_schema(DE_PATH, DE_TITLE, lang='de'),
    {"@context": "https://schema.org", "@type": "Service", "@id": f"{BASE}/de/#service",
     "name": "Metal Mastering", "serviceType": "Audio-Mastering für Metal und Gothic", "url": f"{BASE}/de/",
     "provider": BIZ, "areaServed": [{"@type": "Country", "name": "Deutschland"}, {"@type": "Country", "name": "Österreich"}, {"@type": "Country", "name": "Schweiz"}],
     "availableLanguage": ["de", "en"],
     "offers": {"@type": "AggregateOffer", "priceCurrency": "EUR", "lowPrice": "79", "highPrice": "629", "offerCount": "4", "url": f"{BASE}/de/#preise", "priceSpecification": {"@type": "PriceSpecification", "priceCurrency": "EUR", "valueAddedTaxIncluded": True}}},
    faq_schema(DE_FAQS),
]
write(DE_PATH, page(path=DE_PATH, lang='de', title=DE_TITLE,
      description='Online-Mastering-Studio aus Deutschland für Black Metal, Death Metal, Doom & Gothic. Schriftliches Audio-Audit vor jedem Master. Kosten ab 79 € inkl. USt.',
      og_title='Polished — Metal Mastering Studio online', body=de_body, schemas=de_schemas,
      counterpart={'en': '/', 'de': '/de/'}))

# ---------------------------------------------------------------- 404
nf_body = '''<header class="page-hero">
  <div class="wrap">
    <div class="eyebrow">404</div>
    <h1>This page <em>doesn't exist.</em></h1>
    <p class="lead">The link may be outdated. Here's where you probably wanted to go:</p>
    <div class="cta-row">
      <a href="/" class="cta-btn">Home →</a>
      <a href="/#packages" class="cta-btn outline">Packages &amp; Pricing</a>
      <a href="/metal-mastering-loudness/" class="cta-btn outline">Loudness Guide</a>
    </div>
  </div>
</header>'''
write('/404.html', page(path='/404.html', lang='en', title='Page not found | Polished',
      description='This page does not exist.', og_title='Page not found — Polished', body=nf_body, schemas=[],
      robots='noindex, follow', canonical=False))
