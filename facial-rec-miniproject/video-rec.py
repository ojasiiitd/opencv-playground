import os
import time
import cv2
import numpy as np
import face_recognition

REC_DIR = "recognized/"
TOLERANCE = 0.6
MODEL = "hog"

cap = cv2.VideoCapture(0)

face_map = {}

while True:
    startFrame = time.time()
    
    _ , frame = cap.read()

    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    
    face_loc = face_recognition.face_locations(gray , model=MODEL)
    if len(face_loc) == 0 :
        continue

    face_enc = face_recognition.face_encodings(frame)

    recognized = False
    for cur_encoding , location in zip(face_enc , face_loc):
        results = face_recognition.compare_faces(list(face_map.values()) , cur_encoding , TOLERANCE)

        if True in results:
            recognized = True
            top_left = (location[3] , location[0])
            bot_right = (location[1] , location[2])
            
            cv2.rectangle(frame , top_left , bot_right , (0,255,0) , 3)
            cv2.putText(frame , "REC_FACE" , (top_left[0]-10 , top_left[1]-10) , cv2.FONT_HERSHEY_PLAIN , 3 , (0,0,255) , 2)
            cv2.imshow("Frame" , frame)

    if not recognized:
        newName = input("New face detected! Please provide a name for the same: ")
        face_map[newName] = face_enc[0]
        cv2.imwrite(REC_DIR + newName + ".jpg" , frame[face_loc[0][0]-60:face_loc[0][2]+60 , face_loc[0][3]-60:face_loc[0][1]+60])

    # cv2.rectangle(frame , top_left , bot_right , (0,255,0) , 3)
    # cv2.imshow("the Face" , frame[face_loc[0][0]-60:face_loc[0][2]+60 , face_loc[0][3]-60:face_loc[0][1]+60])

    print("Time taken per frame:" , str(time.time() - startFrame))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()