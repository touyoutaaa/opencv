import numpy as np
import cv2 as cv

x=np.uint8([250])
y=np.uint8([10])
#OpenCV 添加是饱和操作，而 Numpy 添加是模运算。
print(x+y)
print(cv.add(x,y))

#图像混合
#将图像相加，但是对图像赋予不同的权重，从而给出混合感或透明感
img1=cv.imread('0.jpg')
img2=cv.imread('1.jpg')
dst=cv.addWeighted(img1,0.91,img2,0.09,0)

cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()