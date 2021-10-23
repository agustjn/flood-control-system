from flask import request,session
from app.models.configuration import Configuration
from app.models.views_sort import View_issues, View_users, View_meeting_points
from app.db import db
from app.helpers.configurations import putConfigurationsValuesInSession

def configSessionAttributes(user):
    #Hacer una consulta a la clase configuracion, y traerme los atributos de la clase
    session["user_object"] = user
    session["user"] = user.email
    session["first_and_last_name"] = user.first_name + ' ' + user.last_name
    session["first_name"] = user.first_name
    session["last_name"] = user.last_name
    session["email"] = user.email
    putConfigurationsValuesInSession()
    