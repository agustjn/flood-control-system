
from flask import Flask, render_template, g, Blueprint,session
from app.resources.profile import Profile


class RoutesConfig():
    def __init__(self,app):
        # Profile rute
        app.add_url_rule("/profile/<username>","index_profile",Profile.index_profile)
        



    
