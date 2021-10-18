from flask import redirect, render_template, request, url_for, flash,session
from app.models.configuration import Configuration
from app.models.views_sort import View_issues, View_users, View_meeting_points
from app.db import db
from app.helpers.configurations import putConfigurationsValuesInSession

background_dict = { "Gris claro" : "bg-light",
                     "Amarillo" : "bg-warning",
                     "Celeste" : "bg-info"}      


def index():
   getViewConfigs()
   valid_values = {  
      "items-per-page" : Configuration.get_valid_paginations(),
      "background-color" : Configuration.get_valid_colors()
   }
   print(session["configurations"]["items_per_page"])
   print(valid_values["items-per-page"])
   print(type(session["configurations"]["items_per_page"]))
   # Remuevo de el array que voy a presentar en la vista el valor actual de los items por pagina que este seleccionado
   valid_values["items-per-page"].remove(int(session["configurations"]["items_per_page"]))
   
   return render_template("configuration/index.html", values = valid_values)


def update():
    params = request.form
    config_row = Configuration.query.filter_by(id=1).first()
    # Si el valor ingresado en la seleccion de items por listado es invalida, entra al if
    if (int(params["items-per-page"])) not in Configuration.get_valid_paginations():
            flash("El valor de items por pagina es el incorrecto")
            return redirect(url_for("config_index"))
    else:
       config_row.items_per_page = params["items-per-page"]
       session["configurations"]["items_per_page"] = params["items-per-page"]
    if (params["color-background-selected"] not in Configuration.get_valid_colors()):
            flash("El color seleccionado no existe en el sistema")
            return redirect(url_for("home"))
    else:
      config_row.background = params["color-background-selected"]
      session["background"] = params["color-background-selected"]


    db.session.commit()
    return redirect(url_for("user_index"))
       


#def getBackground():


    # print(params)
    # flash(params)
    # return render_template("user_index")
    # return redirect(url_for("config_index"))


def getViewConfigs():
   config_row = Configuration.query.filter_by(id=1).first()
   return { "bg" : config_row.background,
            "items-per-page" : config_row.items_per_page}


   


    
