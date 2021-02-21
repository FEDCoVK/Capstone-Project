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