from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from ocr_engine import run_ocr
from models import OCRResult
import uuid, os, shutil

app = FastAPI(title="OCR API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

UPLOAD_DIR = "uploads"
ANNOTATED_DIR = "annotated"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(ANNOTATED_DIR, exist_ok=True)

@app.post("/ocr", response_model=OCRResult)
async def ocr(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    ext = os.path.splitext(file.filename)[1]
    saved_path = f"{UPLOAD_DIR}/{file_id}{ext}"
    with open(saved_path, "wb") as buf:
        shutil.copyfileobj(file.file, buf)

    result = run_ocr(saved_path, annotated_dir=ANNOTATED_DIR, file_id=file_id)
    return result

@app.get("/annotated/{image_name}")
def get_annotated(image_name: str):
    return FileResponse(f"{ANNOTATED_DIR}/{image_name}")
