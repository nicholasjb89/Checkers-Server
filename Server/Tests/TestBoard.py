from Server.Game.Board import Board

import unittest

class TestGame(unittest.TestCase):
    def test_canJump(self):
        b = Board()
        b.placeChecker((1, 1), "Red")
        b.placeChecker((2, 1), "Black")
        b.update()
        self.assertEqual(b.board[1][1].checker.canJump,True)
        self.assertEqual(b.board[2][1].checker.canJump,True)

    def test_placeCheckers(self):
        b = Board()
        b.setBoard()

        row = 0
        for r in b.board:
            for space in r:
                if row < 3:
                   self.assertEqual(space.checker.color,"Red")

                if row >=3 and row <= 4:
                    self.assertEqual(space.checker,None)
                if row > 4:
                    self.assertEqual(space.checker.color,"Black")
            row += 1

    def test_moveCheckerWithJump(self):
        b = Board()
        b.placeChecker((1, 1), "Red")
        b.placeChecker((2, 1), "Black")
        b.update()

        b.moveChecker(b.board[1][1],b.board[3][2])

        self.assertEqual(b.board[2][1].checker, None)

    def test_moveCheckerNoJump(self):
        b = Board()
        b.placeChecker((1, 1), "Red")
        b.placeChecker((2, 1), "Black")
        b.update()

        b.moveChecker(b.board[1][1],b.board[3][1])

        self.assertEqual(b.board[3][1].checker.color,"Red")




if __name__ == "__main__":
    unittest.main()