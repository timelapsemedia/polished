#!/usr/bin/env python3
"""Notify all IndexNow search engines about changed URLs.

  python3 _tools/indexnow.py                 # all URLs in sitemap.xml
  python3 _tools/indexnow.py URL [URL ...]   # specific URLs

Each participating engine is pinged directly (they also share submissions with
each other): Bing, Yandex, Seznam, Naver, Yep, plus the shared api.indexnow.org.
Key file: /e7ff59cd75746039c862a6ccb5488233.txt (repo root, must stay published).
"""
import json, re, sys, urllib.request, urllib.error

KEY = 'e7ff59cd75746039c862a6ccb5488233'
ENDPOINTS = [
    'https://api.indexnow.org/indexnow',
    'https://www.bing.com/indexnow',
    'https://yandex.com/indexnow',
    'https://search.seznam.cz/indexnow',
    'https://searchadvisor.naver.com/indexnow',
    'https://indexnow.yep.com/indexnow',
]
urls = sys.argv[1:] or re.findall(r'<loc>([^<]+)</loc>', urllib.request.urlopen('https://polished.media/sitemap.xml').read().decode())
body = json.dumps({'host': 'polished.media', 'key': KEY, 'keyLocation': f'https://polished.media/{KEY}.txt', 'urlList': urls}).encode()
for ep in ENDPOINTS:
    req = urllib.request.Request(ep, data=body, headers={'Content-Type': 'application/json; charset=utf-8'})
    try:
        status = urllib.request.urlopen(req, timeout=20).status
    except urllib.error.HTTPError as e:
        status = e.code
    except Exception as e:
        status = type(e).__name__
    print(f'{ep:45} {status}  ({len(urls)} URLs)')
