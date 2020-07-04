  
# path  
import cv2
import numpy as np
   
# Reading an image in default mode 
image = cv2.imread('image.png') 
   
# Window name in which image is displayed 
window_name = 'partition image'
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(image,(x1,y1),(x2,y2),(0,255,0),3)
# Start coordinate, here (270, 50) 
start_point = (270, 50) 
  
# End coordinate, here (270, 750) 

end_point = (270, 700) 
  
# Green color in BGR 
color = (0, 255, 0) 
  
# Line thickness of 3 px 
thickness = 3
  
# Using cv2.line() method 
# Draw a l green line with thickness of 3 px 

image=cv2.line(image,start_point,end_point,color,thickness)
# Displaying the image  
cv2.imshow(window_name, image)
cv2.imwrite('output.jpg',image)

