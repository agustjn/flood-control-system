from app.models.user import User
from app.db import db
from app.models.report import Report
from flask import request
class ReportDAO():
    """Genera las consultas necesarios para consultar la informacion del denuncias en la base de datos en el resource"""

    @staticmethod
    def create_report(title,category, description, coordinates_latitude, coordinates_longitude, user_assing_id, first_name, last_name, phone, email):
        new_report = Report(title,category, description, coordinates_latitude, coordinates_longitude, user_assing_id, first_name, last_name, phone, email)
        db.session.add(new_report)
        try:
            db.session.commit()
            return True
        except:
            return False



    @classmethod
    def create_report_dict(cls,**report_dic):
        #new_report = Report(report_dic["title"],report_dic["category"], report_dic["description"], report_dic["coordinates_latitude"], report_dic["coordinates_longitude"], report_dic["user_assing_id"], report_dic["first_name"], report_dic["last_name"], report_dic["phone"], report_dic["email"])
        return cls.create_report(report_dic["title"],report_dic["category"], report_dic["description"], report_dic["coordinates_latitude"], report_dic["coordinates_longitude"], report_dic["user_assing_id"], report_dic["first_name"], report_dic["last_name"], report_dic["phone"], report_dic["email"])

        #return (new_report)

    @staticmethod
    def existe_coordinates(coordinates = None , coordinates_latitude = None , coordinates_longitude = None):
        if coordinates:
            lis = coordinates.split(",")
            coordinates_latitude = lis[0]
            coordinates_longitude = lis[1]
        if (bool(Report.query.filter(or_(Report.coordinates_latitude == coordinates_latitude, Report.coordinates_longitude == coordinates_longitude)))):
                return False
        return True



    @staticmethod
    def search_by_id(report_id):
        return  Report.query.filter_by(id=report_id).first()


    @classmethod
    def delete_by_id(cls,report_id):
        report_delete = cls.search_by_id(report_id)
        try:
            db.session.delete(report_delete) #Puedo consultar si esto se rompe es porque no existe el usuario
            db.session.commit()
            return True
        except:
            return False

    def update_report(title,category, description, coordinates_latitude, coordinates_longitude, user_assing_id, first_name, last_name, phone, email):
        #Controlar todo
        db.session.add(new_user)
        try:
            db.session.commit()
            return True
        except:
            return False


    @staticmethod
    def recover_reports():
         return Report.query.all()



    @staticmethod
    def filter_by_key(status,items_per_page, key=""):
        key_filtered = "%" + key + "%"
        page = request.args.get('page', 1, type=int)
        if status == "Todos":
            reports =  Report.query.filter(Report.title.like(key_filtered)).paginate(page=page, per_page=items_per_page)
        else:
                reports =  Report.query.filter(Report.title.like(key_filtered)).filter_by(status = status).paginate(page=page, per_page=items_per_page)
        return reports

    @classmethod
    def delete_by_id(cls,report_id):
        report_delete = cls.search_by_id(report_id)
        db.session.delete(report_delete)
        try:
            db.session.commit()
            return True
        except:
            return False
