# Given a set of distinct integers, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.

#https://softwareengineering.stackexchange.com/questions/256141/find-all-possible-subarrays-of-an-array

# Lets take an array of size n. There 2n possible subarrays of this array. Lets take the example array of
# size 4: [1, 2, 3, 4]. There are 24 sub arrays.

# Sub array of the empty set ([]) is the 0th one (0000). The subarray of [1], is the second one (0001),
# the subarray of [2] is the second one... (0010) and the subarray [1, 2] is the third one (0011).
# You should see where this is going.
#
# No recursion is necessary for this. The set of the sub arrays is the binary representation of the the
# nth value ranging from 0 to 2n - 1.
#
# With this realization, the generation of all of the subarrays for a given arrays should be a trivial
# matter of iterating of the integers and looking at them as bit fields for if a particular element
# is in the subarray or not.
#
# See also Number of k combinations for all k on Wikipedia.

#I would point out that this is probably the right way to do it in C and similar languages.
# Trying to force recursion, lists, and backtracking onto what would otherwise be a simple iterative problem
# with a clear and understandable answer may not the best approach.

#Note that other proposed answers to this quickly become functional programming examples and
# solutions. Functional programming is great. However, in a language not suited for such trying to
# force this paradigm of programming on it would be akin to writing C code in Lisp - it might not be
# the best way to approach the problem.

# This is a well known problem known as the subset sum problem and has a number of approaches to solve it...
# generating all the subsets of the array is not required (or even desired) for the faster approaches to solve it

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length_of_nums = len(nums)
        number_of_subarrays = 2 ** length_of_nums

        result = []
        for i in range(0, number_of_subarrays):
            binary_num = bin(i)[2:].zfill(length_of_nums)
            ans = [nums[j] for j in range(length_of_nums-1, -1, -1) if binary_num[j] == "1"]
            result.append(ans)

        return result

my_sol = Solution()

nums = [1,2,3]
print(my_sol.subsets(nums))
