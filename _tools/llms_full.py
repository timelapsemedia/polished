#!/usr/bin/env python3
"""Build /llms-full.txt: the readable text of every page in sitemap.xml, for AI assistants.

Run after `python3 _tools/gen.py` (gen.py calls it automatically). Reads the local HTML files,
so it works before deployment.
"""
import html, os, re
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://polished.media'


def local_file(url):
    path = url.replace(BASE, '').strip('/')
    return os.path.join(ROOT, path, 'index.html') if path else os.path.join(ROOT, 'index.html')


SKIP_CLASSES = ('ab-player', 'audit-visual', 'cursor', 'portrait-corner', 'portrait-indicator', 'genre-arrow', 'icon')
BLOCK = {'p', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'tr', 'summary', 'div', 'section', 'table', 'blockquote', 'br', 'ol', 'ul', 'details', 'header'}
VOID = {'br', 'img', 'input', 'meta', 'link', 'source', 'hr'}


class Extractor(HTMLParser):
    """Collects readable text, skipping decorative/UI subtrees (aria-hidden, player widgets, forms)."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip, self.stack = [], 0, []

    def handle_starttag(self, tag, attrs):
        if tag in VOID:
            if tag == 'br' and not self.skip:
                self.out.append('\n')
            return
        a = dict(attrs)
        cls = a.get('class', '') or ''
        hide = (a.get('aria-hidden') == 'true' or tag in ('script', 'style', 'svg', 'canvas', 'form', 'button', 'nav', 'select')
                or any(c in cls.split() for c in SKIP_CLASSES))
        self.stack.append(hide)
        if hide:
            self.skip += 1
            return
        if self.skip:
            return
        if tag in BLOCK:
            self.out.append('\n')
        if tag in ('h1', 'h2', 'h3', 'h4'):
            self.out.append('#' * (int(tag[1]) + 1) + ' ')
        elif tag == 'li':
            self.out.append('- ')

    def handle_endtag(self, tag):
        if tag in VOID or not self.stack:
            return
        hide = self.stack.pop()
        if hide:
            self.skip -= 1
            return
        if not self.skip and tag in BLOCK:
            self.out.append('\n')
        elif not self.skip and tag in ('strong', 'b'):
            self.out.append(' ')

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)


def page_text(raw):
    title = re.search(r'<title>(.*?)</title>', raw, re.S)
    main = re.search(r'<main[^>]*>(.*?)</main>', raw, re.S)
    ex = Extractor()
    ex.feed(main.group(1) if main else raw)
    text = ''.join(ex.out)
    lines, prev = [], None
    for l in text.split('\n'):
        l = re.sub(r'\s+', ' ', l).strip()
        if not l or l == prev:
            continue
        if lines and re.fullmatch(r'#+', lines[-1]):  # heading marker split from its text
            lines[-1] = lines[-1] + ' ' + l
        elif lines and re.match(r'#+ ', lines[-1]) and not re.match(r'[#-]', l) and len(lines[-1]) < 60 and len(l) < 60 and l[0].islower():
            lines[-1] = lines[-1] + ' ' + l   # heading continued after a <br>
        else:
            lines.append(l)
        prev = l
    return (html.unescape(title.group(1)).strip() if title else ''), '\n'.join(lines)


def main():
    sitemap = open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8').read()
    urls = re.findall(r'<loc>([^<]+)</loc>', sitemap)
    parts = ['# Polished Mastering – full site text\n',
             '> Online mastering studio for Metal & Gothic (Germany). Written audio audit before every master, '
             'unlimited revisions, prices incl. 19% VAT. This file contains the readable text of every page on '
             'polished.media (English and German). Summary: https://polished.media/llms.txt\n']
    for u in urls:
        f = local_file(u)
        if not os.path.exists(f):
            continue
        title, text = page_text(open(f, encoding='utf-8').read())
        parts.append(f'\n---\n\n## {title}\nURL: {u}\n\n{text}\n')
    open(os.path.join(ROOT, 'llms-full.txt'), 'w', encoding='utf-8').write(''.join(parts))
    print('llms-full.txt:', len(urls), 'pages')


if __name__ == '__main__':
    main()
