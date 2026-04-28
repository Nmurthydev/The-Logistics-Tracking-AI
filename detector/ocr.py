#Coded by @nmurthydev 
# detector/ocr.py
import pytesseract
import cv2
import easyocr

_reader = None

def read_plate(img):
    """Attempts to read text from the crop (BGR numpy image) using pytesseract first, then easyocr."""
    global _reader
    try:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    except Exception:
        return ""
    try:
        resized = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    except Exception:
        resized = gray
    try:
        blur = cv2.GaussianBlur(resized, (3,3), 0)
        _, th = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    except Exception:
        th = resized
    try:
        txt = pytesseract.image_to_string(th, config='--psm 7')
        txt = txt.strip()
        if txt and len(txt) >= 3:
            return txt.replace('\n', ' ').strip()
    except Exception:
        pass
    try:
        if _reader is None:
            _reader = easyocr.Reader(['en'], gpu=False)
        res = _reader.readtext(img)
        if res:
            return ' '.join([r[1] for r in res]).strip()
    except Exception:
        pass
    return ""
