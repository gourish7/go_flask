from flask import render_template

from app.controllers.base_controller import BaseController


class DashboardController(BaseController):
    def __init__(self):
        if self.is_logged_in():
            True

    @staticmethod
    def index():
        return render_template('index.html')
