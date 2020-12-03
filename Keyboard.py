import cv2
import numpy
Keyboard = numpy.zeros((200,1000,3),numpy.uint8)
Keyboard[:]=255
cv2.rectangle(Keyboard,(0,0),(50,50),(255,155,40),1)
cv2.rectangle(Keyboard,(50,0),(100,50),(155,255,40),1)
cv2.rectangle(Keyboard,(100,0),(150,50),(155,40,255),1)
cv2.rectangle(Keyboard,(150,0),(200,50),(255,155,40),1)
cv2.rectangle(Keyboard,(0,50),(50,100),(155,255,40),1)
cv2.rectangle(Keyboard,(50,50),(100,100),(155,255,40),1)
cv2.rectangle(Keyboard,(100,50),(150,100),(155,255,40),1)
cv2.imshow("FYP",Keyboard)
cv2.waitKey(0)
