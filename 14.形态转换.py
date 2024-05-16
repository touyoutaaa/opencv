import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('change_model.png')
blur = cv.blur(img,(5,5))
kernel = np.ones((5,5),np.float32)/25
dilation = cv.dilate(img,kernel,iterations = 1)#膨胀
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)#开运算,消除噪音
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)#闭运算,填充小黑点
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)#形态梯度,获得轮廓
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)#顶帽，原图像和原图像开运算结果的差值
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)#黑帽，原图像和原图像的闭的差值

plt.subplot(2,4,1),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(2,4,2),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.subplot(2,4,3),plt.imshow(dilation),plt.title('Dilated')
plt.xticks([]), plt.yticks([])
plt.subplot(2,4,4),plt.imshow(opening),plt.title('Opened')
plt.xticks([]), plt.yticks([])
plt.subplot(2,4,5),plt.imshow(closing),plt.title('Closing')
plt.xticks([]), plt.yticks([])
plt.subplot(2,4,6),plt.imshow(gradient),plt.title('Gradient')
plt.xticks([]), plt.yticks([])
plt.subplot(2,4,7),plt.imshow(tophat),plt.title('Tophat')
plt.xticks([]), plt.yticks([])
plt.subplot(2,4,8),plt.imshow(blackhat),plt.title('Blackhat')
plt.xticks([]), plt.yticks([])
plt.show()
