from flask import request

def configSessionAttributes(session,user):
    #Hacer una consulta a la clase configuracion, y traerme los atributos de la clase
    session["user_object"] = user
    session["user"] = user.email
    session["first_and_last_name"] = user.first_name + ' ' + user.last_name
    session["first_name"] = user.first_name
    session["last_name"] = user.last_name
    session["email"] = user.email

    # Se setean las configuraciones de las vistas para contenerlas mas a mano
    # session["views"] = {  
    #     "view_users" = 
    # }
