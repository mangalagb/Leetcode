# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share
# of the stock), design an algorithm to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.
import sys


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price_so_far = sys.maxsize
        max_profit = 0

        for price in prices:
            min_price_so_far = min(price, min_price_so_far)
            max_profit = max(max_profit, (price - min_price_so_far))
        return max_profit

my_sol = Solution()

nums = [7,1,5,3,6,4]
print(my_sol.maxProfit(nums))

nums = [7,6,4,3,1]
print(my_sol.maxProfit(nums))