import cv2
import numpy as np

# function for Blinking on Keyboard so that user can detect which alphabet he/she is selected to type.
# uptill now it works on whole screen but after integration of other coding parts it blink on specific part.

Time = 1000          # 1000 is equal to 1 secs......time set for blinking period

while True:
    #          np.zeros ((shape=width,height,channels) , dtype= unit8
    keyboard = np.zeros((440, 500, 3), np.uint8)   # display black screen untill time 1sec completed
    cv2.imshow("Keyboard", keyboard)
    cv2.waitKey(Time)

    keyboard = np.zeros((440, 500, 3), np.uint8)  # display white screen untill time 1sec completed
    keyboard[:] = 255        # 255 is white color
    cv2.imshow("Keyboard", keyboard)
    cv2.waitKey(Time)        # wait for time=1000 to perform further event.

    if cv2.waitKey(1) == 27:    # blinking stop when escape key press
        break
