import re
import mylib.regex as regex

def tagImage(content):
    #s = re.sub(r'<[^>]*?>', '', value)
    matches = re.findall(r'<img [^>]*?\/>', content)
    ls = []
    for m in matches:
        src = re.findall(r'src=\"([^\"]*)\"', m)
        #src = src.replace("src=\"","").replace("\"","")
        ls = ls + [src[0]]
    return ls



def tagLink(content):
    #s = re.sub(r'<[^>]*?>', '', value)
    matches = re.findall(r'<a [^>]*?\>', content)
    ls = []
    for m in matches:
        src = re.findall(r'href=\"([^\"]*)\"', m)
        #src = src.replace("src=\"","").replace("\"","")
        if len(src) > 0:
            ls = ls + [src[0]]
    return ls

