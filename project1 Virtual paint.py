import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
### how to read webcam
cap=cv2.VideoCapture(0)
cap.set(3,frameWidth) #set is setting
cap.set(4,frameHeight)
cap.set(10,150)#changing brightness

def findColor(img):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)

while True:
    success, img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break