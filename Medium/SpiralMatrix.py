# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row_begin = 0
        row_end = len(matrix)
        row_front = True

        if row_end == 0:
            return matrix

        col_begin = 0
        col_end = len(matrix[0])
        col_front = True

        result = []
        row_or_col = True

        while True:
            if row_or_col:
                # Loop through columns
                if col_begin == col_end:
                    break

                if row_front:
                    for j in range(col_begin, col_end):
                        num = matrix[row_begin][j]
                        result.append(num)
                    row_front = False
                    row_begin += 1
                else:
                    for j in range(col_end-1, col_begin-1, -1):
                        num = matrix[row_end-1][j]
                        result.append(num)
                    row_front = True
                    row_end -= 1
                row_or_col = False

            # Loop through rows
            else:
                if row_begin == row_end:
                    break

                if col_front:
                    for i in range(row_begin, row_end):
                        num = matrix[i][col_end-1]
                        result.append(num)
                    col_front = False
                    col_end -= 1
                else:
                    for i in range(row_end-1, row_begin-1, -1):
                        num = matrix[i][col_begin]
                        result.append(num)
                    col_front = True
                    col_begin += 1
                row_or_col = True
        return result

my_sol = Solution()

# matrix =[
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# print(my_sol.spiralOrder(matrix)) #[1,2,3,6,9,8,7,4,5]

# matrix = [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# print(my_sol.spiralOrder(matrix)) #[1,2,3,4,8,12,11,10,9,5,6,7]

# matrix = [
#   [1, 2, 3, 4]
# ]
# print(my_sol.spiralOrder(matrix)) #[1,2,3,4]

matrix = [
]
print(my_sol.spiralOrder(matrix)) #[]