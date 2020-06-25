import cv2
import numpy as np
print("package imported")

img = cv2.imread("resourses/1.jpg")
kernel = np.ones((5,5),np.uint8)

#### Converting image into grey scale####
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray image", imgGray)


#### convert img to blur img ###
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
cv2.imshow("Blur image", imgBlur)


#### Edge detector ####

imgCanny = cv2.Canny(img,250,200)

#### To increase thickness of the edge #####
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
cv2.imshow("Canny image", imgCanny)
cv2.imshow("Dilate image", imgDialation)

#### To decrease the thickness of edge ###
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
cv2.imshow("Eroded image", imgEroded)

cv2.waitKey(0)
