# -*- coding: utf-8 -*-
import os
import re
import time
import datetime
import json
import random
import mylib.pymysqlapi as mysqlapi


class HouseRaw3():
    def __init__(self, h):
        self.HouseId = h["HouseId"]
        self.HouseType = h["HouseType"]
        self.Lat = h["Lat"]
        self.Lng = h["Lng"]
        self.Price= h["Price"]
        self.YearBuild = h["YearBuild"]
        self.Surface = h["Surface"]
        self.Bedrooms = h["Bedrooms"]
        self.Floors = h["Floors"]
        self.Toilets = h["Toilets"]
        self.Interior = h["Interior"]
        self.NewRate = h["NewRate"]
        self.Address = h["Address"]
        self.PricePerM2 = h["PricePerM2"]
        self.RegionId = h["RegionId"]
        self.TotalFloors = h["TotalFloors"]
        self.Fake = "1"

colsHouseRaw2 = 'HouseId,HouseType,Lat,Lng,Price,YearBuild,Surface,Bedrooms,Floors,Toilets,Interior,NewRate,Address,PricePerM2,RegionId,TotalFloors'

houses = mysqlapi.queryToDictionary("HouseRaw2",colsHouseRaw2,'')

i = 0
id = 1
while i < len(houses):
    house = houses[i]
    print("clone house " + str(house["HouseId"]) + " total=" + str(id))

    for m in range(-50, 50):
        fakeHouse = HouseRaw3(house)
        fakeHouse.Surface = fakeHouse.Surface + m;
        if fakeHouse.PricePerM2 != None:
            x = random.randint(0, int(fakeHouse.PricePerM2))
            if abs(m) < 10:
                rate = 0.8
            else:
                if abs(m) < 20:
                    rate = 0.6
                else:
                    if abs(m) < 30:
                        rate = 0.5
                    else:
                        rate = 0.3
            fakeHouse.Price = float(fakeHouse.Price) + float(m) * float(fakeHouse.PricePerM2) * rate + x
            fakeHouse.HouseId = str(id)
            mysqlapi.save2(fakeHouse)
            id = id + 1

    i = i + 1








