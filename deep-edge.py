import cv2
import numpy as np


class CropLayer(object):
    def __init__(self, params, blobs):
        self.xstart = 0
        self.xend = 0
        self.ystart = 0
        self.yend = 0
 
    # Our layer receives two inputs. We need to crop the first input blob
    # to match a shape of the second one (keeping batch size and number of channels)
    def getMemoryShapes(self, inputs):
        inputShape, targetShape = inputs[0], inputs[1]
        batchSize, numChannels = inputShape[0], inputShape[1]
        height, width = targetShape[2], targetShape[3]
 
        self.ystart = (inputShape[2] - targetShape[2]) // 2
        self.xstart = (inputShape[3] - targetShape[3]) // 2
        self.yend = self.ystart + height
        self.xend = self.xstart + width
 
        return [[batchSize, numChannels, height, width]]
 
    def forward(self, inputs):
        return [inputs[0][:,:,self.ystart:self.yend,self.xstart:self.xend]]

cv2.dnn_registerLayer('Crop', CropLayer)

frame = cv2.imread('2.png')

net = cv2.dnn.readNet('deploy.prototxt', 'hed_pretrained_bsds.caffemodel')

inp = cv2.dnn.blobFromImage(frame, scalefactor=1.0, size=(640, 480), mean=(104.00698793, 116.66876762, 122.67891434), swapRB=False, crop=False)

net.setInput(inp)
out = net.forward()
out = out[0, 0]
out = cv2.resize(out, (frame.shape[1], frame.shape[0]))
out = 255 * out
out = out.astype(np.uint8)
# out=cv2.cvtColor(out,cv2.COLOR_GRAY2BGR)
# cv.imshow('kWinName',out)
# cv.waitKey(0)

#applying closing function 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(out, cv2.MORPH_CLOSE, kernel)
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
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("image", frame)
    cv2.waitKey(0)