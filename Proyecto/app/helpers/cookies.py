from flask import request

def configCookies(resp,cookies):
    if cookies.get("customizations") == '0': # Si no tiene personalizaciones previamente existentes 
        setDefaultCustomizationsCookies(resp)
    else: # Se cargan los valores previos de sus configuraciones globales
        loadCookiesValues(session,cookies)
    return resp


def setDefaultCustomizationsCookies(resp):
    resp.set_cookie('customizations', '1')
    resp.set_cookie('items-per-page', '15')
    resp.set_cookie('sort-order', 'Alfabetic')
    resp.set_cookie('background-color', 'bg-light')

def loadCookiesValues(resp):
    
    resp.set_cookie('customizations', '1')
    resp.set_cookie('items-per-page', cookies.get("items-per-page"))
    resp.set_cookie('sort-order', session["customizations"]["sort-order"])
    resp.set_cookie('background-color', session["customizations"]["background-color"])


# Cargar cookies
    resp.set_cookie('customizations', '1')
    resp.set_cookie('items-per-page', session["customizations"]["items-per-page"])
    resp.set_cookie('sort-order', session["customizations"]["sort-order"])
    resp.set_cookie('background-color', session["customizations"]["background-color"])
