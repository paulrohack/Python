import cv2
import numpy as np

# cap = cv2.VideoCapture(0)

# while True:
cv2.imread('') 
b = img[0][0][0]
g = img[0][0][1]
r = img[0][0][2]
if b > r and b > g:
    print('blue')
if g > r and g > b:
    print('green')
if r > b and r > g:
    print('red')

cv2.imshow('s', img)
cv2.waitKey(1)