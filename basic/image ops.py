import cv2
import numpy as np

img = cv2.imread('smartphone.jpeg' , cv2.IMREAD_COLOR)
pixel = img[10][400]

# Region of Image (ROI)
screen = img[100:200 , 500:700]
img[300:400 , 200:400] = screen # copy pase

cv2.imshow('image' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()