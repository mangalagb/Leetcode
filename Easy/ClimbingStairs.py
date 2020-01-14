# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct
#  ways can you climb to the top?
#
# Note: Given n will be a positive integer.

class Solution:
    def climbStairs(self, n):

        if n == 1:
            return 1
        elif n == 2:
            return 2

        a = 1
        b = 2
        c = 0

        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return c


my_solution = Solution()

n = 6
print(my_solution.climbStairs(n))

#1 = 1
# 2 = 2
# 3 = 3
# 4 = 5
# 5= 8
# 6 =13
