# Se estan reescribiendo las clases para utilizar la libreria SQLAlchemy
from sqlalchemy import Column, Integer, String
from app.db import db


class User(db.Model):
        __tablename__ = "uses"
        id = Column(Integer, primary_key=True)
        email = Column(String(50), unique=True, nullable=False)
        password = Column(String(50), unique=True, nullable=False)
        first_name = Column(String(50), unique=True, nullable=False)
        last_name = Column(String(50), unique=True, nullable=False)


        def __init__ (self,first_name = None , last_name = None, email = None, password =None):
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.password = password

        def __repr__(self):
            return self.email



# class User(object):
#     @classmethod
#     def all(cls, conn):
#         sql = "SELECT * FROM users"
#         cursor = conn.cursor()
#         cursor.execute(sql)

#         return cursor.fetchall()

#     @classmethod
#     def create(cls, conn, data):
#         sql = """
#             INSERT INTO users (email, password, first_name, last_name)
#             VALUES (%s, %s, %s, %s)
#         """

#         cursor = conn.cursor()
#         cursor.execute(sql, list(data.values()))
#         conn.commit()

#         return True

#     @classmethod
#     def find_by_email_and_pass(cls, conn, email, password):
#         sql = """
#             SELECT * FROM users AS u
#             WHERE u.email = %s AND u.password = %s
#         """

#         cursor = conn.cursor()
#         cursor.execute(sql, (email, password))

#         return cursor.fetchone()
