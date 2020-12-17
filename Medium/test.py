# Given an array of integers nums and an integer limit, return
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

        if limit == 0:
            prev = nums[0]
            max_limit = 0

            i = 1
            begin = 0
            while i < len(nums):
                current = nums[i]

                if prev == current:
                    while i < len(nums) and prev == nums[i]:
                        i += 1
                    max_limit = max(max_limit, (i-begin))

                prev = current
                begin = i
            return max_limit




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
                cur_min, min_index = self.find_min(nums, begin, i+1)
                cur_max, max_index = self.find_max(nums, begin, i+1)

                val1 = abs(current - cur_min)
                val2 = abs(current - cur_max)

                if val1 > limit or val2 > limit:
                    latest_index = max(min_index, max_index)
                    begin = latest_index + 1
                else:
                    break

            max_length = max(max_length, (i - begin + 1))
            i += 1
        return max_length

    def find_min(self, numbers, start, end):
        if len(numbers) == 1:
            return numbers[0], 0

        min_num = -1
        min_index = -1
        for i in range(start, end):
            current = numbers[i]

            if min_index == -1:
                min_num = current
                min_index = i
                continue

            if current < min_num:
                min_num = current
                min_index = i
        return min_num, min_index

    def find_max(self, numbers, start, end):
        if len(numbers) == 1:
            return numbers[0], 0

        max_num = -1
        max_index = -1
        for i in range(start, end):
            current = numbers[i]

            if max_index == -1:
                max_num = current
                max_index = i
                continue

            if current > max_num:
                max_num = current
                max_index = i
        return max_num, max_index



my_sol = Solution()

nums = [8, 2, 4, 7]
limit = 4
print(my_sol.longestSubarray(nums, limit))  # 2

nums = [10, 1, 2, 4, 7, 2]
limit = 5
print(my_sol.longestSubarray(nums, limit))  # 4

nums = [4, 2, 2, 2, 4, 4, 2, 2]
limit = 0
print(my_sol.longestSubarray(nums, limit))  # 3

nums = [5, 25, 100, 300]
limit = -2
print(my_sol.longestSubarray(nums, limit))  # 0

