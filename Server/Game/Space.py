
class Space(object):
    def __init__(self,postion):
        self.occupied = False
        self.checker = None
        self.position = postion

    def __repr__(self):
        return str(self.position)

    def setTouching(self,touching):
        self.touching = touching

    def placeChecker(self,checker):
        self.checker = checker
        self.occupied = True

    def removeChecker(self):
        self.occupied = False
        self.checker = None

    def update(self):
        if self.checker != None:
            self.checker.update(self.touching,self.position)