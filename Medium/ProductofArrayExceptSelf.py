# Given an array nums of n integers where n > 1,  return an array output
# such that output[i] is equal to the product of all the
# elements of nums except nums[i].

class Solution:
    def productExceptSelf(self, nums):
        product = 1
        n = len(nums)
        output = []

        for i in range(0, n):
            output.append(product)
            product *= nums[i]

        product = 1
        for i in range(n-1, -1, -1):
            output[i] = output[i] * product
            product *= nums[i]
        return output



my_sol = Solution()

nums = [1,2,3,4]
print(my_sol.productExceptSelf(nums))