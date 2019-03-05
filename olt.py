import numpy as np 
import cv2 
from matplotlib import pyplot as plt 
  
# Image operation using thresholding 
img = cv2.imread('6.png') 
  
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
ret, thresh = cv2.threshold(gray, 0, 255, 
                            cv2.THRESH_BINARY_INV +
                            cv2.THRESH_OTSU) 
# cv2.imshow('image', thresh)
# cv2.waitKey(0)

# Noise removal using Morphological 
# closing operation 
kernel = np.ones((3, 3), np.uint8) 
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, 
                            kernel, iterations = 2) 
  
# Background area using Dialation 
bg = cv2.dilate(closing, kernel, iterations = 1) 
  
# Finding foreground area 
dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 0) 
ret, fg = cv2.threshold(dist_transform, 0.02
                        * dist_transform.max(), 255, 0) 
  
(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(cnts) != 0:
	# draw in blue the contours that were founded
	#cv2.drawContours(image, cnts, -1, 255, 3)

	#find the biggest area
	c = max(cnts, key = cv2.contourArea)

	x,y,w,h = cv2.boundingRect(c)
	# draw the book contour (in green)
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
	cv2.imshow("image", img)
	cv2.waitKey(0)