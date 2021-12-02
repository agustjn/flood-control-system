from flask import session,abort;
from app.helpers.auth import Auth
from app.dao.user import UserDAO

class PermissionDAO ():
    @classmethod
    def assert_permission(cls,permission_name):
        Auth.verify_authentification()
        user_id = session["id"]
        if cls.has_permission(user_id,permission_name):
            return True
        abort(403)

    @staticmethod
    def has_permission(user_id,permission):
        bool = False
        user = UserDAO.search_by_id(user_id)
        print (user.role.all())
        for role in user.role:
            print ("--------------------entra algunas veces--------------------")
            for permiso in role.permission:
                print (f"-----------------> {permiso.name}")
                if permiso.name == permission:
                    bool = True
                    break
        print (bool)
        return bool

    @staticmethod
    def has_rol(user_id,role):
        user = UserDAO.search_by_id(user_id)
        for un_rol in user.role:
            if un_rol.name == role:
                return True;
        return False;
