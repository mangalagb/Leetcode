# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
#
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        previous_row = None
        for i in range(0, len(matrix)):
            row = matrix[i]
            previous_row, result = self.row_by_row(row, previous_row)
            if not result:
                return False
        return True

    def row_by_row(self, row, previous_row):
        new_previous_row = []
        if not previous_row:
            previous_row = row
            return previous_row, True

        new_previous_row.append(row[0])
        for j in range(1, len(row)):
            num = row[j]

            previous_element = previous_row[j-1]
            if num != previous_element:
                return None, False
            new_previous_row.append(num)
        previous_row = new_previous_row
        return previous_row, True


my_sol = Solution()

matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
print(my_sol.isToeplitzMatrix(matrix)) #True

matrix = [[1,2],[2,2]]
print(my_sol.isToeplitzMatrix(matrix)) #False

matrix = [[1]]
print(my_sol.isToeplitzMatrix(matrix)) #True

matrix = [[1], [1]]
print(my_sol.isToeplitzMatrix(matrix)) #True

matrix = [[1, 2], [3,1]]
print(my_sol.isToeplitzMatrix(matrix)) #True

