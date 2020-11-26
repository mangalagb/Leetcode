# #Given an integer array nums, return the length of the longest strictly increasing subsequence.
#
# A subsequence is a sequence that can be derived from an array by deleting some or no
# elements without changing the order of the remaining elements. For example, [3,6,2,7]
# is a subsequence of the array [0,3,1,6,2,2,7].

#https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        result = 0

        for num in nums:
            if len(stack) == 0:
                stack.append(num)
            elif num > stack[-1]:
                stack.append(num)
            else:
                temp = stack.copy()
                while len(temp) > 0 and num <= temp[-1]:
                    temp.pop(-1)
                temp.append(num)

                if len(temp) >= len(stack):
                    stack = temp

            result = max(result, len(stack))
        return result


my_sol = Solution()

nums = [10,9,2,5,3,7,101,18]
print(my_sol.lengthOfLIS(nums)) #4 #[2,3,7,101]

nums = [0, 1, 0, 3, 2, 3]
print(my_sol.lengthOfLIS(nums)) #4 [0, 1, 2, 3]

nums = [7,7,7,7,7,7,7]
print(my_sol.lengthOfLIS(nums)) #1 [7]

nums = [3,5,6,2,5,4,19,5,6,7,12]
print(my_sol.lengthOfLIS(nums)) #6 [2, 4, 5, 6, 7, 12]
