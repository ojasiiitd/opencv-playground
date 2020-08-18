import cv2
import numpy as np

cap = cv2.VideoCapture(0)

face = cv2.imread("face.png" , 0)
h , w = face.shape

while True:
    _ , frame = cap.read()

    grayFrame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    
    res = cv2.matchTemplate(grayFrame , face , cv2.TM_CCOEFF_NORMED)
    thresh = 0.5
    loc = np.where(res >= thresh)

    cnt = 0
    for pt in zip(*loc[::-1]):
        print(pt)
        cv2.rectangle(frame , pt , (pt[0]+w  , pt[1]+h) , (0,255,0) , 1)
        cnt += 1
        if cnt >= 3:
            break

    cv2.imshow("faces" , frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()