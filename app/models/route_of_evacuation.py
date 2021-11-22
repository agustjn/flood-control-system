# Se estan reescribiendo las clases para utilizar la libreria SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from app.models.configuration import Configuration


from app.db import db
from sqlalchemy.orm import relationship


class Route_of_evacuation(db.Model):
    __tablename__ = "route_of_evacuation"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    description = Column(String(50))
    coordinates_latitude = Column(String(50))
    coordinates_longitude = Column(String(50))
    publicado = Column(Boolean)

    def __init__(self, nombre=None, estado=None, coordenadas_latitud=None,coordenadas_longitud = None,  descripcion=None):
        self.name = nombre
        self.description = descripcion
        self.coordinates_latitude = coordenadas_latitud
        self.coordinates_longitude = coordenadas_longitud
        self.publicado = estado


    def __repr__(self):
        return (self.name)
