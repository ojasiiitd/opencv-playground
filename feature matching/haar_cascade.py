import cv2
import numpy as np

# https://github.com/opencv/opencv/tree/master/data/haarcascades

face_casc = cv2.CascadeClassifier("haar_face.xml")
eye_casc = cv2.CascadeClassifier("haar_eye.xml")
smile_casc = cv2.CascadeClassifier("haar_smile.xml")

cap = cv2.VideoCapture(0)

while True:
    _ , frame = cap.read()
    gray  = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    faces = face_casc.detectMultiScale(gray)
    eyes = eye_casc.detectMultiScale(gray , 1.5)
    smiles = smile_casc.detectMultiScale(gray , 1.25)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame , (x,y) , (x+w , y+h) , (0,255,0) , 2)

    for (x,y,w,h) in eyes:
        cv2.rectangle(frame , (x,y) , (x+w , y+h) , (255,0,0) , 2)

    for (x,y,w,h) in smiles[:2]:
        cv2.rectangle(frame , (x,y) , (x+w , y+h) , (0,0,255) , 2)
        
    cv2.imshow("frame" , frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()