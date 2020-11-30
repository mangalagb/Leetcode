# Implement pow(x, n), which calculates x raised to the power n (i.e. xn).
#


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        negative = False
        if n < 0:
            negative = True
            n = -1 * n

        result = self.find_power(x, n)
        if negative:
            result = 1 / result
        return result


    def find_power(self, x, n):
        if n == 2:
            return x*x
        elif n == 1:
            return x
        elif n == 0:
            return 1

        current_result = 1
        if n % 2 == 0:
            n = n // 2
            current_result = self.find_power(x, n)
            current_result = current_result * current_result
        else:
            n -= 1
            current_result = self.find_power(x, n)
            current_result = current_result * x
        return current_result



my_sol = Solution()

x = 2.00000
n = 10
print(my_sol.myPow(x, n)) #1024.00000

x = 2.10000
n = 3
print(my_sol.myPow(x, n)) #9.26100

x = 2.00000
n = -2
print(my_sol.myPow(x, n)) #0.25000
