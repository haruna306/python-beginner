# Python Beginner

Python初心者向けサンプルです。

このリポジトリでは、

- VS Code
- Claude Code

を使いながら、
Pythonを少しずつ動かしていきます。

## セットアップ

### 1. リポジトリをダウンロード

1. このリポジトリのページ右上の緑色の「Code」ボタンをクリック
2. 「Download ZIP」を選択してダウンロード
3. ダウンロードしたZIPファイルを展開（ダブルクリックで解凍）
4. 展開してできたフォルダをVS Codeで開く

### 2. ライブラリをインストール

サンプルによっては外部ライブラリ（pandas, yfinance など）を使用します。
VS Codeのターミナルで、以下を実行してください。

```bash
pip install -r requirements.txt
```

うまくいかない場合（`error: externally-managed-environment` と出る場合）は、以下を試してください。

```bash
pip install --break-system-packages -r requirements.txt
```

## サンプル

- Hello World（[samples/hello_world.py](samples/hello_world.py)）
- CSVデータ作成（[samples/create_csv.py](samples/create_csv.py)）
- パーフェクトオーダー抽出（[samples/perfect_order.py](samples/perfect_order.py)）
- ゴールデンクロス抽出（[samples/golden_cross.py](samples/golden_cross.py)）
