# Se estan reescribiendo las clases para utilizar la libreria SQLAlchemy
from sqlalchemy import Column, Integer, String
from app.db import db


class User(db.Model):
        __tablename__ = "users"
        id = Column(Integer, primary_key=True)
        email = Column(String(50), unique=True)
        password = Column(String(50), unique=True)
        first_name = Column(String(50), unique=True)
        last_name = Column(String(50), unique=True)

        configuration_id (Integer,ForeignKey("configuration.id"))
        configuration = relationship(customizations)

            
        def __init__ (self,first_name = None , last_name = None, email = None, password = None):
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.password = password

        def __repr__(self):
            return self.email
