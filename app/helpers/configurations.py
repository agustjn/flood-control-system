from app.models.views_sort import View_issues, View_users, View_meeting_points
from app.models.configuration import Configuration
from flask import session

def putConfigurationsValuesInSession():
    config_row = Configuration.query.filter_by(id=1).first()
    view_users_row = View_users.query.filter_by(id=1).first()
    view_issues_row = View_issues.query.filter_by(id=1).first()
    view_meeting_points_row = View_meeting_points.query.filter_by(id=1).first()
    session["configurations"] = {
        "items_per_page" : config_row.items_per_page,
        "background" : config_row.background,
        "view_users" : { "sort_order" : view_users_row.sort_order,
                          "sorted_by_column" : view_users_row.sorted_by_column },
        "view_issues" : { "sort_type" : view_issues_row.sort_type,
                          "sorted_by_column" : view_issues_row.sorted_by_column },
        "view_meeting_points" : { "sort_type" : view_meeting_points_row.sort_type,
                          "sorted_by_column" : view_meeting_points_row.sorted_by_column }



    }
    return session["configurations"]
