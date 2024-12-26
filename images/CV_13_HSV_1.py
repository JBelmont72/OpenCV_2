'''
HSV
note, over 100 methods of color conversion
Hue  base pigment,  0-360
Satruation is amount of color, depth of the pigment, dominance of HUE,
        low saturato is very dilute
Vlaue is the brightness of color, low brightness is plack

smarties.png  
uint8
(356, 413, 3)
441084

'''
import sys
import cv2
print(cv2.__version__)
import numpy as np
print(f"This is version {sys.version}")
print(np.__version__)

def nothing(x):
    pass
cv2.namedWindow('Tracking')

while True:
    # frame = cv2.imread('/Users/judsonbelmont/Documents/Projects/OpenCV_2/images/opencv-logo.png')
    frame = cv2.imread('/Users/judsonbelmont/Documents/Projects/OpenCV_2/images/smarties.png')
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    ###  i ran thisto get the size  356 x 413
    # print(frame.shape)    #returns a tuple of number of rows, columns, and channels
    # print(frame.size)     # returns Total number of pixels accessed
    # print(frame.dtype)    # returns image dataType
    
    lowerBoundary= np.array([110,50,50])
    upperBoundary = np.array([130,255,255])
    
    mask = cv2.inRange(hsv,lowerBoundary,upperBoundary)
    # mask = cv2.inRange(hsv,lowerBoundary,upperBoundary)
    
    res = cv2.bitwise_and(frame,frame,mask =mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    cv2.moveWindow('frame',0,0)
    
    key =cv2.waitKey(1) & 0xFF
    if key == 27:
        break
cv2.destroyAllWindows