import mylib.web as webapi
import mylib.regex as regex
import mylib.fileapi as fileapi
import os
import datetime
import vac.config as config

domain = "http://tieuthuyettinhyeu.hexat.com"


ls = [domain]
oldls = []

while len(ls) > 0:
    for link in ls:
        filename = config.htmls_folder + "/" + link.replace("http://", "").replace("/", "_")
        if os.path.isfile(filename) == True:
            c1 = fileapi.readFile(filename)
        else:
            print(datetime.datetime.now(), "Downloading " + link)
            c1 = webapi.download(link, "")

        fileapi.writeFile(config.htmls_folder+"/" + link.replace("http://","").replace("/","_"), c1)
        newlinks = regex.findAll('<div class="cool"><a href="(.*)">.*</a>', c1)
        for newlink in newlinks:
            if newlink not in oldls:
                ls = ls + [newlink]
        ls.remove(link)
        oldls = oldls + [link]

ls = []


