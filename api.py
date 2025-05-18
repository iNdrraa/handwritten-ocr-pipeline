# api.py
from fastapi import FastAPI, File, UploadFile
from PIL import Image
from io import BytesIO
from ocr_module import run_ocr
from clean_module import clean_text

app = FastAPI()

@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(BytesIO(image_bytes))
    image.save("temp_image.png")  # Save temporarily for your run_ocr (which reads from path)
    raw_text = run_ocr("temp_image.png")
    cleaned = clean_text(raw_text)
    return {"raw_text": raw_text, "cleaned_text": cleaned}
