import os

from app.config.config import APP_TYPE

APP_PATH = os.path.abspath('')  # Webportal app path
if APP_TYPE == 'gui':
    APP_PATH = os.path.abspath('app/') #GUI app path

VIEWS_PATH = os.path.join(APP_PATH, 'views/')
STATIC_FILES_PATH = os.path.join(APP_PATH, 'static/')
