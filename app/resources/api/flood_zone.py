from flask import jsonify, Blueprint, request
from app.dao.flood_zone import FloodZoneDao
from app.scheme.flood_zone import flood_zones_scheme,flood_zone_scheme, flood_zone_pagination_scheme
from app.dao.configuration import ConfigurationDAO

flood_zones_api = Blueprint("zonas_inundables", __name__, url_prefix="/zonas_inundables")


@flood_zones_api.get("/")
def index():
    dao = ConfigurationDAO()
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", dao.items_per_page))
    flood_zones_page = FloodZoneDao.recover_flood_zones_paginated(page, per_page)

    flood_zones = flood_zone_pagination_scheme.dump(flood_zones_page)

    return jsonify(flood_zones)
    


# @flood_zones_api.get("/show")
# def show():
#     report_id = request.get_json()
#     #schema = Report_show_id()
#     #result = scheme.load(report_id)
#     dic = {"name": "nombre", "id": report_id}
#     return jsonify(dic),200
