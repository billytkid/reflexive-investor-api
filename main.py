from fastapi import FastAPI, HTTPException
import requests
import os

app = FastAPI()

FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")

@app.get("/getQuote")
def get_quote(symbol: str):
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={FINNHUB_API_KEY}"
    r = requests.get(url)
    if r.status_code != 200:
        raise HTTPException(status_code=500, detail="Finnhub API error")
    return r.json()

@app.get("/getFundamentals")
def get_fundamentals(symbol: str):
    url = f"https://finnhub.io/api/v1/stock/metric?symbol={symbol}&metric=all&token={FINNHUB_API_KEY}"
    r = requests.get(url)
    if r.status_code != 200:
        raise HTTPException(status_code=500, detail="Finnhub API error")
    return r.json()

@app.get("/getNewsSentiment")
def get_news_sentiment(symbol: str):
    url = f"https://finnhub.io/api/v1/news-sentiment?symbol={symbol}&token={FINNHUB_API_KEY}"
    r = requests.get(url)
    if r.status_code != 200:
        raise HTTPException(status_code=500, detail="Finnhub API error")
    return r.json()