import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('gs.png')
kernel = np.ones((5,5),np.float32)/25#/25：归一化，使卷积核的元素之和为1，从而保持了图像的亮度不变
dst = cv.filter2D(img,-1,kernel)#均值模糊
#-1表示输出图像的深度与输入图像相同
blur = cv.GaussianBlur(img,(5,5),0)#高斯模糊
median = cv.medianBlur(img,5)#中值滤波
blur1 = cv.bilateralFilter(img,9,75,75)#双边滤波


plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur1),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()
