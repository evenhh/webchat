#!/usr/bin/env python
# coding:utf-8
import  SocketServer
from sqlhelper import  MySql

dbstr = {
    'user': 'root',
    'passwd': '',
    'host': '127.0.0.1',
    'port': 3306,
    'db': 'blog',
  #  'charset':'utf8'
}
class MyServer(SocketServer.BaseRequestHandler):
    db = MySql(dbstr)
    def setup(self):pass

    def handle(self):
        con = self.request
        con.send('welcome,please input your username:')
        username = con.recv(1012)
        con.send('please input your passwd:')
        passwd = con.recv(1024)
        if self.login(username,passwd):
            con.send("let's chat now")
            word = con.recv(1024)
            while True:

                if word == 'exit':
                    con.close()
                
                reply = self.reply(word)
                print reply
                con.send(reply)
                word = con.recv(1024)
        else:
            con.send('check your passwd and username')
            con.close()

    def login(self,username,passwd):
        sql = 'select id,name from person where name="%s"'%(username,)
        userinfo = MyServer.db.select(sql)
        print userinfo
        if userinfo==0 or str(userinfo[0][0]) != passwd:
            return False
        else :
            return True
    def reply(self,keyword):
        sql = 'select keyword,reply from chat where keyword="%s"'%(keyword,)
        data = MyServer.db.select(sql)

        if data:
            return data[0][1].encode('utf-8')
        return 'i can not unstand your words'



    def finish(self):pass

if __name__ == "__main__":
    myserver = SocketServer.ThreadingTCPServer(('127.0.0.1',7000),MyServer)
    myserver.serve_forever()