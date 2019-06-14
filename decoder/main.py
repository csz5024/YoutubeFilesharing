import numpy as np
import cv2
import time
from mss import mss
from PIL import Image
from PIL import ImageGrab
import ascii2color
from ctypes import windll
dc=windll.user32.GetDC(0)

#20736 characters per page

#reduced time by a factor of 10
def getpixel(x,y):
    return windll.gdi32.GetPixel(dc,x,y)

def get_pixel_color(ix, iy):
    return ImageGrab.grab().load()[ix,iy]
    # top left pixel at 30, 50
    # bottom right pixel at 930, 1010

# while True:
#     print(get_pixel_color(7,30))

x=7
y=30
counter = 0
repeater = 0
message = []
uniquecolors = {}
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
start = time.time()
for i in range(0,108):
    for j in range(0,192):
        #print("%d: %s // %s" % (counter, getpixel(x,y), ascii2color.colorref2rgb(getpixel(x,y))))
        # if get_pixel_color(x,y) not in uniquecolors.values():
        #     key = "c"+str(i)+str(j)
        #     uniquecolors[key] = get_pixel_color(x,y)
        if getpixel(x,y) == 0:
            repeater+=1
            break
        else:
            if ascii2color.colorref2rgb(getpixel(x,y)) != None:
                message.append(ascii2color.colorref2rgb(getpixel(x,y)))
        x+=10
        counter+=1
    if repeater > 1:
        break
    x=0
    y+=10
end=time.time()
print('')
print(end-start)
# print('')
# print("No. of unique Colors: %d" % (len(uniquecolors)))
# print('')
# print(uniquecolors)
print('')
print(''.join(message))

# while(True):
#         # 800x600 windowed mode
#         printscreen = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
#         cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
#         time.sleep(.02) # should tune to 10fps exactly
#         #print(get_pixel_color(30, 50))
#         #print(get_pixel_color(930,1010))
#         if cv2.waitKey(25) & 0xFF == ord('q'):
#             cv2.destroyAllWindows()
#             break

