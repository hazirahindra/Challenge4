import cv2 as cv
import matplotlib.pyplot as plt

img_input = cv.imread('thumbprint.jpg', cv.IMREAD_UNCHANGED)

img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

dst = cv.equalizeHist(img)

cv.imwrite('After.jpg', dst)

# display the images
cv.imshow('Before', img_input)
cv.imshow('After', dst)

cv.waitKey(0)
cv.destroyAllWindows()
