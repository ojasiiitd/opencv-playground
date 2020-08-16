import cv2
import numpy as np

## load images
# img = cv2.imread('smartphone.jpeg' , cv2.IMREAD_GRAYSCALE)

# cv2.imshow('iPhone' , img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

## work with videos
# cap = cv2.VideoCapture(0) # for video file cv2.VideoCapture('video.mp4')

# # to save your video
# saver = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('curVideo.avi' , saver , 20.0 , (640,480))

# while True:
#     ret , frame = cap.read()

#     gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

#     out.write(frame)

#     cv2.imshow('current frame' , frame)
#     cv2.imshow('gray frame' , gray)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# out.release()
# cv2.destroyAllWindows()

