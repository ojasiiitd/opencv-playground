import cv2
import numpy as np

img = cv2.imread('smartphone.jpeg' , cv2.IMREAD_COLOR)

cv2.line(img , (0,0) , (300,300) , (0,255,0) , 20)
cv2.rectangle(img , (300,50) , (400,400) , (0,0,255) , 10)
cv2.circle(img , (600,600) , 70 , (255,0,0) , 15)

points = np.array( [[10,5] , [90,80] , [140,560] , [50,300] , [400,100]] )
# points = points.reshape((-1,1,2))
cv2.polylines(img , [points] , True , (0,0,0) , 5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img , "iPhone 8S" , (1000,400) , font , 0.7 , (255,0,255) , 2)

cv2.imshow('image' , img)

cv2.waitKey(0)
cv2.destroyAllWindows()