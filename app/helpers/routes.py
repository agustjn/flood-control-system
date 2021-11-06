
from flask import Flask, render_template, g, Blueprint,session
from app.resources.profile import Profile
from app.helpers.auth import Auth
from app.resources import flood_zones

class RoutesConfig():
    def __init__(self,app):
        # Profile rute
        app.add_url_rule("/profile/<username>","index_profile",Profile.index_profile)

        # Zonas inundables
        app.add_url_rule("/flood_zones", "flood_zones_index", flood_zones.flood_zones_index)
        app.add_url_rule("/flood_zones/import_csv", "update_csv", flood_zones.update_csv, methods=["POST"])
        app.add_url_rule("/flood_zones/profile/<int:id>", "flood_zone_profile", flood_zones.profile, methods=["GET"])


        



    
