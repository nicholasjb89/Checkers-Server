import socket
import json
import time

HOST = ''
PORT = 5005

class Network(object):
    def __init__(self):
        self.socketConnect()

    def socketConnect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((HOST, PORT))
        print(self.s)

    def send(self, d):
        self.conn.sendall(str.encode(json.dumps(d)))

    def receive(self):
        self.s.listen(2)
        self.conn, self.addr = self.s.accept()
        data = json.loads(self.conn.recv(1024).decode("utf-8"))
        keys = []
        for k in data.keys():
            keys.append(k)
        return (keys,data)

