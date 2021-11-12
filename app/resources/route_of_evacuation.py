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
    #PermissionDAO.assert_permission(session["id"],"route_of_evacuation_index")
    filtro,texto_a_filtrar = _obtener_valores(status = "Todos",texto = "")
    dao = ConfigurationDAO()
    filtered_route = Route_of_evacuationDAO.filter_by_key(filtro,dao.items_per_page,texto_a_filtrar)
    values = get_values_filter_columns()
    values.remove(filtro)
    return render_template("route_of_evacuation/index.html", routes=filtered_route,values=values, filtro = filtro,texto=texto_a_filtrar)
