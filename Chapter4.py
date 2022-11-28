import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img)

img[200:300,100:300]=255,0,0

img[:]=255,0,0 # this to color whole matrics

cv2.line(img,(0,0),(300,300),(0,255,0),3) #for line
# cv2.line(image, start_point, end_point, color, thickness) 
# start_point: It is the starting coordinates of the line. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value). 
# end_point: It is the ending coordinates of the line. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value). 
# color: It is the color of the line to be drawn. For RGB, we pass a tuple. eg: (255, 0, 0) for blue color.
# thickness: It is the thickness of the line in px.

cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
# cv2.rectangle(image, start_point, end_point, color, thickness)
# Parameters:
# image: It is the image on which rectangle is to be drawn.
# start_point: It is the starting coordinates of rectangle. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
# end_point: It is the ending coordinates of rectangle. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
# color: It is the color of border line of rectangle to be drawn. For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.
# thickness: It is the thickness of the rectangle border line in px. Thickness of -1 px will fill the rectangle shape by the specified color.

cv2.circle(img,(400,50),30,(255,255,0),5)
# cv2.circle(image, center_coordinates, radius, color, thickness)
# Parameters: 

# image: It is the image on which the circle is to be drawn. 
# center_coordinates: It is the center coordinates of the circle. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value). 
# radius: It is the radius of the circle. 
# color: It is the color of the borderline of a circle to be drawn. For BGR, we pass a tuple. eg: (255, 0, 0) for blue color. 
# thickness: It is the thickness of the circle border line in px. Thickness of -1 px will fill the circle shape by the specified color.
# Return Value: It returns an image. 


cv2.putText(img,"Prince",(300,200),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,150,0),1)

# cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
# Parameters:
# image: It is the image on which text is to be drawn.
# text: Text string to be drawn.
# org: It is the coordinates of the bottom-left corner of the text string in the image. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
# font: It denotes the font type. Some of font types are FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN, , etc.
# fontScale: Font scale factor that is multiplied by the font-specific base size.
# color: It is the color of text string to be drawn. For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.
# thickness: It is the thickness of the line in px.
# lineType: This is an optional parameter.It gives the type of the line to be used.
# bottomLeftOrigin: This is an optional parameter. When it is true, the image data origin is at the bottom-left corner. Otherwise, it is at the top-left corner.


cv2.imshow("Image",img)
cv2.waitKey(0)