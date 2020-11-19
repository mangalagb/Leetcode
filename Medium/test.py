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

        #Store all zero elements in queue and do BFS from there
        queue = []

        #Set all non zero elements to a dummy value
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] != 0:
                    matrix[i][j] = -1
                else:
                    queue.append([i, j, 0])

        #Start a BFS from every zero element and compute distance for neighbours
        while len(queue) > 0:
            element = queue.pop(0)
            i = element[0]
            j = element[1]
            length = element[2]

            neighbours = self.find_unvisited_neighbour(matrix, i, j)
            for neighbour in neighbours:
                row = neighbour[0]
                col = neighbour[1]
                neighbour_length = length + 1
                matrix[row][col] = neighbour_length
                queue.append([neighbour[0], neighbour[1], neighbour_length])
        return matrix


    def find_unvisited_neighbour(self, matrix, i, j):
        neighbours = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]
        row_len = len(matrix)
        col_len = len(matrix[0])
        unvisited_neighbours = []

        for neighbour in neighbours:
            row_val = neighbour[0]
            col_val = neighbour[1]

            if 0 <= row_val < row_len and 0 <= col_val < col_len and matrix[row_val][col_val] == -1:
                unvisited_neighbours.append(neighbour)
        return unvisited_neighbours


my_sol = Solution()

matrix = [[0,0,0],
 [0,1,0],
 [1,1,1]]
print(my_sol.updateMatrix(matrix)) #[[0,0,0],
                                    # [0,1,0],
                                     #[1,2,1]]

matrix = [[0,0,0],
 [0,1,0],
 [0,0,0]]
print(my_sol.updateMatrix(matrix)) #[[[0,0,0],
                                    # [0,1,0],
                                    # [0,0,0]]

# matrix = [[1,1,0,0,1,0,0,1,1,0],[1,0,0,1,0,1,1,1,1,1],[1,1,1,0,0,1,1,1,1,0],[0,1,1,1,0,1,1,1,1,1],[0,0,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,0,1,1,1],[0,1,1,1,1,1,1,0,0,1],[1,1,1,1,1,0,0,1,1,1],[0,1,0,1,1,0,1,1,1,1],[1,1,1,0,1,0,1,1,1,1]]
# print(my_sol.updateMatrix(matrix))