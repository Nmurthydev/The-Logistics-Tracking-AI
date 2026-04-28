#Coded by @nmurthydev 

 # sort.py - Pure Python SORT tracker (Simple Online Realtime Tracking)
#import numpy as np
#from collections import deque

#class Sort:
    #def __init__(self, max_age=5, min_hits=1):
     #   """
      #  max_age: number of frames to keep a lost track alive
       # min_hits: minimum detections before track is confirmed
        #"""
        #self.trackers = []
        #self.next_id = 1
        #self.max_age = max_age
        #self.min_hits = min_hits

    #def update(self, detections):
        #"""
        #detections: list of [x1, y1, x2, y2] bounding boxes
        #returns: list of tracked objects with IDs
        #"""
        #updated = []
        #for det in detections:
          #  updated.append({
           #     "id": self.next_id,
            #    "bbox": det
            #})
            #self.next_id += 1
        # updated
    
    # detector/sort.py
import numpy as np
from collections import deque

class Sort:
    def __init__(self, max_age=5, min_hits=1):
        self.trackers = []
        self.next_id = 1
        self.max_age = max_age
        self.min_hits = min_hits

    def update(self, detections):
        """
        detections: list of [x1, y1, x2, y2]
        returns: list of [x1, y1, x2, y2, id]
        """
        updated = []
        for det in detections:
            x1, y1, x2, y2 = det[:4]
            updated.append([x1, y1, x2, y2, self.next_id])
            self.next_id += 1
        return updated