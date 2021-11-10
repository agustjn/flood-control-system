from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from app.models.configuration import Configuration
from app.db import db


class Coordinate(db.Model):
        __tablename__ = "coordinates"
        id = Column(Integer, primary_key=True)
        latitude = Column(String(50))
        longitude = Column(String(50))

        def __init__ (self,latitude = None, longitude = None ):
            self.latitude = latitude
            self.longitude = longitude


class FloodZone_has_coordinate():
    table = db.Table(
        "floodZone_has_coordinate",
        Column("floodZone_id",Integer, ForeignKey("flood_zones.id")),
        Column("coordinate_id",Integer, ForeignKey("coordinates.id")),
        )

    @classmethod
    def get_table_floodZone_has_coordinate(cls):
        return (cls.table)
    