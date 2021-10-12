from flask import request

def configSessionAttributes(session,user):
    session["user"] = user.email
    session["name"] = user.first_name + ' ' + user.last_name
    # if request.cookies.get("customizations") == '0': # Si no tiene personalizaciones previamente existentes 
    #     createCustomizations(session)
        
    # else:
    #     session["customizations"] = request.cookies.get("customizations")
    
# Creacion de las personalizaciones por defecto
# def createCustomizations(session):
#     session["customizations"] = { 
#         "items-per-page": 15 ,
#         "sort-order": "Alfabetic",
#         "background-color": "bg-grey"
#     }


# Se setean las cookies cuando se cierra sesion
# def setCookies(response):
#     response.set_cookie('customizations', '1')
#     response.set_cookie('items-per-page', session["customizations"]["items-per-page"])
#     response.set_cookie('sort-order', session["customizations"]["sort-order"])
#     response.set_cookie('background-color', session["customizations"]["background-color"])

