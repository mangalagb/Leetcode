#To rotate image by 90 degress,
# 1) find transpose of matrix
# 2) For every row, reverse the columns

class Solution:
    def rotate(self, matrix):
        self.print_matrix(matrix)

        #Find transpose
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if i == j:
                    break

                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        self.print_matrix(matrix)

        # For every row, reverse the columns
        for i in range(0, len(matrix)):
            begin = 0
            end = len(matrix[0]) - 1

            while begin != end:
                temp = matrix[i][begin]
                matrix[i][begin] = matrix[i][end]
                matrix[i][end] = temp
                begin += 1
                end -= 1
        self.print_matrix(matrix)

    def print_matrix(self, matrix):
        for row in matrix:
            print(row)
        print("_____________________")


my_sol = Solution()
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
my_sol.rotate(matrix)
# [7, 4, 1]
# [8, 5, 2]
# [9, 6, 3]
