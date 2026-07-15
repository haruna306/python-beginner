# Python Beginner

Python初心者向けサンプルです。

このリポジトリでは、

- VS Code
- Claude Code

を使いながら、
Pythonを少しずつ動かしていきます。

## セットアップ

サンプルによっては外部ライブラリ（pandas, yfinance など）を使用します。
以下の手順で仮想環境を作り、必要なライブラリをインストールしてください。

```bash
python3 -m venv venv
source venv/bin/activate  # Windowsの場合は venv\Scripts\activate
pip install -r requirements.txt
```

## サンプル

- Hello World（[samples/hello_world.py](samples/hello_world.py)）
- CSVデータ作成（[samples/create_csv.py](samples/create_csv.py)）
- パーフェクトオーダー抽出（[samples/perfect_order.py](samples/perfect_order.py)）
- ゴールデンクロス抽出（[samples/golden_cross.py](samples/golden_cross.py)）
