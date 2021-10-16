from flask import redirect, render_template, request, url_for, session, abort,flash
from app.models.user import User
from app.models.configuration import Configuration
from app.helpers.auth import authenticated
from app.db import db

# Protected resources

def index():
    rows_per_page = session
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
    parameter = request.form
    #last_configuration_id = User.get_last_id()
    new_user = User(parameter["first_name"], parameter["last_name"], parameter["email"],parameter["user"],parameter["password"])
    #se crea la tabla de configuracion para asociar a el usuario creado
    #new_configuration = Configuration()
    #db.session.add(new_configuration)
    #db.session.commit()



    db.session.add(new_user)
    db.session.commit()

    flash("Se creo el usuario")
    return redirect(url_for("user_index"))

def update():
    if not authenticated(session):
        abort(401)
    modification_id = request.form["user_id"]
    modification_user = User.query.filter_by(id=modification_id).first()
    return render_template("user/edit.html", user = modification_user)

def delete():
    if not authenticated(session):
        abort(401)
    user_id = request.form["user_id"]
    deletetodo = User.query.filter_by(id=user_id).first()
    db.session.delete(deletetodo)
    db.session.commit()
    return redirect(url_for("user_index"))

def modification(id):
    #User.query.filter_by(id = id_user)
    #if user.email:
    return none
