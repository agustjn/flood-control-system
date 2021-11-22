from flask import redirect, render_template, request, url_for,flash,session
from app.dao.configuration import ConfigurationDAO
from app.dao.route_of_evacuation import Route_of_evacuationDAO
from app.helpers.auth import Auth

from app.helpers.permission import PermissionDAO


# Protected resources


def get_values_filter_columns():
    return ["Publicado","Despublicado","Todos"]


def _obtener_valores(status, texto):
    """ Obtengo los valores para mostrar las rutas de evacuacion, ya sea con un filtro o no"""
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
    #PermissionDAO.assert_permission("route_of_evacuation_index")
    filtro,texto_a_filtrar = _obtener_valores(status = "Todos",texto = "")
    dao = ConfigurationDAO()
    filtered_route = Route_of_evacuationDAO.filter_by_key(filtro,dao.items_per_page,texto_a_filtrar)
    values = get_values_filter_columns()
    values.remove(filtro)
    return render_template("route_of_evacuation/index.html", routes=filtered_route,values=values, filtro = filtro,texto=texto_a_filtrar)

def new():
    #PermissionDAO.assert_permission("route_of_evacuation_new")
    return render_template("route_of_evacuation/new.html")

def create():
    #PermissionDAO.assert_permission("route_of_evacuation_new")
    parameter = request.form
    if (_validate_empty_fields(parameter["name"],parameter["publicado"],parameter["coordinates_lat"],parameter["coordinates_long"],parameter["description"])):
            if not Route_of_evacuationDAO.exist_coordinates(coordinates_latitude = parameter["coordinates_lat"], coordinates_longitude = parameter["coordinates_long"]):
                if Route_of_evacuationDAO.create_route(parameter["name"],bool(parameter.get('publicado')),parameter["coordinates_lat"],parameter["coordinates_long"],parameter["description"]):
                    msj = "Se creo el recorrido de evacuacion " + parameter["name"] + " con exito"
                    flash (msj)
                    return redirect(url_for("route_index"))
                else:
                    msj = "Se produjo un error al momento de crealo, intentelo nuevamente"
            else:
                msj = "Las coordenadas ingresadas ya existen, ingrese otras "
    else:
        msj = "Complete todos los campos para que puedas continuar"
    flash (msj)
    return render_template("route_of_evacuation/new.html")

def _validate_empty_fields(name,publicado,coordinates_lat,coordinates_long,description):
    return bool((name and publicado and coordinates_lat and coordinates_long and description))
