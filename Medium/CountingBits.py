# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in
# their binary representation and return them as an array.

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