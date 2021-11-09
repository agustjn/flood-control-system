from flask import request
from app.models.flood_zone import FloodZone
from app.db import db

class FloodZoneDao():
    
    @staticmethod
    def filter_by_key(status,items_per_page, key=""):
        key_filtered = "%" + key + "%"
        page = request.args.get('page', 1, type=int)
        if status == "Todos":
            zones =  FloodZone.query.filter(FloodZone.name.like(key_filtered)).paginate(page=page, per_page=items_per_page)
        else:
            if status == "Publicado":
                zones =  FloodZone.query.filter(FloodZone.name.like(key_filtered)).filter_by(active = True).paginate(page=page, per_page=items_per_page)
            else:
                zones =  FloodZone.query.filter(FloodZone.name.like(key_filtered)).filter_by(active = False).paginate(page=page, per_page=items_per_page)
        return zones