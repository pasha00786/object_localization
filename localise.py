import pandas as pd
import numpy as np
import cv2

# data = pd.read_csv('./test.csv')
# data = data['image_name']
#for i in tqdm(range(len(data))):
#reading the image 
path = './test/'
src = 'JPEG_20160622_110649_1000527459853.png'
image = cv2.imread('6.png')
edged = cv2.Canny(image, 10, 250)
# cv2.imshow("Edges", edged)
# cv2.waitKey(0)


#applying closing function 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
# cv2.imshow("Closed", closed)
# cv2.waitKey(0)

#finding_contours 
(cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(cnts) != 0:
	# draw in blue the contours that were founded
	#cv2.drawContours(image, cnts, -1, 255, 3)

	#find the biggest area
	c = max(cnts, key = cv2.contourArea)

	x,y,w,h = cv2.boundingRect(c)
	# draw the book contour (in green)
	cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
	cv2.imshow("image", image)
	cv2.waitKey(0)
	# cv2.imwrite('test_output/'+src, image)
# 	row = [src, x, x+w, y, y+h]
# 	#Writing to output file
# 	with open('result.csv', 'a') as csvFile:
# 		writer = csv.writer(csvFile)
# 		writer.writerow(row)
# 	csvFile.close()

# error = [src, 0, 640, 0, 480]
# with open('result.csv', 'a') as csvFile:
# 	writer = csv.writer(csvFile)
# 	writer.writerow(error)
# csvFile.close()