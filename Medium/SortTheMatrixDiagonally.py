#A matrix diagonal is a diagonal line of cells starting from some cell in
# either the topmost row or leftmost column and going in the bottom-right
# direction until reaching the matrix's end. For example, the matrix diagonal
# starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells
# mat[2][0], mat[3][1], and mat[4][2].

#Given an m x n matrix mat of integers, sort each matrix diagonal in
# ascending order and return the resulting matrix.

class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        row_len = len(mat)
        col_len = len(mat[0])

        #sort right matrix split by diagonal
        for j in range(0, col_len):
            i = 0
            self.sort_diagonal(i, j, mat)

        # sort left matrix split by diagonal
        for i in range(0, row_len):
            j = 0
            self.sort_diagonal(i, j, mat)

        return mat

    def sort_diagonal(self, i, j, mat):
        numbers = []
        row_len = len(mat)
        col_len = len(mat[0])

        row_num = i
        col_num = j

        while i < row_len and j < col_len:
            numbers.append(mat[i][j])
            i += 1
            j += 1

        sorted_numbers = sorted(numbers)

        i = row_num
        j = col_num

        for num in sorted_numbers:
            mat[i][j] = num
            i += 1
            j += 1



my_sol = Solution()

# mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# print(my_sol.diagonalSort(mat)) #[[1,1,1,1],[1,2,2,2],[1,2,3,3]]


mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2],[6,5,2,9]]
print(my_sol.diagonalSort(mat)) #[[1,1,1,1],[1,2,2,2],[1,2,3,3], [6,5,2,9]]