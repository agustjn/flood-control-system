# Se estan reescribiendo las clases para utilizar la libreria SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.customization import Customization
from app.models.configuration import Configuration

from app.db import db
from sqlalchemy.orm import relationship


class User(db.Model):
        __tablename__ = "users"
        id = Column(Integer, primary_key=True)
        email = Column(String(50), unique=True)
        password = Column(String(50), unique=True)
        first_name = Column(String(50), unique=True)
        last_name = Column(String(50), unique=True)

        configuration_id = Column(Integer,ForeignKey("configurations.id"))
        configuration = relationship(Configuration)


        def __init__ (self,first_name = None , last_name = None, email = None, password = None, last_configuration_id = None):
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.password = password
            self.configuration_id = last_configuration_id


        def __repr__(self):
            return (f"{self.first} {self.last_name} email: {self.email}")

        @classmethod
        def get_last_id(cls):
            #Se obtiene el ultimo id del utltimo usuario
            last_configuration_id = cls.query.order_by(cls.configuration_id.desc()).first()
            last_configuration_id = last_configuration_id.configuration_id + 1
            return last_configuration_id
