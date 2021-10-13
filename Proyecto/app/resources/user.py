from flask import redirect, render_template, request, url_for, session, abort,flash
from app.models.user import User
from app.helpers.auth import authenticated
from app.db import db

# Protected resources
def index():
    if not authenticated(session):
        abort(401)


    # conn = connection()
    # users = User.all(conn)
    users = User.query.all()
    return render_template("user/index.html", users=users)


def new():
    if not authenticated(session):
        abort(401)

    return render_template("user/new.html")


def create():
    if not authenticated(session):
        abort(401)
    parametros = request.form
    userTest = User(parametros["first_name"], parametros["last_name"], parametros["email"],parametros["password"])
    print(userTest)
    db.session.add(userTest)
    db.session.commit()
    flash("Se creo el usuario")
    #conn = connection()
    #User.create(conn, request.form)
    return redirect(url_for("user_index"))
