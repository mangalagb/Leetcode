# #A binary matrix means that all elements are 0 or 1. For each individual
# row of the matrix, this row is sorted in non-decreasing order.
#
# Given a row-sorted binary matrix binaryMatrix, return leftmost column
# index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.
#
# You can't access the Binary Matrix directly.  You may only access the
# matrix using a BinaryMatrix interface:
#
# BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col)
# (0-indexed).
# BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols],
# which means the matrix is rows * cols.
# Submissions making more than 1000 calls to BinaryMatrix.get will be
# judged Wrong Answer.  Also, any solutions that attempt to circumvent
# the judge will result in disqualification.
#
# For custom testing purposes you're given the binary matrix mat as input
# in the following four examples. You will not have access the binary matrix directly.

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
import sys

class BinaryMatrix(object):
    def initilize(self, matrix):
        self.matrix = matrix

    def get(self, row, col):
        return self.matrix[row][col]

    def dimensions(self):
        return [len(self.matrix), len(self.matrix[0])]


class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        dimensions = binaryMatrix.dimensions()
        row_len = dimensions[0]
        col_len = dimensions[1]

        if row_len == 0 or col_len == 0:
            return -1

        index = sys.maxsize
        for i in range(0, row_len):
            left_index = self.do_binary_search(binaryMatrix, i, col_len)
            if left_index == -1:
                continue

            index = min(index, left_index)

        if index == sys.maxsize:
            return -1
        else:
            return index

    def do_binary_search(self, binaryMatrix, row, col_len):
        low = 0
        high = col_len - 1
        result = -1

        while low <= high:
            mid = low + (high - low) // 2
            mid_element = binaryMatrix.get(row, mid)

            if mid_element == 0:
                low = mid + 1
            elif mid_element == 1:
                result = mid
                high = mid - 1
        return result


my_sol = Solution()

mat = [[0,0],[1,1]]
binary = BinaryMatrix()
binary.initilize(mat)
print(my_sol.leftMostColumnWithOne(binary)) #0

mat = [[0,0],[0,1]]
binary = BinaryMatrix()
binary.initilize(mat)
print(my_sol.leftMostColumnWithOne(binary)) #1

mat = [[0,0],[0,0]]
binary = BinaryMatrix()
binary.initilize(mat)
print(my_sol.leftMostColumnWithOne(binary)) #-1

mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
binary = BinaryMatrix()
binary.initilize(mat)
print(my_sol.leftMostColumnWithOne(binary)) #1

mat = [[0]]
binary = BinaryMatrix()
binary.initilize(mat)
print(my_sol.leftMostColumnWithOne(binary)) #-1

mat = [[1]]
binary = BinaryMatrix()
binary.initilize(mat)
print(my_sol.leftMostColumnWithOne(binary)) #0