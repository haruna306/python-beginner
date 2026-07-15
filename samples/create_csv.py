"""
日経225銘柄の株価データ(過去1年分)を取得してCSVで保存するサンプルスクリプト

事前準備:
    pip install -r requirements.txt
"""

import os
import re
import time

import requests
import yfinance as yf
from bs4 import BeautifulSoup

WIKI_URL = "https://en.wikipedia.org/wiki/Nikkei_225"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "data")
PERIOD = "1y"


def fetch_nikkei225_tickers():
    """Wikipediaの日経225ページから、構成銘柄コード一覧を取得する"""
    response = requests.get(WIKI_URL, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    pattern = re.compile(r"^(.*?)\s*\(TYO:\s*(\d{4})\)")

    tickers = []
    for li in soup.find_all("li"):
        match = pattern.match(li.get_text().strip())
        if match:
            name = match.group(1).strip()
            code = match.group(2)
            tickers.append({"name": name, "code": code, "ticker": f"{code}.T"})

    return tickers


def save_price_csv(ticker, output_dir):
    """指定した銘柄の株価データを取得してCSVに保存する"""
    df = yf.download(ticker, period=PERIOD, progress=False)
    if df.empty:
        return False

    csv_path = os.path.join(output_dir, f"{ticker}.csv")
    df.to_csv(csv_path)
    return True


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    tickers = fetch_nikkei225_tickers()
    print(f"日経225の構成銘柄を {len(tickers)} 件取得しました")

    for i, item in enumerate(tickers, start=1):
        ticker = item["ticker"]
        print(f"[{i}/{len(tickers)}] {item['name']} ({ticker}) を取得中...")

        success = save_price_csv(ticker, OUTPUT_DIR)
        if not success:
            print(f"  -> データを取得できませんでした: {ticker}")

        time.sleep(0.5)  # サーバーに負荷をかけすぎないよう少し待つ

    print("完了しました")


if __name__ == "__main__":
    main()
