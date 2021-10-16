from flask import redirect, render_template, request, url_for, flash
from app.models.configuration import Configuration
from app.models.views_sort import View_issues, View_users, View_meeting_points
from app.db import db


def index():
    return render_template("configuration/index.html")


def update():
    params = request.form
    print("Valor del formulario: " , int(params["items-per-page"]))
    print("Valor del valid paginations: ", Configuration.get_valid_paginations())
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





    
