
from flask import request
from sqlalchemy.sql.expression import desc,asc
from app.models.user import User
from app.models.views_sort import View_users

class UserDAO():
    def users_paginated(items_per_page):
        page = request.args.get('page', 1, type=int)
        # users = User.query.paginate(page=page, per_page=items_per_page)
        # View posee un diccionario con la columna y tipo de orden(asc,desc), para los respectivos ordenes de las listas
        view = View_users.query.first().formatted_values()
        # Con la funcio eval, se "convierte" el string a una funcion
        users = eval("User.query.order_by(User.{}.{}())".format(view["column"], view["type"]))
        return users.paginate(page=page, per_page=items_per_page)

    
