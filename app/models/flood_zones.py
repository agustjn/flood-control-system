from sqlalchemy import Column, Integer, String, Boolean
from app.db import db


class Category(db.Model):
  """Define el modelo de la tabla zonas_inundables"""
  __tablename__ = "flood_zones"
  id = Column(Integer,primary_key=True)
  cod_zone = Column (Integer,unique=True)
  name = Column(String(50), unique=True)
  coordinates=Column(String(50))
  state = Column(Boolean)
  color = Column(String(50))

  def __init__ (self, name = None, coordinates= None):
      self.name = name
      self.coordinates = coordinates


  # def __init__ (self, cod_zone = None, name = None, coordinates= None, state=None, color=None):
  #   self.cod_zone = cod_zone
  #   self.name = name
  #   self.coordinates = coordinates
  #   self.state = state
  #   self.color = color
    