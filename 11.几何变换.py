import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#缩放
img = cv.imread('test.jpg')
res = cv.resize(img,None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)
#fx 和 fy 是水平和垂直方向上的缩放因子，这里都设置为2，表示在水平和垂直方向上都放大两倍。
cv.imshow('img',res)
cv.waitKey(0)
cv.destroyAllWindows()

#平移变换
img1 = cv.imread('1.jpg',0)
rows,cols = img1.shape
M = np.float32([[1,0,100],[0,1,50]])#右移100个单位，下移50
dst = cv.warpAffine(img1,M,(cols,rows))
#img1：要进行变换的图像,M：仿射变换矩阵,(cols, rows)：输出图像的尺寸，即与原图像相同。
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()

#旋转
img2 = cv.imread('0.jpg',0)
rows,cols = img2.shape
# cols-1 and rows-1 are the coordinate limits.
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
#第一个参数：中心点，二：顺时针旋转90度，三：缩放因子
dst = cv.warpAffine(img,M,(cols,rows))

#仿射变换(Affine)
img4 = cv.imread('1.jpg')
rows,cols,ch = img4.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
#根据上面三个坐标与下面三个坐标的关系得出一个矩阵
M = cv.getAffineTransform(pts1,pts2)
dst1 = cv.warpAffine(img4,M,(cols,rows))
plt.subplot(121),plt.imshow(img4),plt.title('Input')
plt.subplot(122),plt.imshow(dst1),plt.title('Output')
plt.show()

#透视变换(Perspective)
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst2 = cv.warpPerspective(img4,M,(rows,cols))
plt.subplot(121),plt.imshow(img4),plt.title('Input')
plt.subplot(122),plt.imshow(dst2),plt.title('Output')
plt.show()