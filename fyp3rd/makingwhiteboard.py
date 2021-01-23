import numpy as np
import cv2


def Alphabet():
    Alphabets = {0: "Q", 1: "W", 2: "E", 3: "R", 4: "T",
                 5: "A", 6: "S", 7: "D", 8: "F", 9: "G",
                 10: "Z", 11: "X", 12: "C", 13: "V", 14: "B",15:'G',
                 16: "Q", 17: "W", 18: "E", 19: "R", 20: "T",
                 21: "A", 22: "S", 23: "D", 24: "F", 25: "G",
                 26: "Z", 27: "X", 28: "C", 29: "V", 30: "B"}
    width = 80
    height = 80
    x = 0
    y = 0
    font_letter = cv2.FONT_HERSHEY_PLAIN
    font_scale = 2
    font_th = 2

    keyboard = np.zeros((300,1000,3),np.uint8)
    white_board = np.zeros((300,600,3),np.uint8)
    white_board[:] = 255

    w=100
    h=100
    Counter =0

    for i in range(0,3):
        for j in range(0,10):
            text_size = cv2.getTextSize(Alphabets[Counter], font_letter, font_scale, font_th)[0]
            width_text, height_text = text_size[0], text_size[1]
            text_x = int((width - width_text) / 2) + x
            text_y = int((height + height_text) / 2) + y
            cv2.putText(keyboard, Alphabets[Counter], (text_x, text_y), font_letter, font_scale, (0, 255, 0), font_th)
            x = x+100
            Counter =Counter+1
        x=0
        y= y+100

    cv2.imshow("Keyboard",keyboard)
    cv2.imshow("White_Board",white_board)
    cv2.waitKey(0)

Alphabet()