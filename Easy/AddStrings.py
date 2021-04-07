# Given two non-negative integers num1 and num2 represented as string,
# return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 or not num2:
            return ""
        elif not num1:
            return num2
        elif not num2:
            return num1

        reversed_num1 = num1[::-1]
        reversed_num2 = num2[::-1]

        len_num1 = len(reversed_num1)
        len_num2 = len(reversed_num2)
        i = 0
        carry = 0
        result = ""

        while i < len_num1 or i < len_num2:
            digit1 = 0
            digit2 = 0
            sum_digits = 0

            if i < len_num1:
                digit1 = reversed_num1[i]
            if i < len_num2:
                digit2 = reversed_num2[i]

            if carry:
                sum_digits += 1
                carry = 0

            sum_digits += (int(digit1) + int(digit2))

            unit_digit = sum_digits % 10
            tens_digit = sum_digits // 10

            result = str(unit_digit) + result
            if tens_digit != 0:
                carry = 1
            i += 1

        if carry:
            result = "1" + result
        return result



my_sol = Solution()

num1 = "62"
num2 = "3"
print(my_sol.addStrings(num1, num2)) #65

num1 = "69"
num2 = "99"
print(my_sol.addStrings(num1, num2)) #168

num1 = "9999"
num2 = "1"
print(my_sol.addStrings(num1, num2)) #10000

num1 = "999"
num2 = "11"
print(my_sol.addStrings(num1, num2)) #1010

num1 = "0"
num2 = "0"
print(my_sol.addStrings(num1, num2)) #0

num1 = "10"
num2 = "0"
print(my_sol.addStrings(num1, num2)) #10
