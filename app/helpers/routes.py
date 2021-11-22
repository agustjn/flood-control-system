
from flask import Flask, render_template, g, Blueprint,session
from app.resources.profile import Profile
from app.helpers.auth import Auth
from app.resources import flood_zone

class RoutesConfig():
    def __init__(self,app):
        # Profile rute
        app.add_url_rule("/profile/<username>","index_profile",Profile.index_profile)

        # Zonas inundables
        app.add_url_rule("/flood_zones", "flood_zone_index", flood_zone.flood_zones_index)
        app.add_url_rule("/flood_zones/import_csv", "update_csv", flood_zone.update_csv, methods=["POST"])
        app.add_url_rule("/flood_zones/profile/<int:id>", "flood_zone_profile", flood_zone.profile, methods=["GET"])
        app.add_url_rule("/flood_zone/delete/<flood_zone_id>", "flood_zone_delete", flood_zone.delete)

        



    
