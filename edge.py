import cv2
import numpy as np

# cap = cv2.VideoCapture(0)


frame = cv2.imread('tee.png')
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lower_red = np.array([30,150,50])
upper_red = np.array([255,255,180])

mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(frame,frame, mask= mask)

cv2.imshow('Original',frame)
edges = cv2.Canny(frame,100,200)
# cv2.imshow('Edges',edges)
(cnts, _) = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(cnts) != 0:
    # draw in blue the contours that were founded
    #cv2.drawContours(image, cnts, -1, 255, 3)

    #find the biggest area
    c = max(cnts, key = cv2.contourArea)

    x,y,w,h = cv2.boundingRect(c)
    # draw the book contour (in green)
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("image", frame)
    cv2.waitKey(0)
    # cv2.imwrite('test_output/'+src, image)
#   row = [src, x, x+w, y, y+h]
#   #Writing to output file
#   with open('result.csv', 'a') as csvFile:
#       writer = csv.writer(csvFile)
#       writer.writerow(row)
#   csvFile.close()

# error = [src, 0, 640, 0, 480]
# with open('result.csv', 'a') as csvFile:
#   writer = csv.writer(csvFile)
#   writer.writerow(error)
# csvFile.close()
