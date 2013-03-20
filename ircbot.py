#!/usr/bin/python2

' Released under GNU GPL v3 http://www.gnu.org/licenses/gpl.html '

import socket

class IRCBot:
    ''' Base class to extend. '''
    def __init__(self, SERVER, PORT, NICKNAME, CHANNEL, PASSWORD):
        self.readbuffer = ''
        self.SERVER, self.PORT, self.NICKNAME = SERVER, PORT, NICKNAME
        self.CHANNEL, self.PASSWORD = CHANNEL, PASSWORD
        self.connect()

    def connect(self):
        # open a socket to handle the connection
        self.IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # actually connect
        self.IRC.connect((self.SERVER, self.PORT))
        self.IRC.send("PASS " + self.PASSWORD + '\r\n')
        self.IRC.send("NICK " + self.NICKNAME + '\r\n')
        self.IRC.send("USER " + self.NICKNAME + " " + self.NICKNAME + " " +
                      self.NICKNAME + " :Python\r\n")
        self.IRC.send("JOIN " + self.CHANNEL + '\r\n')

    def run(self):
        while True:
            self.readbuffer = self.readbuffer + self.IRC.recv(1024)
            temp = self.readbuffer.split("\n")
            self.readbuffer = temp.pop()

            for line in temp:
                self.parse(line)

    def parse(self, line):
        if line[0:4] == "PING":
            self.IRC.send("PONG %s\r\n" % line[1])
