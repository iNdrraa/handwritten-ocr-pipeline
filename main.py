
# main.py
import os
from ocr_module import run_ocr
from clean_module import clean_text

def process_image(image_path, output_dir):
    print(f"Processing: {image_path}")
    raw_text = run_ocr(image_path)
    cleaned = clean_text(raw_text)

    base_name = os.path.splitext(os.path.basename(image_path))[0]
    raw_txt_path = os.path.join(output_dir, f"{base_name}_ocr.txt")
    clean_txt_path = os.path.join(output_dir, f"{base_name}_cleaned.txt")

    with open(raw_txt_path, "w", encoding="utf-8") as f:
        f.write(raw_text)
    with open(clean_txt_path, "w", encoding="utf-8") as f:
        f.write(cleaned)

    print(f"Saved raw OCR to: {raw_txt_path}")
    print(f"Saved cleaned text to: {clean_txt_path}")


if __name__ == "__main__":
    input_path = "images"      # folder or single image path
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    if os.path.isfile(input_path):
        process_image(input_path, output_dir)
    elif os.path.isdir(input_path):
        for filename in os.listdir(input_path):
            if filename.lower().endswith((".png", ".jpg", ".jpeg")):
                full_path = os.path.join(input_path, filename)
                process_image(full_path, output_dir)
    else:
        print("Input path is invalid.")
