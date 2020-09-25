from base import db
import random
import time




class insert_into():
    def __init__(self):
        self.db = db.MySQLCommand()

    def inser(self, db_name, table):

        self.db.connectMysql(db_name)

        for i in range(15, 18):

            addr_id = i
            #addr_id = str(addr_id)

            token_id = 1
            unconfirm_amount = 0
            confirm_amount = 3 + random.random()*2
            safe_amount = 3 + random.random()*2
            transferrable = 0
            updated = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            self.db.insertMysql(table, addr_id, token_id, unconfirm_amount, confirm_amount, safe_amount, transferrable, updated)


a=insert_into()
a.inser('dotwallet_zyd', 'address_amount')