#!/usr/bin/env python3
"""Bing Webmaster Tools helper for polished.media (key: env BING_WEBMASTER_API_KEY or BING_API_KEY).

  python3 _tools/bing.py report              # query stats, traffic, crawl issues, sitemap status
  python3 _tools/bing.py submit [URL ...]    # submit URLs (default: all sitemap URLs) + sitemap
  python3 _tools/bing.py volume              # Bing search impressions (≈ search volume) for the p1 keywords
                                             # from keywords.py serplist, last ~3 months (free, no credits)
"""
import json, os, re, sys, urllib.request

SITE = 'https://polished.media/'
API = 'https://ssl.bing.com/webmaster/api.svc/json/'
KEY = os.environ.get('BING_WEBMASTER_API_KEY') or os.environ.get('BING_API_KEY') or sys.exit('Set BING_WEBMASTER_API_KEY or BING_API_KEY.')


def call(method, params=None, body=None):
    q = '&'.join(f'{k}={urllib.request.quote(str(v), safe="")}' for k, v in (params or {}).items())
    url = f'{API}{method}?apikey={KEY}' + (f'&{q}' if q else '')
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body else None,
                                 headers={'Content-Type': 'application/json; charset=utf-8'})
    raw = urllib.request.urlopen(req, timeout=30).read().decode()
    return json.loads(raw).get('d') if raw else None


def sitemap_urls():
    return re.findall(r'<loc>([^<]+)</loc>', urllib.request.urlopen(SITE + 'sitemap.xml').read().decode())


cmd = sys.argv[1] if len(sys.argv) > 1 else 'report'
if cmd == 'report':
    print('Quota:', call('GetUrlSubmissionQuota', {'siteUrl': SITE}))
    for f in call('GetFeeds', {'siteUrl': SITE}) or []:
        print('Sitemap:', f['Url'], f['Status'], f['UrlCount'], 'URLs')
    traffic = call('GetRankAndTrafficStats', {'siteUrl': SITE}) or []
    print('Traffic days:', len(traffic), '| impressions', sum(t.get('Impressions', 0) for t in traffic),
          '| clicks', sum(t.get('Clicks', 0) for t in traffic))
    print('\n-- queries --')
    for r in sorted(call('GetQueryStats', {'siteUrl': SITE}) or [], key=lambda r: -r.get('Impressions', 0))[:40]:
        print(f"{r['Query'][:60]:60} imp={r.get('Impressions', 0):5} clk={r.get('Clicks', 0):4} pos={r.get('AvgImpressionPosition', 0)}")
    print('\n-- crawl issues --')
    for i in call('GetCrawlIssues', {'siteUrl': SITE}) or []:
        print(i)
elif cmd == 'submit':
    urls = sys.argv[2:] or sitemap_urls()
    call('SubmitUrlBatch', body={'siteUrl': SITE, 'urlList': urls})
    print('submitted', len(urls), 'URLs')
    try:
        call('SubmitFeed', body={'siteUrl': SITE, 'feedUrl': SITE + 'sitemap.xml'})
        print('sitemap resubmitted')
    except Exception as e:  # sitemap resubmission is best-effort
        print('sitemap resubmit failed:', e)
elif cmd == 'volume':
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import keywords
    seen = set()
    print(f"{'market':14} {'keyword':38} {'exact':>6} {'broad':>6}  (Bing impressions, summed over the weeks Bing returns)")
    for kw, page, cluster, prio in keywords.KEYWORDS:
        country, _ = keywords.market(page)
        cc, lang = ('de', 'de-DE') if country == 'Germany' else ('us', 'en-US')
        if prio != 1 or cluster == 'brand' or (kw, cc) in seen:
            continue
        seen.add((kw, cc))
        rows = call('GetKeywordStats', {'q': kw, 'country': cc, 'language': lang}) or []
        print(f"{country:14} {kw:38} {sum(r.get('Impressions', 0) for r in rows):6} {sum(r.get('BroadImpressions', 0) for r in rows):6}")
else:
    sys.exit(__doc__)
