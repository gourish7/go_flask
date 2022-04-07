import requests

from app.config.config import BASE_URL


class BaseController(object):
    # Constructor
    def __init__(self):
        self.session = requests.Session()

    def is_logged_in(self):
        try:
            response = self.session.get(BASE_URL + '/ isUserLoggedIn')
        except BaseException as e:
            response = e
        finally:
            response = False
        return response
