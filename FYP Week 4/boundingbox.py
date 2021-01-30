# I have used the Mubeen code for capturing images. The images that captured through this is stored in Data folder then
# I create bounding-box around face on  All these images through LabelImg s/w through this we get an information
# of labels in the form of .txt which we later use in training
import numpy
import cv2

cam = cv2.VideoCapture(0)

sampleNum=0

while(True):

    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    sampleNum = sampleNum + 1
    cv2.imwrite("Data/" +  str(sampleNum) + ".jpg", gray)
    cv2.imshow("Face",img)
    if cv2.waitKey(1) == 27:
        break
    elif sampleNum > 100: # 100 is the number of pictures
        break

cam.release()
cv2.destroyAllWindows()