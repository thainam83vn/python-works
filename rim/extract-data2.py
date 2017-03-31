import os
import re
import time
import datetime
import json
from neo4j.v1 import GraphDatabase, basic_auth
import nod4j

def searchStringG1(pattern, s):
    m = re.search(pattern, s)
    if m != None:
        return m.group(1)
    return ""


driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "Baotue@123"))
session = driver.session()


htmls_houses = "../htmls/houses"
htmls_houses_processed = "../htmls/houses_processed"
index = 0
types = [
    {"url": "ban-nha-rieng", "from_page":1118, "to_page": 1481, "typeid" : 1},
    {"url": "ban-nha-mat-pho", "from_page":190, "to_page": 621, "typeid" : 2},
    {"url": "ban-nha-biet-thu-lien-ke", "from_page":1, "to_page": 307, "typeid" : 3},
    {"url": "ban-can-ho-chung-cu", "from_page":1, "to_page": 1736, "typeid" : 4},
    {"url": "ban-dat-nen-du-an", "from_page":1, "to_page": 555, "typeid" : 5},
    {"url": "ban-dat", "from_page":1, "to_page": 1206, "typeid" : 6}
]

def findType(folder):
    for f in types:
        if str(folder).startswith(f["url"]):
            return f["typeid"]

while 1:
    folders = os.listdir(htmls_houses)
    for folder in folders:
        files = os.listdir(htmls_houses + "/" + folder)
        type = findType(folder)

        i = 0
        for filename in files:
            full_path = htmls_houses + "/" + folder + "/" + filename
            index = index + 1
            f = open(full_path)
            content = f.read()

            address = searchStringG1("hdAddress\" value=\"(.*)\"", content)
            lat = searchStringG1("hdLat\" value=\"(.*)\"", content)
            long = searchStringG1("hdLong\" value=\"(.*)\"", content)
            price = searchStringG1("<b>\s*Gia:\s*</b>\s*.*\s*<strong>\s*(.*)&nbsp;\s*</strong>", content)
            surface = searchStringG1("<b>\s*Dien tich:\s*</b>\s*.*\s*<strong>\s*(.*)\s*</strong>", content)
            bedrooms = searchStringG1("So phong ngu\s*</div>\s*<div class=\"right\">\s*(.*)\s*</div>", content)
            floors = searchStringG1("So tang\s*</div>\s*<div class=\"right\">\s*(\d*)\s*\(tang\)\s*</div>", content)
            toilets = searchStringG1("So toilet\s*</div>\s*<div class=\"right\">\s*(.*)\s*</div>", content)
            interior = searchStringG1("Noi that\s*</div>\s*<div class=\"right\">\s*(.*)\s*</div>", content)
            onstreet_wide = searchStringG1("Mat tien\s*</div>\s*<div class=\"right\">\s*(.*)\s*\(m\)\s*</div>", content)
            onstreet_far = searchStringG1("Duong vao\s*</div>\s*<div class=\"right\">\s*(.*)\s*\(m\)\s*</div>", content)


            house = {
                "id": index,
                "address": address.replace(",","-").replace(":","="),
                "lat": lat,
                "long": long,
                "price": price,
                "surface": surface,
                "bedrooms": bedrooms,
                "floors": floors,
                "toilets": toilets,
                "interior": interior.replace(",","-").replace(":","="),
                "onstreet_width": onstreet_wide.replace(",","-").replace(":","="),
                "onstreet_distance": onstreet_far.replace(",","-").replace(":","="),
                "type": type
            }

            s = nod4j.jsonDump(house)

            print(s)
            nql = "merge (h" + str(index) + ":House "+s+")"

            session.run(nql)

            #save_folder = htmls_houses_processed + "/" + folder
            #if os.path.isdir(save_folder) == False:
            #    os.mkdir(save_folder)
            #new_path = save_folder + "/" + filename
            #os.rename(full_path, new_path)
            print(index, filename + "\n")
            i = i + 1
            # print(house)

        if index > 100:
            break

    break
session.close()
# print(lat, long, address, price, surface, bedrooms, floors, toilets, interior, onstreet_wide, onstreet_far)



