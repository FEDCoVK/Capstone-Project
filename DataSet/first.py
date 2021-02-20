import cv2
#video capturing
Video = cv2.VideoCapture(0)

# Row and coloumn value
def Cord(Event,x,y,flags,param):
    if Event == cv2.EVENT_LBUTTONDOWN:
        print("Coordinates",x,y)

#display a window then bind window with a function
cv2.namedWindow("Video")
cv2.setMouseCallback("Video",Cord)

while True:
    Condition,frame = Video.read()
    cv2.imshow("Video",frame)
    if cv2.waitKey(1) == 27: #27 is escape_key
        break

