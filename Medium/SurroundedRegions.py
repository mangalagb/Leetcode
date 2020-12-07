# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        elif not board[0]:
            return

        #Change all regions in the border with O to !
        self.remove_border_regions(board)

        # 1) Change all the ! to O
        # 2) Change all O to X (They are valid regions)
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] is "!":
                    board[i][j] = "O"
                elif board[i][j] is "O":
                    board[i][j] = "X"

        print(board)

    def remove_border_regions(self, board):
        # Remove all O s on the border rows and columns
        for i in range(0, len(board)):
            j = 0
            if board[i][j] == "O":
                self.do_DFS(board, i, j)

            j = len(board[0]) - 1
            if board[i][j] == "O":
                self.do_DFS(board, i, j)

        for j in range(0, len(board[0])):
            i = 0
            if board[i][j] == "O":
                self.do_DFS(board, i, j)

            i = len(board) - 1
            if board[i][j] == "O":
                self.do_DFS(board, i, j)


    def do_DFS(self, board, row, col):
        # Stack's top is at index 0
        stack = [[row, col]]
        visited = []

        while len(stack) > 0:
            top_element = stack[0]
            top_row = top_element[0]
            top_col = top_element[1]

            # Mark current as visited
            board[top_row][top_col] = "!"

            # Find unvisited neighbours
            neighbour = self.find_unvisited_neighbour(board, top_row, top_col)

            if len(neighbour) > 0:
                stack.insert(0, neighbour)
            else:
                stack.pop(0)


    def find_unvisited_neighbour(self, board, row, col):
        neighbours = [[row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]]
        non_border_rows = len(board) - 2
        non_border_cols = len(board[0]) - 2

        for neighbour in neighbours:
            row_num = neighbour[0]
            col_num = neighbour[1]

            if 1 <= row_num <= non_border_rows and 1 <= col_num <= non_border_cols and board[row_num][col_num] == "O":
                return [row_num, col_num]
        return []


my_sol = Solution()

board = [["X", "X", "X", "X"],
         ["X", "O", "O", "X"],
         ["X", "X", "O", "X"],
         ["X", "O", "X", "X"]]
my_sol.solve(board)
# [['X', 'X', 'X', 'X'],
# ['X', 'X', 'X', 'X'],
# ['X', 'X', 'X', 'X'],
# ['X', 'O', 'X', 'X']]

board = [["O", "O"],
         ["O", "O"]]
my_sol.solve(board)  # [['O', 'O'], ['O', 'O']]

board = [["O", "O", "O"],
         ["O", "O", "O"],
         ["O", "O", "O"]]
my_sol.solve(board)  # [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]

board = [["X", "O", "X"],
         ["X", "O", "X"],
         ["X", "O", "X"]]
my_sol.solve(board)  # [['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']]

board = [["O", "X", "X", "O", "X"],
         ["X", "O", "O", "X", "O"],
         ["X", "O", "X", "O", "X"],
         ["O", "X", "O", "O", "O"],
         ["X", "X", "O", "X", "O"]]
my_sol.solve(
    board)  # [['O', 'X', 'X', 'O', 'X'],
# ['X', 'X', 'X', 'X', 'O'],
# ['X', 'X', 'X', 'O', 'X'],
# ['O', 'X', 'O', 'O', 'O'],
# ['X', 'X', 'O', 'X', 'O']]
