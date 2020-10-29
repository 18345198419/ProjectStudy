from base.wbf import db


class updataDatakey:

    def __init__(self):
        self.db = db.MySQLCommand()

    def selectdb(self, db_name,table):

        self.db.connectMysql(db_name)
        # print(self.ad)
        sc = self.db.queryMysql(table)
        # list =list(sc)
        print(sc)


b = updataDatakey()
b.selectdb("bsvwallet_zyd", "address")
