import numpy as np
import cv2
import time

# def song(binary):
#     img = cv2.imread('tame.jpg', 0)
#     img = np.zeros((1080,1920, 3), np.uint8)
#
#     placement = 10
#     row = 0


def outcode(chucks):
    img = cv2.imread('tame.jpg', 0)
    # cv2.imshow('cara.jpg', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    img = np.zeros((800, 600, 3), np.uint8)

    #img = cv2.line(img, (0,0), (511, 511), (255, 0, 0), 5)

    placement = 10
    row = 0
    for i in chucks:
        vals = i.split(',')
        vals[0] = vals[0][1:]
        vals[1] = vals[1].strip()
        vals[2] = vals[2][:-1].strip()
        print(vals)
        img = cv2.rectangle(img,(placement-10,row),(placement,row+10),(int(vals[2]), int(vals[1]), int(vals[0])),-1)
        if ((placement%800==0)):
            placement = 0
            row+=10
        if (row>600):
            print("Error: Color Matrix Overflow")
            break
        placement += 10

    cv2.imwrite('testing.jpg', img)
    cv2.imshow('testing.jpg', img)

    #img = cv2.circle(img,(447,63), 63, (0,0,255), -1)
    #img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

    #pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
    #pts = pts.reshape((-1,1,2))
    #img = cv2.polylines(img,[pts],True,(0,255,255))

    # font = cv2.FONT_HERSHEY_SIMPLEX
    # cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

    # cv2.namedWindow('cara.jpg', cv2.WINDOW_NORMAL)
    # cv2.imshow('cara.jpg', img)
    # cv2.imwrite('testing.jpg', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return