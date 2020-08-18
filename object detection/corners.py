import cv2
import numpy as np

img = cv2.imread("corners_sent.jpg")
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray , 1000 , 0.15 , 10)

for corner in corners:
    x , y = corner.ravel()
    cv2.circle(img , (x,y) , 3 , (0,255,0) , 2)

cv2.imshow("corner" , img)

cv2.waitKey(0)
cv2.destroyAllWindows()