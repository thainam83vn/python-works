# -*- coding: utf-8 -*-
import os
import re
import time
import datetime
import json
import accents
import MySQLdb
import mapapi
import fileapi
import mysqlapi
import accents

place_path = "/home/thai/Realtate/htmls/places"
processed_place_path = "/home/thai/Realtate/htmls/places_processed"
map_key = "AIzaSyC9VVLu7knKJrANG81A6Qcr9e21lmkAXQo"
#map_key="AIzaSyB1IOO-u4a8KU4hfGtIbbyCdTphiKDJuI0"
dic = [
        {"key": "School", "values": ["truong", "thpt", "thcs"]},
        {"key": "University", "values": ["dai hoc", "hoc vien"]},
        {"key": "Store", "values": ["cua hang", "shop"]},
        {"key": "Market", "values": ["cho "]},
        {"key": "SuperMarket", "values": ["sieu thi"]},
        {"key": "Park", "values": ["cong vien"]},
        {"key": "Transportation", "values": ["ben xe"]},
        {"key": "Bank", "values": ["ngan hang", "bank"]},
        {"key": "Restaurant", "values": ["nha hang", "restaurant"]},
        {"key": "Entertainment", "values": ["khu vui choi"]},
        {"key": "Hospital", "values": ["benh vien"]},
        {"key": "Town", "values": ["khu do thi"]},
        {"key": "Community", "values": ["khu dan cu", "chung cu"]},
        {"key": "Temple", "values": ["chua", "nha tho"]},
        {"key": "Post", "values": ["buu dien"]},
        {"key": "Theater", "values": ["nha hat"]},
        {"key": "Cinema", "values": ["cinema"]},
        {"key": "Factory", "values": ["nha may", "xi nghiep"]},
        {"key": "Political", "values": ["ubnd"]},
        {"key": "Police", "values": ["cong an"]},
        {"key": "Army", "values": ["quan doi", "quan khu"]},
        {"key": "Club", "values": ["clb", "cau lac bo","nha van hoa","nvh"]}
    ];

def getTypeOfPoint(point):
    try:
        name = str(point["name"]).lower()
        for item in dic:
            for value in item["values"]:
                if value in name:
                    return item["key"]

        for t in point["types"]:
            if t == "school":
                return "School"
            if t == "store":
                return "Store"
            if t == "political":
                return "Political"
            if t == "market":
                return "Market"
            if t == "park":
                return "Park"
            if t == "restaurant":
                return "Restaurant"
        return "Other"
    except:
        pass
    return "Other"

def removeSpecial(s):
   return accents.remove_accents(s.encode('utf-8')).replace("'", "''")

# Open database connection
db = MySQLdb.connect("localhost","thai","Baotue@123","realtate" )
cursorI = db.cursor()
cursorP = db.cursor()
place_path = "/home/thai/Realtate/htmls/places"
files = os.listdir(place_path)
i = 0
for file in files:
    content = fileapi.readFile(place_path + "/" + file)
    point = json.loads(content)
    exists = mysqlapi.queryCursorFirst(cursorP,"select count(*) from POI where PlaceId='{placeId}'".format(placeId=point["place_id"]))[0]
    print(exists)
    if exists == 0:
       placeType = getTypeOfPoint(point)
       sql = "insert into POI(PlaceId,PlaceName,Lat,Lng,Vicinity,PlaceType) values('{placeId}','{placeName}','{lat}','{lng}','{vinicity}','{placeType}')".format(placeId=point["place_id"],placeName=removeSpecial(point["name"]),lat=point["geometry"]["location"]["lat"],lng=point["geometry"]["location"]["lng"],vinicity=removeSpecial(point["vicinity"]),placeType=placeType)
       print(sql)
       cursorI.execute(sql)
       db.commit()
       os.rename(place_path+"/"+file,processed_place_path+"/"+file)
       i = i + 1
       print(i, file)

db.close()
# print(lat, long, address, price, surface, bedrooms, floors, toilets, interior, onstreet_wide, onstreet_far)




