import os
import re
import time
import datetime
import json
from mylib import pymysqlapi
from models import POI,Mapper

dataPOI = pymysqlapi.queryToDictionary("POI","PlaceId,PlaceName,Lat,Lng,Vicinity,PlaceType","")
mapper = Mapper()

for row in dataPOI:
    place = mapper.Map(row, POI)
    place.save()
    print("Save ", place.PlaceId)





