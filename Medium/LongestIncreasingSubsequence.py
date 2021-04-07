# #Given an integer array nums, return the length of the longest strictly increasing subsequence.
#
# A subsequence is a sequence that can be derived from an array by deleting some or no
# elements without changing the order of the remaining elements. For example, [3,6,2,7]
# is a subsequence of the array [0,3,1,6,2,2,7].

#https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/

#SOLUTION

#[1,3,5,2,8,4,6]
# For this list, we can have LIS with different length.
# For length = 1, [1], [3], [5], [2], [8], [4], [6], we pick the one with smallest tail element as
# the representation of length=1, which is [1]
# For length = 2, [1,2] [1,3] [3,5] [2,8], ...., we pick [1,2] as the representation of length=2.
# Similarly, we can derive the sequence for length=3 and length=4
# The result sequence would be:
# len=1: [1]
# len=2: [1,2]
# len=3: [1,3,4]
# len=4: [1,3,5,6]
#
# According to the logic in the post,we can conclude that:
# (1) If there comes another element, 9
# We iterate all the sequences, found 9 is even greater than the tail of len=4 sequence, we then copy len=4 sequence to be a new sequece, and append 9 to the new sequence, which is len=5: [1,3,5,6,9]
# The result is:
# len=1: [1]
# len=2: [1,2]
# len=3: [1,3,4]
# len=4: [1,3,5,6]
# len=5: [1,3,5,6,9]
#
# (2) If there comes another 3,
# We found len=3 [1,3,4], whose tailer is just greater than 3, we update the len=3 sequence tobe [1,3,3]. The result is:
# len=1: [1]
# len=2: [1,2]
# len=3: [1,3,3]
# len=4: [1,3,5,6]
#
# (3) If there comes another 0,
# 0 is smaller than the tail in len=1 sequence, so we update the len=1 sequence. The result is:
# len=1: [0]
# len=2: [1,2]
# len=3: [1,3,3]
# len=4: [1,3,5,6]

class Solution:
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i = 0
            j = size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size


my_sol = Solution()

nums = [1,3,5,2,8,4,6]
print(my_sol.lengthOfLIS(nums)) #4 #[2,3,7,101]

nums = [10,9,2,5,3,7,101,18]
print(my_sol.lengthOfLIS(nums)) #4 #[2,3,7,101]

nums = [0, 1, 0, 3, 2, 3]
print(my_sol.lengthOfLIS(nums)) #4 [0, 1, 2, 3]

nums = [7,7,7,7,7,7,7]
print(my_sol.lengthOfLIS(nums)) #1 [7]

nums = [3,5,6,2,5,4,19,5,6,7,12]
print(my_sol.lengthOfLIS(nums)) #6 [2, 4, 5, 6, 7, 12]
