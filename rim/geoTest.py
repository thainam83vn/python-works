from mylib import mapapi
from mylib import pymysqlapi

def classifyRegion():
    houses = pymysqlapi.queryToDictionary("HouseRaw2", "HouseId,Lat,Lng", "RegionId is NULL")
    regions = pymysqlapi.queryToDictionary("Region", "RegionId,Lat,Lng", "")
    for h in houses:
        minDistance = 10000
        minRegionId = 0
        for r in regions:
            distance = mapapi.geopyDistance(h["Lat"], h["Lng"], r["Lat"], r["Lng"])
            if distance < minDistance:
                minDistance = distance
                minRegionId = r["RegionId"]
        pymysqlapi.execSql("update HouseRaw2 set RegionId=" + str(minRegionId) + " where HouseId=" + str(h["HouseId"]))
        print(h["HouseId"])

def computeRegionPrice():
    pymysqlapi.execSql("update HouseRaw2 set TotalFloors=Floors+1")
    pymysqlapi.execSql("update HouseRaw2 set PricePerM2=Price/(Surface + Floors*Surface/3) where Surface*TotalFloors<>0")
    data = pymysqlapi.query("select RegionId, sum(PricePerM2)/count(PricePerM2) as PricePerM2 from HouseRaw2 where PricePerM2<>0 group by RegionId")
    for row in data:
        id = row[0]
        price = row[1]
        pymysqlapi.execSql("update Region set PricePerM2=" + str(price) + " where RegionId=" + str(id))
        print(id)

def exportCsv():
    pymysqlapi.queryToDictionary2("")


#classifyRegion()
computeRegionPrice()
