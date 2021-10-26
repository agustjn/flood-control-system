from flask import request
from app.models.point import Point
from app.db import db




class PointDAO():
    def points_paginated(items_per_page):
        page = request.args.get('page', 1, type=int)
        points = Point.query.paginate(page=page, per_page=items_per_page)
        return points

    @staticmethod
    def filter_by_key(status,key):
        key_filtered = "%" + key + "%"
        if status == "Todos":
            return Point.query.filter(Point.nombre.like(key_filtered)).all()
        else:
            return Point.query.filter(Point.nombre.like(key_filtered)).filter_by(estado = status).all()

    @staticmethod
    def filter_by(status):
        if status == "Todos":
            return Point.query.all()
        else:
            return Point.query.filter_by(estado = status).all()

    @staticmethod
    def recover_points():
         return Point.query.all()

    @staticmethod
    def exist_name(nombre):
        print (f"---------------------entro ------------------------ name")
        return bool((Point.query.filter_by(nombre=nombre).first()))

    @staticmethod
    def exist_adress(direccion):
        return bool((Point.query.filter_by(direccion=direccion).first()))


    @staticmethod
    def create_user(name, address, coordinates, phone, email, status):
        new_point = Point(name,address,coordinates,phone,email,status)
        db.session.add(new_point)
        try:
            db.session.commit()
            return True
        except:
            return False

    @staticmethod
    def search_by_id(point_id):
        return Point.query.filter_by(id=point_id).first()

    @staticmethod
    def update(point_update,parameter):
        if parameter["name"]:
            point_update.nombre = parameter["name"]
        if parameter["answer"]:
            point_update.direccion = parameter["answer"]
        if parameter["coordinates"]:
            point_update.coordenadas = parameter["coordinates"]
        if parameter["status"]:
            point_update.estadp = parameter["status"]
        if parameter["phone"]:
            point_update.telefono = parameter["phone"]
        if parameter["email"]:
            point_update.email = parameter["email"]
        try:
            db.session.commit()
            return True
        except:
            return False

    @staticmethod
    def delete(point_delete):
        db.session.delete(point_delete)
        try:
            db.session.commit()
            return True
        except:
            return False
