# Given a binary array, find the maximum number of consecutive 1s in this array.

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        begin = 0
        end = 0
        count = 0

        while end < len(nums):
            num = nums[end]
            if num == 0:
                begin = end + 1
                if begin == len(nums):
                    return count

            local_count = end - begin + 1
            count = max(count, local_count)
            end += 1
        return count

my_sol = Solution()

nums = [1,1,0,1,1,1]
print(my_sol.findMaxConsecutiveOnes(nums))

nums = [1,1,0,1]
print(my_sol.findMaxConsecutiveOnes(nums))