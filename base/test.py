from base import db
import pymysql

class updataDatakey():


    def __init__(self):
        self.db = db.MySQLCommand()


    def connetdb(self, db_name,table):

        self.ad=self.db.connectMysql(db_name)
        print(self.ad)
        sc = self.db.queryMysql(table)
        #list =list(sc)
        

        print(sc)
    #def getValue(self):
       # self.ad





b=updataDatakey()
b.connetdb('bsvwallet_zyd','address')