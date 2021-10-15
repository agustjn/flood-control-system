from flask import redirect, render_template, request, url_for


def index():
    return render_template("configuration/index.html")

    
