# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
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

            # if the target is greater than the value in current position, then the target can not be in current row
            # because the row is sorted
            if target > element:
                row += 1

            # if the target is less than the value in current position, then the target can not be in current column
            # because the column is sorted
            elif target < element:
                col -= 1

            elif target == element:
                return True
        return False

    def searchMatrix_normal(self, matrix, target):
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

        [col_begin, col_end] = self.find_columns(matrix, target)
        [row_begin, row_end] = self.find_rows(matrix, target)

        if col_begin is None and col_end is None:
            return True
        elif col_begin == -1 and col_end == -1:
            return False
        elif col_begin != -1 and col_end == -1:
            col_end = num_cols - 1

        if row_begin is None and row_end is None:
            return True
        elif row_begin == -1 and row_end == -1:
            return False
        elif row_begin != -1 and row_end == -1:
            row_end = num_rows - 1

        for i in range(row_begin, row_end+1):
            for j in range(col_begin, col_end+1):
                if matrix[i][j] == target:
                    return True

        return False

    def find_rows(self, matrix, target):
        row_begin = -1
        row_end = -1
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        for i in range(0, num_rows):
            left = matrix[i][0]
            right = matrix[i][num_cols-1]

            if left == target or right == target:
                return [None, None]

            if left < target < right:
                if row_begin == -1:
                    row_begin = i
                else:
                    row_end = i
        return [row_begin, row_end]


    def find_columns(self, matrix, target):
        col_begin = -1
        col_end = -1
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        for j in range(0, num_cols):
            top = matrix[0][j]
            bottom = matrix[num_rows - 1][j]

            if top == target or bottom == target:
                return [None, None]

            if top < target < bottom:
                if col_begin == -1:
                    col_begin = j
                else:
                    col_end = j
        return [col_begin, col_end]

my_sol = Solution()

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

target = 5
print(my_sol.searchMatrix(matrix, target))

target = 20
print(my_sol.searchMatrix(matrix, target))

target = 0
print(my_sol.searchMatrix([[]], target))
