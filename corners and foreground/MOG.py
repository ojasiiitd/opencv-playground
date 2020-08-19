import cv2
import numpy as np

cap = cv2.VideoCapture("people-walking.mp4")

fgbgKNN = cv2.createBackgroundSubtractorKNN()
fgbgMOG = cv2.createBackgroundSubtractorMOG2()

while True:
    _ , frame = cap.read()
    if not _ :
        break

    fgmaskKNN = fgbgKNN.apply(frame)
    fgmaskMOG = fgbgMOG.apply(frame)

    cv2.imshow("KNN" , fgmaskKNN)
    cv2.imshow("MOG" , fgmaskMOG)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()