#resizing and croping
import cv2

img =cv2.imread("resource/duragji.jpg")
print("shape of original image",img.shape)

imgResize = cv2.resize(img,(1000,500))
print("Resizedshape of original image",imgResize.shape)

imgCropped = img[0:200,200:500]

cv2.imshow("Image",img)
#cv2.waitKey(0)
cv2.imshow("Image Resize",imgResize)
#cv2.waitKey(0)
cv2.imshow("Image cropped",imgCropped)
#cv2.waitKey(0)