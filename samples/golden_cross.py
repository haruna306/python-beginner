"""
5日線が20日線を直近5日以内に上抜いた(ゴールデンクロス)銘柄を抽出するサンプルスクリプト

事前準備:
    samples/create_csv.py を実行して株価CSVを用意しておくこと
"""

import glob
import os

import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
SHORT_WINDOW = 5
LONG_WINDOW = 20
LOOKBACK_DAYS = 5


def load_price_csv(csv_path):
    """create_csv.pyが保存したCSV(yfinance形式)を読み込む"""
    return pd.read_csv(csv_path, header=0, skiprows=[1, 2], index_col=0, parse_dates=True)


def has_golden_cross(df):
    """直近LOOKBACK_DAYS日以内に、短期線が長期線を上抜いたかどうかを判定する"""
    if len(df) < LONG_WINDOW + LOOKBACK_DAYS:
        return False

    short_ma = df["Close"].rolling(SHORT_WINDOW).mean()
    long_ma = df["Close"].rolling(LONG_WINDOW).mean()

    diff = short_ma - long_ma
    was_below_or_equal = diff.shift(1) <= 0
    is_above = diff > 0
    crossed = was_below_or_equal & is_above

    return bool(crossed.iloc[-LOOKBACK_DAYS:].any())


def main():
    csv_paths = sorted(glob.glob(os.path.join(DATA_DIR, "*.csv")))
    print(f"{len(csv_paths)} 件の銘柄データを確認します")

    result = []
    for csv_path in csv_paths:
        ticker = os.path.basename(csv_path).replace(".csv", "")
        df = load_price_csv(csv_path)

        if has_golden_cross(df):
            result.append(ticker)

    print(f"\nゴールデンクロス(直近{LOOKBACK_DAYS}日以内)の銘柄: {len(result)} 件")
    for ticker in result:
        print(f"  - {ticker}")


if __name__ == "__main__":
    main()
