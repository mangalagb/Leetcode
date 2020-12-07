# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.

#SOLUTION
# https://leetcode.com/problems/maximal-square/discuss/61845/9-lines-Python-DP-solution-with-explaination

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        dp = [[0 for _1_ in range(len(matrix[0]))] for ___ in range(len(matrix))]
        maxArea = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                elif int(matrix[i][j]) == 1:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

                maxArea = max(maxArea, dp[i][j])
        return maxArea * maxArea



my_sol = Solution()

matrix = [["1", "0", "1", "0", "0"],
          ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["1", "0", "0", "1", "0"]]
print(my_sol.maximalSquare(matrix)) #4
