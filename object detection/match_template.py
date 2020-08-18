import cv2
import numpy as np

img_bgr = cv2.imread("main img.jpg" , cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_bgr , cv2.COLOR_BGR2GRAY)

template = cv2.imread("template.jpg" , 0) # what does 0 mean?
h , w = template.shape

res = cv2.matchTemplate(img_gray , template , cv2.TM_CCOEFF_NORMED)
thresh = 0.9
loc = np.where(res >= thresh)

# zip(*list) ?!?
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr , pt , (pt[0]+w , pt[1]+h) , (0,230,40) , 1)

cv2.imshow("detected" , img_bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()