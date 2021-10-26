from app.models.issue import Issue
from app.db import db


class IssueDAO():
    @staticmethod
    def recover_issues():
        return Issue.query.all()

    @staticmethod
    def create_issue(parameter):
        new_issue = Issue(parameter["email"],parameter["description"],parameter["category_id"],parameter["status_id"])
        db.session.add(new_issue)
        try:
            db.session.commit()
            return True
        except:
            return False
