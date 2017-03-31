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

#for folder in folders:
#    for i in range(folder["from_page"], folder["to_page"]):
#        print(datetime.datetime.now(), folder["url"] + "-p" + str(i))
#        content = downloadLink(htmls_folder + "/" + folder["url"] + "-p" + str(i), domain, folder["url"] + "/p" + str(i))

for folder in folders:
    fd = folder["url"] + "-p"
    index = 1
    error = 0
    for p in range(1,folder["to_page"]):
        filename = fd + str(p)
        #print(datetime.datetime.now(), "Processing " + filename,index)
        full_path = htmls_folder+"/"+filename
        if os.path.isfile(full_path) == False:
            continue

        f = open(full_path)
        content = f.read()
        pattern = re.compile("search-productItem'>\s*<div class='p-title'>\s*<a href='(.*)' title")
        pos = 0
        while 1:
            m = pattern.search(content, pos)
            if (m != None):
                url = m.group(1)
                url_arr = url.split('/')

                if (pos >= m.end()):
                    break;
                pos = m.end()
                #print(datetime.datetime.now(), "count=", index, "error=", error, pos, url_arr)

                save_folder = htmls_houses + "/" + url_arr[1]
                if os.path.exists(save_folder) == False:
                    os.mkdir(save_folder)
                save_file = save_folder + "/" + url_arr[2] + ".html"
                if os.path.exists(save_file) == False:
                    try:
                        print(datetime.datetime.now(), "Downloading " + url)
                        downloadLink(save_file, domain, url)
                        print(datetime.datetime.now(), "Finish Download " + url)
                        index = index + 1
                        time.sleep(10)
                    except (RuntimeError, TypeError, NameError):
                        error = error + 1
                        pass
                        continue
                #else:
                    #print(datetime.datetime.now(), save_file + " already processed.")

            else:
                break
        new_path = htmls_folder_processed + "/" + filename
        os.rename(full_path, new_path)





