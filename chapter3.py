import cv2
import numpy as np

img = cv2.imread("resourses/1.png")
print(img.shape) ##### shows (435,500,3) (height,width,rgbcolor)

###Resizing Image ####
imgResize = cv2.resize(img,(300,200))

#### Cropping Image ####
imgCropped = img[0:200,200:450]


#### Display Images #####
cv2.imshow("Image",img)
cv2.imshow("Resized Image",imgResize)
cv2.imshow("Cropped Image",imgCropped)


cv2.waitKey(0)