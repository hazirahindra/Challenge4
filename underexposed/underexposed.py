# Importing the libraries
import numpy as np
import cv2 as cv

# Reading the image from the disk using cv2.imread() function
img_input = cv.imread('thumbprint.jpg')

# Change the colour of the image 
img_yuv = cv.cvtColor(img_input, cv.COLOR_BGR2YUV)

# equalize the histogram of the Y channel
img_yuv[:,:,0] = cv.equalizeHist(img_yuv[:,:,0])

# convert the YUV image back to RGB format
img_output = cv.cvtColor(img_yuv, cv.COLOR_YUV2BGR)

# display both picture before and after
cv.imwrite('After.jpg', img_output)

cv.imshow('Before', img_input)
cv.imshow('After - Histogram equalized', img_output)
cv.waitKey(0)