from flask import jsonify, Blueprint
from app.models.flood_zone import FloodZone 

flood_zones_api = Blueprint("zonas_inundables", __name__, url_prefix="/zonas_inundables")


@flood_zones_api.get("/")
def index():
    flood_zones_rows  = FloodZone.query.all()
    flood_zones = [flood_zone.as_dict() for flood_zone in flood_zones_rows]
    
    return jsonify(zonas=flood_zones)
