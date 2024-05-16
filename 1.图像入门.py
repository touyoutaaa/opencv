import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#读取图像
img=cv.imread('0.jpg',1)

#先创建一个窗口，加载图像到该窗口
cv.namedWindow('image',cv.WINDOW_NORMAL)#第二个参数可以控制大小

#在名字为image的窗口加载img图像
cv.imshow('image',img)
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()

#保存图像
cv.imwrite('0.png',img)
