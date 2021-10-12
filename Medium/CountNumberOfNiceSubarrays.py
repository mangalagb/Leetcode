#Given an array of integers nums and an integer k. A continuous
# subarray is called nice if there are k odd numbers on it.

#Return the number of nice sub-arrays.

from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        odd_numbers_seen_so_far = 0
        odd_num_frequency = defaultdict(int)
        odd_num_frequency[0] = 1

        for number in nums:
            if number % 2 != 0:
                odd_numbers_seen_so_far += 1

            if (odd_numbers_seen_so_far - k) in odd_num_frequency:
                result += odd_num_frequency[(odd_numbers_seen_so_far-k)]

            #update current off number
            odd_num_frequency[odd_numbers_seen_so_far] += 1
        return result

my_sol = Solution()


nums = [1,1,2,1,1]
k = 3
print(my_sol.numberOfSubarrays(nums, k))#2

nums = [2,4,6]
k = 1
print(my_sol.numberOfSubarrays(nums, k))#0

nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
print(my_sol.numberOfSubarrays(nums, k))#16
