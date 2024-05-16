import cv2 as cv
import numpy as np

# img1 = cv.imread('1.jpg')
# gray_img = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Image', gray_img)
# cv.waitKey(0)
# cv.destroyAllWindows()

cap = cv.VideoCapture(0)
while(1):

    _, frame = cap.read()#frame返回读取的视频帧
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    #定义在hsv中的蓝色的范围
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # 阈值化
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    #掩码将在指定的蓝色范围内为白色（255），而在其他地方为黑色（0）

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)

    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()

#如何找到 HSV 值去追踪?
green = np.uint8([[[0,255,0 ]]])
hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)
print( hsv_green )
#你可以取 [H-10, 100,100] 和 [H+10, 255, 255] 分别作为上界和下界

