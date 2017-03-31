drop table HouseType;
create table if not exists HouseType(
	HouseTypeId int,
    HouseTypeName varchar(500)
);

truncate HouseType;
insert into HouseType values(1,'ban-nha-biet-thu-lien-ke',10);
insert into HouseType values(2,'ban-nha-rieng',7);
insert into HouseType values(3,'ban-nha-mat-pho',9);
insert into HouseType values(4,'ban-can-ho-chung-cu',5);
insert into HouseType values(5,'ban-dat-nen-du-an',3);
insert into HouseType values(6,'ban-dat',2);

drop table HouseRaw2;
create table HouseRaw2(
	HouseId int primary key,
    HouseType int,
	Lat varchar(50),
	Lng varchar(50),
	Price Decimal(13,2),
	YearBuild int,
	NewRate Decimal(10,2),
	Surface Decimal(10,2),
	Bedrooms Decimal(10,2),
	Floors Decimal(10,2),
	Toilets Decimal(10,2),
	Interior Decimal(10,2),
	OnStreet_Width Decimal(10,2),
	OnStreet_Distance Decimal(10,2),
    CityId int,
    DistrictId int,
    WardId int,
    StreetId int,
    AreaId int,
    NoAddress varchar(200),
    Address varchar(2000)
);    


insert into HouseRaw2(
	HouseId,	Address,    HouseType,	Lat,	Lng,	Price,	
    YearBuild,	NewRate,	Surface,	
    Bedrooms,	Floors,	Toilets,	Interior,
	OnStreet_Width,	OnStreet_Distance    
)
Select HouseId, 
	Address,
    getHouseType(HouseType),
	Lat,
	Lng,
	getPrice(Price) as Price,
	YearBuild,
	NewRate,
    getSurface(Surface) as Surface,
    getBedrooms(Bedrooms) as Bedrooms,
	parseDecimal(Floors) as Floors,
	parseDecimal(Toilets) as Toilets,
	getInterior(Interior) as Interior,
	parseDecimal(OnStreet_Width) as OnStreet_Width,
	parseDecimal(OnStreet_Distance) as OnStreet_Distance
From HouseRaw1;

Select * from HouseRaw2;
Select * from HouseRaw1 where flag2=1;
Select count(*) from HouseRaw2;
select * from AreaScore;
/*
drop table HouseRaw2;
create table HouseRaw2(
	HouseId int primary key,
    AreaScoreId int,
    AreaScore Decimal(10,2),
    HouseType int,
	Lat varchar(50),
	Lng varchar(50),
	Price Decimal(10,2),
	YearBuild int,
	NewRate varchar(50),
	Surface varchar(50),
	Bedrooms varchar(50),
	Floors varchar(50),
	Toilets varchar(50),
	Interior varchar(50),
	OnStreet_Width varchar(50),
	OnStreet_Distance varchar(50)
);    


insert into HouseRaw2(
	HouseId,	AreaScoreId,    HouseType,	Lat,	Lng,	Price,	YearBuild,	NewRate,	Surface,	Bedrooms,	Floors,	Toilets,	Interior,
	OnStreet_Width,	OnStreet_Distance
)
Select HouseId, 
	getAreaScore(Address) as AreaScoreId,
    HouseType,
	Lat,
	Lng,
	getPrice(Price) as Price,
	YearBuild,
	NewRate,
    trim(replace(Surface, 'mÂ²', '')) as Surface,
    trim(replace(Bedrooms, '(phong)', '')) as Bedrooms,
	trim(Floors),
	trim(Toilets),
	1 as Interior,
	replace(OnStreet_Width,',','.') as OnStreet_Width,
	replace(OnStreet_Distance,',','.') as OnStreet_Distance
From HouseRaw1;
*/

/*
Select * from HouseRaw1;
Select count(*) from HouseRaw1 where flag1=0;
Select count(*) from HouseRaw2;
Select count(*) from POI;
select * from NearBy;
Select POIId,count(POIId) from NearBy group by POIId having count(POIId)>=2;
Select distinct areascoreid from HouseRaw2;
select * from AreaScore;
Select HouseId, 
	1 as AreaScoreId,
    HouseType,
	Lat,
	Lng,
	getPrice(Price) as Price,
	YearBuild,
	NewRate,
    cast(trim(replace(Surface, 'mÂ²', '')) as decimal(10,2)) as Surface,
    cast(trim(replace(Bedrooms, '(phong)', '')) as decimal(10,2)) as Bedrooms,
	cast(Floors as unsigned) as Floors,
	cast(Toilets as unsigned) as Toilets,
	getInterior(Interior) as Interior,
	convertToDecimal(OnStreet_Width) as OnStreet_Width,
	convertToDecimal(OnStreet_Distance) as OnStreet_Distance
From HouseRaw1 limit 0,1;
*/
