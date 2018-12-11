# coding: utf-8
# python 3.6.1 x86_64

import os
import socket
import math

##############################################################################

class MySocketIRC:

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        try:
            self.sock.connect((host, port))
        except InterruptedError as err:
            print(err)
        except Exception as err:
            print(err)

    def request(self, msg):
        len_request = 0
        if len(msg) > len_request:
            print(f'send: {msg}')
            msg 
            try:
                bmsg = bytes(msg+'\r\n', 'utf-8')
                self.sock.send(bmsg)
            except InterruptedError as err:
                print(err)
            except Exception as err:
                print(err)
                
    def auth(self, name):
        name += ' '
        self.request(f'NICK {name}')
        self.request(f'USER {name *4}')

    def join_chan(self, chan):
        self.request(f'JOIN {chan}')

    def pong (self):
        self.request('PONG')

###############################################################################

sock = MySocketIRC()
sock.connect('irc.root-me.org', 6667)
sock.auth('zancrows')

while True:

    reception = sock.sock.recv(4096).decode().split("\r\n")
    
    for line in reception:
        if len(line.split(' ')) > 1 :
            if line.split(' ')[1] == '396':
                print(line)
                print('connection OK')
                sock.join_chan('#root-me_challenge')
            elif line.split(' ')[1] == '366':
                sock.request('PRIVMSG candy !ep1')
            elif line.split('!')[0] == ':Candy':
                print(line)
                readbuffer = line.split(':')[-1]
                """
                    Traitement
                """
                result = ""
                sock.request(f'PRIVMSG Candy !ep1 -rep {result} ')
            elif line.split(' ')[0] == 'PING':
                print('recv: ' + line)
                sock.pong()
            else:
                print(line)

