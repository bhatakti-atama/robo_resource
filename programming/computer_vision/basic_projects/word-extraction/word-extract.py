import cv2 
import numpy as np 
image = cv2.imread("image2.png")

#colour conversion
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1] 

#horizontal line removal
hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 1)) 
hori_remove = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, hori_kernel, iterations=2) 
contours = cv2.findContours(hori_remove, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
if len(contours) == 2: 
   contours = contours[0]  
else:  
   countours = contours[1] 
for cnt in contours: 
   cv2.drawContours(image, [cnt], -1, (255, 255, 255), 3) 
   
   #vertical line removal
verti_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 40)) 
verti_remove = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, verti_kernel, iterations=2) 
contours = cv2.findContours(verti_remove, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
if len(contours) == 2: 
    contours = contours[0]  
else:  
    contours = contours[1] 
for cnt in contours: 
   cv2.drawContours(image, [cnt], -1, (255, 255, 255), 3) 
   
   #adding morphological effects
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
mask = cv2.threshold(image, 130, 255, cv2.THRESH_BINARY_INV)[1] 
mask = cv2.dilate(mask, np.ones((4, 4), np.uint8), iterations=2) 
mask = cv2.erode(mask,np.ones((3, 3), np.uint8),iterations = 1) 
cont = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2] 
 
 #color conversion back to rgb
result= cv2.cvtColor(image, cv2.COLOR_GRAY2RGB) 

#formation of rectangles around words with blue color 
for c in cont: 
   (x, y, w, h) = cv2.boundingRect(c) 
   cv2.rectangle(result, (x, y), (x+w, y+h), (255,0, 0), 5)  
   
   #resizing image and printing them 
output = cv2.resize(result, (640, 640)) 
cv2.imshow('result', output) 
cv2.imwrite('output.png', output) 
cv2.waitKey() 
cv2.destroyAllWindows()
