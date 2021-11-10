import re
from app.helpers.auth import Auth
from flask import render_template, request
from app.dao.configuration import ConfigurationDAO
from app.dao.flood_zone import FloodZoneDao
import csv


# def flood_zones_index():
#     Auth.is_authenticated()
#     # Permisos de ver index: Operador/Administrador
    
#     return render_template("flood_zone/index.html")

def get_values_filter_columns():
    return ["Publicado","Despublicado","Todos"]

def _obtener_valores(status, texto):
    """ Obtengo los valores para mostrar las zonas, ya sea con un filtro o no"""
    if request.args.get('status_id') is None:
        filtro = status
    else:
        filtro = request.args.get('status_id')
    if request.args.get('texto_id') is None:
        texto_a_filtrar = texto
    else:
        texto_a_filtrar = request.args.get('texto_id')
    return (filtro,texto_a_filtrar)

def flood_zones_index():
    # Permisos de ver index: Operador/Administrador
    
    filtro,texto_a_filtrar = _obtener_valores(status = "Todos",texto = "")
    dao = ConfigurationDAO()
    filtered_zones = FloodZoneDao.filter_by_key(filtro,dao.items_per_page,texto_a_filtrar)
    values = get_values_filter_columns()
    values.remove(filtro)
    return render_template("flood_zone/index.html", zones=filtered_zones,values=values, filtro = filtro,texto=texto_a_filtrar)


def update_csv():
    file = request.files['file']
    # with open(file, 'r') as csv:
    #     for row in csv:
    #         print(row)
    print('--------------------------')
    print(file)

def profile(id):
    return render_template("flood_zone/profile.html")
    
