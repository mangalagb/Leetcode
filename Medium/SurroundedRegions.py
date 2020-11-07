#Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
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

        for i in range(1, len(board)-1):
            for j in range(1, len(board[0])-1):
                if board[i][j] == "O" and self.is_surrounded_by_atleast_one_X(board, i, j):
                    self.do_DFS(board, i, j)
        #print(board)


    def is_surrounded_by_atleast_one_X(self, board, row, col):
        # 1) Should have atleast 1 X surrounding it
        # 2) Should not have a O in the border

        neighbours = [[row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]]

        at_least_1_X = False
        has_good_border = False
        for neighbour in neighbours:
            board_row = neighbour[0]
            board_col = neighbour[1]

            row_len = len(board)
            col_len = len(board[0])

            if 0 <= board_row <= row_len and 0 <= board_col <= col_len:
                if board[board_row][board_col] == "X":
                    at_least_1_X = True

                if board_row == 0 or board_row == row_len-1 or board_col == 0 or board_col == col_len:
                    if board[board_row][board_col] != "O":
                        has_good_border = True

                local_result_for_current_neighbour = at_least_1_X and has_good_border
                if not local_result_for_current_neighbour:
                    return False
        return True

    def do_DFS(self, board, row, col):
        # Stack's top is at index 0
        stack = [[row, col]]
        visited = []

        while len(stack) > 0:
            top_element = stack[0]
            top_row = top_element[0]
            top_col = top_element[1]

            #Mark current as visited
            board[top_row][top_col] = "X"

            #Find unvisited neighbours
            neighbour = self.find_unvisited_neighbour(board, top_row, top_col)

            if len(neighbour) > 0:
                stack.insert(0, neighbour)
            else:
                stack.pop(0)


    def find_unvisited_neighbour(self, board, row, col):
        neighbours = [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]
        non_border_rows = len(board) - 2
        non_border_cols = len(board[0]) -2

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
my_sol.solve(board) #[['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']]


board = [["O", "O"],
        ["O", "O"]]
my_sol.solve(board) #[['O', 'O'], ['O', 'O']]


board = [["O","O","O"],
         ["O","O","O"],
         ["O","O","O"]]
my_sol.solve(board) #[['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]

board = [["X","O","X"],
         ["X","O","X"],
         ["X","O","X"]]
my_sol.solve(board) #[['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']]


board = [["O","X","X","O","X"],
         ["X","O","O","X","O"],
         ["X","O","X","O","X"],
         ["O","X","O","O","O"],
         ["X","X","O","X","O"]]
my_sol.solve(board) #[['O', 'X', 'X', 'O', 'X'], ['X', 'X', 'X', 'X', 'O'], ['X', 'X', 'X', 'O', 'X'], ['O', 'X', 'O', 'O', 'O'], ['X', 'X', 'O', 'X', 'O']]

