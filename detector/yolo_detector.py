# detector/yolo_detector.py
#from ultralytics import YOLO
#import cv2

#class YOLODetector:
    #def __init__(self, model_path="yolov8n.pt", device=None, conf=0.4):
      #  # device None => auto (cpu or cuda if torch detects GPU)
       # self.model = YOLO(model_path)
        #self.conf = conf
        #try:
           # self.model.fuse()
        #except Exception:
           # pass
        #self.class_names = self.model.names

    #def detect(self, frame):
     #   # frame: numpy BGR image from cv2
      #  results = self.model(frame, imgsz=640, conf=self.conf, verbose=False)
       # detections = []
        #for res in results:
         #   boxes = getattr(res, 'boxes', None)
           # if boxes is None:
           #     continue
            #for box in boxes:
             #   cls = int(box.cls[0])
              #  conf = float(box.conf[0])
               # x1,y1,x2,y2 = map(float, box.xyxy[0])
                #w = x2 - x1; h = y2 - y1
                #detections.append({
                 #   "class_id": cls,
                  #  "class_name": self.class_names.get(cls, str(cls)),
                   # "conf": conf,
                    #"bbox": [x1, y1, w, h]
                #})
        #return detections
    
# detector/yolo_detector.py
# detector/yolo_detector.py
from ultralytics import YOLO
import cv2

class YOLODetector:
    def __init__(self,
                 vehicle_model_path="yolov8n.pt",
                 plate_model_path="license_plate_detector.pt",
                 conf=0.4):

        # Load vehicle detector
        self.vehicle_model = YOLO(vehicle_model_path)

        # Load number plate detector
        self.plate_model = YOLO(plate_model_path)

        self.vehicle_conf = conf
        self.plate_conf = 0.3

        self.vehicle_names = self.vehicle_model.names

    def detect_vehicles(self, frame):
        results = self.vehicle_model(
            frame, imgsz=640, conf=self.vehicle_conf, verbose=False
        )
        vehicles = []
        for res in results:
            for box in res.boxes:
                cls = int(box.cls[0])
                name = self.vehicle_names.get(cls, "")
                if name.lower() in ["car","truck","bus","motorbike","van","bike"]:
                    x1,y1,x2,y2 = map(int, box.xyxy[0])
                    vehicles.append((x1,y1,x2,y2))
        return vehicles

    def detect_plates(self, vehicle_crop):
        results = self.plate_model(
            vehicle_crop, imgsz=320, conf=self.plate_conf, verbose=False
        )
        plates = []
        for res in results:
            for box in res.boxes:
                x1,y1,x2,y2 = map(int, box.xyxy[0])
                plates.append((x1,y1,x2,y2))
        return plates