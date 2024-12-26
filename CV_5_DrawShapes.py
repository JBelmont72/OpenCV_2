'''ProgrammingKnowledge OpenCV Python video 5 Geometric Shapes
python -m venv .venv
source .venv/bin/activate
use the pyenv
use the 3.9.6 ('pyenv':venv)  version in the interpreter!!

www.fourcc.org/codecs.php   video codes by fourcc, compressed formats  that you see displayed when you don't have the right CODEC installed to play a given AVI file
color picker    https://math.hws.edu/graphicsbook/demos/c2/rgb-hsv.html
https://colorpicker.me/#ca64b6
lena.jpg is 500 x 500
'''
import sys
import cv2
print(cv2.__version__)
import numpy as np
print(f"This is version {sys.version}")
print(np.__version__)

width=640
height=360
thickness = 5
fontH = 2
fontThickness = 4
image = np.zeros([512,512,3],np.uint8)
# image = cv2.imread('/Users/judsonbelmont/Documents/Projects/OpenCV_2/images/lena.jpg',1)
while True:     #if true then the first arguement (ret) is true and the frame is captured
    
    imageBGR =cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    image1 = cv2.line(image,(0,0),(255,255),(255,0,0),thickness,4)
    image2 = cv2.line(image,(300,255),(500,0),(182,100,202),thickness,4)
    image3 = cv2.arrowedLine(image,(0,300),(200,300),(125,125,0),thickness,6)
    image4 =cv2.rectangle(image,(255,255),(325,325),(0,0,255),7)
    image5 =cv2.rectangle(image,(400,0),(510,500),(0,0,255),7)
    image6 =cv2.circle(image,(250,250),25,(125,125,0),4)
    image7 =cv2.putText(image,'This is fun!',(20,400),cv2.FONT_HERSHEY_TRIPLEX,fontH,(255,255,255),fontThickness,cv2.LINE_4)
    cv2.imshow('image',image)
    
    if cv2.waitKey(1) & 0xff ==ord('c'):
        break

cv2.destroyAllWindows()
    
 