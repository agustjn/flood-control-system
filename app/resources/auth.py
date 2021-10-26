from flask import redirect, render_template, request, url_for, abort, session, flash,make_response
from app.models.user import User
from app.helpers.sessionConfig import configSessionAttributes
from app.dao.auth import AuthDAO

def login():
    return render_template("auth/login.html")


def authenticate():
    params = request.form
    user = AuthDAO.authenticate(params["email"],params["password"])

    
    if not user:
        flash("Usuario o clave incorrecto.")
        return redirect(url_for("auth_login"))
    configSessionAttributes (user)

    flash("La sesión se inició correctamente.")
    return redirect(url_for("home"))


def logout():
    del session["user"]
    session.clear()
    flash("La sesión se cerró correctamente.")
    return redirect(url_for("auth_login"))
