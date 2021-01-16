import cv2
import numpy
Imagecap = cv2.VideoCapture(0)

while True:
    Output = numpy.zeros((480, 640), dtype=numpy.uint8)
    _,Image = Imagecap.read()
    R = Image[:,:,2]
    G = Image[:,:,1]
    B = Image[:,:,0]

    print(R.shape)
    for Rows in range(0,480):
        for Col in range(0,640):
            if R[Rows,Col]>G[Rows,Col]>B[Rows,Col]:
                  Output[Rows,Col] = 255



    cv2.imshow("Original", Image)
    cv2.imshow("Output", Output)
    if cv2.waitKey(1) == 27:
        break