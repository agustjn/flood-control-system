from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.sql.sqltypes import VARCHAR
from app.db import db
from app.models.customization import Customization

# Futura clase para usar herencia
# class Views_sort(db.model):
#     "Contiene la columna por la que se ordena el listado de usuarios y el tipo de orden (ASC,DESC)"


#     def __init__(self, column = None , type = None):
#         __tablename__ = table_name
#         id = Column(Integer,primary_key=True)
#         sorted_by_column = Column(VARCHAR(30))
#         sort_type = Column(VARCHAR(30))
#         self.sorted_by_column = column
#         self.type = type

#     def __repr__():
#         #return (f"{__tablename__},{self.sorted_by_column} {self.sort_type}")
#          return (f"{self.sorted_by_column} {self.sort_type}")

class View_users(db.Model):
    "Contiene la columna por la que se ordena el listado de usuarios y el tipo de orden (ASC,DESC)"
    __tablename__ = "view_users"
    id = Column(Integer,primary_key=True)
    sorted_by_column = Column(VARCHAR(30))
    sort_type = Column(VARCHAR(30))

    def __init__(self, column = None , type = None):
        self.sorted_by_column = column
        self.type = type

    def __repr__():
        return (f"{self.sorted_by_column} {self.sort_type}")


class View_issues(db.Model):
    "Contiene la columna por la que se ordena el listado de usuarios y el tipo de orden (ASC,DESC)"
    __tablename__ = "view_issues"
    id = Column(Integer,primary_key=True)
    sorted_by_column = Column(VARCHAR(30))
    sort_type = Column(VARCHAR(30))

    def __init__(self, column = None , type = None):
        self.sorted_by_column = column
        self.type = type

    def __repr__():
        return (f"{self.sorted_by_column} {self.sort_type}")

class View_meeting_points(db.Model):
    "Contiene la columna por la que se ordena el listado de usuarios y el tipo de orden (ASC,DESC)"
    __tablename__ = "view_meeting_points"
    id = Column(Integer,primary_key=True)
    sorted_by_column = Column(VARCHAR(30))
    sort_type = Column(VARCHAR(30))

    def __init__(self, column = None , type = None):
        self.sorted_by_column = column
        self.type = type

    def __repr__():
        return (f"{self.sorted_by_column} {self.sort_type}")
