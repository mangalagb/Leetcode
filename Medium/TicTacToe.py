# Design a Tic-tac-toe game that is played between two players on a n x n grid.
#
# You may assume the following rules:
#
#     A move is guaranteed to be valid and is placed on an empty block.
#     Once a winning condition is reached, no more moves is allowed.
#     A player who succeeds in placing n of their marks in a horizontal,
#  vertical, or diagonal row wins the game.

# The key observation is that in order to win Tic-Tac-Toe you must have the
# entire row or column. Thus, we don't need to keep track of an entire n^2
#  board. We only need to keep a count for each row and column. If at any
# time a row or column matches the size of the board then that player has won.
#
# To keep track of which player, I add 1 for Player1 and -1 for Player2.
# There are two additional variables to keep track of the count of the
# diagonals. Each time a player places a piece we just need to check the
# count of that row, column, diagonal and anti-diagonal.

class TicTacToe:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0
        self.size = n


    def move(self, row, col, player):
        value = 1
        if player == 2:
            value = -1

        winner = 0

        self.rows[row] += value
        self.cols[col] += value

        if row == col:
            self.diagonal += value

        if col == self.size - row - 1:
            self.anti_diagonal += value

        row_result = [x for x in self.rows if abs(x) == self.size]
        col_result = [x for x in self.cols if abs(x) == self.size]

        if row_result or col_result or abs(self.diagonal) == self.size or abs(self.anti_diagonal) == self.size:
            print("PLAYER " + str(player) + " wins")
            winner = player
            return winner

        return winner

toe = TicTacToe(3)
toe.move(0, 0, 1)
toe.move(0, 2, 2)
toe.move(2, 2, 1)
toe.move(1, 1, 2)
toe.move(2, 0, 1)
toe.move(1, 0, 2)
toe.move(2, 1, 1)
