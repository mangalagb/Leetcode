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
                if board[i][j] == "O":
                    self.do_DFS(board, i, j)
        #print(board)

    def do_DFS(self, board, row, col):

        # If boundary condition is not satisfied
        if not self.does_not_have_O_in_boundary(board, row, col):
            return

        # Stack's top is at index 0
        stack = [[row, col]]
        visited = []

        while len(stack) > 0:
            top_element = stack[0]
            top_row = top_element[0]
            top_col = top_element[1]

            #Mark current as visited
            visited.insert(0, top_element)

            #Find unvisited neighbours
            neighbour = self.find_unvisited_neighbour(board, top_row, top_col, visited)

            good_neighbour = self.does_not_have_O_in_boundary(board, top_row, top_col)
            # The whole area needs to be cleared
            if not good_neighbour:
                visited.clear()
                break

            if len(neighbour) > 0:
                stack.insert(0, neighbour)
            else:
                stack.pop(0)

        for node in visited:
            row_num = node[0]
            col_num = node[1]
            board[row_num][col_num] = "X"


    def find_unvisited_neighbour(self, board, row, col, visited):
        neighbours = [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]
        non_border_rows = len(board) - 2
        non_border_cols = len(board[0]) -2

        for neighbour in neighbours:
            row_num = neighbour[0]
            col_num = neighbour[1]

            if 1 <= row_num <= non_border_rows and 1 <= col_num <= non_border_cols and board[row_num][col_num] == "O":
                if [row_num, col_num] not in visited:
                    return [row_num, col_num]
        return []


    def does_not_have_O_in_boundary(self, board, row, col):
        # Should not have a O in the border
        neighbours = [[row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]]

        #Check if any of the borders contain 0
        for neighbour in neighbours:
            board_row = neighbour[0]
            board_col = neighbour[1]

            row_len = len(board)
            col_len = len(board[0])

            if board_row == 0 or board_row == row_len - 1 or board_col == 0 or board_col == col_len:
                if board[board_row][board_col] == "O":
                    return False
        return True


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
my_sol.solve(board) #[['O', 'X', 'X', 'O', 'X'], ['X', 'X', 'X', 'X', 'O'], ['X', 'X', 'X', 'O', 'X'],
# ['O', 'X', 'O', 'O', 'O'], ['X', 'X', 'O', 'X', 'O']]

board = [["X","O","X","X"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]]
my_sol.solve(board) #[["X","O","X","X"],["O","X","X","X"],["X","X","X","O"],["O","X","O","X"]]

