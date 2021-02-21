import numpy as np
import cv2

def key(keyboard,x,y,w,h):
    cv2.rectangle(keyboard, (x, y), (x + w, y + h), (82, 69, 69), 1)

def blink(keyboard,choice_x,choice_y,w,h):
    cv2.rectangle(keyboard, (choice_x, choice_y), (choice_x + w, choice_y + h), (100, 100, 100), -1)

def KeyAlphabet(x_axis,y_axis,x_blink,y_blink):
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
            key(keyboard, x, y, w, h)
            x = x + 65
            Counter = Counter + 1
        x = 0
        y = y + 75

# Second Row of keyboard
    for i in range(0, 1):
        x = x + 30
        for j in range(0, 8):
            key(keyboard, x, y, w, h)
            x = x + 65
            Counter = Counter + 1
        for k in range(0, 1):
            key(keyboard, x, y, w * 2, h)
            x = x + 130
            Counter = Counter + 1
        for l in range(0, 3):
            key(keyboard, x, y, w, h)
            x = x + 65
            Counter = Counter + 1
        x = 0
        y = y + 75

# Third Row of keyboard
    for i in range(0, 1):
        x = x + 30
        for j in range(0, 8):
            key(keyboard, x, y, w, h)
            x = x + 65
            Counter = Counter + 1
        x = x + 35
        for k in range(0, 1):
            key(keyboard, x, y, w + 10, h)
            x = x + 95
            Counter = Counter + 1
        for l in range(0, 3):
            cv2.rectangle(keyboard, (x, y), (x + 60, y + h), (82, 69, 69), 1)
            x = x + 65
            Counter = Counter + 1
        x = 0
        y = y + 75

# fourth row of keyboard
    w = 280
    for i in range(0, 1):
            x = x + 30
            for j in range(0, 1):
                key(keyboard, x, y, w, h)
                x = x + 285
                Counter = Counter + 1
            for k in range(0, 1):
                cv2.rectangle(keyboard, (x, y), (x + w - 105, y + h), (82, 69, 69), 1)
                x = x + 175
                Counter = Counter + 1
            x = x + 20
            for l in range(0, 3):
                cv2.rectangle(keyboard, (x, y), (x + 70, y + h), (82, 69, 69), 1)
                x = x + 75
                Counter = Counter + 1
            x = x + 10
            for m in range(0, 1):
                cv2.rectangle(keyboard, (x, y), (x + 60, y + h), (82, 69, 69), 1)
                x = x + 70
                Counter = Counter + 1
            x = 0
            y = y + 75
    cv2.imshow("Keyboard", keyboard)

x_axis = 30
y_axis = 10
w = 60
h = 70

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


    if cv2.waitKey(1) == 27:
        break


