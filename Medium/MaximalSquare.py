# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                current = matrix[i][j]
                if current is "1":
                    self.do_DFS(i, j, matrix)

    def do_DFS(self, row, col, matrix):
        stack = [[row, col]]
        size = 1
        




my_sol = Solution()

matrix = [["1", "0", "1", "0", "0"],
          ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["1", "0", "0", "1", "0"]]
print(my_sol.maximalSquare(matrix))
