import re

from werkzeug.utils import redirect, secure_filename
from app.helpers.auth import Auth
from flask import render_template, request, url_for, flash
from app.dao.configuration import ConfigurationDAO
from app.dao.flood_zone import FloodZoneDao
from app.models.coordinate import Coordinate
from app.models.flood_zone import FloodZone
import csv
import os

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


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'csv', 'xls', 'xlsx'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def update_csv():
    
    file = request.files['file']
    print(allowed_file(file.filename))
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # NECESITO GUARDARLO PORQUE NO SE COMO ABRIRLO COMO CSV
        # File es una instancia de FileStorage, y no se como obtener el csv solo para hacer un open
        file_route = os.path.join('app/static/uploaded_files', filename)
        file.save(file_route)
        with open(file_route, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                FloodZone(name=row[0])
                print('--------------------------')
                print("Nombre de zona: {}".format(row[0]))
                print('--------------------------')


    else:
        flash("No ha subido ningun archivo.")
        return redirect(url_for("flood_zone_index"))
    return redirect(url_for("flood_zone_index"))

def profile(id):
    return render_template("flood_zone/profile.html")
    
