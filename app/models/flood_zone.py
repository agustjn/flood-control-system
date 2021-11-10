from sqlalchemy import Column, Integer, String, Boolean
from app.db import db
from app.models.coordinate import Coordinate , FloodZone_has_coordinate
import random

class FloodZone(db.Model):
  """Define el modelo de la tabla zonas_inundables"""
  __tablename__ = "flood_zones"
  id = Column(Integer,primary_key=True)
  cod_zone = Column (Integer)
  name = Column(String(50), unique=True)
  state = Column(Boolean)
  colour = Column(String(50))

  coordinates = db.relationship(
            "Coordinate",
            secondary = FloodZone_has_coordinate.get_table_floodZone_has_coordinate(),
            backref= db.backref("coordinates_floodZone", lazy="dynamic"),
            lazy = "dynamic",
        )
 
  # por defectos se cargan con estos valores por el tema de que en el csv solo viene nombre y coordenadas
  def __init__ (self, name = None, cod_zone = None, state = None, color = None):
      self.name = name
      if not cod_zone:
          self.cod_zone = random.choice(['Cod 0', 'Cod 1', 'Cod 2', 'Cod 3', 'Cod 4', 'Cod 5', 'Cod 6', 'Cod 7'])
      else:
          self.cod_zone = cod_zone
      if not state:
          self.state = random.choice(['Publicado', 'Despublicado'])
      else:
          self.state = state
      if not color:
          self.color = random.choice(['Amarillo', 'Verde', 'Rojo', 'Azul', 'Celeste', 'Azul', 'Violeta'])
      else:
          self.color = color






  



  # def __init__ (self, cod_zone = None, name = None, coordinates= None, state=None, color=None):
  #   self.cod_zone = cod_zone
  #   self.name = name
  #   self.coordinates = coordinates
  #   self.state = state
  #   self.color = color
    