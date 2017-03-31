import os
import re
import time
import datetime
import json
from neomodel import (StructuredNode, StringProperty, IntegerProperty, RelationshipTo, RelationshipFrom)
from models import House, Mapper
from mylib import pymysqlapi


def searchStringG1(pattern, s):
    m = re.search(pattern, s)
    if m != None:
        return m.group(1)
    return ""

data = pymysqlapi.queryToDictionary('HouseRaw2','HouseId,HouseType,Lat,Lng,Price,YearBuild,NewRate,Surface,Bedrooms,Floors,Toilets,Interior,Address', '')
mapper = Mapper()

for listitem in data:

    #houseId = listitem["HouseId"]
    #address = listitem["Address"]
    #lat = listitem["Lat"]
    #long = listitem["Lng"]
    #price = listitem["Price"]
    #surface = listitem["Surface"]
    #bedrooms = listitem["Bedrooms"]
    #floors = listitem["Floors"]
    #toilets = listitem["Toilets"]
    #interior = listitem["Interior"]
    #newrate = listitem["NewRate"]
    #type = listitem["HouseType"]


    #h = House(houseId=houseId, address=address, lat=lat, long=long, price=price,
    #          surface=surface, bedrooms=bedrooms, floors=floors, toilets=toilets,
    #          interior=interior, type=type, newrate=newrate).save()
    h = mapper.Map(listitem, House)
    h.save()

    print(h.HouseId)



