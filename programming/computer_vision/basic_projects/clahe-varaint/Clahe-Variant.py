import cv2
import numpy as np

#Reading the image from the present directory
image = cv2.imread("0.jpeg")
#Resizing the image for compatibility
image = cv2.resize(image, (500,600))

#The initial processing of the image
#image = cv2.medianBlur(image, 3)
image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#The declaration of CLAHE 
#clipLimit -> Threshold for contrast limiting
clahe = cv2.createCLAHE(clipLimit=5)
final_img = clahe.apply(image_bw) + 30

#Ordinary thresholding the same image
_,ordinary_img = cv2.threshold(image_bw,155, 255, cv2.THRESH_BINARY)

#Showing all the three images
cv2.imshow("input image",image)
cv2.imwrite("clahe_done.jpg", final_img)
cv2.imwrite("threshhold.jpg", ordinary_img)
cv2.imshow("ordinary threshhold", ordinary_img)
cv2.imshow("CLAHE image", final_img)

cv2.waitKey(10000)
cv2.destroyAllWindows()
