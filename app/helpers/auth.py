from flask import abort,session

class Auth():
    def verify_authentification():
        if not session.get("user"):
            abort(401)
        return True

   