from sqlalchemy import Column, Integer, String, Boolean
from app.db import db


class FloodZone(db.Model):
  """Define el modelo de la tabla zonas_inundables"""
  __tablename__ = "flood_zones"
  id = Column(Integer,primary_key=True)
  cod_zone = Column (Integer,unique=True)
  name = Column(String(50), unique=True)
  coordinates=Column(String(50))
  state = Column(Boolean)
  colour = Column(String(50))

  def __init__ (self, name = None, cod_zone = None, state = None, color= None, coordinates= None):
      self.name = name
      self.coordinates = coordinates
      self.cod_zone = cod_zone
      self.state = state
      self.color = color



  # def __init__ (self, cod_zone = None, name = None, coordinates= None, state=None, color=None):
  #   self.cod_zone = cod_zone
  #   self.name = name
  #   self.coordinates = coordinates
  #   self.state = state
  #   self.color = color
    