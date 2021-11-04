from flask import redirect, render_template, request, url_for,flash,session
from app.dao.configuration import ConfigurationDAO
from app.dao.user import UserDAO
from app.helpers.auth import Auth

from app.helpers.permission import PermissionDAO

# Protected resources


def get_values_filter_columns():
    return ["Activo","Bloqueado","Todos"]


def obtener_valores(status, texto):
    """ Obtengo los valores para mostrar los usuarios, ya sea con un filtro o no"""
    try:
        filtro = request.form["status_id"]
        print (f"------------------ status funcionnn tiene {p}----------------------------")
    except:
        filtro = status
    try:
        texto_a_filtrar = request.form["texto_id"]
    except:
        texto_a_filtrar = texto
    return (filtro,texto_a_filtrar)

def index():
    Auth.verify_authentification()
    #p = request.form["status_id"]
    #print (f"------------------ status tiene {p}----------------------------")
    filtro,texto_a_filtrar = obtener_valores(status = "Todos",texto = "")
    print (f"------------------{filtro}---------------texto {texto_a_filtrar}-----------")
    dao = ConfigurationDAO()
    if texto_a_filtrar:
        filtered_users = UserDAO.filter_by_key(filtro,dao.items_per_page,texto_a_filtrar)
        texto = texto_a_filtrar
    else:
        texto = None
        filtered_users = UserDAO.filter_by_key(filtro,dao.items_per_page)

    values = get_values_filter_columns()
    values.remove(filtro)
    print (f"------------------{values}-----------------")

    return render_template("user/index.html", users=filtered_users,values=values, filtro = filtro,texto=texto)


def new():
    # Auth.verify_authentification()
    return render_template("user/new.html")

# def assert_permission(session,permission_name):
#     Auth.verify_authentification()
#     user = session["user"]
#     if user.is_admin:
#         return True
#     if not PermissionDAO.has_permission(user,permission_name):
#         abort(403)


def create():
    Auth.verify_authentification()
    # assert_permission(session,"user_create")
    parameter = request.form
    errors = []

    validos = validate_empty_fields(parameter["first_name"], parameter["last_name"], parameter["email"],parameter["user"],parameter["password"])
    if validos:
        if UserDAO.exist_email(parameter["email"]):
            errors.append("El email " + parameter["email"] +" ya existe, ingrese otro")
        elif UserDAO.exist_username(parameter["user"]):
            errors.append("El usuario " + parameter["user"] + " ya existe, ingrese otro")
        else:
            if (UserDAO.create_user(parameter)):
                msj = "Se creo el usuario " + parameter["user"] + " exitosamente"
                flash(msj)
                return redirect(url_for("user_index"))
    else:
        errors.append("Por favor complete todos los campos")
    # flash(msj)
    return render_template("user/new.html", errors = errors)


def validate_empty_fields(first_name,last_name,email,user,password):
    if  email  and password and user  and first_name and last_name:
        return True
    else:
        return False


def edit(user_id):

    PermissionDAO.assert_permission(session["id"],"usuario_actualizate")

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
            msj = "Se modifico el usuario " + user_update.user + " exitosamente"
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
        msj = "El usuario " + user_delete.user + " a sido eliminado con exito"
    else:
        msj = "Error al quere borrar el usuario " + user_delete.user + " de la tabla"
    flash (msj,"info")
    return redirect(url_for("user_index"))

def activate_desactivate(user_id):
    Auth.verify_authentification()
    UserDAO.activate_desactivate(user_id)
    return redirect(url_for("user_index"))
