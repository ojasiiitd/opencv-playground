import cv2
import numpy as np

cap = cv2.VideoCapture("people-walking.mp4")

fgbg = cv2.createBackgroundSubtractorMOG2()
# cv2.createBackgroundSubtractorKNN()

while True:
    _ , frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow("org" , frame)
    cv2.imshow("fg" , fgmask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()