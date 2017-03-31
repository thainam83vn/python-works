SELECT t.HouseTypeScore, h.YearBuild, h.NewRate, h.Surface, h.Bedrooms, h.TotalFloors,IF(h.Toilets = 0, 1, h.Toilets) as Toilets,
	h.Interior,h.PricePerM2,r.PricePerM2 as RegionPrice,h.Price
FROM HouseRaw2 h
INNER JOIN Region r on h.RegionId=r.RegionId
INNER JOIN HouseType t on h.HouseType=t.HouseTypeId
Where
	Price>0 and h.PricePerM2>0;