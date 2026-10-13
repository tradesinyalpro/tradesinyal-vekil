from flask import Flask, request, Response
import requests, os

app = Flask(__name__)
IZINLI = ("/fapi/v1/ticker/24hr", "/fapi/v1/ticker/price", "/fapi/v1/klines")

@app.route("/<path:yol>")
def vekil(yol):
    yol = "/" + yol
    if yol not in IZINLI:
        return Response("izin yok", status=403)
    r = requests.get("https://fapi.binance.com" + yol, params=request.args, timeout=15)
    return Response(r.content, status=r.status_code, content_type="application/json")

@app.route("/")
def ana():
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))