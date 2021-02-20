#opencv
import cv2
W=480
H=640
Original_image = cv2.imread("Face_image.jpg")
Resized_Image = cv2.resize(Original_image,(W,H))
Gray_image = cv2.cvtColor(Resized_Image,cv2.COLOR_BGR2GRAY)

[R,C] = Gray_image.shape
for r in range(0,R):
    for c in range(0,C):
        if Gray_image[r,c] >=100:
            Gray_image[r,c] = 255
        else:
            Gray_image[r,c] = 0


cv2.imshow("Gray_image",Gray_image)
#cv2.imshow("Original_image",Original_image)
cv2.waitKey(0)