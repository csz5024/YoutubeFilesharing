from pyzbar import pyzbar
import cv2
import imutils
from decoder import colors

class shapeDetect:
    def __init__(self):
        pass

    def detect(self, c):
        #initialize shape name and contour
        shape = "unidentified"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)

        if len(approx) == 3:
            shape = "triangle"

        elif len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w/float(h)

            shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"

        elif len(approx) == 5:
            shape = "pentagon"

        else:
            shape = "circle"

        return shape


img = cv2.imread("norfnorf.PNG")
resized = imutils.resize(img, width=300)
ratio = img.shape[0] / float(resized.shape[0])

# swap img for resized and vice versa
blurred = cv2.GaussianBlur(resized, (5,5), 0)
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
lab = cv2.cvtColor(blurred, cv2.COLOR_RGB2LAB)
thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
sd = shapeDetect()
cl = colors.ColorLabeler()

# add or subtract ratio
for c in cnts:
    # Compute the center of the contour, then detect the name of the shape using the conntours
    M = cv2.moments(c)
    cX = int((M["m10"] / M["m00"]) * ratio)
    cY = int((M["m01"] / M["m00"]) * ratio)
    shape = sd.detect(c)
    color = cl.label(lab, c)

    c = c.astype("float")
    c *= ratio
    c = c.astype("int")
    text = "{} {}".format(color, shape)
    cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
    cv2.putText(img, text, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    cv2.imshow("nnshapes.jpg", img)
    cv2.waitKey(0)
    cv2.imwrite('nngray.jpg', thresh)
    cv2.imshow('nngray.jpg', thresh)
