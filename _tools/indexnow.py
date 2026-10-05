#!/usr/bin/env python3
"""Notify Bing / IndexNow engines about changed URLs.

  python3 _tools/indexnow.py                 # all URLs in sitemap.xml
  python3 _tools/indexnow.py URL [URL ...]   # specific URLs
Key file: /e7ff59cd75746039c862a6ccb5488233.txt (repo root, must stay published).
"""
import json, re, sys, urllib.request

KEY = 'e7ff59cd75746039c862a6ccb5488233'
urls = sys.argv[1:] or re.findall(r'<loc>([^<]+)</loc>', urllib.request.urlopen('https://polished.media/sitemap.xml').read().decode())
body = json.dumps({'host': 'polished.media', 'key': KEY, 'keyLocation': f'https://polished.media/{KEY}.txt', 'urlList': urls}).encode()
req = urllib.request.Request('https://api.indexnow.org/IndexNow', data=body, headers={'Content-Type': 'application/json; charset=utf-8'})
print('IndexNow', urllib.request.urlopen(req).status, len(urls), 'URLs')
