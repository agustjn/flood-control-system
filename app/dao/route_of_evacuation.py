from flask import request
from app.models.route_of_evacuation import Route_of_evacuation as Route
from app.db import db
from sqlalchemy import or_
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

    @staticmethod
    def exist_coordinates(coordinates = None , coordinates_latitude = None , coordinates_longitude = None):
        "Si ingresa las coordenadas todas juntas usa 'coordinates', sino por nombre las referencia por separadas"
        if coordinates:
            lis = coordinates.split(",")
            coordinates_latitude = lis[0]
            coordinates_longitude = lis[1]
        if (db.session.query(Route).filter(or_(Route.coordinates_latitude == coordinates_latitude, Route.coordinates_longitude == coordinates_longitude)).first()):
                return True
        return False

    @staticmethod
    def create_route(name,publicado,coordinates_lat,coordinates_long,description):
        new_route = Route(name,publicado,coordinates_lat,coordinates_long,description)
        db.session.add(new_route)
        try:
            db.session.commit()
            return True
        except:
            return False
