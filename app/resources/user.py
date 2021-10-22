from flask import redirect, render_template, request, url_for, session, abort,flash
from app.models.user import User
from app.models.configuration import Configuration
from app.helpers.auth import authenticated
from app.db import db

# Protected resources



def index():
    if not authenticated(session):
        abort(401)
    rows_per_page = session["configurations"]["items_per_page"]
    page = request.args.get('page', 1, type=int)
    users = User.query.paginate(page=page, per_page=rows_per_page)
    return render_template("user/index.html", users=users)


def new():
    if not authenticated(session):
        abort(401)

    return render_template("user/new.html")


def create():
    if not authenticated(session):
        abort(401)
    parameter = request.form
    new_user = User(parameter["first_name"], parameter["last_name"], parameter["email"],parameter["user"],parameter["password"])
    validos = validate_empty_fields(new_user)
    if validos:
        answer = User.exist(new_user.email,new_user.usuario)

        db.session.add(new_user)
        try:
            db.session.commit()
        except:
            if answer:
                msj = "El " + answer + " ya existe, ingrese otro"
                flash(msj,"error")
            return redirect(url_for("user_new"))

        if not answer:
            msj = "Se creo el usuario " + new_user.usuario + " exitosamente"
            flash(msj)
            return redirect(url_for("user_index"))

    else:
        msj = "Por favor complete todos los campos"
        flash(msj,"error")
        return redirect(url_for("user_new"))

def validate_empty_fields(new_user):
    if  new_user.email  and new_user.password and new_user.usuario  and new_user.first_name and new_user.last_name:
        return True
    else:
        return False

def edit(user_id):
    if not authenticated(session):
        abort(401)
    modification_user = User.query.filter_by(id=user_id).first()
    flash ("Los campos que desea dejar igual dejenlo sin rellenar")
    return render_template("user/edit.html", user = modification_user)

def modify(user_id):
    parameter = request.form
    answer = User.exist(parameter["email"],parameter["user"])
    user_update = User.query.filter_by(id = user_id).first()
    if answer:
        msj = "El " + answer + " ya existe, por favor ingrese otro"
        flash(msj,"warning")
        return render_template("user/edit.html" , user = user_update)

    user_update = update(user_update,parameter)
    try:
        db.session.commit()
        msj = "Se modifico el usuario "+ user_update.usuario + " exitosamente"


    except Exception as e:
        msj = "Se produjo un error al modificar, intente nuevamente "
    flash (msj)
    return redirect(url_for("user_index"))

def update (user_update,parameter):
    if parameter["user"]:
        user_update.usuario = parameter["user"]
    if parameter["email"]:
        user_update.email = parameter["email"]
    if parameter["password"]:
        user_update.password = parameter["password"]
    if parameter["first_name"]:
        user_update.first_name = parameter["first_name"]
    if parameter["last_name"]:
        user_update.last_name = parameter["last_name"]
    return user_update

def delete(user_id):
    if not authenticated(session):
        abort(401)
    user_delete = User.query.filter_by(id=user_id).first()
    db.session.delete(user_delete)
    try:
        db.session.commit()
    except Exception:
        msj = "Error al quere borrar el usuario " + user_delete.usuario + " de la tabla"
        flash (msj,"error")

    msj = "El usuario " + user_delete.usuario + " a sido eliminado con exito"
    flash (msj,"info")
    return redirect(url_for("user_index"))
