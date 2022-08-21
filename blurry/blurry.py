
# Importing the OpenCV, Numpy and Matplotlib libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
  
img_input = cv2.imread('zira.jpeg')
  
# Apply kernel for sharpening
sharp_kernel = np.array([[0, -1, 0],
                    [-1, 5, -1],
                    [0, -1, 0]])
  
img_sharp = cv2.filter2D(src=img_input, ddepth=-1, kernel=sharp_kernel)


cv2.imwrite('After.jpg',img_sharp)

cv2.imshow('Before', img_input)
cv2.imshow('After - Image Sharpened', img_sharp)
cv2.waitKey(0)
