# ocr_module.py
from PIL import Image
from transformers import AutoModel, AutoTokenizer

# Load MiniCPM model once (avoid reloading for each call)
model = AutoModel.from_pretrained('openbmb/MiniCPM-V-2_6-int4', trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained('openbmb/MiniCPM-V-2_6-int4', trust_remote_code=True)
model.eval()

def run_ocr(image_path):
    prompt = (
        "Extract only the handwritten text from the image. "
        "Do not include any additional descriptions or irrelevant details—"
        "return just the text content as it appears in the image."
    )
    image = Image.open(image_path).convert("RGB")
    msgs = [{'role': 'user', 'content': [image, prompt]}]
    result = model.chat(image=None, msgs=msgs, tokenizer=tokenizer)
    return result




