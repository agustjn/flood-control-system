from app.dao.report import ReportDAO
from flask import jsonify, Blueprint, request
from app.scheme.report import  reports_scheme,report_scheme, ReportScheme, Report_show_id

report_api = Blueprint("reportes",__name__, url_prefix = "/report")

@report_api.get("/")
def index():
    """Recupera todos las denuncias de la base de dato, habria que ver si hay campos que no hay que mostrar"""
    recover_reports_row = ReportDAO.recover_reports()
    reports = reports_scheme.dump(recover_reports_row)
    return jsonify(reports)

@report_api.post("/")
def create():
    user_data = request.get_json()
    schema = ReportScheme()
    result = schema.load(user_data)
    return jsonify([]),201

@report_api.get("/show")
def show():
    report_id = request.get_json()
    #schema = Report_show_id()
    #result = scheme.load(report_id)
    dic = {"name": "nombre", "id": report_id}
    return jsonify(dic),200
