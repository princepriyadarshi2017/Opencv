import cv2
 
img = cv2.imread("resource/duragji.jpg")

imgGry=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gry Image",imgGry)
cv2.waitKey(0)

imgBlur=cv2.GaussianBlur(imgGry,(7,7),0)
cv2.imshow("Blur Image",imgBlur)
cv2.waitKey(0)

imgCanny=cv2.Canny(img,100,100)
cv2.imshow("Canny Image",imgCanny)
cv2.waitKey(0)