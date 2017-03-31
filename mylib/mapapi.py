from mylib import web
from geopy.distance import vincenty
import json


def findNearBy(lat, long, radius, key):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+lat+","+long+"&radius="+str(radius)+"&key="+key
    #print(url)
    data = json.loads(web.downloadUrl(url))
    if data["status"] == "OVER_QUERY_LIMIT":
       return None
    return data["results"]


def findLocation(lat, long, key):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address={lat},{lng}&key={key}".format(lat=lat,lng=long,key=key)
    #print(url)
    data = json.loads(web.downloadUrl(url))
    if data["status"] == "OVER_QUERY_LIMIT":
        raise NameError('OVER_QUERY_LIMIT')
    if len(data["results"]) > 0:
        return data["results"][0]["address_components"]
    return None

def getDistance(address1, addresses2, key):
    addressList2 = ""
    for add in addresses2:
        if addressList2 == "":
            addressList2 = add['lat'] + "," + add['lng']
        else:
            addressList2 = addressList2 + "|" + add['lat'] + "," + add['lng']

    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={address1}&destinations={addresses2}&key={key}".format(address1=address1['lat']+","+address1['lng'],addresses2=addressList2,key=key)
    #print(url)
    data = json.loads(web.downloadUrl(url))
    if data["status"] == "OVER_QUERY_LIMIT":
        raise NameError('OVER_QUERY_LIMIT')
    if len(data['rows']) > 0:
        elements = data['rows'][0]['elements']

        i = 0
        for add in addresses2:
            r = elements[i]
            if r["status"] == "ZERO_RESULTS":
                print("ZERO_RESULTS")
                continue
            add['distance'] = r['distance']['value']
            add['duration'] = r['duration']['value']
            i = i + 1

    return addresses2

def geopyDistance(lat1, lng1, lat2, lng2):
    p1 = (lat1, lng1)
    p2 = (lat2, lng2)
    return vincenty(p1, p2).miles