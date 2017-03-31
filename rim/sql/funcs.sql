DROP FUNCTION IF EXISTS SPLIT_STR;
CREATE FUNCTION SPLIT_STR(
  x VARCHAR(255),
  delim VARCHAR(12),
  pos INT
)
RETURNS VARCHAR(255)
RETURN REPLACE(SUBSTRING(SUBSTRING_INDEX(x, delim, pos),
       LENGTH(SUBSTRING_INDEX(x, delim, pos -1)) + 1),
       delim, '');
       
DROP FUNCTION IF EXISTS getAddress;
DELIMITER //
CREATE FUNCTION getAddress(address varchar(500)) RETURNS int
BEGIN
  DECLARE addr1,addr2,addr3 VARCHAR(200);
  Declare addrCount int;
  
  declare cityId, districtId, wardId, streetId int;
  
  SET addr4 = trim(SPLIT_STR(address, ',', 4)); 
  SET addr3 = SPLIT_STR(address, ',', 3);    
  SET addr2 = SPLIT_STR(address, ',', 2);
  SET addr1 = SPLIT_STR(address, ',', 1);
  if addr4<>'' then
	set addrCount = 4;
  elseif addr3<>'' then
	set addrCount = 3;
  elseif addr2<>'' then
	set addrCount = 2;
  elseif addr1<>'' then
	set addrCount = 1;

  /*
  if addrCount = 4 then	
  begin
	cityId = getCityId(addr4);
    districtId = getDistrictId(addr3);
    wardId = getWardId(addr2);
    streetId = getStreetId(addr1);
  end;
  
  if addrCount = 3 then	
  begin
	cityId = getCityId(addr3);
    districtId = getDistrictId(addr2);
    streetId = getStreetId(addr1);
  end;
  
  if addrCount = 2 then	
  begin
	cityId = getCityId(addr3);
    streetId = getStreetId(addr1);
  end;
  */
  
    
  RETURN 1;
END;
DELIMITER ;

/*
truncate AreaScore;
select getAreaScore('Duong Huynh Van Luy, Phuong Phu My, Thu Dau Mot, Binh Duong')
select getAreaScore('Duong Nguyen Cong Tru, Binh Thanh, Ho Chi Minh')
select * from AreaScore where Address='Duong Huynh Van Luy, Phuong Phu My, Thu Dau Mot, Binh Duong'
*/
DROP FUNCTION IF EXISTS getAreaScore;
DELIMITER //
CREATE FUNCTION getAreaScore(addr varchar(500)) 
RETURNS int
BEGIN
  declare id int;
  select AreaScoreId into id from AreaScore where Address=addr limit 0,1;
  if id is null then 
	insert into AreaScore(Address) values(addr);
    select AreaScoreId into id from AreaScore where Address=addr limit 0,1;
    
  end if;
  return id;
END //
DELIMITER ;

DROP FUNCTION IF EXISTS getHouseType;
DELIMITER //
CREATE FUNCTION getHouseType(typename varchar(1000)) 
RETURNS int
BEGIN
  declare typeid int;
  select HouseTypeId into typeid from HouseType where typename like concat(HouseTypeName,'%') limit 0,1;
  return typeid;
END //
DELIMITER ;

DROP FUNCTION IF EXISTS getSurface;
DELIMITER //
CREATE FUNCTION getSurface(d varchar(500)) 
RETURNS Decimal(10,2)
BEGIN
  declare s varchar(100);
  /*DECLARE CONTINUE HANDLER FOR SQLSTATE '23000' SET r = cast(trim(replace(d, 'mÂ²', '')) as unsigned); */
  set s = trim(replace(d, 'mÂ²', ''));
  return parseDecimal(s);
END //
DELIMITER ;

DROP FUNCTION IF EXISTS getBedrooms;
DELIMITER //
CREATE FUNCTION getBedrooms(d varchar(500)) 
RETURNS Decimal(10,2)
BEGIN
  declare s varchar(10);
  declare r int;
  set s = trim(replace(d, '(phong)', ''));  
  set r = parseDecimal(s);
  return r;
END //
DELIMITER ;

DROP FUNCTION IF EXISTS getPrice;
DELIMITER //
CREATE FUNCTION getPrice(d varchar(500)) 
RETURNS DECIMAL(13,2)
BEGIN
  /*
  980 trieu
  3.98 ty
  
  select '980 trieu' like '%trieu'
  select (SUBSTRING_INDEX('3.98 ty', 'ty', 1))
  SELECT REPLACE('www.mysql.com', 'w', 'Ww');
  select trim(SUBSTRING_INDEX(Price, 'ty', 1)) from HouseRaw1;
  */
  declare s varchar(100);
  declare i int;
  if (d like '%trieu') > 0 then
	set s = trim(SUBSTRING_INDEX(d, 'trieu', 1));
    return parseDecimal(s);
  end if;
  if (d like '%ty') > 0 then
	set s = trim(SUBSTRING_INDEX(d, 'ty', 1));
    return cast(parseDecimal(s)*1000 as DEcimal(13,2));
  end if;
  return 0;
END //
DELIMITER ;



DROP FUNCTION IF EXISTS getInterior;
DELIMITER //
CREATE FUNCTION getInterior(d varchar(500)) 
RETURNS int
BEGIN
  return 1;
END //
DELIMITER ;

DROP FUNCTION IF EXISTS convertToDecimal;
DELIMITER //
CREATE FUNCTION convertToDecimal(d varchar(500)) 
RETURNS Decimal(10,2)
BEGIN
  declare s varchar(10);
  set s = trim(replace(d, ',', '.'));
  return parseDecimal(s);
END //
DELIMITER ;

DROP FUNCTION IF EXISTS parseDecimal;
DELIMITER //
CREATE FUNCTION parseDecimal(d varchar(500)) 
RETURNS Decimal(10,4)
BEGIN
  declare s varchar(500);
  set s = replace(trim(d),',','.');
  IF isNumber(s) = 0 then
	return 0;
  end if;
  return cast(s as Decimal(10,4));
  /*
  declare s varchar(10);
  set s = trim(replace(d, ',', '.'));
  return cast(s as Decimal(10,2));
  */
END //
DELIMITER ;

DROP FUNCTION IF EXISTS isNumber;
DELIMITER //
CREATE FUNCTION isNumber(d varchar(500)) 
RETURNS int
BEGIN
  return d REGEXP '^-?[0-9]+.?[0-9]*$';
  /*
  declare s varchar(10);
  set s = trim(replace(d, ',', '.'));
  return cast(s as Decimal(10,2));
  */
END //
DELIMITER ;



