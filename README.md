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

### 2. 仮想環境を作る

このプロジェクト専用のPython環境を作ります。

1. VS Codeでこのフォルダを開く
2. `Ctrl + Shift + P` を押す  
   Macの場合は `Command + Shift + P`
3. 検索欄に `Python: Create Environment` と入力して選択
4. `Venv` を選択
5. 使用するPythonを選択
6. `requirements.txt` を選択

作成が完了するまで、少し待ちます。

VS Codeの画面右下に `.venv` と表示されていれば、仮想環境が選択されています。

### 3. ライブラリを確認する

仮想環境の作成時に `requirements.txt` を選択すると、
必要なライブラリが自動的にインストールされます。

うまくインストールされなかった場合は、
VS Codeのターミナルで以下を実行してください。

```bash
python -m pip install -r requirements.txt
```

## サンプル

- Hello World（[samples/hello_world.py](samples/hello_world.py)）
- CSVデータ作成（[samples/create_csv.py](samples/create_csv.py)）
- パーフェクトオーダー抽出（[samples/perfect_order.py](samples/perfect_order.py)）
- ゴールデンクロス抽出（[samples/golden_cross.py](samples/golden_cross.py)）
