import cv2  
import numpy as np

img = cv2.imread("C:\Users\Xiaoxi Chen\Downloads\OpenCV_Preperation\OpenCV_homework\Test_images\Lenna")
cv2.nameWindow("Lenna")
cv2.imshow("Lenna", img)

#show RGB
r,g,b = cv2.split(img)
cv2.imshow('Original Image', img)
cv2.imshow('Red', r)
cv2.imwrite('Red.png', r)
cv2.imshow('Green', g)
cv2.imwrite('Green.png', g)
cv2.imshow('Blue', b)
cv2.imwrite('Blue.png', b)
rgbPixel = img[20,25]
print rgbPixel

#YCC
imgYCC = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)
Y,Cb,Cr = cv2.split(ycrcb_image)
cv2.imshow('Y', y)
cv2.imwrite('Y.png', y)
cv2.imshow('Cr', cr)
cv2.imwrite('Cr.png', cr)
cv2.imshow('Cb', cb)
cv2.imwrite('Cb.png', cb)
ycrcbPixel = imgYCC[20,25]
print ycrcbPixel

#HSV

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv_image)
cv2.imshow("Hue", h)
cv2.imwrite('Hue.png', h)
cv2.imshow("Saturation", s)
cv2.imwrite("Saturation.png", s)
cv2.imshow("Value", v)
cv2.imwrite("Value.png", v)
hsvPixel = imgHSV[20,25]
print hsvPixel

cv2.waitkey(0)