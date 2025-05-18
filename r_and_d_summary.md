# R&D Summary: Handwritten Text OCR Pipeline

## 🔍 OCR Tools and Models Used

- **Model**: `MiniCPM-V-2_6-int4` (OpenBMB)
- **Library**: Hugging Face Transformers
- **Why MiniCPM**: It’s a lightweight vision-language model fine-tuned for tasks like OCR, especially on low-resource or handwritten content.

---

## 🧪 Preprocessing Steps

- No preprocessing was applied in this pipeline.
- We tested the model directly on **raw handwritten note images**.
- The OCR accuracy was high without grayscale conversion, binarization, or skew correction.

---

## 🧼 Post-Processing Logic

Implemented in `clean_module.py`:
- Removed unnecessary special characters and symbols.
- Normalized extra whitespace and line breaks.
- Returned cleaned, structured text output.

---

## 📊 Accuracy Comparison: Raw vs Processed Images

- **Only raw images** were tested, since the model handled them well.
- Sample results were manually verified and deemed clean and readable.
- Preprocessing was skipped because it did not yield significant improvement.

---

## 🚧 Challenges & Solutions

| Challenge | Solution |
|----------|----------|
| Handwritten variation across images | Chose MiniCPM model, which generalizes well |
| Maintaining output quality without preprocessing | Relied on model's internal vision-language understanding |
| Need for clean structured text | Created custom text cleaning logic |
| Need for API access | Built FastAPI endpoint to serve predictions |

---

## 🌍 Generalization & Scaling

- The system is designed to handle **varied handwriting styles**.
- With the FastAPI interface, this can scale to large document batches.
- Potential future improvements:
  - Add support for multiple OCR backends
  - Include preprocessing switch (optional)
  - Batch queue/image uploads

---

## 🧪 Future Work

- Add benchmarking on standard handwriting OCR datasets
- Quantify improvement when preprocessing is optionally turned on
- Evaluate latency on GPU vs CPU deployment

---

