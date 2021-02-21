import numpy as np
import cv2

def key(keyboard,x,y,w,h):
    cv2.rectangle(keyboard, (x, y), (x + w, y + h), (82, 69, 69), 1)

def blink(keyboard,choice_x,choice_y,w,h):
    cv2.rectangle(keyboard, (choice_x, choice_y), (choice_x + w, choice_y + h), (100, 100, 100), -1)

def KeyAlphabet(x_axis,y_axis,x_blink,y_blink):
    Alphabets = {0: "Q", 1: "W", 2: "E", 3: "R", 4: "T",
                 5: "Y", 6: "U", 7: "I", 8: "0", 9: "P",
                 10: "1", 11: "2", 12: "3", 13: "A", 14: "S", 15: "D",
                 16: "F", 17: "G", 18: "H", 19: "J", 20: "K",
                 21: "Enter", 22: "4", 23: "5", 24: "6", 25: "L",
                 26: "Z", 27: "X", 28: "C", 29: "V", 30: "B", 31: "N", 32: "M", 33: "Up", 34: "7", 35: "8", 36: "10",
                 37: "SpaceBar", 38: "BackSpace", 39: "Left", 40: "Down", 41: "Right", 42: "0"} # Taking Keys of Keyboard In array

    width = 80
    height = 80
    font_letter = cv2.FONT_HERSHEY_PLAIN
    font_size = 1.5
    font_bold = 2


    x = 0
    y = 0
    keyboard = np.zeros((320, 900, 3), np.uint8)
    keyboard[:] = 255
    w = 60
    h = 70
    Counter = 0
    for i in range(0, 1):
        y = y + 10
        x = x + 30
        for j in range(0, 13):
            text_size = cv2.getTextSize(Alphabets[Counter], font_letter, font_size, font_bold)[0]
            width_text, height_text = text_size[0], text_size[1]
            text_x = int((width - width_text) / 2) + x
            text_y = int((height + height_text) / 2) + y

            key(keyboard, x, y, w, h)
            blink(keyboard, choice_x=x_axis, choice_y=y_axis,w=x_blink,h=y_blink) 
            cv2.putText(keyboard, Alphabets[Counter], (text_x - 8, text_y), font_letter, font_size, (82, 69, 69),font_bold)

            x = x + 65
            Counter = Counter + 1
        x = 0
        y = y + 75

# Second Row of keyboard
    for i in range(0, 1):
        x = x + 30
        for j in range(0, 8):
            text_size = cv2.getTextSize(Alphabets[Counter], font_letter, font_size, font_bold)[0]
            width_text, height_text = text_size[0], text_size[1]
            text_x = int((width - width_text) / 2) + x
            text_y = int((height + height_text) / 2) + y

            key(keyboard, x, y, w, h)
            cv2.putText(keyboard, Alphabets[Counter], (text_x - 8, text_y), font_letter, font_size, (82, 69, 69),font_bold)

            x = x + 65
            Counter = Counter + 1
        for k in range(0, 1):
            text_size = cv2.getTextSize(Alphabets[Counter], font_letter, font_size, font_bold)[0]
            width_text, height_text = text_size[0], text_size[1]
            text_x = int((width - width_text) / 2) + x
            text_y = int((height + height_text) / 2) + y

            key(keyboard, x, y, w * 2, h)
            cv2.putText(keyboard, Alphabets[Counter], (text_x + 28, text_y), font_letter, font_size, (82, 69, 69),font_bold)

            x = x + 130
            Counter = Counter + 1
        for l in range(0, 3):
            text_size = cv2.getTextSize(Alphabets[Counter], font_letter, font_size, font_bold)[0]
            width_text, height_text = text_size[0], text_size[1]
            text_x = int((width - width_text) / 2) + x
            text_y = int((height + height_text) / 2) + y

            key(keyboard, x, y, w, h)
            cv2.putText(keyboard, Alphabets[Counter], (text_x - 8, text_y), font_letter, font_size, (82, 69, 69),font_bold)

            x = x + 65
            Counter = Counter + 1
        x = 0
        y = y + 75

# Third Row of keyboard
    for i in range(0, 1):
        x = x + 30
        for j in range(0, 8):
            text_size = cv2.getTextSize(Alphabets[Counter], font_letter, font_size, font_bold)[0]
            width_text, height_text = text_size[0], text_size[1]
            text_x = int((width - width_text) / 2) + x
            text_y = int((height + height_text) / 2) + y

            key(keyboard, x, y, w, h)
            cv2.putText(keyboard, Alphabets[Counter], (text_x - 8, text_y), font_letter, font_size, (82, 69, 69), font_bold)

            x = x + 65
            Counter = Counter + 1
        x = x + 35
        for k in range(0, 1):
            text_size = cv2.getTextSize(Alphabets[Counter], font_letter, font_size, font_bold)[0]
            width_text, height_text = text_size[0], text_size[1]
            text_x = int((width - width_text) / 2) + x
            text_y = int((height + height_text) / 2) + y

            key(keyboard, x, y, w + 10, h)
            cv2.putText(keyboard, Alphabets[Counter], (text_x - 8, text_y), font_letter, font_size, (82, 69, 69),font_bold)

            x = x + 95
            Counter = Counter + 1
        for l in range(0, 3):
            text_size = cv2.getTextSize(Alphabets[Counter], font_letter, font_size, font_bold)[0]
            width_text, height_text = text_size[0], text_size[1]
            text_x = int((width - width_text) / 2) + x
            text_y = int((height + height_text) / 2) + y

            cv2.rectangle(keyboard, (x, y), (x + 60, y + h), (82, 69, 69), 1)
            cv2.putText(keyboard, Alphabets[Counter], (text_x - 8, text_y), font_letter, font_size, (82, 69, 69),font_bold)

            x = x + 65
            Counter = Counter + 1
        x = 0
        y = y + 75

