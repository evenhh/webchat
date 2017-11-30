#!/usr/bin/env python
# coding:utf-8
from server import  MyServer
from sqlhelper import  *
import SocketServer

myserver = SocketServer.ThreadingTCPServer(('127.0.0.1',9999),server.MyServer)
myserver.serve_forever()