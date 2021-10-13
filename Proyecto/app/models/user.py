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


        def __init__ (self,first_name = None , last_name = None, email = None, password = None,configuration_id = None):

            #customization = Customizations()
            #db.session.add(customization)

            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.password = password
            self.configuration_id = configuration_id


        def __repr__(self):
            return self.email
