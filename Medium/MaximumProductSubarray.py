# Given an integer array nums, find the contiguous subarray within an array (containing at least one number)
# which has the largest product.

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length_of_nums = len(nums)
        if length_of_nums == 1:
            return nums[0]

        break_on_negative = True
        count = sum(1 for x in nums if x < 0)
        if count % 2 == 0:
            break_on_negative = False

        i = 0
        j = 1
        result = 0
        product = nums[i]
        while j < length_of_nums:
            current = nums[j]
            result = max(result, current)

            product *= current





    def maxProduct1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length_of_nums = len(nums)
        if length_of_nums == 1:
            return nums[0]

        i = 0
        j = 1
        result = 0
        while i < length_of_nums:
            product = nums[i]

            if j >= length_of_nums:
                result = max(result, product)
                break

            while j < length_of_nums and nums[j] * product > result:
                product *= nums[j]
                result = product
                j += 1

            #remove from beginning
            if j < length_of_nums:
                product = nums[j]
                result = max(result, product)

                i = j + 1
                j = i + 1
        return result

my_sol = Solution()

nums = [2,3,-2,4]
print(my_sol.maxProduct(nums)) # 6
#
# nums = [2,3,-2,10]
# print(my_sol.maxProduct(nums)) # 10
#
# nums = [-2,0,-1]
# print(my_sol.maxProduct(nums)) #0
#
# nums = [0,2]
# print(my_sol.maxProduct(nums)) #2
#
# nums = [-4,-3]
# print(my_sol.maxProduct(nums)) # 12

# nums = [-2,3,-4]
# print(my_sol.maxProduct(nums)) # 24

# nums = [-2,13,-4]
# print(my_sol.maxProduct(nums)) # 13