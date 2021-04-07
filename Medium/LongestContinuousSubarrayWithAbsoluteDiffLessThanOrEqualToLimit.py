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

        # Min element is at index 0
        # store index not num
        min_queue = []

        # Max element is at index 0
        max_queue = []

        start = 0
        end = 0
        max_length = 0

        while end < len(nums):
            current = nums[end]

            if not min_queue and not max_queue:
                min_queue.append(end)
                max_queue.append(end)
                continue

            #Min element has to be in the front
            while len(min_queue) > 0 and current <= nums[min_queue[-1]]:
                min_queue.pop(-1)

            # Max element has to be in the front
            while len(max_queue) > 0 and current >= nums[max_queue[-1]]:
                max_queue.pop(-1)

            min_queue.append(end)
            max_queue.append(end)

            #Check the starting 2 elements for limit
            min_queue_front = nums[min_queue[0]]
            max_queue_front = nums[max_queue[0]]
            if abs(min_queue_front - max_queue_front) > limit:
                start += 1

                if start > min_queue[0]:
                    min_queue.pop(0)

                if start > max_queue[0]:
                    max_queue.pop(0)
            else:
                max_length = max(max_length, (end-start) +1)
                end += 1
        return max_length



my_sol = Solution()

nums = [8]
limit = 10
print(my_sol.longestSubarray(nums, limit)) #1

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
limit = 2
print(my_sol.longestSubarray(nums, limit)) #0

