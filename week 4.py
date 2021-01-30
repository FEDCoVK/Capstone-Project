import cv2
import numpy as np
import csv

# read image and convert into gray scale

Image = cv2.imread('C:/Users/Hamna Khalid/PycharmProjects/capstone/Face_image.jpeg')
Image_gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)

# convert grayscale image into matrix
# R(row) , C(column)

[R, C] = Image_gray.shape       # R(row) , C(column)
value = np.zeros((R, C), np.uint8)
for i in range(0, R):
    for j in range(0, C):
        value[i, j] = Image_gray[i, j]

# store that matrix in txt file

with open("img_pixels.txt", 'a') as f:
    writer = csv.writer(f)
    writer.writerow(value)
