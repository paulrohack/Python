import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    l = np.array([0, 0, 0])
    u = np.array([43, 222, 152])
    img = cv2.inRange(img, l, u)
    cv2.imshow('s', img)

    cv2.waitKey(1)