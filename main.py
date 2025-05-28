from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

FINNHUB_API_KEY = "d0r3kqhr01qn4tjg8qtgd0r3kqhr01qn4tjg8qu0"
FINNHUB_BASE = "https://finnhub.io/api/v1"

@app.get("/batch/getFundamentals")
def batch_get_fundamentals(symbols: list[str] = Query(...)):
    results = {}
    for symbol in symbols:
        r = requests.get(f"{FINNHUB_BASE}/stock/metric", params={
            "symbol": symbol,
            "metric": "valuation",
            "token": FINNHUB_API_KEY
        })
        results[symbol] = r.json()
    return {"data": results}
