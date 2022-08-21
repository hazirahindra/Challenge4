
# Importing the OpenCV, Numpy and Matplotlib libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
  
# Reading the image from the disk using cv2.imread() function
# Showing the original image using matplotlib library function plt.imshow()
img_input = cv2.imread('zira.jpeg')
# plt.imshow(img_input)
# plt.show()
  
# Apply kernel for sharpening
sharp_kernel = np.array([[0, -1, 0],
                    [-1, 5, -1],
                    [0, -1, 0]])
  
# Sharpeneded image is obtained using the variable sharp_img
# cv2.fliter2D() is the function used
# src is the source of image(here, img)
# ddepth is destination depth. -1 will mean output image will have same depth as input image
# kernel is used for specifying the kernel operation (here, sharp_kernel)
img_sharp = cv2.filter2D(src=img_input, ddepth=-1, kernel=sharp_kernel)
  
# Showing the sharpened image using matplotlib library function plt.imshow()
# plt.imshow(sharp_img)
# plt.show()

cv2.imwrite('After.jpg',img_sharp)

cv2.imshow('Before', img_input)
cv2.imshow('After - Image Sharpened', img_sharp)
cv2.waitKey(0)

# plt.imshow(img_input)
# plt.show()
# plt.imshow(img_sharp)
# plt.show()
# cv2.waitKey(0)