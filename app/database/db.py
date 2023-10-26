from app.config.config import DB_CONNECTION, DB_DATABASE
from app.database.sqlite import SQLite


class Database:
    def __init__(self):
        self.connection = DB_CONNECTION

    def load(self):
        if self.connection == 'sqlite':
            # sqlite = SQLite()
            # self.connection = sqlite
            db = self.connection_detail()
            # print(db['database'])
            return SQLite(db['database'])

    def connection_detail(self):
        response = {}
        if self.connection == 'sqlite':
            response['database'] = 'database.sqlite'
            if DB_DATABASE is not None:
                response['database'] = DB_DATABASE

        if self.connection == 'mysql':
            response['url'] = 'go_flask'
            response['host'] = '127.0.0.1'
            response['port'] = '3306'
            response['database'] = ''
            response['username'] = ''
            response['password'] = ''

        return response
