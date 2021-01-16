import numpy
import cv2

Video = cv2.VideoCapture(0)

while True:
    Condition,Frame = Video.read()
    Blur_Image_One = cv2.GaussianBlur(Frame, (3, 3), 0)
    Blur_Image_Two = cv2.GaussianBlur(Frame, (7, 7), 0)
    cv2.imshow("Blur Image(3x3) Filter",Blur_Image_One)
    cv2.imshow("Blur Image(7x7) Filter", Blur_Image_Two)

    cv2.imshow("Original", Frame)

    if cv2.waitKey(1) == 27:
        break