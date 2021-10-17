# Se estan reescribiendo las clases para utilizar la libreria SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.customization import Customization
from app.models.configuration import Configuration


from app.db import db
from sqlalchemy.orm import relationship


class Point(db.Model):
        __tablename__ = "points"
        id = Column(Integer, primary_key=True)
        nombre = Column(String(50), unique=True)
        direccion = Column (String (50))
        coordenadas = Column(String(50))
        estado = Column(String(50))
        telefono = Column(Integer)
        email = Column(String(50))


        def __init__ (self,nombre = None, direccion = None, coordenadas = None, telefono = None, email = None ):
            self.nombre = Nombre
            self.direccion = direccion
            self.coordenadas = coordenadas
            self.estado = status
            self.telefono = telefono
            self.email = email


        def __repr__(self):
            return (self.nombre)

        @classmethod
        def exist(cls,nombre,direccion):
            exist_nombre = cls.query.filter_by(nombre = nombre).first()
            exist_direccion = cls.query.filter_by(direccion = direccion).first()
            if exist_nombre:
                return ("nombre "+ nombre )
            elif exist_usuario:
                return ("direccion" + direccion)
            else:
                return (None)
