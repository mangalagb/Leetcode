# Given a non negative integer number num. For every numbers i in the
# range 0 ≤ i ≤ num calculate the number of 1's in
# their binary representation and return them as an array.

# <<
# When shifting left, the most-significant bit is lost,
# and a 00 bit is inserted on the other end.
# A single left shift multiplies a binary number by 2:

# >>
#When shifting right with a logical right shift,
# the least-significant bit is lost and a 00 is inserted on the other end.
#For positive numbers, a single logical right shift divides a number by 2,
# throwing out any remainders.

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0] * (num+1)
        for i in range(1, num+1):
            number = i
            if number % 2 == 0:
                number = number >> 1
                result[i] = result[number]
            else:
                result[i] = result[i-1] + 1
        return result

my_sol = Solution()

num = 2
print(my_sol.countBits(num))