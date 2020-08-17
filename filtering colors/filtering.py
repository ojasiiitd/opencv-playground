import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _ , frame = cap.read()
    
    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)

    # hsv hue value
    low_orange = np.array([12,90,0])
    up_orange = np.array([70,160,255])

    mask = cv2.inRange(hsv , low_orange , up_orange)
    # cv2.imshow("mask" , mask)
    res = cv2.bitwise_and(frame , frame , mask=mask) # where maskValue == 1, only in those areas bitwise and is applied

    # removing noise (blur techniques)
    blurBlock = 5
    kernel = np.ones((blurBlock,blurBlock))/(blurBlock**2)
    smoothed = cv2.filter2D(res , -1 , kernel)

    blur = cv2.GaussianBlur(res , (blurBlock,blurBlock) , 0)

    median = cv2.medianBlur(res , blurBlock)

    bilat = cv2.bilateralFilter(res , blurBlock , 75 , 75)

    # cv2.imshow("smooth blur" , smoothed)
    # cv2.imshow("guass blur" , blur)
    cv2.imshow("median blur" , median)
    # cv2.imshow("bilat blur" , bilat)
    
    # exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()