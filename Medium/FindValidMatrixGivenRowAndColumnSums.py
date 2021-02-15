# You are given two arrays rowSum and colSum of non-negative
# integers where rowSum[i] is the sum of the elements in the ith row
# and colSum[j] is the sum of the elements of the jth column of a 2D
# matrix. In other words, you do not know the elements of the matrix,
# but you do know the sums of each row and column.
#
# Find any matrix of non-negative integers of size rowSum.length x
# colSum.length that satisfies the rowSum and colSum requirements.
#
# Return a 2D array representing any matrix that fulfills the requirements.
# It's guaranteed that at least one matrix that fulfills the requirements exists.

class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        num_rows = len(rowSum)
        num_cols = len(colSum)
        result = []

        for i in range(0, num_rows):
            curr_row = [0] * num_cols
            result.append(curr_row)

        i = 0
        j = 0
        while i < num_rows and j < num_cols:
            #Find the minimum among rowsum and colsum
            minimum_element = min(rowSum[i], colSum[j])
            result[i][j] = minimum_element

            #Subtract this num from the rowsum and colsum
            rowSum[i] -= minimum_element
            colSum[j] -= minimum_element

            #If we have already used up all the numbers in a row, do row++
            if rowSum[i] == 0:
                i += 1
            if colSum[j] == 0:
                j += 1

        return result


my_sol = Solution()

rowSum = [3,8]
colSum = [4,7]
print(my_sol.restoreMatrix(rowSum, colSum))

rowSum = [5,7,10]
colSum = [8,6,8]
print(my_sol.restoreMatrix(rowSum, colSum))

