# Se estan reescribiendo las clases para utilizar la libreria SQLAlchemy
from app.db import db


class Users(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(80), unique=True, nullable=False)
        password = db.Column(db.String(120), unique=True, nullable=False) 
        first_name = db.Column(db.String(120), unique=True, nullable=False)
        last_name = db.Column(db.String(120), unique=True, nullable=False)

        def __repr__(self):
            return self.username

test1 = Users(email='Arthut', password='test',first_name='Art',last_name='Wett')
db.session.add(test1)
db.session.commit()



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
