from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from app.db import db
from app.models.customization import Customization


class Configuration(db.Model):
  """Es la tabla intermedia la cual define la configuracion del usuario """
  __tablename__ = "configurations"
  id = Column(Integer,primary_key=True)
  customizations_id  = Column (Integer,ForeignKey("customizations.id"))
  customization = relationship(Customization)



  def __init__ (self):
      new_customization = Customization()
      db.session.add(new_customization)
      db.session.commit()
