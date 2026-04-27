# download_model.py
# Script to download yolov8n.pt model using ultralytics helper.
# Run this after installing dependencies. This will download the model to the project root.

try:
    from ultralytics.yolo.utils.downloads import attempt_download
except Exception:
    # fallback if ultralytics path changes
    try:
        from ultralytics.utils import download as attempt_download
    except Exception:
        attempt_download = None

MODEL = 'yolov8n.pt'

if attempt_download is None:
    print('Automatic downloader not available. Please install ultralytics and download yolov8n.pt manually:')
    print('https://github.com/ultralytics/ultralytics/releases')
else:
    print('Downloading', MODEL)
    attempt_download(MODEL)
    print('Downloaded', MODEL)
