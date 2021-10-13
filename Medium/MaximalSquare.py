# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.

#SOLUTION
# https://leetcode.com/problems/maximal-square/discuss/61845/9-lines-Python-DP-solution-with-explaination

class Solution(object):
    def maximalSquare(self, matrix):
        row_len = len(matrix)
        col_len = len(matrix[0])

        for i in range(0, row_len):
            for j in range(0, col_len):
                val = matrix[i][j]
                matrix[i][j] = int(val)

        # Make a dp matrix of size row+1, col+1
        dp_matrix = []
        for i in range(0, row_len+1):
            new_row = []
            for j in range(0, col_len+1):
                new_row.append(0)
            dp_matrix.append(new_row)

        max_size = 0
        for i in range(0, row_len):
            for j in range(0, col_len):
                if matrix[i][j] == 1:
                    dp_matrix[i][j] = min(dp_matrix[i-1][j-1], dp_matrix[i-1][j], dp_matrix[i][j-1]) + 1
                    max_size = max(max_size, dp_matrix[i][j])

        area = max_size * max_size
        return area


my_sol = Solution()

matrix = [["1", "0", "1", "0", "0"],
          ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["1", "0", "0", "1", "0"]]
print(my_sol.maximalSquare(matrix)) #4

matrix = [["0","1"],["1","0"]]
print(my_sol.maximalSquare(matrix)) #1


matrix = [["0"]]
print(my_sol.maximalSquare(matrix)) #0
