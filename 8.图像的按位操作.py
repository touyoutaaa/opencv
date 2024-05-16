import numpy as np
import cv2 as cv

img1 = cv.imread('1.jpg')
img2 = cv.imread('0.jpg')
#我想在左上角放置一个logo，所以我创建了一个 ROI(感兴趣区域),并且这个ROI的宽和高为我想放置的logo的宽和高
rows,cols,channels = img2.shape
roi = img1 [0:rows,0:cols]

#现在创建一个logo的掩码，通过对logo图像进行阈值，并对阈值结果并创建其反转掩码
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

#阈值化
ret,mask = cv.threshold(img2gray,10,255,cv.THRESH_BINARY)
#将img2gray中像素值大于10的部分设为255（白色），小于等于10的部分设为0（黑色）,存在mask中

#位求反
mask_inv = cv.bitwise_not(mask)
#将之前得到的掩码中的白色区域变为黑色，黑色区域变为白色

#现在使 ROI 中的徽标区域变黑
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
#仅从徽标图像中获取徽标区域。
img2_fg = cv.bitwise_and(img2,img2,mask = mask)
#在 ROI 中放置徽标并修改主图像
dst = cv.add(img1_bg,img2_fg)
img1 [0:rows,0:cols] = dst

cv.imshow('res',img1)
cv.waitKey(0)
cv.destroyAllWindows()
