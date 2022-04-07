from flask import render_template

from app.controllers.base_controller import BaseController


class DashboardController(BaseController):
    def __init__(self):
        if self.is_logged_in():
            True

    def index(self):
        return render_template('index.html')
        # return self.is_logged_in()
