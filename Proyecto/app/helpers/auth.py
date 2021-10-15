def authenticated(session):
    return session.get("user")

def is_administrator(session):
    return session.get("user") == "admin"
