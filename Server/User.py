from Server.FTP import Network
class User(Network):
    def __init__(self,addr,conn,s,username,botname):
        self.addr = addr
        self.conn = conn
        self.username = username
        self.botname = botname
        self.s = s
