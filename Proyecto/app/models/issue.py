from app.db import db
from app.models.category import Category
from app.models.status import Status

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Issue(db.Model):
    __tablename__ = "issues"
    id = Column(Integer,primary_key=True)
    email = Column(String(50), unique=True)
    description = Column(String(30),unique=True)
    category_id = Column(String(30),unique =True)
    #
    category = Column(Integer,ForeignKey("categories_id"))
    category = relationship(Category)
    status_id = Column(Integer,ForeignKey("statuses_id"))
    status = relationship(Status)

"""class Issue(object):
    @classmethod
    def all(cls, conn):
        sql = "SELECT * FROM issues"

        cursor = conn.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def create(cls, conn, data):
        sql =
            INSERT INTO issues (email, description, category_id, status_id)
            VALUES (%s, %s, %s, %s)


        cursor = conn.cursor()
        cursor.execute(sql, list(data.values()))
        conn.commit()

        return True
"""