# fourth row of keyboard
    w = 280
    for i in range(0, 1):
            x = x + 30
            for j in range(0, 1):
                text_size = cv2.getTextSize(Alphabets[Counter], font_letter, font_size, font_bold)[0]
                width_text, height_text = text_size[0], text_size[1]
                text_x = int((width - width_text) / 2) + x
                text_y = int((height + height_text) / 2) + y

                key(keyboard, x, y, w, h)
                cv2.putText(keyboard, Alphabets[Counter], (text_x + 100, text_y), font_letter, font_size, (82, 69, 69), font_bold)

                x = x + 285
                Counter = Counter + 1
            for k in range(0, 1):
                text_size = cv2.getTextSize(Alphabets[Counter], font_letter, font_size, font_bold)[0]
                width_text, height_text = text_size[0], text_size[1]
                text_x = int((width - width_text) / 2) + x
                text_y = int((height + height_text) / 2) + y

                cv2.rectangle(keyboard, (x, y), (x + w - 105, y + h), (82, 69, 69), 1)
                cv2.putText(keyboard, Alphabets[Counter], (text_x + 50, text_y), font_letter, font_size, (82, 69, 6),font_bold)

                x = x + 175
                Counter = Counter + 1
            x = x + 20
            for l in range(0, 3):
                text_size = cv2.getTextSize(Alphabets[Counter], font_letter, font_size, font_bold)[0]
                width_text, height_text = text_size[0], text_size[1]
                text_x = int((width - width_text) / 2) + x
                text_y = int((height + height_text) / 2) + y

                cv2.rectangle(keyboard, (x, y), (x + 70, y + h), (82, 69, 69), 1)
                cv2.putText(keyboard, Alphabets[Counter], (text_x - 5, text_y), font_letter, font_size, (82, 69, 69),font_bold)

                x = x + 75
                Counter = Counter + 1
            x = x + 10
            for m in range(0, 1):
                text_size = cv2.getTextSize(Alphabets[Counter], font_letter, font_size, font_bold)[0]
                width_text, height_text = text_size[0], text_size[1]
                text_x = int((width - width_text) / 2) + x
                text_y = int((height + height_text) / 2) + y

                cv2.rectangle(keyboard, (x, y), (x + 60, y + h), (82, 69, 69), 1)
                cv2.putText(keyboard, Alphabets[Counter], (text_x - 8, text_y), font_letter, font_size, (82, 69, 69),font_bold)

                x = x + 70
                Counter = Counter + 1
            x = 0
            y = y + 75
    cv2.imshow("Keyboard", keyboard)

x_axis = 30
y_axis = 10
w = 60
h = 70
delay=0
while True:

    KeyAlphabet(x_axis, y_axis, w, h)
    if x_axis == 550 and y_axis == 85:
        KeyAlphabet(x_axis, y_axis, w * 2, h)
    if x_axis == 550 and y_axis == 160:
        KeyAlphabet(x_axis + 35, y_axis, w + 10, h)
    if x_axis == 30 and y_axis == 235:
        KeyAlphabet(x_axis, y_axis, w * 4 + 40, h)
    if x_axis == 315 and y_axis == 235:
        KeyAlphabet(x_axis, y_axis, w * 3 - 5, h)
    if x_axis == 510 and y_axis == 235:
        KeyAlphabet(x_axis, y_axis, w + 10, h)
    if x_axis == 585 and y_axis == 235:
        KeyAlphabet(x_axis, y_axis, w + 10, h)
    if x_axis == 660 and y_axis == 235:
        KeyAlphabet(x_axis, y_axis, w + 10, h)
   
    if delay > 300:
            if x_axis == 550 and y_axis == 85:
                x_axis = 615
            if x_axis == 550 and y_axis == 160:
                x_axis = 615
            if x_axis == 30 and y_axis == 235:
                x_axis = 250
            if x_axis == 315 and y_axis == 235:
                x_axis = 445
            if x_axis == 510 and y_axis == 235:
                x_axis = 520
            if x_axis == 585 and y_axis == 235:
                x_axis = 595
            if x_axis == 660 and y_axis == 235:
                x_axis = 680
            if x_axis == 745 and y_axis == 235:
                x_axis = -35
                y_axis = 10

            x_axis += 65
            if x_axis > 850:
                x_axis = 30
                y_axis += 75
            if y_axis == 300:
                x_axis=30
                y_axis =0
            delay =0
    else:
            delay += 1



    if cv2.waitKey(1) == 27:
        break


