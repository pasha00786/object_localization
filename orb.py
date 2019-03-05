import cv2
import numpy as np
 
roi = cv2.imread("hima.png")
x = 0
y = 0
height, width, channels = roi.shape

hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])
roi_hist = cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
 
term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
 
while True:
    frame = cv2.imread('t.png')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

    _, track_window = cv2.meanShift(mask, (x, y, width, height), term_criteria)
    x, y, w, h = track_window
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)

    cv2.imshow("Mask", mask)
    cv2.imshow("Frame", frame)
    cv2.imshow('lookup', roi)

    key = cv2.waitKey(60)
    if key == 27:
        break
cv2.destroyAllWindows()