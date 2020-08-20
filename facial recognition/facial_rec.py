import face_recognition
import os
import cv2

KNOWN_DIR = "known_faces/"
UNKNOWN_DIR = "unknown_faces/"
TOLERANCE = 0.6
MODEL = "cnn"

print("Loading known faces")
known_faces = []
known_names = []

for name in os.listdir(KNOWN_DIR):
    for f in os.listdir(f"{KNOWN_DIR}/{name}"):
        image = face_recognition.load_image_file(f"{KNOWN_DIR}/{name}/{f}")
        encoding = face_recognition.face_encodings(image)[0]
        known_faces.append(encoding)
        known_names.append(name)
print("Sucessfully processed all known faces")

print("Looking for unknown faces")
for f in os.listdir(f"{UNKNOWN_DIR}"):
    print(f)
    image = face_recognition.load_image_file(f"{UNKNOWN_DIR}/{f}")
    face_locs = face_recognition.face_locations(image , model=MODEL)
    encodings = face_recognition.face_encodings(image , face_locs)
    image = cv2.cvtColor(image , cv2.COLOR_RGB2BGR)
    
    for face_encoding , locations in zip(encodings , face_locs):
        results =  face_recognition.compare_faces(known_faces , face_encoding , TOLERANCE)
        match = None
        if True in results:
            match = known_names[results.index(True)]

            top_left = (locations[3] , locations[0])
            bot_right = (locations[1] , locations[2])

            cv2.rectangle(image , top_left , bot_right , (0,255,0) , 3)
            cv2.putText(image , match , (top_left[0]-10 , top_left[1]-10) , cv2.FONT_HERSHEY_PLAIN , 3 , (0,0,255) , 2)
        
        if match == None:
            print("MATCH NOT FOUND")
        
        cv2.imshow(f , image)
        cv2.waitKey(10000)