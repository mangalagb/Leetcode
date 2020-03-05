# Your are given an array of positive integers nums.
#
# Count and print the number of (contiguous) subarrays where the product of all the elements in the
# subarray is less than k.

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        begin = 0
        end = 0
        count = 0
        length_of_nums = len(nums)
        product = 1

        while end < length_of_nums:
            current = nums[end]
            if current < k:
                count += 1

            product *= current
            if product < k and end - begin != 0:
                count += 1

            end += 1
            while begin < length_of_nums and product >= k:
                begin_num = nums[begin]
                begin += 1

                if begin_num != 0:
                    product = product // begin_num

                if product < k and end - begin > 1:
                    count += 1

        return count



my_sol = Solution()

nums = [10, 5, 2, 6]
k = 100
print(my_sol.numSubarrayProductLessThanK(nums, k)) #8

nums = [1,2,3]
k = 0
print(my_sol.numSubarrayProductLessThanK(nums, k)) #0

nums = [10,9,10,4,3,8,3,3,6,2,10,10,9,3]
k = 19
print(my_sol.numSubarrayProductLessThanK(nums, k)) #18 4 [[4,3], [3,3], [3,6], [6,2]]
