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

# Open database connection
db = MySQLdb.connect("localhost","thai","Baotue@123","realtate" )
cursor = db.cursor()
cursorPlace = db.cursor()
cursorI = db.cursor()
cursor.execute("select HouseId,Lng,Lat from HouseRaw1 where Flag1=0 limit 0,1000")
houses = cursor.fetchall()
placeId = 1;
for house in houses:
    houseId = house[0]
    print(houseId)
    long = house[1]
    lat = house[2]
    if long == None or lat == None:
        continue
    long = str(long).strip()
    lat = str(lat).strip()
    points = mapapi.findNearBy(lat, long, 500, map_key)
    if points == None:
       print("MapApi over query limit daily")
       break

    #nql = "match (h:House {id: \""+house["id"]+"\"})\n"
    print(lat, long, len(points))
    for p in points:
        #print(p)
        #print(p["name"], p["geometry"]["location"]["lat"], p["geometry"]["location"]["lng"], p["types"])
        try:
            typeOfPoint = getTypeOfPoint(p)
            point = {
                "name":accents.remove_accents(p["name"]),
                "lat":p["geometry"]["location"]["lat"],
                "long": p["geometry"]["location"]["lng"],
                "place_id":p["place_id"],
                "vicinity":accents.remove_accents(p["vicinity"]),
                "types":typeOfPoint
            }

            exists = mysqlapi.queryCursor(cursor,"select count(*) from POI where PlaceId='{placeId}'".format(placeId=point["place_id"]))[0]
            if exists==0:
               sjson = json.dumps(p)
               filename = place_path + "/" +point["place_id"]
               fileapi.writeFile(filename, sjson)

            cursorI.execute(
                "insert into NearBy values('{houseId}','{placeId}')".format(houseId=houseId, placeId=point["place_id"]))
            cursorI.execute(
                "update HouseRaw1 set Flag1=1 where HouseId="+str(houseId))

            '''
            nPlace = cursorPlace.execute("select POIId from POI where PlaceId='" + point["place_id"] + "'")
            if nPlace == 0:
                cursorI.execute("insert into POI values('{POIId}','{PlaceName}','{Lat}','{Lng}','{PlaceId}','{Vinicity}','{PlaceType}')".format(
                    POIId=placeId,PlaceName=point["name"],Lat=point["lat"],Lng=point["long"],PlaceId=point["place_id"],Vinicity=point["vicinity"],PlaceType=typeOfPoint
                )
                )
                placeId = placeId + 1
            else:
                place = cursorPlace.fetchone()
                cursorI.execute(
                    "insert into NearBy values('{houseId}','{placeId}')".format(houseId=houseId, placeId=point["place_id"]))
            '''

            db.commit()


        except:
            print("Error: data error = ", point["name"], point["vicinity"])
            pass


db.close()
# print(lat, long, address, price, surface, bedrooms, floors, toilets, interior, onstreet_wide, onstreet_far)




