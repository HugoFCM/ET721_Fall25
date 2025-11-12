"""
Hugo Carcamo
10/25/25
Project 2
"""

import unittest
from main import Connect4


class TestPlayGame(unittest.TestCase):
    def setUp(self):
        self.game = Connect4()

    def test_horizontal_win_condition(self):
        for col in range(1, 5):
            self.game.drop_chip(col)
        self.assertTrue(self.game.check_win("X"))

    def test_vertical_win_condition(self):
        for _ in range(4):
            self.game.drop_chip(1)
        self.assertTrue(self.game.check_win("X"))

    def test_diagonal_down_right_win(self):
        self.game.board[5][0] = "X"
        self.game.board[4][1] = "X"
        self.game.board[3][2] = "X"
        self.game.board[2][3] = "X"
        self.assertTrue(self.game.check_win("X"))

    def test_diagonal_up_right_win(self):
        self.game.board[2][0] = "X"
        self.game.board[3][1] = "X"
        self.game.board[4][2] = "X"
        self.game.board[5][3] = "X"
        self.assertTrue(self.game.check_win("X"))

    def test_no_win_condition(self):
        self.game.drop_chip(1)
        self.game.drop_chip(2)
        self.game.drop_chip(3)
        self.assertFalse(self.game.check_win("X"))

    def test_full_column(self):
        for _ in range(self.game.ROWS):
            self.game.drop_chip(1)
        self.assertFalse(self.game.drop_chip(1))

    def test_invalid_column_number(self):
        self.assertFalse(self.game.drop_chip(0))
        self.assertFalse(self.game.drop_chip(8))

    def test_full_board(self):
        for col in range(1, self.game.COLS + 1):
            for _ in range(self.game.ROWS):
                self.game.drop_chip(col)
        self.assertTrue(self.game.is_full())


if __name__ == "__main__":
    unittest.main()


"""
Documentation

test_horizontal_win_condition: Passed
test_vertical_win_condition: Passed (minor issue: game didn’t switch players correctly at first)
test_diagonal_down_right_win: Passed
test_diagonal_up_right_win: Passed (bug found – diagonal check missed one direction, now fixed)
test_no_win_condition: Passed
test_full_column: Passed
test_invalid_column_number: Passed
test_full_board: Passed (issue fixed – board was not detecting full state properly)
"""
