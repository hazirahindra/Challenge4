# Importing the libraries 
import cv2
import numpy as np

# Reading image from folder where it is stored
img_input = cv2.imread('zira.jpg', cv2.IMREAD_UNCHANGED)
  
# Denoising of image saving it into dst image
dst = cv2.fastNlMeansDenoisingColored(img_input, None, 10, 10, 7, 15)
# img_input – Source Image Array
# None – Destination Image Array
# 10 – Size in pixels of the template patch that is used to compute weights.
# 10 - Size in pixels of the window that is used to compute a weighted average for the given pixel.
# 7 - Parameter regulating filter strength for luminance component.
# 15 - Same as above but for color components // Not used in a grayscale image.

# Display the images
cv2.imwrite('After.jpg',dst)

cv2.imshow('Before', img_input)
cv2.imshow('After', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()