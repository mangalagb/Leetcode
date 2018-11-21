# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.

from collections import defaultdict

class Solution(object):
    def majorityElement(self, nums):

        if not nums:
            return -1

        half_size = len(nums) //2
        biggest_num = -1
        biggest_count = -1
        num_dict = defaultdict(int)

        for num in nums:
            num_dict[num] += 1

        for key, val in num_dict.items():

            if val > biggest_count and val > half_size:
                biggest_count = val
                biggest_num = key

        #print(biggest_num, biggest_count)
        return biggest_num


my_sol = Solution()

nums  = [3,2,3]
print(my_sol.majorityElement(nums))

nums = [2,2,1,1,1,2,2]
print(my_sol.majorityElement(nums))

