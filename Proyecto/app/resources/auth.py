from flask import redirect, render_template, request, url_for, abort, session, flash
from app.models.user import User
from app.helpers.sessionConfig import configSessionAttributes


def login():
    return render_template("auth/login.html")


def authenticate():
    # conn = connection()
    # params = request.form

    #user = User.find_by_email_and_pass(conn, params["email"], params["password"])
    params = request.form
    user = User.query.filter( User.email == params["email"] and User.password == params["password"]).first()

    if not user:
        flash("Usuario o clave incorrecto.")
        return redirect(url_for("auth_login"))


    configSessionAttributes (session,user)    

    session["email"] = user.email
    flash("La sesión se inició correctamente.")
    return redirect(url_for("home"))


def logout():
    del session["user"]
    session.clear()
    flash("La sesión se cerró correctamente.")

    return redirect(url_for("auth_login"))
