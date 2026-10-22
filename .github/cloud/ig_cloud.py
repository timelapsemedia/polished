# -*- coding: utf-8 -*-
"""Cloud-Publisher fuer Instagram (GitHub Actions, oeffentliche Repos = Minuten gratis). Tim 22.10.2026:
fehlende Posts, weil der PC aus war (15.-18.10. alle Marken), sollen trotzdem rausgehen.

Laeuft stuendlich im Workflow .github/workflows/ig-cloud.yml jeder Marke. Liest die Warteschlange, die der lokale
Publisher bei jedem Lauf nach Branch `cloud-publisher` (queue.json) spiegelt, und postet faellige Eintraege, die
noch nicht live sind. Idempotent wie der lokale Nachholer: EXAKTER Caption-Abgleich gegen die letzten 50 Posts.
Hoechstens 1 Post pro Lauf (keine Flut nach langer PC-Pause), nur Termine der letzten FENSTER_H Stunden.

queue.json: {"marke": "...", "stand": "...", "posts": [{"id", "due" (ISO mit Offset), "caption",
             "image_urls": [...], "video_url": "..." | null, "cover_url"/"thumb_offset" (ms): optional,
             "hold": optional}]}
Umgebung: IG_TOKEN, optional IG_USER_ID (Std. me), QUEUE (Pfad), STATE (Pfad, jsonl), optional FENSTER_H (Std. 48), TROCKEN=1.
Exit 1 bei Fehler (Actions zeigt rot, Nachhol-Waechter sieht es)."""
import datetime as dt
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://graph.instagram.com/v21.0"
TOKEN = os.environ.get("IG_TOKEN", "")
USER = os.environ.get("IG_USER_ID") or "me"   # Instagram-Login-Token: /me reicht
FENSTER_H = float(os.environ.get("FENSTER_H", "48"))
TROCKEN = os.environ.get("TROCKEN") == "1"


def api(methode, pfad, **p):
    p["access_token"] = TOKEN
    url = f"{API}/{pfad.lstrip('/')}"
    daten = None
    if methode == "POST":
        daten = urllib.parse.urlencode(p).encode()
    else:
        url += "?" + urllib.parse.urlencode(p)
    try:
        with urllib.request.urlopen(urllib.request.Request(url, daten, method=methode), timeout=90) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        text = e.read().decode("utf-8", "replace")
        try:
            f = json.loads(text)["error"]
            text = f"code={f.get('code')} sub={f.get('error_subcode')} {f.get('message')}"
        except Exception:
            pass
        raise RuntimeError(text.replace(TOKEN, "***")[:300]) from None


def warte(cid, versuche):
    for _ in range(versuche):
        s = api("GET", cid, fields="status_code,status")
        if s.get("status_code") == "FINISHED":
            return
        if s.get("status_code") == "ERROR":
            raise RuntimeError(f"Container-Fehler: {s.get('status')}")
        time.sleep(5)
    raise RuntimeError("Timeout beim Warten auf den Container")


def posten(p):
    if p.get("video_url"):
        extra = {"cover_url": p["cover_url"]} if p.get("cover_url") else {}
        if p.get("thumb_offset") is not None:
            extra["thumb_offset"] = str(int(p["thumb_offset"]))
        c = api("POST", f"{USER}/media", media_type="REELS", video_url=p["video_url"], caption=p["caption"],
                share_to_feed="true", **extra)
        warte(c["id"], 120)
    elif len(p["image_urls"]) == 1:
        c = api("POST", f"{USER}/media", image_url=p["image_urls"][0], caption=p["caption"])
        warte(c["id"], 40)
    else:
        kinder = [api("POST", f"{USER}/media", image_url=u, is_carousel_item="true")["id"] for u in p["image_urls"]]
        c = api("POST", f"{USER}/media", media_type="CAROUSEL", children=",".join(kinder), caption=p["caption"])
        warte(c["id"], 40)
    r = api("POST", f"{USER}/media_publish", creation_id=c["id"])
    link = api("GET", r["id"], fields="permalink").get("permalink", "")
    return r["id"], link


def protokoll(eintrag):
    eintrag["at"] = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    with open(os.environ["STATE"], "a", encoding="utf-8") as f:
        f.write(json.dumps(eintrag, ensure_ascii=False) + "\n")
    print(json.dumps(eintrag, ensure_ascii=False))


def main():
    if not TOKEN:
        sys.exit("IG_TOKEN fehlt")
    q = json.load(open(os.environ["QUEUE"], encoding="utf-8"))
    jetzt = dt.datetime.now(dt.timezone.utc)
    faellig = []
    for p in q["posts"]:
        due = dt.datetime.fromisoformat(p["due"])
        alter_h = (jetzt - due).total_seconds() / 3600
        if 0 <= alter_h <= FENSTER_H and not p.get("hold"):
            faellig.append((due, p))
    print(f"{q.get('marke')}: Warteschlange vom {q.get('stand')}, {len(q['posts'])} Posts, {len(faellig)} faellig")
    if not faellig:
        return
    live = {(m.get("caption") or "").strip() for m in api("GET", f"{USER}/media", fields="caption", limit=50)["data"]}
    offen = [p for _, p in sorted(faellig, key=lambda x: x[0]) if p["caption"].strip() not in live]
    print(f"davon schon live: {len(faellig) - len(offen)}, offen: {len(offen)}")
    if not offen:
        return
    p = offen[0]                                         # hoechstens einer pro Lauf
    if TROCKEN:
        print(f"TROCKEN: wuerde {p['id']} posten ({'Reel' if p.get('video_url') else len(p['image_urls'])})")
        return
    try:
        mid, link = posten(p)
        protokoll({"post": p["id"], "status": "OK", "media_id": mid, "permalink": link, "von": "cloud"})
    except Exception as e:
        protokoll({"post": p["id"], "status": "FEHLER", "msg": str(e)[:300], "von": "cloud"})
        sys.exit(1)


if __name__ == "__main__":
    main()
