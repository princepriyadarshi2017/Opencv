## How to read images video and webcam
import cv2

img =cv2.imread("resource/duragji.jpg")

cv2.imshow("Output",img)
cv2.waitKey(0)


### how to read video
cap=cv2.VideoCapture("resource/1.mp4")

while True:
    success, img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

### how to read webcam
cap=cv2.VideoCapture(0)
cap.set(3,640) #set is setting
cap.set(4,480)
cap.set(10,100)#changing brightness

while True:
    success, img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break