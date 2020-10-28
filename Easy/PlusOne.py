# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and
# each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.

class Solution:
    def plusOne(self, digits):
        num = digits[0]

        for i in range(1, len(digits)):
            digit = digits[i]
            num = (num * 10) + digit

        result = []
        num += 1

        while num > 0:
            digit = num % 10
            num = num // 10
            result.insert(0, digit)
        return result



my_sol = Solution()

digits = [1,2,3]
print(my_sol.plusOne(digits))

digits = [4,3,2,1]
print(my_sol.plusOne(digits))

digits = [0]
print(my_sol.plusOne(digits))

digits = [1,9]
print(my_sol.plusOne(digits))
