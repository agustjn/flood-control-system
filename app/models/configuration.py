from sqlalchemy import Column, Integer, String,ForeignKey,VARCHAR
from sqlalchemy.orm import relationship
from app.db import db
from app.models.views_sort import View_users, View_issues, View_meeting_points
from flask import session


class Configuration(db.Model):
  """Es la tabla intermedia la cual define la configuracion del usuario """
  __tablename__ = "configurations"
  id = Column(Integer,primary_key=True)
  background = Column(VARCHAR(50))
  items_per_page = Column(Integer)
  view_users_id = Column(Integer,ForeignKey("view_users.id"))
  view_users = relationship(View_users)
  view_meeting_points_id = Column(Integer,ForeignKey("view_meeting_points.id"))
  view_meeting_points = relationship(View_meeting_points)
  view_issues_id = Column(Integer,ForeignKey("view_issues.id"))
  view_issues = relationship(View_issues)
  




  def __repr__(self):
    return (f"{self.background} {self.items_per_page}")


  @staticmethod
  def setItemsPerPage(value):
      items_per_page = value
      db.session.commit()

  
  @staticmethod
  def get_valid_paginations():
      return [5,10,15,20,25]

  @staticmethod
  def get_valid_colors():
    return ["Gris","Amarillo","Celeste"]
    
  



