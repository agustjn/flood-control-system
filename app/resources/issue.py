from flask import redirect, render_template, request, url_for, flash
from app.dao.issue import IssueDAO

# Public resources
def index():
    issue = IssueDAO.recover_issues()
    return render_template("issue/index.html", issues=issue)


def new():
    return render_template("issue/new.html")


def create():
    #conn = connection()
    #Issue.create(conn, request.form)

    #validar ()       -faltaria metodo validar
    if IssueDAO.create_issue(request.form):
            flash("se creo flama")
    else:
        flash("No se cre")
    return redirect(url_for("issue_index"))
