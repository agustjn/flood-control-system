from sqlalchemy import Column, Integer, String
from app.db import db

class Customization(db.Model):
  """Define la configuracion de la personalizacion de las vistas"""
  __tablename__ = "customizations"
  id = Column(Integer,primary_key=True)
  __items_per_page  = Column (Integer,unique=True)
  sort_order = Column(String(30),unique =True)
  background_color = Column(String(30),unique=True)

  def __init__ (self):
    self.items_per_page = 15
    self.sort_order = "alfabetica"
    self.background_color = "bg-light"
