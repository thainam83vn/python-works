import os
import re
import time
import datetime
import json
import accents
from mylib import mapapi
from neo4j.v1 import GraphDatabase, basic_auth
import nod4j

map_key = "AIzaSyC9VVLu7knKJrANG81A6Qcr9e21lmkAXQo"

driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "Baotue@123"))
session = driver.session()

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
    ];

def getTypeOfPoint(point):
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

houses = session.run("match (n:House) return n")
for h in houses:
    #print(h["name"])
    house = nod4j.jsonLoad(str(h))
    #print(house)


    long = house.get("long")
    lat = house.get("lat")
    if long == None or lat == None:
        continue
    long = str(long).strip()
    lat = str(lat).strip()
    points = mapapi.findNearBy(lat, long, 500, map_key)

    nql = "match (h:House {id: \""+house["id"]+"\"})\n"
    index = 1
    for p in points:
        #print(p)
        #print(p["name"], p["geometry"]["location"]["lat"], p["geometry"]["location"]["lng"], p["types"])
        typeOfPoint = getTypeOfPoint(p)
        point = {
            "name":nod4j.correctString(p["name"]),
            "lat":p["geometry"]["location"]["lat"],
            "long": p["geometry"]["location"]["lng"],
            "place_id":p["place_id"],
            "vicinity":nod4j.correctString(p["vicinity"]),
            "types":typeOfPoint
        }


        s = nod4j.jsonDump(point)
        nql = nql + "merge (p" + str(index) + ":"+typeOfPoint+" " + s + ")\n"
        nql = nql + "merge (h)-[:nearBy {distance: 500}]->(p" + str(index) + ")\n"
        index = index + 1
    session.run(nql)

session.close()
# print(lat, long, address, price, surface, bedrooms, floors, toilets, interior, onstreet_wide, onstreet_far)




