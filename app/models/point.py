# Se estan reescribiendo las clases para utilizar la libreria SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.configuration import Configuration


from app.db import db
from sqlalchemy.orm import relationship


class Point(db.Model):
    __tablename__ = "points"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    address = Column(String(50))
    coordinates = Column(String(50))
    status = Column(String(50))
    phone = Column(Integer)
    email = Column(String(50))

    def __init__(self, nombre=None, direccion=None, coordenadas=None, telefono=None, email=None, estado=None):
        self.name = nombre
        self.address = direccion
        self.coordinates = coordenadas
        self.status = estado
        self.phone = telefono
        self.email = email

    def __repr__(self):
        return (self.name)
