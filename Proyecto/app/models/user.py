# Se estan reescribiendo las clases para utilizar la libreria SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.customizations import Customizations
from app.db import db
from sqlalchemy.orm import relationship


class User(db.Model):
        __tablename__ = "users"
        id = Column(Integer, primary_key=True)
        email = Column(String(50), unique=True)
        password = Column(String(50), unique=True)
        first_name = Column(String(50), unique=True)
        last_name = Column(String(50), unique=True)
        
        configuration_id = Column(Integer,ForeignKey("configuration.id"))
        configuration = relationship(Customizations)

        def __init__ (self,first_name = None , last_name = None, email = None, password = None):
            customization = Customizations()
            db.session.add(customization)

            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.password = password


        def __repr__(self):
            return self.email
