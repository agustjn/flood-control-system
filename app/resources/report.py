from flask import redirect, render_template, request, url_for,flash,session
from app.dao.configuration import ConfigurationDAO
from app.dao.user import UserDAO
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
    PermissionDAO.assert_permission(session["id"],"denuncia_index")
    filtro,texto_a_filtrar = _obtener_valores(status = "Todos",texto = "")
    dao = ConfigurationDAO()
    filtered_reports = ReportDAO.filter_by_key(filtro,dao.items_per_page,texto_a_filtrar)
    values = get_values_filter_columns()
    values.remove(filtro)
    return render_template("report/index.html", reportes=filtered_reports,values=values, filtro = filtro,texto=texto_a_filtrar)

def new():
    PermissionDAO.assert_permission(session["id"],"denuncia_new")
    #PermissionDAO.assert_permission(session["id"],"report_new")
    return render_template("report/new.html")

def create():
    PermissionDAO.assert_permission(session["id"],"denuncia_new")
    return render_template("report/new.html")

def delete(report_id):
    PermissionDAO.assert_permission(session["id"],"denuncia_destroy")
    report_delete = ReportDAO.search_by_id(report_id)
    if ReportDAO.delete_by_id(report_id):
        msj = "El reporte " + report_delete.title + " a sido eliminado con exito"
    else:
        msj = "Error al quere borrar el reporte  " + report_delete.title + " de la tabla"
    flash (msj,"info")
    return redirect(url_for("report_index"))


def edit(report_id):
    PermissionDAO.assert_permission(session["id"],"denuncia_update")
    modification_report = ReportDAO.search_by_id(report_id)
    users_assign = UserDAO.recover_users()
    msj = "Los campos que desea dejar igual dejenlo sin rellenar"
    user_asignado = modification_report.user_assing
    try:
        users_assign.remove(user_asignado)
    except:
        user_asignado = ""

    return render_template("report/edit.html", report = modification_report, msj = msj, users = users_assign,user_assing = user_asignado)

def modify(report_id):
    PermissionDAO.assert_permission(session["id"],"denuncia_update")
    parameter = request.form
    user_id = int(parameter["user_assing"])
    if (bool(UserDAO.search_by_id(user_id)) or (user_id == -1)):
        report_update = ReportDAO.search_by_id(report_id)
        if ReportDAO.existe_coordinates(coordinates_latitude = parameter["coordenada_lat"],coordinates_longitude = parameter["coordenda_long"]):
            msj = "Las coordenadas ya existen, se esta trabajando para arreglar el problema"
        else:
            if ReportDAO.update_report(report_update,parameter["title"],parameter["category"],parameter["description"],parameter["coordenada_lat"],parameter["coordenda_long"],
                parameter["first_name"],parameter["last_name"],parameter["phone"],parameter["email"],user_id):
                msj = "se modifico con exito el reporte " + parameter["title"]
            else:
                msj = "Se produjo un error al modificar, intente nuevamente "
                flash(msj)
                return redirect(url_for("report_edit",report_id = report_id))
    else:
        msj = "Ingrese un usuario valido "

    flash (msj)
    return redirect(url_for("report_index"))


def show(report_id):
    PermissionDAO.assert_permission(session["id"],"denuncia_show")
    report = ReportDAO.search_by_id(report_id)
    if report.status in ["Cerrada","Resuelta"]:
        cerrada = True
    else:
        cerrada = False
    return render_template("/report/detail.html",report = report,cerrada = cerrada)

def add_monitoring(report_id):
    PermissionDAO.assert_permission(session["id"],"denuncia_add_monitoring")
    if request.form["description"] != " ":
        description_create = ReportDAO.create_monitoring(request.form["description"],session["id"])
        ReportDAO.add_monitoring(report_id, description_create)
        flash ("Se agrego el seguimiento correctamente")
    else:
        flash("Ingrese una descripcion ")
    return redirect(url_for("report_show",report_id = report_id))

def close(report_id):
    PermissionDAO.assert_permission(session["id"],"denuncia_close")
    if ReportDAO.satisfy_three_monitoring(report_id):
        if ReportDAO.closing(report_id,request.form["description"],session["id"]):
            flash ("Se cerro la denuncia con exito")
        else:
            flash ("La denuncia ya estaba cerrada")
    else:
        flash ("Usted tien que generar 3 descripciones para cerrar el seguimiento")
    return redirect(url_for("report_show",report_id = report_id))

def resolved(report_id):
    PermissionDAO.assert_permission(session["id"],"denuncia_resolved")
    if request.form["description"] != " ":
        if ReportDAO.resolved(report_id,request.form["description"],session["id"]):
            flash ("Se cerro la denuncia con exito")
        else:
            flash ("La denuncia ya estaba cerrada")
    else:
        flash("Ingrese una descripcion ")
    return redirect(url_for("report_show",report_id = report_id))

def open(report_id):
    PermissionDAO.assert_permission(session["id"],"denuncia_open")
    report = ReportDAO.search_by_id(report_id)
    if  report.status in ["Cerrada","Resuelta"]:
        ReportDAO.open(report_id)
        flash("Se abrio nuevamente la denuncia")
    else:
        flash ("La denuncia ya estaba abierta")
    return redirect(url_for("report_show",report_id = report_id))
