#Given an array of integers nums and an integer limit, return
# the size of the longest non-empty subarray such that the absolute
# difference between any two elements of this subarray is less than or equal to limit.

class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        if not nums:
            return 0

        begin = 0
        max_length = 0
        i = 0
        while i < len(nums):
            current = nums[i]

            if max_length == -1 and abs(current - current) <= limit:
                max_length = 1
                i += 1
                continue

            while begin <= i:
                cur_min = min(nums[begin:i + 1])
                cur_max = max(nums[begin:i + 1])

                val1 = abs(current - cur_min)
                val2 = abs(current - cur_max)

                if val1 > limit or val2 > limit:
                    begin += 1
                else:
                    break

            max_length = max(max_length, (i - begin + 1))
            i += 1
        return max_length


my_sol = Solution()

nums = [8,2,4,7]
limit = 4
print(my_sol.longestSubarray(nums, limit)) #2

nums = [10,1,2,4,7,2]
limit = 5
print(my_sol.longestSubarray(nums, limit)) #4

nums = [4,2,2,2,4,4,2,2]
limit = 0
print(my_sol.longestSubarray(nums, limit)) #3

nums = [5, 25, 100, 300]
limit = -2
print(my_sol.longestSubarray(nums, limit)) #0

