import cv2
import numpy as np

img = cv2.imread('smartphone.jpeg' , cv2.IMREAD_GRAYSCALE)

cv2.imshow('iPhone' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()