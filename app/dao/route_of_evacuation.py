from flask import request
from app.models.route_of_evacuation import Route_of_evacuation as Route
from app.db import db

class Route_of_evacuationDAO ():

    @staticmethod
    def recover_route_of_evacuation():
         return Route.query.all()

    @staticmethod
    def filter_by_key(status,items_per_page, key=""):
        key_filtered = "%" + key + "%"
        page = request.args.get('page', 1, type=int)
        if status == "Todos":
            routes =  Route.query.filter(Route.name.like(key_filtered)).paginate(page=page, per_page=items_per_page)
        else:
            if status == "Publicado":
                routes =  Route.query.filter(Route.name.like(key_filtered)).filter_by(publicado = True).paginate(page=page, per_page=items_per_page)
            else:
                routes =  Route.query.filter(Route.name.like(key_filtered)).filter_by(publicado = False).paginate(page=page, per_page=items_per_page)
        return routes
