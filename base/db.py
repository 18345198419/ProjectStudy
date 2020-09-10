# -*- coding: utf-8 -*-


import pymysql
from base import readConfig


# 用来操作数据库的类

class MySQLCommand(object):

    # 类的初始化
    def __init__(self):
        a = readConfig.getConfig('test')
        self.host = a[0]
        self.port = a[1]
        self.user = a[2]
        self.password = a[3]

    # 链接数据库

    def connectMysql(self, db_name):
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user,passwd=self.password, db=db_name, charset='utf8')
            self.cursor = self.conn.cursor()
            print('连接成功')
        except:
            print('connect mysql error.')
        return self.cursor
    # 查询数据
    def queryMysql(self, table):
        sql = "SELECT * FROM " + table;
        try:
            self.cursor.execute(sql)
            row = self.cursor.fetchall()
            for i in row:
                print(i)
        except:
            print(sql + ' execute failed.')

        return row


    # 插入数据

    def insertMysql(self, table, *args):
        sql = "INSERT INTO " + table + " VALUES(" + args + "," + "'" + args + "'," + "'" + args + "')"
        try:
            self.cursor.execute(sql)
        except:
            print("insert failed.")

    # 更新数据

    def updateMysqlSN(self, table, *args):
        sql = "UPDATE " + table + " SET sex='" + args + "'" + " WHERE name='" + args + "'"
        print("update sn:" + sql)

        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()

    def closeMysql(self):
        self.cursor.close()
        self.conn.close()


# 创建数据库操作类的实例
#mySQLCommand = MySQLCommand()
#mySQLCommand.connectMysql(db_name='bsvwallet_zyd')
# mySQLCommand.queryMysql('int_config')