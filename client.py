#!/usr/bin/env python
# coding:utf-8

import socket

def chat():
    client = socket.socket()
    client.connect(('127.0.0.1',7000))
    while True:
        data=client.recv(1024)
        print data
        word = raw_input("send to server:")
        client.send(word)
        if word == 'exit':
            break
        #client.close()


def getRecord():
    pass



if __name__ == "__main__":
    # while True:
    #     print """
    #         choice : 1 :chat
    #                  2 :get chat records
    #                  q :exit
    #     """
    #     cmd = raw_input("input your choice: ")
    #     if cmd == '1':
    #         chat()
    #     elif cmd == '2':
    #         getRecords()
    #     elif cmd.lower() == 'q' or cmd.lower() == 'quit':
    #         exit(0)
    chat()