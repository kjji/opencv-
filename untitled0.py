Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ## save the video cap.

import cv2
import numpy as np

img = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi' , fourcc , 20.0 ,(640,480))
while True:
    ret, frame = img.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    out.write(frame)
    
    cv2.imshow('frame' ,frame )
    cv2.imshow('gray' , gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cap.release()
cv2.destroyAllWindows()
