#detector/tracker.py
#import numpy as np
#try:
 #   from detector.sort import Sort
#except Exception:
  #  raise

#class TrackerWrapper:
 #   def __init__(self, max_age=30, min_hits=1):
  #      self.tracker = Sort(max_age=max_age, min_hits=min_hits)

   # def update(self, detections):
    #    if len(detections) == 0:
     #       dets = np.empty((0,5))
      #  else:
       #     dets = np.array(detections)
        #trackers = self.tracker.update(dets)
        #return trackers

# detector/tracker.py

import numpy as np
from detector.sort import Sort  # ✅ Import directly

class TrackerWrapper:
    def __init__(self, max_age=30, min_hits=1):
        # ✅ Create a Sort tracker with given parameters
        self.tracker = Sort(max_age=max_age, min_hits=min_hits)

    def update(self, detections):
        """
        detections: list of [x1, y1, x2, y2] bounding boxes
        returns: list of tracked objects with IDs
        """
        if len(detections) == 0:
            dets = np.empty((0, 4))
        else:
            dets = np.array(detections)

        # ✅ Update SORT tracker with current detections
        trackers = self.tracker.update(dets)
        return trackers