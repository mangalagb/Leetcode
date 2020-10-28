#Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row_len = len(matrix)
        if not row_len:
            return False

        col_len = len(matrix[0])
        if not col_len:
            return False

        row_num = self.find_row(matrix, target)
        if row_num == -1:
            return True
        elif row_num is None:
            return False

        result = self.binary_search(matrix[row_num], target)
        return result

    def binary_search(self, nums, target):
        low = 0
        high = len(nums)

        while low <= high:
            mid = low + (high-low)//2

            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
        return False


    def find_row(self, matrix, target):
        col_length = len(matrix[0])

        row_num = 0
        col_num = col_length-1

        while row_num < len(matrix):
            element = matrix[row_num][col_num]

            if target == element:
                return -1
            elif target < element:
                return row_num
            elif target > element:
                row_num += 1

        return None



my_sol = Solution()

# matrix = [[1, 3, 5, 7],
#           [10, 11, 16, 20],
#           [23, 30, 34, 50]]
# target = 16
# print(my_sol.searchMatrix(matrix, target)) #True
#
# target = 23
# print(my_sol.searchMatrix(matrix, target)) #True
#
# target = 15
# print(my_sol.searchMatrix(matrix, target)) #False
#
# matrix = [[]]
# target = 1
# print(my_sol.searchMatrix(matrix, target)) #False

matrix = []
target = 1
print(my_sol.searchMatrix(matrix, target)) #False
