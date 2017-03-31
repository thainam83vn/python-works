from PIL import Image
from urllib import request
import io
#from StringIO import StringIO

url = "http://23.92.212.251:21080/h/b2b5114fd217b366d5fd7e3c64d225f23a822822-888142-1280-1919-jpg/keystamp=1480562400-ee8de95266/TBA_Alexa_Kee_84.jpg"
f = request.urlopen(url)
b1 = f.read(1)
i = 0
while i < 1024:
    #print(b1)
    if b1 == b'\xff':
        b2 = f.read(1)
        #print(b1, b2)
        if b2 == b'\xc0':
            break
        b1 = b2
    else:
        b1 = f.read(1)
    i = i + 1
f.read(3)
h = f.read(2)
w = f.read(2)
f.close()
#h = (h << 8) + f.read(1)
height = int.from_bytes(h, byteorder='big')
width = int.from_bytes(w, byteorder='big')
#print(w,h)
print(width, 'x', height)

#s = f.read(512).decode('ISO-8859-1')
#print(s)
#print(Image.open(s).size)