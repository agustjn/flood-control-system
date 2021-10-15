from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from app.db import db
from app.models.customization import Customization


class Configuration(db.Model):
  """Es la tabla intermedia la cual define la configuracion del usuario """
  __tablename__ = "configurations"

  id = Column(Integer,primary_key=True)
  customization_id  = Column (Integer,ForeignKey("customizations.id"))
  customization = relationship(Customization)


  def __init__ (self):
      new_customization = Customization()
      db.session.add(new_customization)
      db.session.commit()
      self.customization_id = self.obtener_id_customization()
      print (f"------------------------------------{new_customization}---------------------------------------------------")

  def obtener_id_customization(self):
      last_customization_id = Customization.query.order_by(Customization.id.desc()).first()
      last_customization_id = last_customization_id.id
      return last_customization_id
  
  @staticmethod
  def get_valid_paginations():
      return [10,20,50,100]
