from flask import redirect, render_template, request, url_for
from app.models.issue import Issue

# Public resources
def index():
    issue = Issue.query.all()
    return render_template("issue/index.html", issues=issue)


def new():
    return render_template("issue/new.html")


def create():
    #conn = connection()
    #Issue.create(conn, request.form)

    return redirect(url_for("issue_index"))
