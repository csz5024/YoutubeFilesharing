import ascii2color as a2c
import gridiron as gd
import binascii
import cv2
import numpy as np

outbuf = []
f=open("inputfile.txt", "r")

count = 0
song=open("06 NEW MAGIC WAND.mp3", "rb")
hexd = b'aa'

img = cv2.imread('tame.jpg', 0)
img = np.zeros((600, 800, 3), np.uint8)
placement = 5
row = 0
counter = 0
while hexd != b'':
    byte = song.read(1)
    hexd = binascii.hexlify(byte)
    decm = int(hexd,16)
    binary = bin(decm)[2:].zfill(8)
    print("%s %s %s" % (hexd, decm, binary))

    vals = a2c.bin2color(str(binary))
    img = cv2.rectangle(img, (placement - 5, row), (placement, row + 5),
                        (int(vals[2]), int(vals[1]), int(vals[0])), -1)
    if ((placement % 800 == 0)):
        placement = 0
        row += 5
    if (row > 600):
        #print("Error: Color Matrix Overflow")
        filename = "song\cesting"+str(counter)+".jpg"
        cv2.imwrite(filename, img)
        #cv2.imshow(filename, img)
        img = cv2.imread('tame.jpg', 0)
        img = np.zeros((600, 800, 3), np.uint8)
        counter+=1
        row=0
        #break
    placement += 5

# cv2.imwrite('testing.jpg', img)
# cv2.imshow('testing.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()


# for x in f:
#     #print("Enter a String: ")
#     converted = a2c.text2color(x)
#     #print(converted)
#     outbuf=outbuf+converted

#gd.outcode(outbuf)
