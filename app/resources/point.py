from flask import redirect, render_template, request, url_for, session, abort,flash
from app.models.point import Point
from app.models.configuration import Configuration
from app.helpers.auth import authenticated
from app.db import db

# Protected resources

def index_filtro():
    if not authenticated(session):
        abort(401)
    status = request.form["status_id"]
    points = Point.query.filter_by(estado = status).all()
    return render_template("point/index.html", points=points)

def index():
    if not authenticated(session):
        abort(401)
    points = Point.query.all()
    return render_template("point/index.html", points = points)


def new():
    if not authenticated(session):
        abort(401)

    return render_template("point/new.html")


def create():
    if not authenticated(session):
        abort(401)
    parameter = request.form
    new_point = Point(parameter["name"], parameter["adress"], parameter["coordinates"],parameter["phone"],parameter["email"],parameter["status"])
    validos = validate_empty_fields(new_point)
    if validos:
        answer = Point.exist(new_point.nombre,new_point.direccion)
        db.session.add(new_point)
        try:
            db.session.commit()
        except Exception:
            if answer:
                msj = "El " + answer + " ya existe, ingrese otro"
                flash(msj,"error")
            return redirect(url_for("point_new"))

        if not answer:
            msj = "Se creo el punto de encuentro " + new_point.nombre + " exitosamente"
            flash(msj)
            return redirect(url_for("point_index"))

    else:
        msj = "Por favor complete todos los campos"
        flash(msj,"error")
        return redirect(url_for("point_new"))

def validate_empty_fields(new_point):
    if  new_point.nombre  and new_point.direccion and new_point.coordenadas  and new_point.estado and new_point.telefono and new_point.email:
        return True
    else:
        return False

def edit(point_id):
    if not authenticated(session):
        abort(401)
    modification_point = Point.query.filter_by(id=point_id).first()
    flash ("Los campos que desea dejar igual dejenlo sin rellenar")
    return render_template("point/edit.html", point = modification_point)

def modify(point_id):
    print (f"---------------------------entro------------------------------")
    parameter = request.form
    answer = Point.exist(parameter["name"],parameter["adress"])
    point_update = Point.query.filter_by(id = point_id).first()
    if answer:
        msj = "El " + answer + " ya existe, por favor ingrese otro"
        flash(msj,"warning")
        return render_template("point/edit.html" , point = point_update)

    point_update = update(point_update,parameter)
    try:
        db.session.commit()
        msj = "Se modifico el punto de encuentro "+ point_update.nombre + " exitosamente"
    except Exception as e:
        msj = "Se produjo un error al modificar, intente nuevamente "
    flash (msj)
    return redirect(url_for("point_index"))

def update (point_update,parameter):
    if parameter["name"]:
        point_update.nombre = parameter["name"]
    if parameter["answer"]:
        point_update.direccion = parameter["answer"]
    if parameter["coordinates"]:
        point_update.coordenadas = parameter["coordinates"]
    if parameter["status"]:
        point_update.estadp = parameter["status"]
    if parameter["phone"]:
        point_update.telefono = parameter["phone"]
    if parameter["email"]:
        point_update.email = parameter["email"]
    return point_update

def delete(point_id):
    if not authenticated(session):
        abort(401)
    point_delete = Point.query.filter_by(id=point_id).first()
    db.session.delete(point_delete)
    try:
        db.session.commit()
    except Exception:
        msj = "Error al querer borrar el punto de encuentro " + point_delete.nombre + " de la tabla, intene nuevamente"
        flash (msj,"error")

    msj = "El punto de encuentro " + point_delete.nombre + " a sido eliminado con exito"
    flash (msj,"info")
    return redirect(url_for("point_index"))
