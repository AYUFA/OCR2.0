# OCR2.0

このリポジトリには、FastAPI と小さな JavaScript フロントエンドを使用したシンプルな OCR デモが含まれています。バックエンドでは画像を受け取り Tesseract OCR を実行し、検出したテキストと注釈付き画像を返す `/ocr` API を提供します。

## デモの実行方法

1. Python の依存関係をインストールします:

   ```bash
   pip install -r backend/requirements.txt
   ```

   Tesseract 本体もシステムにインストールされている必要があります。

2. `backend` ディレクトリから API サーバーを起動します:

   ```bash
   uvicorn main:app --reload
   ```

3. ブラウザで `frontend/index.html` を開きます。画像を選択した後に `OCR 実行` ボタンを押すと結果が表示されます。

注釈付き画像とアップロードされた画像は、それぞれ `backend/annotated` と `backend/uploads` に保存されます。
