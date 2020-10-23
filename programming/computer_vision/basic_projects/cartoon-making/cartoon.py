import cv2
import numpy


#Opening the camera
capture= cv2.VideoCapture(0)

#Here we create infinite loop which continousy makes frames
while(True):
	ret,frame = capture.read()
	
	#converting the image to greyscale for edge detection
	image_bw = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	# Applying the bilateral filter for smoothening the image without edge loss  
	image_bw = cv2.bilateralFilter(image_bw, -1,10, 1)
    # Making it blur using gaussian blur
	image_bw = cv2.GaussianBlur(image_bw, (5,5), 0)
	
	#Getting the edges of the image using Laplacian
	edges = cv2.Laplacian(image_bw,-1,ksize=5)
	#Threshholding the edges for the mask to be blended
	_,mask = cv2.threshold(edges,30, 255, cv2.THRESH_BINARY_INV)

	#taking the impurities out of the mask using median blur
	for i in range(13):
		#Here the kernel size can be varied according to the resolution of camera 
		mask= cv2.medianBlur(mask,3)

	#Eroding and dilating the mask for making it look realistic 
	kernel = numpy.ones((3,3),numpy.uint8)
	mask = cv2.erode(mask, kernel)
	mask =cv2.erode(mask, kernel)
	mask = cv2.dilate(mask, kernel)
	
	#Final task of splitting the frame into three layers(b,g,r) and application of mask
	image_b, image_g, image_r = cv2.split(frame)

	final_b = cv2.bitwise_and(image_b, mask)
	final_g = cv2.bitwise_and(image_g, mask)
	final_r = cv2.bitwise_and(image_r, mask)

	final = cv2.merge((final_b,final_g,final_r))

	cv2.imshow("fine", final)
	#Exiting the application on press of q
	if(cv2.waitKey(2)==ord('q')):
		break

capture.release()
cv2.destroyAllWindows()
