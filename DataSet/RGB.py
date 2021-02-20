import cv2
heightImg = 640
widthImg = 480

Image = cv2.imread("image/Face_image.jpeg")
Resized_Image = cv2.resize(Image,(widthImg,heightImg))
R=Resized_Image [:,:,2]
G= Resized_Image [:,:,1]
B= Resized_Image [:,:,0]
Gray_image = cv2.cvtColor(Resized_Image,cv2.COLOR_BGR2GRAY)
#cv2.imshow("Image",Image)
cv2.imshow("Resized_Image",Resized_Image)
cv2.imshow("Gray_image",Gray_image)
cv2.imshow("RED", R)
cv2.imshow("GREEN", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)