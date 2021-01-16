#open cv
import cv2
import numpy

Vid = cv2.VideoCapture(0)

while True:
    Con, frame = Vid.read()
    Image_Gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    Image_Gauss = cv2.GaussianBlur(Image_Gray, (5, 5), 1)
    Image_Canny = cv2.Canny(Image_Gauss, 10, 200)
    cv2.imshow("Output",Image_Canny)
    cv2.imshow("Original",frame)

    if cv2.waitKey(1) == 27:
        break