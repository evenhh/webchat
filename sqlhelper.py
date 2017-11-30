#!/usr/bin/env python
# coding:utf-8
import  MySQLdb

class MySql(object):

    def __init__(self,dbstr):
        self.db = MySQLdb.connect(**dbstr)
        self.cursor = self.db.cursor()
    def select(self,sql):
        #fd = ','.join(fields)
        #sql = "select %s from %s"%(fd,table)
       # print sql
        code=self.cursor.execute(sql)
        data = self.cursor.fetchall()
        print code
        return data
    def insert(self,table,data):
        fd=""
        values = ""
        strtype = type('str')
        for k,v in data.iteritems():
            fd = fd+k+','
            if type(v) == strtype:
                values = values+'"'+v+'",'
            else:
                values = values+str(v)+','
        fd = fd.strip(',')
        values = values.strip(',')
        sql = "insert into %s (%s)values(%s)"%(table,fd,values)

        print  sql
        try:
            code = self.cursor.execute(sql)
            self.db.commit()
            return code
        except Exception,e:
            print e
            print "insert failed"
    def __del__(self):
        self.cursor.close()
        self.db.close()

if __name__ == "__main__":
    dbstr = {
        'user': 'root',
        'passwd': '',
        'host': '127.0.0.1',
        'port': 3306,
        'db': 'blog',

    }
    db = MySql(dbstr)

    sql = 'select * from person where name="hhh" '
    data = db.select(sql)
    print data
    res = db.insert('person',{'name':'刘哲','id':5})
    print res