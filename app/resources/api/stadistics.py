from app.dao.report import ReportDAO
from flask import jsonify, Blueprint, request
from app.scheme.report import  reports_scheme

stadistics_api = Blueprint("estadisticas",__name__, url_prefix = "/stadistics")

@stadistics_api.get("/")
def index():
    """Recupera todas las denuncias de la base de dato"""
    recover_reports_stadistics_row = ReportDAO.recover_reports()
    reports = reports_scheme.dump(recover_reports_stadistics_row)
    return jsonify(reports)
'denuncias por categoria= grafico de torta'
'denuncias asignadas a usuario= grafico de barra'
'linea de tiempo denuncias por dia'
'cantidad de denuncias por zona inundable'
'estado de las denuncias'

