from PIL import Image
from urllib import request
import io
#from StringIO import StringIO


def imageSize(url):
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
    return {'width': width, 'height': height}

def readStream(stream, b):
    result = []
    for i in range(0, b):
        if stream['cursor'] >= len(stream['data']):
            break
        result = result + [stream['data'][stream['cursor']]]
        stream['cursor'] = stream['cursor'] + 1

    return bytes(result)

def imageSizeFast(url):
    f = request.urlopen(url)
    header = f.read(1024)
    f.close()
    stream = {'data': header, 'cursor': 0}
    b1 = readStream(stream, 1)
    i = 0
    while i < 1024:
        #print(b1)
        if b1 == b'\xff':
            b2 = readStream(stream, 1)
            #print(b1, b2)
            if b2 == b'\xc0':
                break
            b1 = b2
        else:
            b1 = readStream(stream, 1)
        i = i + 1
    if (i < 1024):
        readStream(stream, 3)
        h = readStream(stream, 2)
        w = readStream(stream, 2)
        height = int.from_bytes(h, byteorder='big')
        width = int.from_bytes(w, byteorder='big')
        return {'width': width, 'height': height}
    else:
        return {'width': 0, 'height': 0}