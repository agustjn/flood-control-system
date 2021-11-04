from flask import redirect, render_template, request, url_for, session, abort,flash
from app.dao.point import PointDAO
from app.dao.configuration import ConfigurationDAO
from app.models.configuration import Configuration
from app.helpers.auth import Auth


from app.db import db
from app.models.point import Point

# Protected resources

def get_values_filter_columns():
    return ["Publicado","Despublicado","Todos"]

def _obtener_valores(status,texto):
    """ Obtengo los valores para mostrar los puntos de encuentro, ya sea con un filtro o no"""
    try:
        filtro = request.form["status_id"]
    except:
        filtro = status
    try:
        texto_a_filtrar = request.form["texto_id"]
    except:
        texto_a_filtrar = texto
    return (filtro,texto_a_filtrar)

def index():
    Auth.verify_authentification()
    filtro,texto_a_filtrar = _obtener_valores(status = "Todos",texto = "")
    dao = ConfigurationDAO()
    if texto_a_filtrar:
        filtered_points = PointDAO.filter_by_key(filtro,dao.items_per_page,texto_a_filtrar)
        texto = texto_a_filtrar
    else:
        texto = None
        filtered_points = PointDAO.filter_by_key(filtro,dao.items_per_page)

    values = get_values_filter_columns()
    values.remove(filtro)
    return render_template("point/index.html", points=filtered_points,values=values, filtro = filtro,texto=texto)

def new():
    Auth.verify_authentification()
    return render_template("point/new.html")


def create():
    Auth.verify_authentification()

    parameter = request.form
    validos = validate_empty_fields(parameter["name"], parameter["address"], parameter["coordinates_lat"],parameter["coordinates_long"],parameter["phone"],parameter["email"],parameter["status"])
    if validos:
        if PointDAO.exist_name(parameter["name"]):
            msj = "el Nombre "+ parameter["name"] + " ya existe, ingrese otro"
        elif PointDAO.exist_adress(parameter["address"]):
            msj = "La direccion " + parameter["address"] + " ya existe , ingrese otro "
        else:

            if PointDAO.create_user(parameter["name"], parameter["address"], parameter["coordinates_lat"],parameter["coordinates_long"],parameter["phone"],parameter["email"],parameter["status"]):
                msj = "Se creo el punto de encuentro " + parameter["name"] + " exitosamente"
            else:
                msj = "Ocurrio un error al crear el punto de encuentro, intente nuevamente"
            flash (msj)
            return redirect(url_for("point_index"))
    else:
        msj = "Por favor complete todos los campos"
    flash(msj,"error")
    return redirect(url_for("point_new"))



def validate_empty_fields(name, adress, coordinates,phone,email,status):
    if  name  and adress and coordinates  and phone and email and status:
        return True
    else:
        return False

def edit(point_id):
    Auth.verify_authentification()

    modification_point = PointDAO.search_by_id(point_id)
    msj = "Los campos que desea dejar igual dejenlo sin rellenar"
    return render_template("point/edit.html", point = modification_point, msj= msj)

def modify(point_id):
    parameter = request.form
    point_update = PointDAO.search_by_id(point_id)
    a = parameter["address"]
    if PointDAO.exist_name(parameter["name"]):
        msj = "el Nombre "+ parameter["name"] + " ya existe, ingrese otro"
    elif PointDAO.exist_adress(parameter["address"]):
        msj = "La direccion " + parameter["address"] + " ya existe , ingrese otro "

    else:
        if PointDAO.update(point_update,parameter["name"], parameter["address"], parameter["coordinates_lat"],parameter["coordinates_long"],parameter["phone"],parameter["email"],parameter["status"]) :
            msj = "Se modifico el punto de encuentro "+ point_update.name + " exitosamente"
        else:
            msj = "Se produjo un error al modificar, intente nuevamente "
        flash (msj)
        return redirect(url_for("point_index"))

    flash(msj,"warning")
    return render_template("point/edit.html" , point = point_update)


def delete(point_id):
    Auth.verify_authentification()
    point_delete = PointDAO.search_by_id(point_id)
    if PointDAO.delete(point_delete):
         msj = "El punto de encuentro " + point_delete.name + " a sido eliminado con exito"
    else:
        msj = "Error al querer borrar el punto de encuentro " + point_delete.name + " de la tabla, intene nuevamente"

    flash (msj,"info")
    return redirect(url_for("point_index"))
