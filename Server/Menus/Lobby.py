from Server.User import User
from Server.Game import GameLoop
class Lobby(object):
    def __init__(self,net):
        self.net = net
        self.users = []

    def loop(self):

        while len(self.users) != 2:
            keys,call = self.net.receive()
            if self.testCall(call,keys) == "":
                user = self.getUserInfo(call)
                self.users.append(User(self.net.addr, self.net.conn, self.net.s, user["UserName"], user["BotName"]))
                if len(self.users) != 2:
                    message = {"Message": "Waiting for one more bot to start", "Succes": True,
                                "CurrentMenu": "Lobby"}
                    self.users[0].send(message)

                else:
                    message = {"Message":"Starting Game", "Succes": True, "CurrentMenu": "Game"}
                    for user in self.users:
                        user.send(message)

        GameLoop.main(self.users[0],self.users[1])
        print("GameOver")

    def getUserInfo(self,call):
        userInfo = {"UserName":call["UserName"], "BotName":call["BotName"],"Ready":call["Ready"]}
        return userInfo

    def testCall(self, call, keys):
        """

        :param call: Dict()
        :param keys: List()
        :return: String() Message
        """

        ready = False
        userName = False
        botName = False

        for k in keys:
            if k == "UserName":
                userName = call[k]
            elif k == "BotName":
                botName = call[k]
            elif k == "Ready":
                ready = call[k]

        if ready and userName and botName:
            message = ""
            return message
        else:
            message = "missing Ready or UserName or BotName"
            return message