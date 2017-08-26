from Server.FTP import *
from Server.Menus.Lobby import Lobby
from Server.Menus.API import API

class Main(object):
    def __init__(self):
        """
        :param menues: dict of class Menus {"API": class API()}
        """
        self.menus = {"Lobby": lambda net: Lobby(net), "API": lambda net: API(net)}

    def loop(self):
        net = Network()
        while True:
            keys, call  = net.receive()
            if self.testCall(call,keys) == "":
                selectedMenu = keys[0]
                message = {"Message": self.testCall(call,keys), "Succes": True, "CurrentMenu": selectedMenu}
                net.send(message)
                self.menus[selectedMenu](net).loop()
            else:
                message = {"Message": self.testCall(call,keys), "Succes": False, "CurrentMenu": "Main"}
                net.send(message)

    def testCall(self,call, keys):
        """

        :param call: Dict()
        :param keys: List()
        :return: String() message
        """

        for k in keys:
            if k in self.menus and call[k] == True:
                return ""
            elif k not in self.menus:
                message = k + " is not a menu choice"
                return message
            elif call[k] != True:
                message = k + " = False. Must set flag to True to enter next menu"
                return message
            else:
                message = "Catch all. Something strange has happend"
                return message
Main().loop()



