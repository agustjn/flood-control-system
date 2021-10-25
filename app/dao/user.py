
from flask import request
from app.models.user import User

class UserDAO():
    def users_paginated(items_per_page):
        page = request.args.get('page', 1, type=int)
        users = User.query.paginate(page=page, per_page=items_per_page)
        return users

    @staticmethod
    def exist_email(email):
        return bool((User.query.filter_by(email=email).first()))

    @staticmethod
    def exist_username(username):
        return bool((User.query.filter_by(username=username).first()))
