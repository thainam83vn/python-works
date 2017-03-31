# -*- coding: utf-8 -*-
import os
import re
import time
import datetime
import json

import mylib.mapapi as mapapi
import mylib.fileapi as fileapi
import mylib.mysqlapi as mysqlapi

house_json_path = "/home/thai/workspace/data/rim/jsons/houses"

map_key = "AIzaSyDg87khCnyYKbC0NCAfF4IELWcjoewVFuU"
#map_key = "AIzaSyCoUX9Fvr4ulO304CDYCWfUm6wpjH7JdUU"
#map_key = "AIzaSyAFeTGX-oDnjfvqIhzoAugQmZye0UlQUyk"

# Open database connection
def getAddressComponent(addr, type):
    for component in addr:
        if type in component["types"]:
            return component["long_name"]
    return None

houses = mysqlapi.query("select HouseId,Lng,Lat from HouseRaw1 where Flag2=0 and Lat<>'' and Lng<>''")
for house in houses:
    houseId = house[0]

    long = house[1]
    lat = house[2]
    if long == None or lat == None:
        continue
    long = str(long).strip()
    lat = str(lat).strip()
    filename = house_json_path+"/"+str(houseId)+".json"
    if os.path.isfile(filename) == False:
        address = mapapi.findLocation(lat, long, map_key)
        if address == None:
            print(houseId, "Zero result.")
            continue
        saddress=json.dumps(address)
        fileapi.writeFile(filename, saddress)
        print(houseId)
        mysqlapi.execSql("update HouseRaw1 set flag2=1 where HouseId={houseId}".format(
            houseId=houseId
        ))
        print(houseId)

    ''''
    street_number = accents.remove_accents(getAddressComponent(address, "street_number"))
    route = accents.remove_accents(getAddressComponent(address, "route"))
    sublocality = accents.remove_accents(getAddressComponent(address, "sublocality"))
    locality = accents.remove_accents(getAddressComponent(address, "locality"))
    administrative_area_level_1 = accents.remove_accents(getAddressComponent(address, "administrative_area_level_1"))
    country = accents.remove_accents(getAddressComponent(address, "country"))

    print(houseId, street_number, route, sublocality, locality, administrative_area_level_1, country)
    mysqlapi.execSql("update HouseRaw1 set flag2=1,street_number='{street_number}', route='{route}', sublocality='{sublocality}', locality='{locality}', administrative_area_level_1='{administrative_area_level_1}', country='{country}' where HouseId={houseId}".format(
        street_number=street_number,route=route,sublocality=sublocality,locality=locality,administrative_area_level_1=administrative_area_level_1,country=country,houseId=houseId
    ))
    '''

    #nql = "match (h:House {id: \""+house["id"]+"\"})\n"
    #print(lat, long, address)

# print(lat, long, address, price, surface, bedrooms, floors, toilets, interior, onstreet_wide, onstreet_far)




