#Given a matrix A, return the transpose of A.

#The transpose of a matrix is the matrix flipped over it's main diagonal,
# switching the row and column indices of the matrix.

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = [[]] * len(A[0])
        value = len(A)
        for i in range(0, len(result)):
            result[i] = [0] * value

        for i in range(0, len(A)):
            for j in range(0, len(A[0])):
                if j == i:
                    result[i][j] = A[i][j]
                else:
                    result[j][i] = A[i][j]
        return result

my_sol = Solution()

matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
# [[1,4,7],[2,5,8],[3,6,9]]
print(my_sol.transpose(matrix1))

matrix2 = [[1,2,3],[4,5,6]]
# [[1,4],[2,5],[3,6]]
print(my_sol.transpose(matrix2))

