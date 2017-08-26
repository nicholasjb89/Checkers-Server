import random
from .Player import Player
from .Board import Board
from .PlayerMove import Move

def randomColor():
    colors = ["Red","Black"]
    c1 = random.choice(colors)
    colors.remove(c1)
    c2 = colors[0]
    return c1,c2

def main(user1,user2):
    gameBoard = Board()
    c1,c2 = randomColor()
    if c1 == "Red":
        player1 = Player(c1, user1,gameBoard.getCheckerByColor(c1))
        player2 = Player(c2, user2, gameBoard.getCheckerByColor(c2))
    else:
        player1 = Player(c2,user1,gameBoard.getCheckerByColor(c2))
        player2 = Player(c1, user2, gameBoard.getCheckerByColor(c1))

    gameBoard.setBoard()
    while len(gameBoard.getCheckerByColor("Red")) != 0 or len(gameBoard.getCheckerByColor("Black")) != 0:
        message = "Your move " + player1.color
        while True:
            player1.update(gameBoard.getCheckerByColor(player1.color))
            playersMove = player1.turn(gameBoard.getSerializableBoard(),message)
            playersMove = playersMove[1]["From"],playersMove[1]["To"]
            starting = gameBoard.board[playersMove[0][0]][playersMove[0][1]]
            ending = gameBoard.board[playersMove[1][0]][playersMove[1][1]]
            legal, message  = Move(starting,ending,player1).legal()
            if legal:
                gameBoard.moveChecker(starting,ending)
                mustMove = gameBoard.board[playersMove[0][0]][playersMove[0][1]]
                if mustMove.checker != None:
                    while True:
                        if mustMove.checker.canJump:
                            playersMove = player1.turn(gameBoard.getSerializableBoard(),"Must jump last checker again at position" + str(ending.checker.position))
                            starting = gameBoard.board[playersMove[0][0]][playersMove[0][1]]
                            ending = gameBoard.board[playersMove[1][0]][playersMove[1][1]]
                            if starting == mustMove:
                                legal,message = Move(starting,ending,player1)
                                if legal:
                                    gameBoard.moveChecker(starting,ending)
                                    mustMove = gameBoard.board[playersMove[0][0]][playersMove[0][1]]
                        else:
                            break
                else:
                    break
        player1.send(gameBoard.getSerializableBoard(),"Move accepted")
        message = "Your move " + player2.color
        player2 = player2
        while True:
            player2.update(gameBoard.getCheckerByColor(player2.color))
            playersMove = player2.turn(gameBoard.getSerializableBoard(),message)
            playersMove = playersMove[1]["From"],playersMove[1]["To"]
            starting = gameBoard.board[playersMove[0][0]][playersMove[0][1]]
            ending = gameBoard.board[playersMove[1][0]][playersMove[1][1]]
            legal, message  = Move(starting,ending,player2).legal()
            if legal:
                gameBoard.moveChecker(starting,ending)
                mustMove = gameBoard.board[playersMove[0][0]][playersMove[0][1]]
                if mustMove.checker != None:
                    while True:
                        if mustMove.checker.canJump:
                            playersMove = player2.turn(gameBoard.getSerializableBoard(),"Must jump last checker again at position" + str(ending.checker.position))
                            starting = gameBoard.board[playersMove[0][0]][playersMove[0][1]]
                            ending = gameBoard.board[playersMove[1][0]][playersMove[1][1]]
                            if starting == mustMove:
                                legal,message = Move(starting,ending,player2)
                                if legal:
                                    gameBoard.moveChecker(starting,ending)
                                    mustMove = gameBoard.board[playersMove[0][0]][playersMove[0][1]]
                        else:
                            break
                else:
                    break
        player2.send(gameBoard.getSerializableBoard(), "Move accepted")