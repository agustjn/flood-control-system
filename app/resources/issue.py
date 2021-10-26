from flask import redirect, render_template, request, url_for
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
    
    return redirect(url_for("issue_index"))
