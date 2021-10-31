
from flask import request
from app.models.user import User
from app.models.views_sort import View_users
from app.db import db

class UserDAO():
    """Genera las consultas necesarioas para el resource hacia el modelo de la base de datos"""
    def users_paginated(items_per_page):
        page = request.args.get('page', 1, type=int)
        view = View_users.query.first().formatted_values()
        # Con la funcio eval, se "convierte" el string a una funcion
        users = eval("User.query.order_by(User.{}.{}())".format(view["column"], view["type"]))
        # column = getattr(User,view["column"])
        # order = getattr(column,view["type"])
        # users = User.query.order_by(order)
        users = eval("User.query.order_by(User.{}.{}())".format(view["column"], view["type"]))
        # Luego de ya tenerlos ordenados por la columna y el tipo correspondiente, se los pagina
        users = users.paginate(page=page, per_page=items_per_page)
        return users
        
    @staticmethod
    def create_user(new_user):
        db.session.add(new_user)
        try:
            db.session.commit()
            return True
        except:
            return False

    @staticmethod
    def new_user(first_name = None , last_name = None, email = None, usuario = None, password = None):
        return User(first_name,last_name,email,usuario,password)

    @staticmethod
    def exist_email(email):
        return User.query.filter_by(email=email).exist()

    @staticmethod
    def exist_username(username):
        return bool((User.query.filter_by(usuario=username).first()))

    @staticmethod
    def search_by_id(user_id):
        return  User.query.filter_by(id=user_id).first()

    @staticmethod
    def update (user_update,parameter):
        if parameter["user"]:
            user_update.usuario = parameter["user"]
        if parameter["email"]:
            user_update.email = parameter["email"]
        if parameter["password"]:
            user_update.password = parameter["password"]
        if parameter["first_name"]:
            user_update.first_name = parameter["first_name"]
        if parameter["last_name"]:
            user_update.last_name = parameter["last_name"]
        try:
            db.session.commit()
            return True
        except:
            return False

    @classmethod
    def delete_by_id(cls,user_id):
        user_delete = cls.search_by_id(user_id)
        db.session.delete(user_delete)
        try:
            db.session.commit()
            return True
        except:
            return False
