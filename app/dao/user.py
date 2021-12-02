
from flask import request
from app.models.user import User
from app.models.views_sort import View
from app.db import db
from app.models.permission import Permission


from app.models.permission import Role, Permission

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
        return users

    @staticmethod
    def recover_users():
         return User.query.all()



    @staticmethod
    def inicializate_permission_with(functions):
        """Recibe una lista la cual contiene 2 lista, la 1ra con los permisos para las funciones, y la 2da con la funciones permitidas"""
        permisos = []
        if (not functions[0] == []) and  (not functions[1] == []):
            values = functions[0]
            dar_permiso = functions[1]
            for type in values:
                for dar in dar_permiso:
                    perm = f"{dar}_{type}"
                    print (perm)
                    permisos.append(Permission(perm))
        return permisos

    @classmethod
    def inicializate_role_with(cls,role,permisos):
        """Recibe un rol y una lista con los funciones sobre que asignar y devuelve al rol con sus permisos asignados"""
        values = ["index","new","update","show"]
        if role == "administrador":
            values.append("destroy")
        functions = [values,permisos]
        functions_update = cls.inicializate_permission_with(functions)
        role_update = Role(role)
        for f in functions_update:
            role_update.permission.append(f)
        return role_update






    @staticmethod
    def create_user(first_name,last_name,email,user,password,active = True):
        new_user = User(first_name,last_name,email,user,password,active)
        db.session.add(new_user)
        try:
            db.session.commit()
            return True
        except:
            return False

    @classmethod
    def activate_desactivate(cls,user_id):
        user = cls.search_by_id(user_id)
        user.active = not (user.active)
        try:
            db.session.commit()
            return True
        except:
            return False


    @staticmethod
    def exist_email(email):
        return bool(User.query.filter_by(email=email).first())


    @staticmethod
    def exist_username(username):
        return bool((User.query.filter_by(username=username).first()))

    @staticmethod
    def search_by_id(user_id):
        return  User.query.filter_by(id=user_id).first()

    @staticmethod
    def search_by_email(user_email):
        return  User.query.filter_by(email=user_email).first()

    @classmethod
    def update (cls,user_update,user,email,password,first_name, last_name,role):
        if role:
            permisos = ["zonas_inundables","usuario","puntos_encuentro","denuncia","route_of_evacuation"]
            rol = cls.inicializate_role_with(role,permisos)
            user_update.role.append(rol)

        if user:
            user_update.username = user
        if email:
            user_update.email = email
        if password:
            user_update.password = password
        if first_name:
            user_update.first_name = first_name
        if last_name:
            user_update.last_name = last_name
        # if role:
        #     user_update.role.append = rol

        try:
            db.session.commit()
            return True
        except:
            return False

    @classmethod
    def delete_by_id(cls,user_id):
        report_delete = cls.search_by_id(user_id)
        db.session.delete(report_delete)
        try:
            db.session.commit()
            return True
        except:
            return False
