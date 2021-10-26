from app.models.issue import Issue

class IssueDAO():
    @staticmethod
    def recover_issues():
        return Issue.query.all()
