from flask import Flask, render_template

from app.config.constants import VIEWS_PATH, STATIC_FILES_PATH
from app.routes import route

app = Flask(__name__, template_folder=VIEWS_PATH, static_folder="static")


@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
    return render_template("404.html")

def create_app():
    app.register_blueprint(route)
    return app
