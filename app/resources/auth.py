from flask import redirect, render_template, request, url_for, abort, session, flash,make_response
from app.models.user import User
from app.helpers.sessionConfig import configSessionAttributes
from app.dao.auth import AuthDAO

def login():
    return render_template("auth/login.html")


def authenticate():
    params = request.form
    us = request.form["email"]
    pa = request.form["password"]
    print (f"el usuario es {us} y la contra {pa} --------------------------------------------")
    user = AuthDAO.authenticate(params["email"],params["password"])


    if not user:
        msj = "Usuario o clave incorrecto."
        return render_template("auth/login.html",msj=msj)
    configSessionAttributes (user)

    msj = "La sesión se inició correctamente."
    return render_template("home.html",msj=msj)


def logout():
    del session["user"]
    session.clear()
    flash("La sesión se cerró correctamente.")
    return redirect(url_for("auth_login"))
