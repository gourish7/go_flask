from flask import render_template

from app.config.config import APP_NAME
from app.controllers.base_controller import BaseController


class WebController(BaseController):
    @staticmethod
    def index():
        return render_template('index.html', app_name=APP_NAME)

    @staticmethod
    def layout_index():
        return render_template('layout-index.html')