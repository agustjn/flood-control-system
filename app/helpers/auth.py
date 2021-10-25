from flask import abort,session

class Auth():
    def verify_authentification():
        if not session.get("user"):
            return False
        return True

   