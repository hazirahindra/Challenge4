# Importing the libraries
import cv2 as cv

# Reading the image from the disk using cv2.imread() function
img_input = cv.imread('thumbprint.jpg', cv.IMREAD_UNCHANGED)

# Change the colour of the image 
img = cv.cvtColor(img_input, cv.COLOR_BGR2GRAY)

# Histogram equalization 
dst = cv.equalizeHist(img)

# display both picture before and after 
cv.imwrite('After.jpg', dst)

cv.imshow('Before', img_input)
cv.imshow('After', dst)

cv.waitKey(0)
cv.destroyAllWindows()
