import cv2
import numpy as np

img = cv2.imread("C:\Users\Xiaoxi Chen\Downloads\OpenCV_Preperation\OpenCV_homework\Test_image\baboon.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.iwrite("C:\Users\Xiaoxi Chen\Downloads\OpenCV_Preperation\OpenCV_homework\Test_image\baboon.jpg", gray)

#gray
threshold_type = 2
threshold_value = 128
ret,dst = cv2.threshold(gray, threshold_value, 255, cv2.TRESH_TRUNC)
cv2.imshow("threshold",dst)
cv2.nameWindow("threshold image")

#binary threshold
current_threshold = 128
max_threshold = 255
ret,thre = cv2.threshold(gray, current_threshold, max_threshold, cv2.THRESH_BINARY)
cv2.imshow("binary threshold", thre)
cv2.nameWindow("binary threshold")

#band thresholding
threshold1 = 27
threshold2 = 125
ret,bin1 = cv2.thresold(gray, threshold1, 255, cv2.THRESH_BINARY)
ret,bin2 = cv2.thresold(gray, threshold2, 255, cv2.THRESH_BINARY_INV)
band_thre_img = np.bitwise_and(bin1, bin2)
cv2.imshow("binary thresholding", band_thre_img)
cv2.nameWindow("binary thresholding")

#semi thresholding
ret,semi_thre_img = cv2.threshold(gray, current_threshold, max_threshold, cv2.THRESH_BINARY_INV | cv2.THRESH_BINARY)
semi_thre_img = np.bitwise_and(gray, semi_thre_img)
cv2.imshow("semi thresholding", semi_thre_img)
cv2.namedWindow("semi thresholding")

#adaptive thresolding
adaptive_thresh = cv2.adaptiveThreshold(gray, 255.0, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 10)
cv2.imshow("adaptive thresholding", adaptive_thresh)
cv2.nameWindow("adaptive thresholding")

cv2.waitKey(0)