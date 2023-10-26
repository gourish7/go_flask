"""
    This is route for Go flask application, The endpoints are defined here with function
"""

from flask import Blueprint
from app.controllers.dashboard_controller import DashboardController
from app.controllers.web_controller import WebController

routes = Blueprint('routes', __name__)
web = WebController()
dashboard = DashboardController()


@routes.route('/')
def web_index():
    return web.index()


@routes.route('/layout/')
def web_layout_index():
    return web.layout_index()
