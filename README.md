# Handwritten Text Extraction & OCR Processing Pipeline

This project extracts handwritten text from images using a transformer-based OCR model (MiniCPM).  
It processes handwritten notes to produce raw and cleaned text outputs without explicit image preprocessing.

---

## Project Structure

- `images/` — Input handwritten note images (e.g., `.png`, `.jpg`)
- `outputs/` — Generated text files from OCR and cleaned output
- `ocr_module.py` — Loads MiniCPM model and runs OCR on images
- `clean_module.py` — Cleans and structures raw OCR text
- `main.py` — Batch processing script for images in a folder or single image
- `api.py` — FastAPI app providing an OCR endpoint for image uploads
- `requirements.txt` — Required Python packages

---

## Setup Instructions

1. **Clone the repo:**
   ```bash
   git clone https://github.com/your-username/handwritten-ocr-pipeline.git
   cd handwritten-ocr-pipeline
