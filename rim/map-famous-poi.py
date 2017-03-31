# -*- coding: utf-8 -*-
import os
import re
import time
import datetime
import json

import mylib.mapapi as mapapi
import mylib.fileapi as fileapi
import mylib.pymysqlapi as mysqlapi

from models import NearByFamousPOI


house_json_path = "/home/thai/workspace/data/rim/jsons/famous-poi"

map_keys = [
    "AIzaSyCoUX9Fvr4ulO304CDYCWfUm6wpjH7JdUU",
    "AIzaSyA8WhxLY_S6LlJP3tEDJvyfCPhGNTg9g0g",
    "AIzaSyBGb53IZcPtJijHcUISu4RF7bw5ryHqd3U",
    "AIzaSyAilazpzNCe4YVQEBMJ_1wwFokpbFDGJfY",
    "AIzaSyApdxnPdEXhuWAe6rHiexJchIJ6d7CEy4o",
    "AIzaSyD4vRws4VQXtZTKzDnxENj9QCpT91k2NpQ",
    "AIzaSyDfNys32D1tZgiTFBVXkU7ywG8yHt5xSZg"
]

#map_key = "AIzaSyCoUX9Fvr4ulO304CDYCWfUm6wpjH7JdUU"
#map_key = "AIzaSyA8WhxLY_S6LlJP3tEDJvyfCPhGNTg9g0g"
#map_key = "AIzaSyBGb53IZcPtJijHcUISu4RF7bw5ryHqd3U"
#map_key = "AIzaSyAilazpzNCe4YVQEBMJ_1wwFokpbFDGJfY"
#map_key = "AIzaSyApdxnPdEXhuWAe6rHiexJchIJ6d7CEy4o"
#map_key ="AIzaSyD4vRws4VQXtZTKzDnxENj9QCpT91k2NpQ"
#map_key = "AIzaSyDfNys32D1tZgiTFBVXkU7ywG8yHt5xSZg"


# Open database connection
def getAddressComponent(addr, type):
    for component in addr:
        if type in component["types"]:
            return component["long_name"]
    return None

houses = mysqlapi.queryToDictionary("HouseRaw2","HouseId,Lng,Lat","Lat<>'' and Lng<>'' and GetFamousPOI=0")
famousPOIs = mysqlapi.queryToDictionary("FamousPOI","PlaceId,Lng,Lat","")

ikey = 0
i = 0
while i < len(houses):
    house = houses[i]
    map_key = map_keys[ikey]
    print(house["HouseId"])
    address1 = {"lat": house["Lat"], "lng": house["Lng"]}
    addresses2 = []
    for poi in famousPOIs:
        addr2 = {"placeId": poi["PlaceId"], "lat": poi["Lat"], "lng": poi["Lng"]}
        addresses2 = addresses2 + [addr2]
    try:
        addresses2 = mapapi.getDistance(address1, addresses2, map_key)
    except NameError as ex:
        print(ex)
        ikey = ikey + 1
        continue


    for addr2 in addresses2:
        if 'distance' in addr2:
            near = NearByFamousPOI(HouseId=house["HouseId"], PlaceId=addr2["placeId"], Distance=addr2['distance'], Duration=addr2['duration'])
            mysqlapi.save(near)
    mysqlapi.execSql("update HouseRaw2 set GetFamousPOI=1 where HouseId=" + str(house['HouseId']))
    i = i + 1


    #sql = "insert into NearByPOI(HouseId, PlaceId, Distance, Duration) values('{HouseId}'"






