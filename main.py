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

@app.get("/getQuote")
def get_quote(symbol: str):
    r = requests.get(f"{FINNHUB_BASE}/quote", params={"symbol": symbol, "token": FINNHUB_API_KEY})
    return r.json()

@app.get("/getFundamentals")
def get_fundamentals(symbol: str):
    r = requests.get(f"{FINNHUB_BASE}/stock/metric", params={"symbol": symbol, "metric": "all", "token": FINNHUB_API_KEY})
    return r.json()

@app.get("/getNewsSentiment")
def get_news_sentiment(symbol: str):
    r = requests.get(f"{FINNHUB_BASE}/news-sentiment", params={"symbol": symbol, "token": FINNHUB_API_KEY})
    return r.json()

@app.get("/batch/getQuotes")
def batch_get_quotes(symbols: list[str] = Query(...)):
    results = {}
    for symbol in symbols:
        r = requests.get(f"{FINNHUB_BASE}/quote", params={"symbol": symbol, "token": FINNHUB_API_KEY})
        results[symbol] = r.json()
    return results

@app.get("/batch/getFundamentals")
def batch_get_fundamentals(symbols: list[str] = Query(...)):
    results = {}
    for symbol in symbols:
        r = requests.get(f"{FINNHUB_BASE}/stock/metric", params={"symbol": symbol, "metric": "all", "token": FINNHUB_API_KEY})
        results[symbol] = r.json()
    return results

@app.get("/batch/getNewsSentiment")
def batch_get_news_sentiment(symbols: list[str] = Query(...)):
    results = {}
    for symbol in symbols:
        r = requests.get(f"{FINNHUB_BASE}/news-sentiment", params={"symbol": symbol, "token": FINNHUB_API_KEY})
        results[symbol] = r.json()
    return results
