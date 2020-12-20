from threading import Thread
import cv2

<<<<<<< HEAD
vcap = cv2.VideoCapture("rtsp://admin:admin@ip/video0.sdp")
=======
vcap = cv2.VideoCapture("rtsp://admin:admin@172.17.10.118/video0.sdp")
>>>>>>> 5592f8e... Initial commit
cv2.namedWindow('VIDEO', cv2.WINDOW_NORMAL)

while(1):
    ret, frame = vcap.read()
    cv2.imshow('VIDEO', frame)
    cv2.waitKey(1)