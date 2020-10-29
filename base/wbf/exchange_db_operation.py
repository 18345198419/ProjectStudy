from base.wbf import db
from base.wbf import readConfig
import random
import time
db_name = 'exchange'
table = 'crypto_address_nuc'


class insert_into:
    def __init__(self, test, dbname):
        self.dc = db.MySQLCommand(test)
        self.dc.connectMysql(dbname)
        self.addrlist = readConfig.getaddr()

    def insert(self, table_name):

        # 遍历地址
        for addr in self.addrlist:
            self.dc.insert_addr_exchange(table_name, addr)
        self.dc.closeMysql()


        # for i in range(15, 18):
        #
        #     addr_id = i
        #     token_id = 1
        #     unconfirm_amount = 0
        #     confirm_amount = 3 + random.random()*2
        #     safe_amount = 3 + random.random()*2
        #     transferrable = 0
        #     updated = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        #
        #     self.db.insertMysql(table, addr_id, token_id, unconfirm_amount, confirm_amount, safe_amount, transferrable, updated)



a = insert_into(test='exchange', dbname=db_name)
a.insert(table)
