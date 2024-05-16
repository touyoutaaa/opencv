import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('jianbian.png',0)

#二进制阈值化
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
#二进制反转
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
#截断阈值化，即超过阈值的像素点被截断为阈值，而其他像素点保持不变
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
#表示超过阈值的像素点保持不变，而低于阈值的像素点被设定为 0
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
#超过阈值的像素点被设定为 0，而低于阈值的像素点保持不变。
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

#自适应阈值处理
img = cv.medianBlur(img,5)#中值模糊处理，去除图像中的噪点
#5是指定的卷积核大小，表示模糊处理的窗口大小。它指定了一个 5x5 的窗口
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
#基于邻域区域的平均值进行阈值处理
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,11,2)
#11:计算阈值的局部邻域的大小11*11,2:平均值减去的常数,微调结果

#计算局部邻域内的加权平均值，其中权重是一个高斯窗口
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()


img = cv.imread('noisy.png',0)
# 全局阈值
ret1,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)

# Otsu 阈值
ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
#在使用OTSU方法时不需要提供一个明确的阈值，它基于图像的直方图来选择最佳阈值

# 经过高斯滤波的 Otsu 阈值
blur = cv.GaussianBlur(img,(5,5),0)
#值为0表示OpenCV将根据提供的核大小自动计算标准偏差

ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
# 画出所有的图像和他们的直方图
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])

    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    #256:直方图中条柱的数量,ravel:将多维数组转换为一维数组
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])

    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()
