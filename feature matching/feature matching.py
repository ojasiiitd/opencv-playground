import cv2
import numpy as np
import matplotlib.pyplot as plt

book = cv2.imread("book.jpeg")
room = cv2.imread("book-in-room.jpeg")

orb = cv2.ORB_create() # detector

kp1 , des1 = orb.detectAndCompute(book , None)
kp2 , des2 = orb.detectAndCompute(room , None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING , crossCheck=True)

matches = bf.match(des1 , des2)
matches = sorted(matches , key=lambda x:x.distance)

print(len(matches))
res = cv2.drawMatches(book , kp1 , room , kp2 , matches[-10:] , None , flags=2)

res = cv2.cvtColor(res , cv2.COLOR_BGR2RGB)
plt.imshow(res)
plt.show()