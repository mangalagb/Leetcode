#Given two binary strings a and b, return their sum as a binary string.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        str1 = a[::-1]
        str2 = b[::-1]

        length_str1 = len(str1)
        length_str2 = len(str2)

        i = 0
        carry = 0
        ans = ""
        while i < length_str1 or i < length_str2:
            num1 = "0"
            num2 = "0"

            if i < length_str1:
                num1 = str1[i]
            if i < length_str2:
                num2 = str2[i]

            result, carry = self.add_binary(num1, num2, carry)
            ans = str(result) + ans
            i += 1

        if carry:
            ans = "1" + ans
        return ans



    def add_binary(self, num1, num2, carry):
        result = 0
        if num1 == "1" and num2 == "1":
            if carry:
                result = 1
                carry = 1
            else:
                result = 0
                carry = 1
        elif num1 == "0" and num2 == "0":
            if carry:
                result = 1
            else:
                result = 0
            carry = 0
        else:
            if carry:
                result = 0
                carry = 1
            else:
                result = 1
                carry = 0

        return result, carry


my_sol = Solution()

a = "11"
b = "1"
print(my_sol.addBinary(a, b)) #"100"

a = "1010"
b = "1011"
print(my_sol.addBinary(a, b)) #  "10101"

a = "00"
b = "00"
print(my_sol.addBinary(a, b)) #  "00"

a = "011"
b = ""
print(my_sol.addBinary(a, b)) #  "011"