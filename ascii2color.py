import string
import math

# Compiles a dictionary of ascii characters and their corresponding hex values

s2h = {}
for i in string.printable:
    dec = ord(i)
    #hexi = hex(dec)
    temp = '' + bin(dec)
    while len(temp) < 10:
        temp = temp[:2] + '0' + temp[2:]

    s2h[i] = temp

def text2color(str):
    rgb8to24 = []
    for i in str:
        r = (int(s2h[i][2:5], 2)) * 255 / 7
        g = (int(s2h[i][5:8], 2)) * 255 / 7
        b = (int(s2h[i][8:], 2)) * 255 / 7
        rgb8to24.append("(%d, %d, %d)" % (r, g, b))
        #print(int(s2h[i][2:5], 2), int(s2h[i][5:8], 2), int(s2h[i][8:], 2))

    return rgb8to24

def bin2color(bin):
    r = (int(bin[0:3], 2)) * 255 / 7
    g = (int(bin[3:6], 2)) * 255 / 7
    b = (int(bin[6:8], 2)) * 255 / 7

    return (r, g, b)

#colorref = r + g<<8 + b<<16
# 0x00BBGGRR
def colorref2rgb(color):
    #dec to hex, to rgb
    hcolor = hex(color) + ""
    hcolor=str(hcolor)
    while(len(hcolor)<8):
        hcolor=hcolor[:2]+"0"+hcolor[2:]
    b="0x"+hcolor[2:4]
    g="0x"+hcolor[4:6]
    r="0x"+hcolor[6:8]

    #print((int(r,16),int(g,16),int(b,16)))
    letter = color2text((int(r,16),int(g,16),int(b,16)))
    return letter


def color2text(str):
    #print(s2h)
    r = round(str[0] * 7 / 255)
    g = round(str[1] * 7 / 255)
    b = round(str[2] * 7 / 255)
    #print(r,g,b)

    temp = '' + bin(r)
    while len(temp)<5:
        temp=temp[:2]+'0'+temp[2:]
    r=temp[2:]
    temp = '' + bin(g)
    while len(temp) < 5:
        temp = temp[:2] + '0' + temp[2:]
    g = temp[2:]
    temp = '' + bin(b)
    while len(temp) < 4:
        temp = temp[:2] + '0' + temp[2:]
    b = temp[2:]
    letter='0b'+r+g+b
    #print(letter)

    #print(s2h)
    text = []
    for letterf,dec in s2h.items():
        #print(dec,letter)
        if dec == letter:
            return letterf


    #print(bin(r),bin(g),bin(b))



# print(s2h)
# text2hex("hello")
