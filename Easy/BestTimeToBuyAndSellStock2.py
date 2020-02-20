# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as
# you like (i.e., buy one and sell one share of the stock multiple times).
#
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the
# stock before you buy again).

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit

my_sol = Solution()

nums = [7,1,5,3,6,4]
print(my_sol.maxProfit(nums))

nums = [1,2,3,4,5]
print(my_sol.maxProfit(nums))

nums = [6,1,3,2,4,7]
print(my_sol.maxProfit(nums))