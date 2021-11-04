from app.db import db

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime as dt

class Report(db.Model):
    """ Crea el modelo de las denuncias con toda la informacion relacionada y el id de el usuario asignado """
    __tablename__ = "report"
    id = Column(Integer,primary_key=True)
    title = Column(String(50), unique=True)
    category = Column(String(30))
    creation_date = Column(String(30))
    closing_date = Column(String(30))
    description = Column(String(255))
    coordinates_latitude = Column(String(50),unique=True)  #Unico y si ya se elijo pedir otra
    coordinates_longitude = Column(String(50),unique=True)
    assing = Column(int(10))  #Ver tipo, podria ser el id de el usuario
    first_name = Column(String(30))
    last_name = Column(String(30))
    phone = Column(int(30))
    email = Column(String(30))

    def __init__ (self,title,category, description, coordinates_latitude, coordinates_longitude, assing, first_name, last_name, phone, email):
        self.title = title
        self.category = category
        self.creation_date = dt.today()
        self.closing_date = "--"
        self.description = description
        self.coordinates_latitude = coordinates_latitude
        self.coordinates_longitude = coordinates_longitude
        self.assing = assing
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
