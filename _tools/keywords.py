#!/usr/bin/env python3
"""Keyword map + tracking for polished.media.

Every target keyword has exactly one target page. Two checks:

  python3 _tools/keywords.py audit          # on-page: is each keyword in title / H1 / H2 / description / text of its page?
  python3 _tools/keywords.py track [days]   # Search Console: impressions, clicks, position per keyword,
                                            # this period vs. the period before, which page ranks, plus new
                                            # queries that are not in the map yet (needs GSC credentials, see gsc.py)

Matching is case/accent-insensitive, hyphens count as spaces. A phrase "matches" text when its words appear
in order with at most 2 filler words between them ("mastering service kosten in deutschland" matches
"mastering service kosten deutschland"). A heading "covers" a keyword when it contains all its words
(any order); FAQ questions count as headings.

  p1 (proven demand): covered by the title or one H1/H2/H3/FAQ question AND phrase in the text
  p2: phrase in the text OR covered by one heading
  p3: all words somewhere in the text
"""
import html, os, re, sys, unicodedata
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (keyword, target page, cluster, priority 1-3). Priority 1 = money keyword with proven demand in GSC.
KEYWORDS = [
    # --- DE: prices / costs (biggest proven demand) ---
    ('mastering kosten', '/de/mastering-kosten/', 'preis-de', 1),
    ('mastering preise', '/de/mastering-kosten/', 'preis-de', 1),
    ('mastering studio preise', '/de/mastering-kosten/', 'preis-de', 1),
    ('online mastering preise', '/de/mastering-kosten/', 'preis-de', 1),
    ('mastering service kosten deutschland', '/de/mastering-kosten/', 'preis-de', 1),
    ('song mastern lassen kosten', '/de/mastering-kosten/', 'preis-de', 1),
    ('vinyl mastering kosten', '/de/mastering-kosten/', 'preis-de', 1),
    ('mastering service preis', '/de/mastering-kosten/', 'preis-de', 2),
    ('song mastering kosten', '/de/mastering-kosten/', 'preis-de', 2),
    ('mastering studio preis', '/de/mastering-kosten/', 'preis-de', 2),
    ('mastering angebot', '/de/mastering-kosten/', 'preis-de', 3),
    ('album mastering kosten', '/de/mastering-kosten/', 'preis-de', 2),
    ('ep mastering kosten', '/de/mastering-kosten/', 'preis-de', 3),
    # mix+mastering: Polished masters only, the cost page explains market prices for mixing honestly
    ('mix und mastering preise', '/de/mastering-kosten/', 'mix-de', 2),
    ('mixing mastering preise', '/de/mastering-kosten/', 'mix-de', 2),
    ('mixing mastering kosten', '/de/mastering-kosten/', 'mix-de', 2),
    ('mixing preise', '/de/mastering-kosten/', 'mix-de', 3),
    ('mixing kosten', '/de/mastering-kosten/', 'mix-de', 3),
    ('song mischen lassen kosten', '/de/mastering-kosten/', 'mix-de', 3),
    ('online mixing preise', '/de/mastering-kosten/', 'mix-de', 3),
    ('song mixing kosten', '/de/mastering-kosten/', 'mix-de', 3),
    # --- DE: service / studio ---
    ('professionelles mastering', '/de/', 'service-de', 1),
    ('audio mastering studio deutschland', '/de/', 'service-de', 1),
    ('mastering service deutschland', '/de/', 'service-de', 2),
    ('mastering studio deutschland', '/de/', 'service-de', 2),
    ('mastering deutschland', '/de/', 'service-de', 2),
    ('online mastering', '/de/', 'service-de', 1),
    ('mastering lassen', '/de/', 'service-de', 2),
    ('song mastern lassen', '/de/', 'service-de', 1),
    ('album mastern lassen', '/de/', 'service-de', 2),
    ('metal mastering', '/de/', 'service-de', 1),
    ('gothic mastering', '/de/doom-gothic-mastering/', 'genre-de', 2),
    # --- DE: genres ---
    ('black metal mastering', '/de/black-metal-mastering/', 'genre-de', 1),
    ('death metal mastering', '/de/death-metal-mastering/', 'genre-de', 1),
    ('doom metal mastering', '/de/doom-gothic-mastering/', 'genre-de', 2),
    ('metalcore mastering', '/de/metalcore-djent-mastering/', 'genre-de', 2),
    ('djent mastering', '/de/metalcore-djent-mastering/', 'genre-de', 3),
    # --- DE: stems / loudness ---
    ('stem mastering', '/de/stem-mastering/', 'stem-de', 1),
    ('stem mastering preise', '/de/stem-mastering/', 'stem-de', 2),
    ('stem mastering kosten', '/de/stem-mastering/', 'stem-de', 3),
    ('metal mastering lautstärke', '/de/metal-mastering-lautstaerke/', 'loud-de', 2),
    ('lufs spotify', '/de/metal-mastering-lautstaerke/', 'loud-de', 2),
    ('wie laut mastern', '/de/metal-mastering-lautstaerke/', 'loud-de', 3),
    # --- EN ---
    ('metal mastering', '/', 'service-en', 1),
    ('online metal mastering', '/', 'service-en', 1),
    ('metal mastering service', '/', 'service-en', 1),
    ('gothic mastering', '/doom-gothic-mastering/', 'genre-en', 2),
    ('black metal mastering', '/black-metal-mastering/', 'genre-en', 1),
    ('death metal mastering', '/death-metal-mastering/', 'genre-en', 1),
    ('doom metal mastering', '/doom-gothic-mastering/', 'genre-en', 2),
    ('metalcore mastering', '/metalcore-djent-mastering/', 'genre-en', 2),
    ('djent mastering', '/metalcore-djent-mastering/', 'genre-en', 3),
    ('stem mastering', '/stem-mastering/', 'stem-en', 1),
    ('mastering cost', '/mastering-cost/', 'price-en', 1),
    ('how much does mastering cost', '/mastering-cost/', 'price-en', 1),
    ('mastering prices', '/mastering-cost/', 'price-en', 2),
    ('album mastering cost', '/mastering-cost/', 'price-en', 2),
    ('metal mastering loudness', '/metal-mastering-loudness/', 'loud-en', 2),
    ('lufs for metal', '/metal-mastering-loudness/', 'loud-en', 2),
    # --- brand ---
    ('polished media', '/', 'brand', 2),
    ('polished mastering', '/', 'brand', 2),
]
LANG = {'de': lambda p: p.startswith('/de/')}


