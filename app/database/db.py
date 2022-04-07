from app import helper
import app.config.constants as constant
# from app.excel.excel_db import ExcelDatabase
# from app.json_db.json_db import JsonDatabase

APP_DATABASE_TYPE = constant.APP_DATABASE_TYPE

# excel_db = ExcelDatabase()
# json_db = JsonDatabase()

class Database:
    # def __init__(self):
    # Opening JSON file
    # general db
    # self.jsonDb = open("database.json", "r+")
    # self.write_jsonDb = open("database.json", "w")

    # private db to store access tokens
    # self.jsonDb_private = open("private_database.json", "r")
    # self.write_jsonDb_private = open("private_database.json", "w")

    @staticmethod
    def get_trading_accounts():
        trading_accounts_list = []
        # if APP_DATABASE_TYPE == "excel":
            # trading_accounts_list = excel_db.get_trading_accounts()
        # if APP_DATABASE_TYPE == "json":
            # trading_accounts_list = json_db.get_trading_accounts()
        return trading_accounts_list

    @staticmethod
    def update_trading_account_details(broker_user_id, access_token):
        response = False
        if APP_DATABASE_TYPE == "excel":
            response = excel_db.update_trading_account_details(broker_user_id, access_token)
        if APP_DATABASE_TYPE == "json":
            response = json_db.get_trading_accounts()

        return response

