# OCR2.0

This repository contains a simple OCR demo using FastAPI and a small
JavaScript frontend. The backend provides an `/ocr` API that accepts an
image, runs Tesseract OCR, and returns detected text together with an
annotated image.

## Running the demo

1. Install Python dependencies:

   ```bash
   pip install -r backend/requirements.txt
   ```

   Tesseract itself must also be installed on your system.

2. Start the API server from the `backend` directory:

   ```bash
   uvicorn main:app --reload
   ```

3. Open `frontend/index.html` in your browser. Press the `OCR 実行` button
   after selecting an image to see the result.

The annotated images and uploads are stored under `backend/annotated` and
`backend/uploads` respectively.
