import numpy as np
import cv2 as cv

#使用 OpenCV 测量性能
img1 = cv.imread('1.jpg')
e1 = cv.getTickCount()
for i in range(5,49,2):
    img1 = cv.medianBlur(img1,i)
e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()
print( t )

