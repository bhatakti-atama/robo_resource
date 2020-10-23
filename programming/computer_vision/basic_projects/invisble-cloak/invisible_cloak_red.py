# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 13:00:28 2020

@author: krati
"""

import numpy as np
import cv2

capture = cv2.VideoCapture(0)
cod = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Kratika_r.avi',cod,20.0,(640,480))

background = 0
for i in range(30):
    ret, background = capture.read()
while(capture.isOpened()):
    ret, img = capture.read()
    if not ret:
        break
        
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv , lower_red , upper_red)
    
    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv , lower_red , upper_red)
    
    mask1 = mask1 + mask2 
    mask1=cv2.morphologyEx(mask1, cv2.MORPH_OPEN ,np.ones((3,3) , np.uint8) , iterations=2)
        
    mask2=cv2.morphologyEx(mask1, cv2.MORPH_DILATE ,np.ones((3,3) , np.uint8) , iterations=1)
        
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