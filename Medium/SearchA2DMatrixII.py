# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
#
#     Integers in each row are sorted in ascending from left to right.
#     Integers in each column are sorted in ascending from top to bottom.

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        num_rows = len(matrix)
        if num_rows == 0:
            return False

        num_cols = len(matrix[0])
        if num_cols == 0:
            return False

        # Start at the top right corner
        row = 0
        col = num_cols - 1

        while row < num_rows and col > -1:
            element = matrix[row][col]

            # if the target is greater than the value in current position, then the
            # target can not be in current row
            # because the row is sorted
            if target > element:
                row += 1

            # if the target is less than the value in current position, then the target
            # can not be in current column
            # because the column is sorted
            elif target < element:
                col -= 1

            elif target == element:
                return True
        return False


my_sol = Solution()

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

target = 5
print(my_sol.searchMatrix(matrix, target)) #True

target = 20
print(my_sol.searchMatrix(matrix, target)) #False

target = 0
print(my_sol.searchMatrix([[]], target)) #False

target = 13
print(my_sol.searchMatrix(matrix, target)) #True
