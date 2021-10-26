from app.models.configuration import Configuration
from app.db import db

class ConfigurationDAO():

    @staticmethod
    def search_by_id(user_id):
        return Configuration.query.filter_by(id=1).first()
