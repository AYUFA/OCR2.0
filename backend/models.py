from pydantic import BaseModel
from typing import List

class OCRBox(BaseModel):
    text: str
    conf: int
    x: int; y: int; w: int; h: int
    color: str

class OCRResult(BaseModel):
    text: str
    boxes: List[OCRBox]
    annotated_url: str
