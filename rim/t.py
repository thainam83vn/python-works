import os
import re
import urllib.request as request
import time
import datetime
import web

domain = "http://batdongsan.com.vn/"
htmls_folder = "/home/thai/Realtate/htmls/folders"
htmls_folder_processed = "/home/thai/Realtate/htmls/folders_processed"
htmls_houses = "/home/thai/Realtate/htmls/houses"
folders = [
    #{"url": "ban-nha-rieng", "from_page":1118, "to_page": 1481}
    #{"url": "ban-nha-mat-pho", "from_page":190, "to_page": 621}#85
    #{"url": "ban-nha-biet-thu-lien-ke", "from_page":1, "to_page": 307}#85
    #{"url": "ban-can-ho-chung-cu", "from_page":1, "to_page": 1736}
    #{"url": "ban-dat-nen-du-an", "from_page":1, "to_page": 555}
    {"url": "ban-dat", "from_page":1, "to_page": 1206}




]


def downloadLink(filename, domain, url):
    fw = open(filename, 'w')
    #print(url + "\n")
    s = web.downloadLinkContent(domain, url)
    fw.write(s)
    fw.close()

for folder in folders:
    for i in range(folder["from_page"], folder["to_page"]):
        print(datetime.datetime.now(), folder["url"] + "-p" + str(i))
        if os.path.isfile(htmls_folder + "/" + folder["url"] + "-p" + str(i)) == False:
            content = downloadLink(htmls_folder + "/" + folder["url"] + "-p" + str(i), domain, folder["url"] + "/p" + str(i))