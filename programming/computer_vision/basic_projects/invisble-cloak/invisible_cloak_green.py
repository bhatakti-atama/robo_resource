# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:59:22 2020

@author: krati
"""

import numpy as np
import cv2

capture = cv2.VideoCapture(0)
cod = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Kratika_green.avi',cod,20.0,(640,480))

background = 0
for i in range(30):
    ret, background = capture.read()
while(capture.isOpened()):
    ret, img = capture.read()
    if not ret:
        break
        
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_green = np.array([65,60,60])
    upper_green = np.array([80,255,255])
    mask1 = cv2.inRange(hsv , lower_green , upper_green)
     
    mask1=cv2.morphologyEx(mask1, cv2.MORPH_OPEN ,np.ones((3,3) , np.uint8) , iterations=2)
        
    
        
    mask2 = cv2.bitwise_not(mask1)
    
    result_1 = cv2.bitwise_and(background, background, mask=mask1)
    result_2 = cv2.bitwise_and(img, img, mask=mask2)
    
    final_output = cv2.addWeighted(result_1 , 1, result_2 , 1, 0)
    
    cv2.imshow('invisible' , final_output)
    out.write(final_output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
        
capture.release()
out.release()
cv2.destroyAllWindows()