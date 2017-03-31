from urllib import request
from mylib import accents

def download(domain, url):
    full_url = domain
    if url != "":
        full_url = domain + "/" + url
    s = request.urlopen(full_url)
    r = s.read()
    return r

def downloadLinkContent(domain, url):
    full_url = domain + "/" + url
    s = ""
    with request.urlopen(domain + "/" + url) as f:
        s = f.read().decode("utf-8")
    return accents.remove_accents(s)

def downloadUrl(url):
    full_url = url
    s = request.urlopen(full_url).read()
    s = s.decode("utf-8")
    return s

def post(url, values):
    data = request.urlencode(values)
    #req = request(url, data)
    #rsp = request.urlopen(req)
    #content = rsp.read()
    #return content
    return None