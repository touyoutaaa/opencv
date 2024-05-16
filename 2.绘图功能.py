import numpy as np
import cv2 as cv

#画线
#创建一个黑色图像当幕布
img=np.zeros((512,512,3),np.uint8)#图像大小为512

#画一个5px宽的蓝色对角线
cv.line(img,(0,0),(511,511),(255,0,0),5)

#画矩形
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

#画圆
cv.circle(img,(445,63),63,(0,0,255),-1)#-1实心圆

#画椭圆
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

#cv.polylines(),绘制多边形
pts=np.array([[29,43],[60,90],[33,209]])
pts=pts.reshape((-1,1,2))#-1自动计算数组行数,转化成一行两列,三维数组
cv.polylines(img,[pts],True,(255,0,0),3)


cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()