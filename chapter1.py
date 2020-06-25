import cv2

print("package imported")

#### Read and Display images ####
img = cv2.imread("resourses/1.jpg")

cv2.imshow("output",img)
cv2.waitKey(0)


##### Read and play video####
cap = cv2.VideoCapture("resourses/v1.mp4")

while True:
    success, img= cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0XFF ==ord('q'):
        break


##### How to use Webcam #####
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4,480)
cap.set(10,100)

while True:
     success, img= cap.read()
     cv2.imshow("video",img)
     if cv2.waitKey(1) & 0XFF ==ord('q'):
         break
