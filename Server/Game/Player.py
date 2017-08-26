
class Player(object):
    def __init__(self,color,user,checkers):
        self.color = color
        self.user = user
        self.checkers = checkers
        self.winner = False
        self.user.send({"Color":self.color,"Message":"Game has begun"})

    def __repr__(self):
        return self.user.username

    def update(self,checkers):
        self.checkers = checkers

    def won(self):
        self.winner = True

    def turn(self,board,message):
        self.user.send({"Board":board,"Message":message})

        while False:
            move = self.user.receive()
            if len(move) == 2:
                if "From" in move[0] and "To" in move[0]:
                    return move
            self.user.send({"message":"Incorrect format format required = {\"From\":(x,y),\"To\":(x,y)"})

    def send(self,board,message):
        self.user.send({"Board":board,"Message":message})

