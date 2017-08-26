
class Move(object):
    def __init__(self,starting,ending,player):
        """

        :param starting: Space Object
        :param ending: Space Object
        :param player: Player Object
        """
        self.starting = starting
        self.ending = ending
        self.player = player

        self.checker = self.starting.checker
    def legal(self):
        if self._spaceOccupied(self.starting) == False:
            return False,"No checker to move on space "+str(self.starting.position)
        if self._spaceOccupied(self.ending) == True:
            return False, "There is a checker already occupying this space " + str(self.ending.position)
        if self._isOwner(self.starting) == False:
            return False, "You are not the owner of the checker you want to move on space " + str(self.starting.position)
        if self._legalEndingLocation() == False:
            return False, "You can not move that checker to location " + str(self.starting.position)
        if self._hasToJump():
            if self._isJump() == False:
                return False, "You have a possible jump on the board. You must jump when you can"

        return True, "Legal move"
    def _spaceOccupied(self,space):
        if space.checker != None:
            return True
        else:
            return False
    def _isOwner(self,space):
        if space.checker.color == self.player.color:
            return True
        else:
            return False
    def _legalEndingLocation(self):
        possibleMoves = self.checker.canMoveTo
        for space in self.checker.canJumpSpaces:
            possibleMoves.append(space)

        for space in possibleMoves:
            if space == self.ending:
                return True
        return False
    def _hasToJump(self):
        for checker in self.player.checkers:
            if checker.canJump:
                return True
        return False
    def _isJump(self):
        """
        Is the move a jump or a normal move
        :return: Bool()
        """

        if self.ending in self.starting.checker.canJumpSpaces:
            return True
        return False






