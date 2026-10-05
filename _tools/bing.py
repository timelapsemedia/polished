#!/usr/bin/env python3
"""Bing Webmaster Tools helper for polished.media (key: env BING_WEBMASTER_API_KEY or BING_API_KEY).

  python3 _tools/bing.py report              # query stats, traffic, crawl issues, sitemap status
  python3 _tools/bing.py submit [URL ...]    # submit URLs (default: all sitemap URLs) + sitemap
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
else:
    sys.exit(__doc__)
