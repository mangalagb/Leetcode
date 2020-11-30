# Given a positive integer n, generate an n x n matrix filled with
# elements from 1 to n^2 in spiral order.

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[-1 for x in range(n)] for y in range(n)]

        counter = 1
        row_front = True
        col_down = True
        fill_row = True

        row_begin = 0
        row_end = n - 1
        col_begin = 0
        col_end = n - 1

        while row_begin < row_end+1 or col_begin < col_end+1:
            if fill_row:
                if row_front:
                    for j in range(col_begin, col_end+1):
                        matrix[row_begin][j] = counter
                        counter += 1
                    row_begin += 1
                    row_front = False
                else:
                    for j in range(col_end, col_begin-1, -1):
                        matrix[row_end][j] = counter
                        counter += 1
                    row_end -= 1
                    row_front = True
                fill_row = False
            else:
                if col_down:
                    for i in range(row_begin, row_end+1):
                        matrix[i][col_end] = counter
                        counter += 1
                    col_end -= 1
                    col_down = False
                else:
                    for i in range(row_end, row_begin-1, -1):
                        matrix[i][col_begin] = counter
                        counter += 1
                    col_begin += 1
                    col_down = True
                fill_row = True

        return matrix


my_sol = Solution()

n = 3
print(my_sol.generateMatrix(n)) #[[1,2,3],[8,9,4],[7,6,5]]

n = 1
print(my_sol.generateMatrix(n)) #[[1]]
