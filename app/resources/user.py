from flask import redirect, render_template, request, url_for,flash
from app.dao.configuration import ConfigurationDAO
from app.dao.user import UserDAO
from app.helpers.auth import Auth

# Protected resources




def index():
    Auth.verify_authentification()
    dao = ConfigurationDAO()
    users = UserDAO.users_paginated(dao.items_per_page)
    return render_template("user/index.html", users=users)


def new():
    Auth.verify_authentification()
    return render_template("user/new.html")


def create():
    Auth.verify_authentification()
    parameter = request.form
    validos = validate_empty_fields(parameter["first_name"], parameter["last_name"], parameter["email"],parameter["user"],parameter["password"])

    if validos:
        if UserDAO.exist_email(parameter["email"]):
            msj = "El email " + parameter["email"] +" ya existe, ingrese otro"
        elif UserDAO.exist_username(parameter["user"]):
            msj = "El usuario " + parameter["user"] + " ya existe, ingrese otro"
        else:
            #new_user = UserDAO.new_user(parameter["first_name"], parameter["last_name"], parameter["email"],parameter["user"],parameter["password"])
            if (UserDAO.create_user(parameter)):
                msj = "Se creo el usuario " + parameter["user"] + " exitosamente"
                flash(msj)
                return redirect(url_for("user_index"))
    else:
        msj = "Por favor complete todos los campos"
    flash(msj)
    return redirect(url_for("user_new"))


def validate_empty_fields(first_name,last_name,email,usuario,password):
    if  email  and password and usuario  and first_name and last_name:
        return True
    else:
        return False

def edit(user_id):
    Auth.verify_authentification()
    UserDAO.search_by_id(user_id)
    modification_user = UserDAO.search_by_id(user_id)
    msj = "Los campos que desea dejar igual dejenlo sin rellenar"
    return render_template("user/edit.html", user = modification_user, msj = msj)

def modify(user_id):
    parameter = request.form
    user_update = UserDAO.search_by_id(user_id)
    emailBoolean = UserDAO.exist_email(parameter["email"])
    if emailBoolean:
        msj = "El email " + parameter["email"] +" ya existe, ingrese otro"
    elif UserDAO.exist_username(parameter["user"]):
        msj = "El usuario " + parameter["user"] + " ya existe, ingrese otro"

    else:
        obj = UserDAO.update(user_update,parameter)
        if obj:
            msj = "Se modifico el usuario " + user_update.usuario + " exitosamente"
        else:
            msj = "Se produjo un error al modificar, intente nuevamente "
        flash (msj)
        return redirect(url_for("user_index"))

    flash(msj)
    return render_template("user/edit.html" , user = user_update)

def delete(user_id):
    Auth.verify_authentification()
    user_delete = UserDAO.search_by_id(user_id)
    if UserDAO.delete_by_id(user_id):
        msj = "El usuario " + user_delete.usuario + " a sido eliminado con exito"
    else:
        msj = "Error al quere borrar el usuario " + user_delete.usuario + " de la tabla"
    flash (msj,"info")
    return redirect(url_for("user_index"))
