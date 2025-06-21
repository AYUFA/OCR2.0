from PIL import Image, ImageDraw, ImageOps
import pytesseract
from pytesseract import Output
from models import OCRBox, OCRResult
import os

def _color(conf: int) -> str:
    if conf < 50:  return "red"
    if conf < 80:  return "orange"
    if conf < 90:  return "yellow"
    return "green"

def run_ocr(img_path: str, annotated_dir: str, file_id: str) -> OCRResult:
    img = Image.open(img_path)
    img = ImageOps.exif_transpose(img)          # 画像の回転補正
    data = pytesseract.image_to_data(img, lang="jpn", output_type=Output.DICT)

    draw = ImageDraw.Draw(img)
    boxes: list[OCRBox] = []
    for i in range(len(data["text"])):
        conf = int(data["conf"][i])
        if conf <= 0 or not data["text"][i].strip():
            continue
        x, y, w, h = map(int, (data["left"][i], data["top"][i], data["width"][i], data["height"][i]))
        color = _color(conf)
        draw.rectangle([(x, y), (x + w, y + h)], outline=color, width=2)
        draw.text((x, y - 12), f"{conf}%", fill=color)
        boxes.append(OCRBox(text=data["text"][i], conf=conf, x=x, y=y, w=w, h=h, color=color))

    annotated_name = f"{file_id}_annotated.png"
    annotated_path = os.path.join(annotated_dir, annotated_name)
    img.save(annotated_path)
    img.close()
    try:
        os.remove(img_path)
    except OSError:
        pass

    full_text = " ".join([b.text for b in boxes])
    return OCRResult(
        text=full_text,
        boxes=boxes,
        annotated_url=f"/annotated/{annotated_name}"
    )
