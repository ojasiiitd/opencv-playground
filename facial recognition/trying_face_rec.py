import face_recognition
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _ , frame = cap.read()
    if not _ :
        break

    image = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    face_landmarks_list = face_recognition.face_landmarks(image , model="large")
    # print(face_landmarks_list)

    for face in face_landmarks_list:
        for feature in face :
            # print(feature)
            for pts in face[feature]:
                # print(pts)
                cv2.circle(frame , pts , 2 , (0,255,0) , -1)

    cv2.imshow("landmarks" , frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()