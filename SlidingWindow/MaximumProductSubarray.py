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

        sums = []
        i = 0
        product = 1
        first_num_appended = False

        while i < length_of_nums:
            if i == 0:
                current = nums[i]
                if current >= 0:
                    product *= current
                else:
                    sums.append(current)
                    first_num_appended = True
                i += 1
                continue

            if product == 0:
                sums.append(0)
                product = nums[i]
                i += 1
                if i == length_of_nums:
                    sums.append(product)
                continue

            postive_numbers = False
            while i < length_of_nums and nums[i] > 0:
                product *= nums[i]
                i += 1
                postive_numbers = True
            if postive_numbers or not first_num_appended:
                sums.append(product)
                first_num_appended = True


            if i < length_of_nums and nums[i] <= 0:
                sums.append(nums[i])
                product = 1
                i += 1

        result = None
        product = None
        for num in sums:
            if result is None:
                result = num
                product = num
                continue

            result = max(result, num)
            product *= num
            result = max(result, product)
        return result

my_sol = Solution()

nums = [2,-5,-2,-4,3]
print(my_sol.maxProduct(nums)) # 24

# nums = [2,3,-2,4]
# print(my_sol.maxProduct(nums)) # 6
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
#
# nums = [-2,3,-4]
# print(my_sol.maxProduct(nums)) # 24
#
# nums = [-2,13,-4]
# print(my_sol.maxProduct(nums)) # 104
#
# nums = [7,-2,-4]
# print(my_sol.maxProduct(nums)) # 56