import os
import regex
import MySQLdb
import time
import datetime

# Open database connection
db = MySQLdb.connect("localhost","thai","Baotue@123","realtate" )
cursor = db.cursor()

htmls_houses = "../htmls/houses"
htmls_houses_processed = "../htmls/houses_processed"
index = 0
while 1:
    folders = os.listdir(htmls_houses)
    for folder in folders:
        files = os.listdir(htmls_houses + "/" + folder)

        i = 0
        for filename in files:
            full_path = htmls_houses + "/" + folder + "/" + filename
            index = index + 1
            f = open(full_path)
            content = f.read()

            address = regex.searchStringG1("hdAddress\" value=\"(.*)\"", content)
            lat = regex.searchStringG1("hdLat\" value=\"(.*)\"", content)
            long = regex.searchStringG1("hdLong\" value=\"(.*)\"", content)
            price = regex.searchStringG1("<b>\s*Gia:\s*</b>\s*.*\s*<strong>\s*(.*)&nbsp;\s*</strong>", content)
            surface = regex.searchStringG1("<b>\s*Dien tich:\s*</b>\s*.*\s*<strong>\s*(.*)\s*</strong>", content)
            bedrooms = regex.searchStringG1("So phong ngu\s*</div>\s*<div class=\"right\">\s*(.*)\s*</div>", content)
            floors = regex.searchStringG1("So tang\s*</div>\s*<div class=\"right\">\s*(\d*)\s*\(tang\)\s*</div>", content)
            toilets = regex.searchStringG1("So toilet\s*</div>\s*<div class=\"right\">\s*(.*)\s*</div>", content)
            interior = regex.searchStringG1("Noi that\s*</div>\s*<div class=\"right\">\s*(.*)\s*</div>", content)
            onstreet_wide = regex.searchStringG1("Mat tien\s*</div>\s*<div class=\"right\">\s*(.*)\s*\(m\)\s*</div>", content)
            onstreet_far = regex.searchStringG1("Duong vao\s*</div>\s*<div class=\"right\">\s*(.*)\s*\(m\)\s*</div>", content)

            house = {
                "address":address,
                "lat":lat,
                "long":long,
                "price":price,
                "surface":surface,
                "bedrooms":bedrooms,
                "floors":floors,
                "toilets":toilets,
                "interior":interior,
                "onstreet_width": onstreet_wide,
                "onstreet_distance":onstreet_far
            }
            #print(house)
            # execute SQL query using execute() method.
            sql = "insert into HouseRaw1(Address,Lat,Lng,Price,YearBuild,NewRate,Surface,Bedrooms,Floors, Toilets,Interior,OnStreet_Width,OnStreet_Distance,HouseType) values('{address}', '{lat}', '{long}', '{price}', 2000, 50, '{surface}', '{bedrooms}', '{floors}', '{toilets}', '{interior}', '{onstreet_width}','{onstreet_distance}','{house_type}')".format(
                address = address, lat = lat, long = long, price = price, surface = surface, bedrooms = bedrooms, floors = floors, toilets=toilets, interior = interior, onstreet_width = onstreet_wide, onstreet_distance = onstreet_far, house_type=folder
            )
            cursor.execute(sql)
            db.commit()
            save_folder = htmls_houses_processed + "/" + folder
            if os.path.isdir(save_folder) == False:
                os.mkdir(save_folder)
            new_path = save_folder + "/" + filename
            os.rename(full_path, new_path)
            #print(index, filename + "\n")
            i = i + 1
            #print(house)
    print(datetime.datetime.now(), i)
    time.sleep(20)
    break


db.close()

    #print(lat, long, address, price, surface, bedrooms, floors, toilets, interior, onstreet_wide, onstreet_far)



