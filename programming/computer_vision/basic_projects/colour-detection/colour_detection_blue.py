# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:40:47 2020

@author: krati
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cod = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('green.avi',cod,20.0,(640,480))

while(True):
    ret, img = cap.read()
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    blue1=np.array([94,80,2])
    blue2=np.array([126,255,255])
    
    mask = cv2.inRange(hsv , blue1 , blue2)
    
    blur=cv2.GaussianBlur(mask,(5,5),0)
    
    
    contours, hierarchy = cv2.findContours(blur,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        area=0
        area=cv2.contourArea(cnt)
        if area>1000:
            x,y,m,h=cv2.boundingRect(cnt)
            img= cv2.rectangle(img,(x,y),(x+m,y+h),(0,0,0),2)
            
           
    
    cv2.imshow("frame",img)
    out.write(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break     
cap.release()
out.release()
cv2.destroyAllWindows()