def norm(s):
    s = html.unescape(s).lower().replace('ß', 'ss').replace('-', ' ').replace('–', ' ')
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'\s+', ' ', re.sub(r'[^\w\s€]', ' ', s)).strip()


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = self.desc = ''
        self.h1, self.h2, self.text = [], [], []
        self._tag, self._skip = None, 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('script', 'style'):
            self._skip += 1
        if tag == 'meta' and a.get('name') == 'description':
            self.desc = a.get('content', '')
        if tag in ('title', 'h1', 'h2', 'h3', 'summary'):
            self._tag = tag
            if tag != 'title':
                (self.h1 if tag == 'h1' else self.h2).append('')

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self._skip -= 1
        if tag == self._tag:
            self._tag = None

    def handle_data(self, d):
        if self._skip:
            return
        if self._tag == 'title':
            self.title += d
        elif self._tag == 'h1':
            self.h1[-1] += d
        elif self._tag in ('h2', 'h3', 'summary'):
            self.h2[-1] += d
        self.text.append(d)


def load(path):
    f = os.path.join(ROOT, path.strip('/'), 'index.html') if path != '/' else os.path.join(ROOT, 'index.html')
    p = Page()
    p.feed(open(f, encoding='utf-8').read())
    return {'title': norm(p.title), 'h1': norm(' '.join(p.h1)), 'h2': norm(' | '.join(p.h2)),
            'desc': norm(p.desc), 'text': norm(' '.join(p.text)),
            'heads': [norm(p.title), norm(' '.join(p.h1))] + [norm(x) for x in p.h2]}


def near(k, text):
    return len(re.findall(r'\b' + r'(?: \w+){0,2} '.join(map(re.escape, k.split())) + r'\b', text))


