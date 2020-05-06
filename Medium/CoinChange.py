# You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
import sys

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # num_of_coins[i] will be storing the minimum
        # number of coins required for i value.
        # So num_of_coins[V] will have result
        num_of_coins = [sys.maxsize] * (amount+1)

        # Base case (If given value V is 0)
        # 0 coins for amount 0
        num_of_coins[0] = 0

        # Compute minimum coins required
        # for all values from 1 to amount
        for i in range(1, amount+1):
            for coin in coins:
                # Go through all coins smaller than i
                if coin <= i:
                    sub_result = num_of_coins[i - coin]

                    if sub_result != sys.maxsize and sub_result < num_of_coins[i]:
                        num_of_coins[i] = sub_result + 1

        result = num_of_coins[amount]
        if result == sys.maxsize:
            result = -1
        return result


my_sol = Solution()

coins = [1, 2, 5]
amount = 11
print(my_sol.coinChange(coins, amount)) #3

coins = [2]
amount = 3
print(my_sol.coinChange(coins, amount)) #-1

coins = [2147483647]
amount = 2
print(my_sol.coinChange(coins, amount)) #-1

