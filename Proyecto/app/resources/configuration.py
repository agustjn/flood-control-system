from flask import redirect, render_template, request, url_for, flash,session
from app.models.configuration import Configuration
from app.models.views_sort import View_issues, View_users, View_meeting_points
from app.db import db
from app.helpers.configurations import putConfigurationsValuesInSession


def index():
   view_values = {  
      "items-per-page" : Configuration.get_valid_paginations()
   }
   # Remuevo de el array que voy a presentar en la vista el valor actual de los items por pagina que este seleccionado
   view_values["items-per-page"].remove(session["configurations"]["items_per_page"])
   
   return render_template("configuration/index.html", values = view_values)


def update():
    params = request.form
    if (int(params["items-per-page"])) not in Configuration.get_valid_paginations():
            flash("El valor de items por pagina es el incorrecto")
            return redirect(url_for("config_index"))
    else:
       print("VALOR ITEMS PER PAGE: " ,params["items-per-page"])
       #print(Configuration.items_per_page)
       config_row = Configuration.query.filter_by(id=1).first()
       config_row.items_per_page = params["items-per-page"]
    #    Configuration.setItemsPerPage(int(params["items-per-page"]))
       db.session.commit()
    return redirect(url_for("user_index"))
       

    # print(params)
    # flash(params)
    # return render_template("user_index")
    # return redirect(url_for("config_index"))


   


    
