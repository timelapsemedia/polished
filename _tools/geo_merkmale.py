#!/usr/bin/env python3
"""GEO-Merkmale je Seite prüfen (SISTRIX-Studie „Citation Worthiness“, 22.10.2026, 96.418 URLs).

Misst live jede Sitemap-URL auf die Merkmale, die KI-Zitate (ChatGPT, AI Mode, AI Overviews) am stärksten
mit sich bringen (Faktor = so viel öfter zitiert als eine Seite derselben Domain ohne das Merkmal):
  TOC    sichtbares Inhaltsverzeichnis mit Sprungmarken           1,7
  ART    Article-/BlogPosting-Schema (nicht auf Produktseiten)     1,6
  H2     mindestens 5 H2-Überschriften                             1,6
  FAQ    FAQPage-Schema mit echten Fragen                          1,4–1,5
  TAB    Tabelle mit Kopfzeile (<th>)                              1,4–1,5
  AUTOR  Autorenbox mit Foto                                       1,4–1,5
  DATUM  sichtbares „Zuletzt aktualisiert“                         1,3
  WORTE  mindestens 1.000 Wörter                                   1,5
Ohne messbaren Effekt: llms.txt, Breadcrumb-, HowTo-, QAPage-Schema, Lesbarkeitswerte. Korrelation, keine Kausalität.

  python3 geo_merkmale.py https://polished.media [--json]
  python3 geo_merkmale.py https://polished.media --lokal .   # local build: sitemap.xml + pages from the repo folder
"""
import html, json, os, re, sys, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (geo-merkmale)"}
LOKAL = sys.argv[sys.argv.index("--lokal") + 1] if "--lokal" in sys.argv else None
SITE = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else ""


def holen(u):
    if LOKAL:  # https://site/pfad/ -> <ordner>/pfad/index.html
        rel = u.replace(SITE, "").strip("/")
        datei = os.path.join(LOKAL, rel, "index.html") if not rel.endswith((".xml", ".html")) else os.path.join(LOKAL, rel)
        with open(datei, encoding="utf-8") as f:
            return f.read()
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30).read().decode("utf-8", "replace")


def schema_typen(h):
    """All @type values in the JSON-LD blocks, including type lists like ["SoftwareApplication", "Product"]."""
    typen = set()

    def sammle(o):
        if isinstance(o, dict):
            t = o.get("@type")
            typen.update(t if isinstance(t, list) else [t] if t else [])
            for v in o.values():
                sammle(v)
        elif isinstance(o, list):
            for v in o:
                sammle(v)
    for block in re.findall(r'<script[^>]+ld\+json[^>]*>(.*?)</script>', h, re.S):
        sammle(json.loads(block))  # broken JSON-LD fails loudly
    return typen


def pruefe(u):
    h = holen(u)
    typen = schema_typen(h)
    body = re.sub(r"<script.*?</script>|<style.*?</style>", "", h, flags=re.S)
    text = html.unescape(re.sub(r"<[^>]+>", " ", body))
    produkt = bool(typen & {"Product", "SoftwareApplication"})
    return {
        "TOC": bool(re.search(r'(inhalt|contents|toc|auf dieser seite|on this page)', body, re.I))
               and len(re.findall(r'href="#[^"]+"', body)) >= 3,
        "ART": bool(typen & {"Article", "BlogPosting", "TechArticle", "NewsArticle"}) or produkt,  # Produktseiten: eigenes Schema
        "H2": len(re.findall(r"<h2[\s>]", body, re.I)) >= 5,
        "FAQ": "FAQPage" in typen,
        "TAB": bool(re.search(r"<table.*?<th[\s>]", body, re.S | re.I)),
        "AUTOR": bool(re.search(r'class="[^"]*(autor|author)[^"]*"', body, re.I))
                 and bool(re.search(r'<img[^>]+', body)),
        "DATUM": bool(re.search(r'(zuletzt aktualisiert|aktualisiert am|last updated|updated on)', text, re.I)),
        "WORTE": len(text.split()) >= 1000,
    }


def main():
    site = SITE
    urls = re.findall(r"<loc>(.*?)</loc>", holen(site + "/sitemap.xml"))
    erg = {}
    for u in urls:
        try:
            erg[u] = pruefe(u)
        except Exception as e:  # nie still auf „ok“ fallen
            erg[u] = {"FEHLER": str(e)[:120]}
    if "--json" in sys.argv:
        print(json.dumps(erg, ensure_ascii=False, indent=1))
        return
    zaehl = {}
    for u, r in erg.items():
        fehlt = [k for k, v in r.items() if v is False]
        for k in fehlt:
            zaehl[k] = zaehl.get(k, 0) + 1
        print(f"{len(fehlt)} fehlen  {u.replace(site, '') or '/'}: {', '.join(fehlt) or '–'}")
    print(f"\n{len(urls)} Seiten · fehlend: " + ", ".join(f"{k} {v}" for k, v in sorted(zaehl.items(), key=lambda x: -x[1])))


if __name__ == "__main__":
    main()
