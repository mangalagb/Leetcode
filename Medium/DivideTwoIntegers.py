# Given two integers dividend and divisor, divide two integers without
# using multiplication, division, and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero, which means losing its fractional part.
# For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
#
# Note:
#
# Assume we are dealing with an environment that could only store integers within
# the 32-bit signed integer range: [−231,  231 − 1]. For this problem, assume that
# your function returns 231 − 1 when the division result overflows.

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        negative = False
        max_postive = pow(2, 31) - 1
        max_negative = -1 * (pow(2, 31))

        if divisor * dividend < 0:
            negative = True

        divisor = abs(divisor)
        dividend = abs(dividend)

        power_of_2 = 1
        result = 0
        while dividend >= divisor:
            #divisor can be subtracted atleast once
            # but what if we can subtract it twice or 4 times or 8 times or 16
            #increase it by 2 * previous every time

            value = divisor
            while value <= max_postive and (value + value) < dividend:
                value += value
                power_of_2 += power_of_2

            # repeat the previous process every time always trying to subtract
            # a multiple of divisor from the remaining number
            result += power_of_2
            dividend -= value
            power_of_2 = 1

        if negative:
            result = -result

        if result > max_postive:
            return max_postive
        elif result < max_negative:
            return max_negative
        else:
            return result


my_sol = Solution()

dividend = 10
divisor = 3
print(my_sol.divide(dividend, divisor)) #3

dividend = 7
divisor = -3
print(my_sol.divide(dividend, divisor)) #-2

dividend = 0
divisor = 1
print(my_sol.divide(dividend, divisor)) #0

dividend = 1
divisor = 1
print(my_sol.divide(dividend, divisor)) #1

dividend = pow(2, 30)
divisor = 1
print(my_sol.divide(dividend, divisor)) # 1073741824

dividend = -2147483648
divisor = -1
print(my_sol.divide(dividend, divisor)) # 2147483647
