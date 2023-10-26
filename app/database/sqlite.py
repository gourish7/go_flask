import sqlite3


class SQLite:
    def __init__(self, database_path):
        self.conn = sqlite3.connect(database_path)
        self.cur = self.conn.cursor()

    def execute(self, query):
        self.cur.execute(query)
        self.conn.commit()
        return self.cur

    def __del__(self):
        """ Destroys instance and connection on completion of called method """
        self.conn.close()