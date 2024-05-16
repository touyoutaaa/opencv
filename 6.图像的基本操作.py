import numpy as np
import cv2 as CV
from matplotlib import pyplot as plt
img=CV.imread("0.jpg")
h,w,c=img.shape

print(img[100,100,2])#第三个参数是通道类型
print(img.item(100,10,2))

print(img.size)#像素总数
print(img.dtype)#图像数据类型

#感兴趣的区域
ball=img[234:433,388:445]

#拆分和合并图像通道
#拆分
b,g,r=CV.split(img)
b=img[:,:,0]
g=img[:,:,1]
r=img[:,:,2]
#合并
img=CV.merge((b,g,r))

#给图像加边框
BLUE = [255,0,0]
img1 = CV.imread('0.jpg')
replicate = CV.copyMakeBorder(img1,10,10,10,10,CV.BORDER_REPLICATE)
reflect = CV.copyMakeBorder(img1,10,10,10,10,CV.BORDER_REFLECT)
reflect101 = CV.copyMakeBorder(img1,10,10,10,10,CV.BORDER_REFLECT_101)
wrap = CV.copyMakeBorder(img1,200,200,200,200,CV.BORDER_WRAP)
constant= CV.copyMakeBorder(img1,10,10,10,10,CV.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()