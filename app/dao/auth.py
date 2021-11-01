from app.models.user import User

class AuthDAO():
    @staticmethod
    def authenticate(email,password):
         try:
              user = User.query.filter_by( email == email and password == password).first()
              return user
         except:
             False
