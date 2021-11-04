from flask import redirect, render_template, request, url_for, session, abort,flash
from app.models.user import User
from app.models.configuration import Configuration
from app.helpers.auth import Auth
from app.db import db

class Profile():

    def index_profile(username):
        try:
            user_retorned = User.query.filter_by(user = username).first()
            return render_template("profile.html", user=user_retorned)
        except:
            flash("Ingreso el url de un usuario invalido")
            return redirect(url_for("home"))
