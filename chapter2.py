import cv2
import numpy as np
 
img = cv2.imread("resource/duragji.jpg")

imgGry=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# image: Source/Input image of n-dimensional array.
# code: Conversion code for color space.
cv2.imshow("Gry Image",imgGry)
cv2.waitKey(0)


imgBlur=cv2.GaussianBlur(imgGry,(7,7),0)
# src: Source/Input of n-dimensional array.
# ksize: Kernal is matrix of an (no. of rows)*(no. of columns) order .Its Size is given in the form of tuple (no. of rows, no. of columns). no. of rows and no. of columns should be odd .If ksize is given as (0 0), then ksize is computed from given sigma values i.e. sigmaX and sigmaY.
# sigmaX: Standard deviation value of kernal along horizontal direction.
# sigmaY: Standard deviation value of kernal along vertical direction.
# borderType: This specify boundaries of an image while kernel is applied on borders of an image.
cv2.imshow("Blur Image",imgBlur)
cv2.waitKey(0)


imgCanny=cv2.Canny(img,100,100) 
#image: Source/Input image of n-dimensional array.
# threshold1: It is the High threshold value of intensity gradient.
# threshold2: It is the Low threshold value of intensity gradient.
cv2.imshow("Canny Image",imgCanny)
cv2.waitKey(0)


kernel = np.ones((5,5),np.uint8)
imgDialation=cv2.dilate(img,kernel,iterations=1)
imgEroded=cv2.erode(img,kernel,iterations=1)
 #applies a morphological filter to images
# The first parameter is the original image,
# kernel is the matrix with which image is
# convolved and third parameter is the number
# of iterations, which will determine how much
# you want to erode/dilate a given image.
cv2.imshow("CannyDialation Image",imgDialation)
cv2.waitKey(0)
cv2.imshow("CannyEroded Image",imgEroded)
cv2.waitKey(0)