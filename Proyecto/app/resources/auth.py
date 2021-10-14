from flask import redirect, render_template, request, url_for, abort, session, flash,make_response
from app.models.user import User
from app.helpers.sessionConfig import configSessionAttributes
from app.helpers.cookies import configCookies


def login():

    return render_template("auth/login.html")


def authenticate():
    params = request.form
    user = User.query.filter( User.email == params["email"] and User.password == params["password"]).first()

    #print (f"que imprime esto{user}")
    if not user:
        flash("Usuario o clave incorrecto.")
        return redirect(url_for("auth_login"))


    configSessionAttributes (session,user)


    flash("La sesión se inició correctamente.")
    return redirect(url_for("home"))


def logout():
    #resp = make_response(redirect(url_for("auth_login")))
    #setCookies(session,resp)

    del session["user"]
    session.clear()
    flash("La sesión se cerró correctamente.")

    return redirect(url_for("auth_login"))
