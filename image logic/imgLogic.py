import cv2
import numpy as np

img1 = cv2.imread("img1.png")
img2 = cv2.imread("img2.png")

add = img1 + img2
add = cv2.add(img1 , img2)
# cv2.imshow("added" , add)

weighted = cv2.addWeighted(img1 , 0.4 , img2 , 0.3 , 0)
# cv2.imshow("added" , weighted)

imgLogo = cv2.imread("yt.png")
rows , cols , channels = imgLogo.shape
roi = img1[600:600+rows , 600:600+cols]
img2gray = cv2.cvtColor(imgLogo , cv2.COLOR_BGR2GRAY)

ret , mask = cv2.threshold(img2gray , 130 , 150 , cv2.THRESH_BINARY)
# cv2.imshow("masked" , mask)

mask_inv = cv2.bitwise_not(mask)
imgLogo_bg = cv2.bitwise_and(roi , roi , mask=mask_inv)
img1_fg = cv2.bitwise_and(imgLogo , imgLogo , mask=mask)

dst = cv2.add(imgLogo_bg , img1_fg)
img1[600:600+rows , 600:600+cols] = dst

cv2.imshow("res" , img1)

cv2.waitKey(0)
cv2.destroyAllWindows()