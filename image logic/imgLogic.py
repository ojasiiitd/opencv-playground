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
roi = img1[600:600+rows , 600:600+cols] # bigger image
imgLogogray = cv2.cvtColor(imgLogo , cv2.COLOR_BGR2GRAY) # smaller image to be overlayed
# cv2.imshow("grayed" , imgLogogray)

ret , mask = cv2.threshold(imgLogogray , 100 , 255 , cv2.THRESH_BINARY) # >30 = black , <30 = white
# cv2.imshow("mask" , mask)
mask_inv = cv2.bitwise_not(mask)
# cv2.imshow("mask inv" , mask_inv)

imgLogo_bg = cv2.bitwise_and(roi , roi , mask=mask_inv)
# cv2.imshow("imgLogo_bg" , imgLogo_bg)
img1_fg = cv2.bitwise_and(imgLogo , imgLogo , mask=mask)
# cv2.imshow("img1_fg" , img1_fg)

dst = cv2.add(img1_fg , imgLogo_bg) # or img1_fg + imgLogo_bg
# cv2.imshow("dst" , dst)

img1[600:600+rows , 600:600+cols] = dst
cv2.imshow("final image" , img1[200:800 , 300:1000])

cv2.waitKey(0)
cv2.destroyAllWindows()