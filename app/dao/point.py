from flask import request
from app.models.point import Point



class PointDao():
    def points_paginated(items_per_page):
        page = request.args.get('page', 1, type=int)
        points = Point.query.paginate(page=page, per_page=items_per_page)
        return points
