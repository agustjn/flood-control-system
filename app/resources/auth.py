from flask import redirect, render_template, request, url_for, abort, session, flash,make_response
from app.models.user import User
from app.helpers.sessionConfig import configSessionAttributes


def login():
    print("!!!!!!!!!!!!Q")
    return render_template("auth/login.html")


def authenticate():
    params = request.form
    user = User.query.filter( User.email == params["email"] and User.password == params["password"]).first()

    #print (f"que imprime esto{user}")
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
