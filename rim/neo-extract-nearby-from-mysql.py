import os
import re
import time
import datetime
import json
from mylib import pymysqlapi
from models import House,POI,Mapper

dataHouse = pymysqlapi.queryToDictionary("HouseRaw2","HouseId","")
for h in dataHouse:
    houseId = h["HouseId"]
    house = House.nodes.get(HouseId=houseId)
    dataNear = pymysqlapi.queryToDictionary("NearBy","PlaceId","HouseId=" + str(houseId))
    for near in dataNear:
        placeId = near["PlaceId"]
        place = POI.nodes.get(PlaceId=placeId)
        rel = house.POI.connect(place)
        rel.save()
        print("Save ", houseId, placeId)





