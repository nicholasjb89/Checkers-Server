from Server.Game.Checker import Checker
from Server.Game.Space import Space

def EVEN(i):
    if i % 2 == 0:
        return True
    else:
        return False

def getTouching(position):
    touching = []
    row = position[0]
    col = position[1]
    if EVEN(row):
        #top
        if row - 1 >= 0:
            touching.append((row-1,col))
        #top Right
        if row - 1 >= 0 and col + 1 < 4:
            touching.append((row-1,col+1))
        #bottom
        if row + 1 < 8:
            touching.append((row+1,col))
        #bottom Right
        if row + 1 < 8 and col + 1 < 4:
            touching.append((row+1,col+1))
    else:
        #top
        if row - 1 >= 0:
            touching.append((row-1,col))
        #top Left
        if row - 1 >= 0 and col - 1 >=0:
            touching.append((row-1,col-1))
        #bottom
        if row + 1 < 8:
            touching.append((row+1,col))
        #bottom Left
        if row + 1 < 8 and col - 1 >=0:
            touching.append((row+1,col-1))

    return touching

class Board(object):
    def __init__(self):

        self.board = []
        for r in range(8):
            row = []
            for c in range(4):
                row.append(Space((r,c)))
            self.board.append(row)

        for row in self.board:
            for space in row:
                pos = space.position
                touching = getTouching(pos)
                touchingSpaces = []
                for tPos in touching:
                    touchingSpaces.append(self.board[tPos[0]][tPos[1]])
                space.setTouching(touchingSpaces)

    def setBoard(self):
        row = 0
        for r in self.board:
            col = 0
            for c in r:
                if row < 3:
                    self.board[row][col].placeChecker(Checker("Red", (row, col)))
                if row >=5:
                    self.board[row][col].placeChecker(Checker("Black", (row, col)))
                col+=1
            row+=1

        self.update()

    def update(self):
        for row in self.board:
            for space in row:
               space.update()

    def placeChecker(self, position, color):
        """
        :param position: tuple (row,col)
        :param color Text() Red or Black
        :return:
        """
        self.board[position[0]][position[1]].placeChecker(Checker(color, position))
        self.update()

    def moveChecker(self,space1,space2):
        if space1.checker.canJump:
            i = 0
            while i < len(space1.checker.canJumpSpaces):
                if space1.checker.canJumpSpaces[i] == space2:
                    space1.checker.jumpedCheckers[i].removeChecker()
                i+=1
        space2.placeChecker(space1.checker)
        space1.removeChecker()
        self.update()

    def getCheckerByColor(self,color):
        checkers = []
        for row in self.board:
            for space in row:
                if space.checker != None:
                    if space.checker.color == color:
                        checkers.append(space.checker)
        return checkers

    def getSerializableBoard(self):
        sBoard = []
        for row in self.board:
            sRow = []
            for space in row:
                sSpace = {}
                if space.checker != None:
                    checker = space.checker
                    sSpace["Kinged"] = checker.kinged
                    sSpace["CanJump"] = checker.canJump
                    sSpace["Color"] = checker.color
                sRow.append(sSpace)
            sBoard.append(sRow)

        return sBoard