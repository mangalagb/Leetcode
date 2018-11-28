#To rotate image by 90 degress,
# 1) find transpose of matrix
# 2) For every row, reverse the columns

class Solution:
    def rotate(self, matrix):
        self.print_matrix(matrix)

        #Find transpose
        size = len(matrix[0])
        for i in range(0, size):
            for j in range(i+1, size):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        self.print_matrix(matrix)

        # For every row, reverse the columns
        for i in range(0, size):
            j = 0
            k = size - 1
            while j < k:
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][k]
                matrix[i][k] = temp
                j += 1
                k -= 1
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
