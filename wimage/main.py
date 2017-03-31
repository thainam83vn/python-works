from mylib import web
from mylib import htmltag
from mylib import image



def biggestImage(content):
    sources = htmltag.tagImage(content)
    #images = []
    max = 0
    maxurl = ""
    for src in sources:
        size = image.imageSizeFast(src)
        if max < size['width']*size['height']:
            max = size['width']*size['height']
            maxurl = src
        #images = images + [{'url': src, 'size': size}]
    #print(images)
    return maxurl

def parenturl(url):
    arr = url.split('/')
    result = arr[0]
    for i in range(1, len(arr) - 1):
        result = result + "/" + arr[i]
    return result

def rooturl(url):
    arr = url.split('/')
    result = arr[0] + '/' + arr[1] + '/' + arr[2]
    return result

def scrapImages(starturl):
    parent = rooturl(starturl)
    currentlist = [starturl]
    processedlist = []
    images = []

    while len(currentlist) > 0:
        url = currentlist[0]
        content = web.downloadUrl(url);
        print(content);
        src = biggestImage(content)
        images = images + [src]
        otherLinks = htmltag.tagLink(content)
        for other in otherLinks:
            if parent in other:
                if other not in currentlist and other not in processedlist:
                    currentlist = currentlist + [other]

        currentlist.remove(url)
        processedlist = processedlist + [url]
        print(currentlist)
        print(images)

    return images
url = "http://g.e-hentai.org/s/42ed25d72d/431194-1"
#url = "http://g.e-hentai.org/g/431194/d8c5684ed9/"
images = scrapImages(url)
print(images)

#url = "http://g.e-hentai.org/s/b038ddb51c/431194-84"

#url = "http://g.e-hentai.org/g/431194/d8c5684ed9/"
#content = web.downloadUrl(url);
#print("content:\n")
#print(content)
#print("matches:\n")

#print(biggestImage(content))
#print(htmltag.tagLink(content))


