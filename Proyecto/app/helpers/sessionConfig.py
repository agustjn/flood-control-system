from flask import request

def configSessionAttributes(session,user):
    session["user"] = user.email
    session["first_and_last_name"] = user.first_name + ' ' + user.last_name
    session["first_name"] = user.first_name
    session["last_name"] = user.last_name
    session["email"] = user.email

