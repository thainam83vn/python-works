from neomodel import (StructuredNode, StringProperty, IntegerProperty, RelationshipTo, RelationshipFrom)

class Mapper:
    def Map(self, node, cls):
        dest = cls()
        for key, prop in cls.__all_properties__:
            if key in node:
                setattr(dest,key,node[key])
        return dest

class POI(StructuredNode):
    PlaceId = StringProperty()
    PlaceName = StringProperty()
    Lat = StringProperty()
    Lng = StringProperty()
    Vicinity = StringProperty()
    PlaceType = StringProperty()

class FamousPOI(StructuredNode):
    PlaceId = StringProperty()
    PlaceName = StringProperty()
    Lat = StringProperty()
    Lng = StringProperty()
    City = StringProperty()
    Link = StringProperty()
    Score = IntegerProperty()

class House(StructuredNode):
    HouseId = StringProperty()
    Address = StringProperty()
    Lat = StringProperty()
    Lng = StringProperty()
    Price = StringProperty()
    Surface = StringProperty()
    Bedrooms = StringProperty()
    Floors = StringProperty()
    Toilets = StringProperty()
    Interior = StringProperty()
    NewRate = StringProperty()
    HouseType = StringProperty()
    POI = RelationshipTo(POI, "NEAR")

class NearByFamousPOI(StructuredNode):
    HouseId = StringProperty()
    PlaceId = StringProperty()
    Distance = StringProperty()
    Duration = StringProperty()

class HouseRaw2(StructuredNode):
    HouseId = StringProperty()
    HouseType = StringProperty()
    Lat = StringProperty()
    Lng = StringProperty()
    Price = StringProperty()
    YearBuild = StringProperty()
    Surface = StringProperty()
    Bedrooms = StringProperty()
    Floors = StringProperty()
    Toilets = StringProperty()
    Interior = StringProperty()
    NewRate = StringProperty()
    Address = StringProperty()
    PricePerM2 = StringProperty()
    RegionId = StringProperty()
    TotalFloors = StringProperty()



