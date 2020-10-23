# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:57:30 2020

@author: krati
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, img = cap.read()
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    
    lower_yellow = np.array([20,100,100])
    upper_yellow = np.array([30,255,255])
    mask = cv2.inRange(hsv , lower_yellow , upper_yellow)
    
     
    
    blur=cv2.GaussianBlur(mask,(5,5),0)
    
    
    contours, hierarchy = cv2.findContours(blur,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        area=0
        area=cv2.contourArea(cnt)
        if area>500:
            x,y,m,h=cv2.boundingRect(cnt)
            img= cv2.rectangle(img,(x,y),(x+m,y+h),(255,0,0),2)
            
            
    cv2.imshow("frame",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break     

cv2.destroyAllWindows()