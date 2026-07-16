"""
5日・20日・60日移動平均線を使って「パーフェクトオーダー」(短期>中期>長期の上昇トレンド)
になっている銘柄を抽出するサンプルスクリプト

事前準備:
    samples/create_csv.py を実行して株価CSVを用意
"""

import glob
import os

import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
SHORT_WINDOW = 5
MID_WINDOW = 20
LONG_WINDOW = 60


def load_price_csv(csv_path):
    """create_csv.pyが保存したCSV(yfinance形式)を読み込む"""
    return pd.read_csv(csv_path, header=0, skiprows=[1, 2], index_col=0, parse_dates=True)


def is_rising(ma):
    """移動平均線の値が前日より大きい(上昇している)かどうかを判定する"""
    return ma.iloc[-1] > ma.iloc[-2]


def is_perfect_order(df):
    """短期>中期>長期の順に並び、かつ全ての線が前日より上昇しているかどうかを判定する"""
    if len(df) < LONG_WINDOW + 1:
        return False

    short_ma = df["Close"].rolling(SHORT_WINDOW).mean()
    mid_ma = df["Close"].rolling(MID_WINDOW).mean()
    long_ma = df["Close"].rolling(LONG_WINDOW).mean()

    order_ok = short_ma.iloc[-1] > mid_ma.iloc[-1] > long_ma.iloc[-1]
    rising_ok = is_rising(short_ma) and is_rising(mid_ma) and is_rising(long_ma)

    return order_ok and rising_ok


def main():
    csv_paths = sorted(glob.glob(os.path.join(DATA_DIR, "*.csv")))
    print(f"{len(csv_paths)} 件の銘柄データを確認します")

    result = []
    for csv_path in csv_paths:
        ticker = os.path.basename(csv_path).replace(".csv", "")
        df = load_price_csv(csv_path)

        if is_perfect_order(df):
            result.append(ticker)

    print(f"\nパーフェクトオーダー(上昇トレンド)の銘柄: {len(result)} 件")
    for ticker in result:
        print(f"  - {ticker}")


if __name__ == "__main__":
    main()
