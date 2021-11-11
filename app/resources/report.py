from flask import redirect, render_template, request, url_for,flash,session
from app.dao.configuration import ConfigurationDAO

from app.helpers.auth import Auth

from app.helpers.permission import PermissionDAO

from app.dao.report import ReportDAO
import json

def get_values_filter_columns():
    return ["En curso","Resuelta","Cerrada","Sin confirmar","Todos"]

def _obtener_valores(status, texto):
    """ Obtengo los valores para mostrar los reportes, ya sea con un filtro o no"""
    if request.args.get('status_id') is None:
        filtro = status
    else:
        filtro = request.args.get('status_id')
    if request.args.get('texto_id') is None:
        texto_a_filtrar = texto
    else:
        texto_a_filtrar = request.args.get('texto_id')
    return (filtro,texto_a_filtrar)


def index():
    #PermissionDAO.assert_permission(session["id"],"usuario_index")

    filtro,texto_a_filtrar = _obtener_valores(status = "Todos",texto = "")
    dao = ConfigurationDAO()
    filtered_reports = ReportDAO.filter_by_key(filtro,dao.items_per_page,texto_a_filtrar)
    values = get_values_filter_columns()
    values.remove(filtro)
    return render_template("report/index.html", reportes=filtered_reports,values=values, filtro = filtro,texto=texto_a_filtrar)

def new():
    #PermissionDAO.assert_permission(session["id"],"report_new")
    return render_template("report/new.html")

def create():
    
    return render_template("report/new.html")

def delete(report_id):
    #PermissionDAO.assert_permission(session["id"],"report_destroy")
    report_delete = ReportDAO.search_by_id(report_id)
    if ReportDAO.delete_by_id(report_id):
        msj = "El reporte " + report_delete.title + " a sido eliminado con exito"
    else:
        msj = "Error al quere borrar el reporte  " + report_delete.title + " de la tabla"
    flash (msj,"info")
    return redirect(url_for("report_index"))


def edit(report_id):

    #PermissionDAO.assert_permission(session["id"],"usuario_update")
    modification_report = ReportDAO.search_by_id(report_id)
    msj = "Los campos que desea dejar igual dejenlo sin rellenar"
    return render_template("report/edit.html", report = modification_report, msj = msj)

def modify(report_id):
    #PermissionDAO.assert_permission(session["id"],"usuario_update")

    parameter = request.form
    report_update = ReportDAO.search_by_id(report_id)
    if ReportDAO.existe_coordinates(coordenadas_latitude = parameter["coordinates_latitude"],coordinates_longitude = parameter["coordinates_longitude"]):
        msj = "Las coordenadas ya existen, se esta trabajando para arreglar el problema"
    else:
        if ReportDAO.create_report(parameter["title"],parameter["category"],parameter["coordenada_lat"],parameter["coordenda_long"],parameter["first_name"],parameter["last_name"],parameter["phone"],parameter["email"],parameter["descript"]):
            msj = "se creo con exito el reporte " + parameter["title"] + " con exito"
        else:
            msj = "Se produjo un error al modificar, intente nuevamente "
        return redirect(url_for("report_index"))

    flash(msj)
    return render_template("report/edit.html" , report = report_update)

def show(report_id):
    report_update = ReportDAO.search_by_id(report_id)
    report = {"title": report_update.title,
            "status": report_update.status,
            "category": report_update.category,
            "creation_date": report_update.creation_date,
            "closing_date": report_update.closing_date,
            "description": report_update.description,
            "coordinates_latitude": report_update.coordinates_latitude,
            "coordinates_longitude": report_update.coordinates_longitude,
            "first_name": report_update.first_name,
            "last_name": report_update.last_name,
            "phone": report_update.phone,
            "email": report_update.email,
            "user_assing": report_update.user_assing.name
            }
    report_json = json.dumps(user)
    return report_json