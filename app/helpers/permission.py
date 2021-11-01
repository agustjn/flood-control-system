from flask import session,abort;
from app.helpers.auth import Auth
from app.dao.user import UserDAO

class PermissionDAO ():

    @staticmethod
    def is_admin():
        return session["user"] ==  "Jorgelin"

    @classmethod
    def assert_permission(cls,user_id,permission_name):
        user = UserDAO.search_by_id(user_id)
        Auth.verify_authentification()
        if cls.is_admin():
            return True
        if not cls.has_permission(user,permission_name):
            abort(403)

    @staticmethod
    def has_permission(user,permission):
        for role in user.role:
            for permiso in role.permission:
                if permiso.name   == permission:
                    return True
        return False

    @staticmethod
    def has_rol(user_id,role):
        user = UserDAO.search_by_id(user_id)
        for un_rol in user.role:
            if un_rol.name == role:
                return True;
        return False;