def covers(k, heading):
    hw = set(heading.split())
    return all(w in hw for w in k.split())


def audit():
    cache, gaps = {}, 0
    print(f"{'keyword':38} {'page':32} T H1 H2 D  n   status")
    for kw, page, cluster, prio in KEYWORDS:
        d = cache.setdefault(page, load(page))
        k = norm(kw)
        flags = [k in d[f] for f in ('title', 'h1', 'h2', 'desc')]
        n = near(k, d['text'])
        head = any(covers(k, x) for x in d['heads'])
        words = all(w in d['text'].split() for w in k.split())
        ok = (head and n > 0) if prio == 1 else ((n > 0 or head) if prio == 2 else words)
        gaps += not ok
        mark = lambda b: 'x' if b else '.'
        print(f"{kw:38} {page:32} {mark(flags[0])} {mark(flags[1]):2} {mark(flags[2]):2} {mark(flags[3])} {n:3}   {'ok' if ok else 'GAP'} (p{prio})")
    print(f'\n{gaps} gap(s)')
    return gaps


def track(days):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import datetime, gsc, requests
    h = gsc.creds()
    end = datetime.date.today() - datetime.timedelta(days=2)  # GSC data lags ~2 days

    def rows(start, stop):
        body = {'startDate': str(start), 'endDate': str(stop), 'dimensions': ['query', 'page'], 'rowLimit': 25000}
        r = requests.post(f'{gsc.API}/sites/{gsc.q(gsc.SITE)}/searchAnalytics/query', headers=h, json=body).json()
        out = {}
        for x in r.get('rows', []):
            qn, pg = norm(x['keys'][0]), x['keys'][1].replace('https://polished.media', '')
            o = out.setdefault(qn, {'imp': 0, 'clk': 0, 'pw': 0.0, 'pages': {}})
            o['imp'] += x['impressions']; o['clk'] += x['clicks']; o['pw'] += x['position'] * x['impressions']
            o['pages'][pg] = o['pages'].get(pg, 0) + x['impressions']
        return out

    cur = rows(end - datetime.timedelta(days=days - 1), end)
    prev = rows(end - datetime.timedelta(days=2 * days - 1), end - datetime.timedelta(days=days))
    ever = rows(end - datetime.timedelta(days=480), end)
    pos = lambda o: o['pw'] / o['imp'] if o and o['imp'] else None
    fmt = lambda v: f'{v:5.1f}' if v else '    -'
    print(f'== keywords, last {days} days (to {end}) vs. {days} days before; "16m" = position over 16 months ==')
    print(f"{'keyword':38} {'imp':>5} {'clk':>4} {'pos':>5} {'prev':>5} {'Δ':>6} {'16m':>5}  ranking page")
    seen = set()
    for kw, page, cluster, prio in sorted(KEYWORDS, key=lambda k: (k[3], k[2])):
        k = norm(kw)
        if k in seen:
            continue
        seen.add(k)
        c, p, e = cur.get(k), prev.get(k), ever.get(k)
        pc, pp = pos(c), pos(p)
        delta = f'{pp - pc:+6.1f}' if pc and pp else '     '
        top = max((c or e or {'pages': {'': 0}})['pages'].items(), key=lambda i: i[1])[0]
        warn = ' (≠ target ' + page + ')' if top and top != page and (c or e) else ''
        print(f"{kw:38} {c['imp'] if c else 0:5} {c['clk'] if c else 0:4} {fmt(pc)} {fmt(pp)} {delta} {fmt(pos(e))}  {top}{warn}")
    mapped = {norm(k[0]) for k in KEYWORDS}
    new = sorted(((q, o) for q, o in ever.items() if q not in mapped), key=lambda i: -i[1]['imp'])
    if new:
        print('\n-- queries not in the keyword map yet (16 months) --')
        for q, o in new[:25]:
            print(f"{q:38} {o['imp']:5} {o['clk']:4} {fmt(pos(o))}")


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'audit'
    if cmd == 'audit':
        sys.exit(1 if audit() else 0)
    elif cmd == 'track':
        track(int(sys.argv[2]) if len(sys.argv) > 2 else 7)
    else:
        sys.exit(__doc__)
