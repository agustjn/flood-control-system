
def configSessionAttributes(session,user):
    session["user"] = user.email
    session["name"] = user.first_name + ' ' + user.last_name
