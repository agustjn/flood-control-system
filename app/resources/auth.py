from flask import redirect, render_template, request, url_for, abort, session, flash,make_response
from app.models.user import User
from app.helpers.sessionConfig import configSessionAttributes
from app.dao.auth import AuthDAO
from os import environ

import requests
from oauthlib.oauth2 import WebApplicationClient

from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
import json
# Diego Configuration
GOOGLE_CLIENT_ID = "262521299225-7vupjcju1t6rhe23vu54dmev3vtl1eud.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()

client = WebApplicationClient(GOOGLE_CLIENT_ID)

def login_google():
        print ("entro al Login -------------------------------------------------")

        # Find out what URL to hit for Google login
        google_provider_cfg = get_google_provider_cfg()
        authorization_endpoint = google_provider_cfg["authorization_endpoint"]


        # Use library to construct the request for Google login and provide
        # scopes that let you retrieve user's profile from Google
        request_uri = client.prepare_request_uri(
            authorization_endpoint,
            redirect_uri="https://admin-grupo3.proyecto2021.linti.unlp.edu.ar/login/callback",
            scope=["openid", "email", "profile"],
        )
        print ("retorna---------------------")
        return redirect(request_uri)

def callback():
    print ("entro al calbaack -------------------------------------------------")
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400

    # Create a user in your db with the information provided
    # by Google
    # user = User(
    #     id_=unique_id, name=users_name, email=users_email, profile_pic=picture
    # )
    #
    # # Doesn't exist? Add it to the database.
    # print (userinfo_response.json())
    # if not User.get(unique_id):
    #     User.create(unique_id, users_name, users_email, picture)

    # Begin user session by logging the user in
    # login_user(user)

    # Send user back to homepage
    return redirect(url_for("home.html",msj= "La session se inicio correctamente"))


def login():
    return render_template("auth/login.html")


def authenticate():
    params = request.form
    user = AuthDAO.authenticate(params["email"],params["password"])


    if not user:
        msj = "Usuario o clave incorrecto."
        return render_template("auth/login.html",msj=msj)
    configSessionAttributes (user)

    msj = "La sesión se inició correctamente."
    return render_template("home.html",msj=msj)


def logout():
    del session["user"]
    session.clear()
    flash("La sesión se cerró correctamente.")
    return redirect(url_for("auth_login"))
