from flask import redirect, render_template, request, url_for,flash,session
from app.dao.configuration import ConfigurationDAO

from app.helpers.auth import Auth

from app.helpers.permission import PermissionDAO

from app.dao.report import ReportDAO


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
    filtered_users = ReportDAO.filter_by_key(filtro,dao.items_per_page,texto_a_filtrar)
    values = get_values_filter_columns()
    values.remove(filtro)
    return render_template("report/index.html", reportes=filtered_users,values=values, filtro = filtro,texto=texto_a_filtrar)

def new():
    PermissionDAO.assert_permission(session["id"],"report_new")
    return render_template("user/new.html")


def delete(report_id):
    #PermissionDAO.assert_permission(session["id"],"report_destroy")
    report_delete = ReportDAO.search_by_id(report_id)
    if ReportDAO.delete_by_id(report_id):
        msj = "El reporte " + report_delete.title + " a sido eliminado con exito"
    else:
        msj = "Error al quere borrar el reporte  " + report_delete.title + " de la tabla"
    flash (msj,"info")
    return redirect(url_for("report_index"))
