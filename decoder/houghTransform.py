import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('norfnorf.PNG')
#gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
edges = cv2.Canny(img, 50, 2000, apertureSize=7)

# plt.subplot(121), plt.imshow(img, cmap='gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),
plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()


# # probabilistic hough lines
# minLineLength = 100
# maxLineGap = 10
# lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength, maxLineGap)
# for x1, y1, x2, y2 in lines[0]:
#     cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# hough lines
# lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
# for rho, theta in lines[0]:
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a*rho
#     y0 = b*rho
#     x1 = int(x0 + 1000*(-b))
#     y1 = int(y0 + 1000*(a))
#     x2 = int(x0 - 1000*(-b))
#     y2 = int(y0 - 1000*(a))
#
#     cv2.line(img, (x1, y1), (x2, y2), (0,0,255), 2)

# cv2.imwrite('houghlinesP.jpg', img)
# cv2.imshow('houghlinesP.jpg', img)
# cv2.imshow('houghlinesP.jpg', edges)
# cv2.waitKey(0)