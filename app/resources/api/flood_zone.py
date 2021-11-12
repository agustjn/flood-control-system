from flask import jsonify, Blueprint, request, session
from app.dao.flood_zone import FloodZoneDao
from app.scheme.flood_zone import flood_zones_scheme,flood_zone_scheme, flood_zone_pagination_scheme
from app.dao.configuration import ConfigurationDAO
from app.helpers.permission import PermissionDAO


flood_zones_api = Blueprint("zonas_inundables", __name__, url_prefix="/zonas_inundables")


@flood_zones_api.get("/")
def index():
    PermissionDAO.assert_permission(session["id"],"zonas_inundables_index")
    dao = ConfigurationDAO()
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", dao.items_per_page))
    flood_zones_page = FloodZoneDao.recover_flood_zones_paginated(page, per_page)

    flood_zones = flood_zone_pagination_scheme.dump(flood_zones_page)

    return jsonify(flood_zones)
    
@flood_zones_api.get("/show/<int:id>")
def show(id):
    PermissionDAO.assert_permission(session["id"],"zonas_inundables_index")

    flood_zone_instance = FloodZoneDao.recover_flood_zone(id)
    flood_zone = flood_zone_scheme.dump(flood_zone_instance)

    return jsonify(attributes=flood_zone)


