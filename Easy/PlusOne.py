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

digits = [1,0]
print(my_sol.plusOne(digits))
