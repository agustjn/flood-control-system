from app.db import db

from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
import datetime as dt

from app.models.user import User

class Report(db.Model):
    """ Crea el modelo de las denuncias con toda la informacion relacionada y el id de el usuario asignado """
    __tablename__ = "report"
    id = Column(Integer,primary_key=True)
    title = Column(String(50))
    status = Column(String(50))
    category = Column(Integer)
    creation_date = Column(String(30))
    closing_date = Column(String(30))
    description = Column(String(255))
    coordinates_latitude = Column(String(50),unique=True)  #Unico y si ya se elijo pedir otra
    coordinates_longitude = Column(String(50),unique=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    phone = Column(Integer)
    email = Column(String(30))

    user_assing_id = Column(Integer,ForeignKey("users.id"))
    user_assing = relationship(User)

    def __init__ (self,title,category, description, coordinates_latitude, coordinates_longitude, user_assing_id, first_name, last_name, phone, email):
        self.title = title
        self.category = category
        self.creation_date = dt.date.today().strftime("%b %d %Y %H:%M:%S")
        self.closing_date = ""
        self.description = description
        self.coordinates_latitude = coordinates_latitude
        self.coordinates_longitude = coordinates_longitude
        self.user_assing_id = user_assing_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.status = "Sin confirmar"
