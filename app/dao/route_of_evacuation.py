from flask import request
from app.models.route_of_evacuation import Route_of_evacuation as Route
from app.db import db

class Route_of_evacuationDAO ():

    @staticmethod
    def recover_route_of_evacuation():
         return Route.query.all()
