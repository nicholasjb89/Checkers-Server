
def EVEN(i):
    if i % 2 == 0:
        return True
    else:
        return False

class Checker(object):
    def __init__(self,color,position):
        self.color = color
        self.position = position

        self.kinged = False
        self.canMoveTo = []
        self.canJump = False
        self.canJumpSpaces = []
        self.jumpedCheckers = []

        if self.color == "Red":
            self.direction = 1
        else:
            self.direction = -1

    def kingMe(self):
        self.kinged = True

    def canjump(self,jumpSpace):
        """
        must make sure jumpSpace has a checker on it before running canjump

        :param jumpSpace: Class Space (The space we are looking at jumping
        :return:
        """
        for space in jumpSpace.touching:
            if self.direction == 1:
                if space.position[0] > self.position[0]:
                    if space.occupied == False and jumpSpace.checker.color != self.color:
                        if EVEN(jumpSpace.position[0]) and jumpSpace.position[1] == self.position[1]:
                            if space.position[1] == self.position[1] + 1:
                                self.canJump = True
                                self.canJumpSpaces.append(space)
                                self.jumpedCheckers.append(jumpSpace)
                        elif EVEN(jumpSpace.position[0]) and jumpSpace.position[1] == self.position[1] - 1:
                            if space.position[1] == jumpSpace.position[1]:
                                self.canJump = True
                                self.canJumpSpaces.append(space)
                                self.jumpedCheckers.append(jumpSpace)
                        elif not EVEN(jumpSpace.position[0]) and jumpSpace.position[1] == self.position[1]:
                            if space.position[1] == jumpSpace.position[1] - 1:
                                self.canJump = True
                                self.canJumpSpaces.append(space)
                                self.jumpedCheckers.append(jumpSpace)
                        elif not EVEN(jumpSpace.position[0]) and jumpSpace.position[1] == self.position[1] + 1:
                            if space.position[1] == jumpSpace.position[1]:
                                self.canJump = True
                                self.canJumpSpaces.append(space)
                                self.jumpedCheckers.append(jumpSpace)
            else:
                if space.position[0] < self.position[0]:
                    if space.occupied == False and jumpSpace.checker.color != self.color:
                        if EVEN(jumpSpace.position[0]) and jumpSpace.position[1] == self.position[1]:
                            if space.position[1] == self.position[1] + 1:
                                self.canJump = True
                                self.canJumpSpaces.append(space)
                                self.jumpedCheckers.append(jumpSpace)
                        if EVEN(jumpSpace.position[0]) and jumpSpace.position[1] == self.position[1] - 1:
                            if space.position[1] == jumpSpace.position[1]:
                                self.canJump = True
                                self.canJumpSpaces.append(space)
                                self.jumpedCheckers.append(jumpSpace)
                        elif not EVEN(jumpSpace.position[0]) and jumpSpace.position[1] == self.position[1]:
                            if space.position[1] == jumpSpace.position[1] - 1:
                                self.canJump = True
                                self.canJumpSpaces.append(space)
                                self.jumpedCheckers.append(jumpSpace)
                        elif not EVEN(jumpSpace.position[0]) and jumpSpace.position[1] == self.position[1] + 1:
                            if space.position[1] == jumpSpace.position[1]:
                                self.canJump = True
                                self.canJumpSpaces.append(space)
                                self.jumpedCheckers.append(jumpSpace)

        if self.canJump:
            return True
        else:
            return False

    def update(self,touching,position):
        """

        :param touching: List() of Spaces
        :param position: Tuple of new position of checker
        :return:
        """

        self.position = position
        self.canMoveTo = []
        self.canJump = False
        self.canJumpSpaces = []

        for space in touching:
            if self.direction == 1:
                if space.position[0] >  self.position[0]:
                    if space.occupied == False:
                        self.canMoveTo.append(space)

                    else:
                        self.canjump(space)
            else:
                if space.position[0] < self.position[0]:
                    if space.occupied == False:
                        self.canMoveTo.append(space)
                    else:
                        self.canjump(space)


    def __repr__(self):
        return self.color