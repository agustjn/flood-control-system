from flask import redirect, render_template, request, url_for, abort, session, flash,make_response
from app.db import connection
from app.models.user import User
from app.helpers.sessionConfig import configSessionAttributes
from app.helpers.cookies import configCookies


def login():
    
    return render_template("auth/login.html")


def authenticate():
    conn = connection()
    params = request.form

    user = User.find_by_email_and_pass(conn, params["email"], params["password"])

    if not user:
        flash("Usuario o clave incorrecto.")
        return redirect(url_for("auth_login"))
    # Si el usuario existe y es correcto
    # resp = make_response(redirect(url_for("home")))
    # cookies = request.cookies
    # configCookies(resp,cookies)
    configSessionAttributes(session,user)
    flash("La sesión se inició correctamente.")

    return redirect(url_for("home"))


def logout():
    #resp = make_response(redirect(url_for("auth_login")))
    #setCookies(session,resp)
    
    del session["user"]
    session.clear()
    flash("La sesión se cerró correctamente.")

    return redirect(url_for("auth_login"))
