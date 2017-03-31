from mylib import web
from mylib import htmltag
from mylib import image

url = "http://158.69.54.151:16969/h/f20da218260ed008119a058f9c794e7415208bd5-570504-1280-1919-jpg/keystamp=1480566000-3a65826e4c/TBA_Alexa_Kee_92.jpg"
size = image.imageSizeFast(url)
print(size)