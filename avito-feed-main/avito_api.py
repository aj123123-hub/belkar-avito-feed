"""Мини-клиент Avito API для аккаунта ООО БелКар (ключи из .env рядом, не в git)."""
import json, os, sys, urllib.request, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
FEED_URL = "https://raw.githubusercontent.com/aj123123-hub/belkar-avito-feed/main/avito-feed-main/fleet-main.xlsx"


def token():
    env = dict(l.strip().split("=", 1) for l in open(os.path.join(HERE, ".env")) if "=" in l)
    data = urllib.parse.urlencode({"grant_type": "client_credentials", "client_id": env["AVITO_CLIENT_ID"],
                                   "client_secret": env["AVITO_CLIENT_SECRET"]}).encode()
    return json.load(urllib.request.urlopen("https://api.avito.ru/token", data, timeout=30))["access_token"]


def call(method, path, body=None, tok=None):
    req = urllib.request.Request("https://api.avito.ru" + path, method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": "Bearer " + tok, "Content-Type": "application/json"})
    try:
        raw = urllib.request.urlopen(req, timeout=60).read()
        return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        return {"HTTP": e.code, "body": e.read().decode()[:1000]}


if __name__ == "__main__":
    t = token()
    cmd = sys.argv[1]
    if cmd == "set-profile":
        body = {"autoload_enabled": True, "report_email": "info@bel-car.com",
                "feeds_data": [{"feed_name": "fleet-main", "feed_url": FEED_URL}],
                "schedule": [{"rate": 1000, "weekdays": list(range(7)), "time_slots": list(range(24))}]}
        print(call("POST", "/autoload/v2/profile", body, t))
        print(json.dumps(call("GET", "/autoload/v2/profile", tok=t), ensure_ascii=False))
    elif cmd == "upload":
        print(call("POST", "/autoload/v1/upload", {}, t))
    elif cmd == "last":
        r = call("GET", "/autoload/v2/reports/last_completed_report", tok=t)
        print(json.dumps({k: v for k, v in r.items() if k not in ("items", "_deprecation")}, ensure_ascii=False))
    elif cmd == "reports":
        print(json.dumps(call("GET", "/autoload/v2/reports?per_page=3", tok=t), ensure_ascii=False))
