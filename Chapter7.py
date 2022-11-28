import cv2
import numpy as np

img =cv2.imread("resource/car.jfif")

imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# cv2.cvtColor(src, code[, dst[, dstCn]])
# Parameters:
# src: It is the image whose color space is to be changed.
# code: It is the color space conversion code.
# dst: It is the output image of the same size and depth as src image. It is an optional parameter.
# dstCn: It is the number of channels in the destination image. If the parameter is 0 then the number of the channels is derived automatically from src and code. It is an optional parameter.

# Return Value: It returns an image.

cv2.imshow("Original",img)
cv2.imshow("HSV",imgHSV)

cv2.waitKey(0)