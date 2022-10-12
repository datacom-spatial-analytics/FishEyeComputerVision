import cv2
import numpy as np

import json

# read image
img = cv2.imread('images/Lunch2_000001.jpg')


KitchenBench1 = [600, 1245, 350, 510]
KitchenBench2 = [1125, 1237, 347, 479]
WorkBench1 = [273, 351, 644, 288]
WorkBench2 = [625, 280, 321, 693]
WorkBench3 = [1104, 211, 688, 413]

ROIS = [[600, 1245, 510, 350], [1125, 1237, 479, 347], [273, 351, 288, 644], [625, 280, 321, 693], [1104, 211, 413, 688]]
ROI_Names = ["KitchenBench 1", "KitchenBench 2", "WorkBench 1", "WorkBench 2", "WorkBench 3"]

# Point
Point = [50, 1350]


def DetectOverlap(Boundb, Point):

   IsOccupied = False

   # If top-left point corner is inside the bounding box
   if Boundb[0] < Point[0] and Boundb[1] < Point[1]:

      # If bottom-right point corner is inside the bounding box
      if Point[0] + 1 < Boundb[0] + Boundb[3] \
              and Point[1] + 1 < Boundb[1] + Boundb[2]:
         #print('The point is in BB')
         IsOccupied = True
         # (IsOccupied)
      else:
         #  pass#print('Some part of the box is outside the bounding box.')
         IsOccupied = True
   else:
      pass#print('The point is not in the BB')

   return IsOccupied




#DetectOverlap(KitchenBench1, Point)

# Opening JSON file
f = open('Dataset2.json')

# returns JSON object as
# a dictionary
Points = json.load(f)
iteration = 0

# Iterating through the json
# list
for Roi in ROIS:

   Bool_Detected = False

   for Point in Points:

      Detect = DetectOverlap(Roi, Point)
      #print("ROI: " + str(Roi) + " Point: " + str(Point) + " Is Detected: " + str(Detect))
      if Detect == True:
            Bool_Detected = True


   if Bool_Detected == True:
      print(str(ROI_Names[iteration]) + " region is occupied")
   else:
      print(str(ROI_Names[iteration]) + " This region is not occupied")

   iteration = iteration + 1


# Closing file
f.close()

for i in ROIS:
   x,y,w,h = i
   cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)


imS = cv2.resize(img, (600, 600))
cv2.imshow("Img", imS)
cv2.waitKey(0)
cv2.destroyAllWindows()