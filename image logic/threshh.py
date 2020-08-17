import cv2
import numpy as np

page = cv2.imread("bookpage.jpg")

graypage = cv2.cvtColor(page , cv2.COLOR_BGR2GRAY)

retval1 , threshold1 = cv2.threshold(page , 12 , 255 , cv2.THRESH_BINARY)
retval , threshold = cv2.threshold(graypage , 12 , 255 , cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(graypage , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 75 , 1)

# cv2.imshow("color thresh" , threshold1)
# cv2.imshow("gray thresh" , threshold)
cv2.imshow("gaus" , gaus)

cv2.waitKey(0)
cv2.destroyAllWindows()