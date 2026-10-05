#!/usr/bin/env python3
"""Google Search Console helper for polished.media.

Credentials (first match wins): env GSC_SERVICE_ACCOUNT_JSON_B64 (base64 JSON),
GSC_SERVICE_ACCOUNT_JSON (raw JSON), GSC_SERVICE_ACCOUNT_FILE (path).
Installs google-auth + requests automatically if missing.

  python3 _tools/gsc.py report [days]   # queries, pages, countries, devices
  python3 _tools/gsc.py inspect          # index status of every sitemap URL
  python3 _tools/gsc.py sitemap          # (re)submit sitemap.xml
"""
import base64, datetime, json, os, re, subprocess, sys, urllib.parse

try:
    import requests
    from google.oauth2 import service_account
    from google.auth.transport.requests import Request
except ImportError:  # fresh containers don't ship google-auth
    subprocess.run([sys.executable, '-m', 'pip', 'install', '-q', 'google-auth', 'requests'], check=True)
    import requests
    from google.oauth2 import service_account
    from google.auth.transport.requests import Request

SITE = 'sc-domain:polished.media'
SITEMAP = 'https://polished.media/sitemap.xml'
API = 'https://www.googleapis.com/webmasters/v3'


def creds():
    info = None
    if os.environ.get('GSC_SERVICE_ACCOUNT_JSON_B64'):
        info = json.loads(base64.b64decode(os.environ['GSC_SERVICE_ACCOUNT_JSON_B64']))
    elif os.environ.get('GSC_SERVICE_ACCOUNT_JSON'):
        info = json.loads(os.environ['GSC_SERVICE_ACCOUNT_JSON'])
    elif os.environ.get('GSC_SERVICE_ACCOUNT_FILE'):
        info = json.load(open(os.environ['GSC_SERVICE_ACCOUNT_FILE']))
    if not info:
        sys.exit('No GSC credentials: set GSC_SERVICE_ACCOUNT_JSON_B64 (or _JSON / _FILE).')
    c = service_account.Credentials.from_service_account_info(info, scopes=['https://www.googleapis.com/auth/webmasters'])
    c.refresh(Request())
    return {'Authorization': 'Bearer ' + c.token}


def q(s):
    return urllib.parse.quote(s, safe='')


def query(h, dims, days, limit=100):
    end = datetime.date.today()
    body = {'startDate': str(end - datetime.timedelta(days=days)), 'endDate': str(end), 'dimensions': dims, 'rowLimit': limit}
    return requests.post(f'{API}/sites/{q(SITE)}/searchAnalytics/query', headers=h, json=body).json().get('rows', [])


def report(h, days):
    print(f'== polished.media, last {days} days ==')
    for dims in (['query'], ['page'], ['country'], ['device']):
        print(f'\n-- {dims[0]} --')
        for r in sorted(query(h, dims, days), key=lambda r: -r['impressions'])[:40]:
            print(f"{r['keys'][0][:70]:70} imp={r['impressions']:5} clk={r['clicks']:4} ctr={r['ctr']*100:4.1f}% pos={r['position']:5.1f}")


def inspect(h):
    urls = re.findall(r'<loc>([^<]+)</loc>', requests.get(SITEMAP).text)
    for u in urls:
        d = requests.post('https://searchconsole.googleapis.com/v1/urlInspection/index:inspect', headers=h,
                          json={'inspectionUrl': u, 'siteUrl': SITE, 'languageCode': 'de'}).json()
        i = d.get('inspectionResult', {}).get('indexStatusResult', {})
        print(f"{u:60} {i.get('verdict', '?'):8} {i.get('coverageState', str(d)[:80])} crawled={i.get('lastCrawlTime', '-')[:10]}")


def sitemap(h):
    r = requests.put(f'{API}/sites/{q(SITE)}/sitemaps/{q(SITEMAP)}', headers=h)
    print('submit', r.status_code)
    print(json.dumps(requests.get(f'{API}/sites/{q(SITE)}/sitemaps', headers=h).json(), indent=1))


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'report'
    h = creds()
    if cmd == 'report':
        report(h, int(sys.argv[2]) if len(sys.argv) > 2 else 28)
    elif cmd == 'inspect':
        inspect(h)
    elif cmd == 'sitemap':
        sitemap(h)
    else:
        sys.exit(__doc__)
