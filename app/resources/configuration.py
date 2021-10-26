from flask import config, redirect, render_template, request, url_for, flash,session
from app.models.configuration import Configuration
from app.models.views_sort import View_issues, View_users, View_meeting_points
from app.db import db
from app.helpers.auth import Auth
from app.helpers.configurations import putConfigurationsValuesInSession
from app.dao.configuration import ConfigurationDAO

# background_dict = { "Gris claro" : "bg-light",
#                      "Amarillo" : "bg-warning",
#                      "Celeste" : "bg-info"}


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
    config_row = Configuration.query.filter_by(id=1).first()
    try:
         configDao.items_per_page = int(params["items-per-page"])
    except:
         errors.append("La cantidad de items por pagina que ingreso es invalida")  
         return render_template("configuration/index.html", values = configDao.values_to_render(), errors = errors)

   #  if (int(params["items-per-page"])) not in Configuration.get_valid_paginations():
   #          errors.append("La cantidad de items por pagina que ingreso es invalida") 
   #          return render_template("configuration/index.html", values = configDao.values_to_render(), errors = errors)
   #  else:
   #          # configDao en su setter, hace el commit en la bd.
   #          configDao.items_per_page = int(params["items-per-page"])
      
    try:
       configDao.background = params["color-background-selected"]
    except:
       errors.append("Ingreso un color invalido para el color de fondo")
       return render_template("configuration/index.html", values = configDao.values_to_render(), errors = errors)
   #  if (params["color-background-selected"] not in Configuration.get_valid_colors()):
   #          flash("El color seleccionado no existe en el sistema")
   #          return redirect(url_for("config_index"))
   #  else:
   #          configDao.background = params["color-background-selected"]

    return redirect(url_for("config_index"))
