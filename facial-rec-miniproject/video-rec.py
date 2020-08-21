import os
import cv2
import numpy as np
import face_recognition

REC_DIR = "recognized/"
TOLERANCE = 0.6
MODEL = "cnn"

cap = cv2.VideoCapture(0)

face_map = {}

while True:
    _ , frame = cap.read()

    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    
    face_loc = face_recognition.face_locations(gray , model=MODEL)
    face_enc = face_recognition.face_encodings(gray)

    if len(face_loc) == 0 :
        continue
    
    # recognized = False
    # for name in os.listdir(REC_DIR):

    
    # if not recognized:
    #     newName = input("New face detected! Please provide a name for the same: ")
    #     face_map[newName] = face_enc[0]
    #     cv2.imwrite(REC_DIR + newName + ".jpg" , frame)

    

    break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()