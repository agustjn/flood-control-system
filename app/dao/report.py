from app.models.user import User
from app.db import db
from app.models.report import Report

class ReportDAO():
    """Genera las consultas necesarios para consultar la informacion del denuncias en la base de datos en el resource"""

    @staticmethod
    def create_report(cls,datos):
        new_user = Report(datos)
        db.session.add(new_user)
        try:
            db.session.commit()
            return True
        except:
            return False
