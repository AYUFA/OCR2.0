# OCR2.0

このリポジトリには、FastAPI と小さな JavaScript フロントエンドを用いた
シンプルな OCR デモが含まれています。バックエンドでは画像を受け取り
Tesseract OCR を実行して、検出したテキストと注釈付き画像を返す
`/ocr` API を提供します。

## デモの実行

1. Python の依存関係をインストールします:

   ```bash
   pip install -r backend/requirements.txt
   ```

   さらに Tesseract 本体もシステムにインストールしておく必要があります。

2. リポジトリのルートで `./start_dev.sh` を実行すると、バックエンド
   (port 8000) とフロントエンド (port 3000) が同時に起動します。終了する
   には `Ctrl+C` を押してください。

3. ブラウザで `http://localhost:3000` を開き、画像を選択して
   `OCR 実行` ボタンを押すと結果が表示されます。

注釈付き画像とアップロードされたファイルはそれぞれ
`backend/annotated` と `backend/uploads` に保存されます。

---

## uvicorn が認識されない場合

`"uvicorn" は、内部コマンドまたは外部コマンド、操作可能なプログラムまたはバッチ ファイルとして認識されていません。` というエラーは、uvicorn がインストールされていないか、仮想環境が有効になっていないことを意味します。

### ステップ 1: 仮想環境を有効化

フォルダ構成が次のようになっている場合を例とします。

```text
OCR2.0/
  ├─ backend/
  │   └─ main.py
  └─ venv/
```

Windows なら以下を実行して仮想環境を有効化します。

```cmd
..\venv\Scripts\activate
```

`(venv)` という表示が出れば成功です。

### ステップ 2: uvicorn が入っているか確認

```bash
pip list
```

`uvicorn` が表示されない場合はインストールします。

```bash
pip install uvicorn[standard]
```

### ステップ 3: サーバーを起動

```bash
uvicorn main:app --reload
```

`http://localhost:8000` でアプリが起動し、Swagger UI は `http://localhost:8000/docs` からアクセスできます。

### 仮想環境がない場合

```bash
cd OCR2.0
python -m venv venv
.\venv\Scripts\activate
pip install -r backend/requirements.txt
```

仮想環境を使わずにグローバルへ `uvicorn` をインストールすることもできますが、可能であれば仮想環境を利用することを推奨します。
