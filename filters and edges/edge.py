import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _ , frame = cap.read()

    cv2.imshow("org" , frame)

    # gradient and edge techniques
    
    # laplate = cv2.Laplacian(frame , cv2.CV_64F)
    # sobelx = cv2.Sobel(frame , cv2.CV_64F , 1 , 0 , ksize=5)
    # sobely = cv2.Sobel(frame , cv2.CV_64F , 0 , 1 , ksize=5)
    edge = cv2.Canny(frame , 90 , 90) # more imp edges, threshold = big

    # cv2.imshow("laplated" , laplate)
    # cv2.imshow("sobel x" , sobelx)
    # cv2.imshow("sobel y" , sobely)
    cv2.imshow("edges" , edge)

    # exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()