/*
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
*/

create table if not exists City(
	CityId int primary key auto_increment,
    CityName varchar(500)
);

create table if not exists Ward(
	WardId int primary key auto_increment,
    WardName varchar(500),
    CityId int
);

create table if not exists Street(
    StreetId int primary key auto_increment,
    StreetName varchar(500),
    WardId int,
    CityId int
);

create table if not exists AreaScore(
    AreaScoreId int primary key auto_increment,
    Address varchar(500),
    Lat float,
    Lng float,
    Radius float,
    Score int
);

create table if not exists HouseRaw1(
	HouseId int primary key auto_increment,
    HouseType varchar(1000),
	Address varchar(500),
	Lat varchar(500),
	Lng varchar(500),
	Price varchar(500),
	YearBuild int,
	NewRate int,
	Surface varchar(500),
	Bedrooms varchar(500),
	Floors varchar(500),
	Toilets varchar(500),
	Interior varchar(500),
	OnStreet_Width varchar(500),
	OnStreet_Distance varchar(500),
    Flag1 int,
    Flag2 int
);
	
create table if not exists POI(
    PlaceId varchar(50),
    PlaceName varchar(1000),
    Lat varchar(500),
    Lng varchar(500),    
    Vicinity varchar(1000),
    PlaceType varchar(500),
    Score int,
    CityId int
);    

create table if not exists NearBy(
	HouseId int,
	PlaceId varchar(50)
);   

create table if not exists BestPOI(
	PlaceId varchar(50),
	Name varchar(1000),
	Address varchar(2000),
	Lat varchar(500),
	Lng varchar(500),
	Score int,
	CityId int
);

create table if not exists NearByBestPOI(
	HouseId int,
	PlaceId varchar(50)
);
