import numpy as np
import cv2 as cv

img_input = cv.imread('thumbprint.jpg')
img_yuv = cv.cvtColor(img_input, cv.COLOR_BGR2YUV)

# equalize the histogram of the Y channel
img_yuv[:,:,0] = cv.equalizeHist(img_yuv[:,:,0])

# convert the YUV image back to RGB format
img_output = cv.cvtColor(img_yuv, cv.COLOR_YUV2BGR)

cv.imwrite('After.jpg', img_output)

cv.imshow('Before', img_input)
cv.imshow('After - Histogram equalized', img_output)
cv.waitKey(0)