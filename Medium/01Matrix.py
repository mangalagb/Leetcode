# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
#
# The distance between two adjacent cells is 1.
import sys


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return matrix
        if not matrix[0]:
            return matrix

        check_first_element = False
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                current = matrix[i][j]

                if i == 0 and j == 0 and current != 0:
                    check_first_element = True
                    continue

                if current != 0:
                    self.is_neighbour_zero(i, j, matrix, False)

        if check_first_element:
            self.is_neighbour_zero(0,0, matrix, True)

        return matrix

    def is_neighbour_zero(self, i, j, matrix, check_first_element):
        neighbours = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
        row_len = len(matrix)
        col_len = len(matrix[0])

        for neighbour in neighbours:
            row_val = neighbour[0]
            col_val = neighbour[1]

            if 0 <= row_val < row_len and 0 <= col_val < col_len and matrix[row_val][col_val] == 0:
                return True

        min_neighbour = sys.maxsize
        for neighbour in neighbours:
            row_val = neighbour[0]
            col_val = neighbour[1]

            if 0 <= row_val < row_len and 0 <= col_val < col_len:
                neighbour_value = matrix[row_val][col_val]

                if row_val == i and col_val > j and matrix[row_val][col_val] != 0 and not check_first_element:
                    continue

                if col_val == j and row_val > i and matrix[row_val][col_val] != 0 and not check_first_element:
                    continue

                min_neighbour = min(neighbour_value, min_neighbour)
        matrix[i][j] = min_neighbour + 1



my_sol = Solution()

# matrix = [[0,0,0],
#  [0,1,0],
#  [1,1,1]]
# print(my_sol.updateMatrix(matrix)) #[[0,0,0],
#                                     # [0,1,0],
#                                      #[1,2,1]]
#
# matrix = [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
# print(my_sol.updateMatrix(matrix)) #[[[0,0,0],
#                                     # [0,1,0],
#                                     # [0,0,0]]

matrix = [[1,1,0,0,1,0,0,1,1,0],[1,0,0,1,0,1,1,1,1,1],[1,1,1,0,0,1,1,1,1,0],[0,1,1,1,0,1,1,1,1,1],[0,0,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,0,1,1,1],[0,1,1,1,1,1,1,0,0,1],[1,1,1,1,1,0,0,1,1,1],[0,1,0,1,1,0,1,1,1,1],[1,1,1,0,1,0,1,1,1,1]]
print(my_sol.updateMatrix(matrix))