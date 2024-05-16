import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#这是一个多阶段算法
#1.降噪
#2.寻找图像强度梯度（检查像素是否是其在梯度方向上的邻域中的局部最大值）
#3.非最大抑制（您得到的结果是具有“细边”的二进制图像）
#4.滞后阈值（大于maxval肯定是，小于minval舍去，连接到“可靠边缘”像素，则它们被视为边缘的一部分）


img = cv.imread('1.jpg',0)
edges = cv.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
