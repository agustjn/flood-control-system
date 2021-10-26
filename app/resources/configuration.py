from flask import render_template, request, flash
from app.models.configuration import Configuration
from app.helpers.auth import Auth
from app.dao.configuration import ConfigurationDAO

def index():
   Auth.verify_authentification()
   dao = ConfigurationDAO()
   config_values = dao.values_to_render()
   flash(config_values)
   return render_template("configuration/index.html", values = config_values)


def update():
    Auth.verify_authentification()
    errors = []
    configDao = ConfigurationDAO()
    params = request.form
    if (int(params["items-per-page"])) not in Configuration.get_valid_paginations():
            errors.append("La cantidad de items por pagina que ingreso es invalida") 

    else:
            # configDao en su setter, hace el commit en la bd.
            configDao.items_per_page = int(params["items-per-page"])

    if (params["color-background-selected"] not in Configuration.get_valid_colors()):
       errors.append("Ingreso un color invalido para el color de fondo")
    else:
            configDao.background = params["color-background-selected"]
    if ( (params["user-col-selected"] not in Configuration.get_valid_user_columns()) or (params["user-type-selected"] not in Configuration.get_valid_sort_types()) ):
         errors.append("El campo seleccionado para ordenar los usuario o su tipo de orden son incorrectos.")
    else:
       configDao.set_view_user_values({ 
          "column":params["user-col-selected"],
          "type":params["user-type-selected"]
       })

    return render_template("configuration/index.html", values = configDao.values_to_render(), errors = errors)
