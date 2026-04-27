# Logistics AI Tracking 🚚

**Logistics-AI-Tracking** is a full-stack AI-based logistics vehicle tracking system built with Python, Flask, and YOLOv8.
It detects vehicles in surveillance video, extracts number plates using OCR, and shows their **last known location** based on the camera that captured them.

## Quick start (local run)

1. Create & activate a virtualenv:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install Python deps:
   ```
   pip install -r requirements.txt
   ```
3. Install system Tesseract (Ubuntu):
   ```
   sudo apt-get update && sudo apt-get install -y tesseract-ocr
   ```
4. Download the YOLOv8 model (script included):
   ```
   python download_model.py
   ```
5. Run the server:
   ```
   python app.py
   ```
6. Open http://localhost:5000

## Notes
- The zip does **not** include the YOLO model file due to environment restrictions. Use `python download_model.py` to fetch it automatically.
- Author: Simha6776
- License: MIT
