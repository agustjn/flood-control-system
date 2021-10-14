from sqlalchemy import Column, Integer, String
from app.db import db

class Customization(db.Model):
  """Define la configuracion de la personalizacion de las vistas"""
  __tablename__ = "customizations"
  id = Column(Integer,primary_key=True)
  items_per_page  = Column (Integer)
  sort_order = Column(String(30))
  background_color = Column(String(30))

  def __init__ (self):
    print (f"------------------------Entro Customization-------------------")
    self.items_per_page = 15
    self.sort_order = "alfabetica"
    self.background_color = "bg-light"
