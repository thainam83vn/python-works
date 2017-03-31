import os
import re
import urllib.request as request
import time
import datetime
import json
import mapapi
import mysql

key = "AIzaSyC9VVLu7knKJrANG81A6Qcr9e21lmkAXQo"

houses = mysql.query("select houseid, lat,lng from HouseRaw1")
print(houses)

#results = mapapi.findNearBy("10.828381050730991", "106.63944945767207", 500, key)
#for p in results:
#    print(p)
#    print(json.dumps(p))
