from threading import Thread
import cv2

vcap = cv2.VideoCapture("rtsp://admin:admin@ip/video0.sdp")
cv2.namedWindow('VIDEO', cv2.WINDOW_NORMAL)

while(1):
    ret, frame = vcap.read()
    cv2.imshow('VIDEO', frame)
    cv2.waitKey(1)