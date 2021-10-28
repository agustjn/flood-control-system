# Se estan reescribiendo las clases para utilizar la libreria SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from app.models.configuration import Configuration
from datetime import datetime as dt

from app.db import db
from sqlalchemy.orm import relationship


class User(db.Model):
        __tablename__ = "users"
        id = Column(Integer, primary_key=True)
        email = Column(String(50), unique=True)
        usuario = Column (String (50),unique=True)
        password = Column(String(50))
        first_name = Column(String(50))
        last_name = Column(String(50))
        activo = Column(Boolean)
        created_at = Column(String(30))

        configuration_id = Column(Integer,ForeignKey("configurations.id"))
        configuration = relationship(Configuration)


        def __init__ (self,first_name = None , last_name = None, email = None, usuario = None, password = None):
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.usuario = usuario
            self.password = password
            self.configuration_id = 1
            self.activo = 1
            self.created_at = dt.today()


        def __repr__(self):
            return (f"{self.first_name} {self.last_name} email: {self.email}")

        @classmethod
        def exist(cls,email,user):
            exist_email = cls.query.filter_by(email = email).first()
            exist_usuario = cls.query.filter_by(usuario = user).first()
            if exist_email:
                return ("email "+ email )
            elif exist_usuario:
                return ("usuario " + user)
            else:
                return (None)
