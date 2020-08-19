import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("foreground.png")
# img = cv2.imread("fg_sent.jpg")
mask = np.zeros(img.shape[:2] , np.uint8)

bgModel = np.zeros((1,65) , np.float64)
fgModel = np.zeros((1,65) , np.float64)

# cv2.rectangle(img , (200,15) , (250,400) , (0,255,0), thickness=2)
# cv2.imshow("rectChekc" , img)
rect = (200, 15 , 250 , 400)

cv2.grabCut(img , mask , rect , bgModel , fgModel , 5 , cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2) | (mask==0) , 0 , 1).astype('uint8')
img = img * mask2[:,:,np.newaxis]

# plt.imshow(img)
# plt.colorbar()
# plt.show()
cv2.imshow("grabbed" , img)

cv2.waitKey(0)
cv2.destroyAllWindows()