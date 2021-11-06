import re
from app.helpers.auth import Auth
from flask import render_template, request
import csv


def flood_zones_index():
    Auth.is_authenticated()
    # Permisos de ver index: Operador/Administrador
    
    return render_template("flood_zones/index.html")


def update_csv():
    file = request.files['file']
    # with open(file, 'r') as csv:
    #     for row in csv:
    #         print(row)
    print('--------------------------')
    print(file)

def profile(id):
    return render_template("flood_zones/profile.html")
    
