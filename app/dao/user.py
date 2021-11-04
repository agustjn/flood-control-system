
from flask import request
from app.models.user import User
from app.models.views_sort import View
from app.db import db

#import logging
#logger = logging.getLogger(__name__)
#logger.exception("mensaje")


class UserDAO():
    """Genera las consultas necesarios para consultar la informacion del usuario en la base de datos en el resource"""
    def users_paginated(items_per_page):
        page = request.args.get('page', 1, type=int)
        view = View.query.filter_by(id = "user").first().formatted_values()
        # Con la funcio eval, se "convierte" el string a una funcion
        users = eval("User.query.order_by(User.{}.{}())".format(view["column"], view["type"]))
        # column = getattr(User,view["column"])
        # order = getattr(column,view["type"])
        # users = User.query.order_by(order)
        # # Luego de ya tenerlos ordenados por la columna y el tipo correspondiente, se los pagina
        return users.paginate(page=page, per_page=items_per_page)

    @staticmethod
    def filter_by_key(status,items_per_page, key=""):
        key_filtered = "%" + key + "%"
        page = request.args.get('page', 1, type=int)

        if status == "Todos":
            users =  User.query.filter(User.username.like(key_filtered)).paginate(page=page, per_page=items_per_page)
        else:
            if status == "Activo":
                users =  User.query.filter(User.username.like(key_filtered)).filter_by(active = True).paginate(page=page, per_page=items_per_page)
            else:
                users =  User.query.filter(User.username.like(key_filtered)).filter_by(active = False).paginate(page=page, per_page=items_per_page)
        #points.order_by(Point.email)
        return users

    @staticmethod
    def recover_users():
         return User.query.all()

    @staticmethod
    def create_user(parameter):
        new_user = User(parameter["first_name"],parameter["last_name"],parameter["email"],parameter["user"],parameter["password"])
        db.session.add(new_user)
        try:
            db.session.commit()
            return True
        except:
            return False

    @staticmethod
    def activate_desactivate(user_id):
        user = User.query.get(user_id)
        user.active = not (user.active)
        try:
            db.session.commit()
            return True
        except:
            return False


    @staticmethod
    def exist_email(email):
        # return User.query.filter_by(email=email).exists()
        return bool(User.query.filter_by(email=email).first())

    @staticmethod
    def exist_username(username):
        return bool((User.query.filter_by(username=username).first()))

    @staticmethod
    def search_by_id(user_id):
        return  User.query.filter_by(id=user_id).first()

    @staticmethod
    def update (user_update,parameter):
        if parameter["user"]:
            user_update.username = parameter["user"]
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
