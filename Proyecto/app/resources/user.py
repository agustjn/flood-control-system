from flask import redirect, render_template, request, url_for, session, abort,flash
from app.models.user import User
from app.models.configuration import Configuration
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
    parameter = request.form

    last_configuration_id = User.query.order_by(User.configuration_id.desc()).first()

    last_configuration_id = last_configuration_id.configuration_id

    print (f"-------------------------------------------------{last_configuration_id}--------------------------------------------")
    new_user = User(parameter["first_name"], parameter["last_name"], parameter["email"],parameter["password"],last_configuration_id)

    new_configuration = Configuration()
    db.session.add(new_configuration)
    db.session.commit()

    db.session.add(new_user)
    db.session.commit()
    flash("Se creo el usuario")

    return redirect(url_for("user_index"))

def update():
    if not authenticated(session):
        abort(401)

    session["users"]
