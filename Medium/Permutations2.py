#Given a collection of numbers, nums, that might contain duplicates,
# return all possible unique permutations in any order.

#The set of the sub arrays is the binary representation of the the nth value ranging from 0 to 2n - 1.

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length_of_nums = len(nums)
        number = (2 ** length_of_nums) - 1
        result = []


        while True:
            binary = bin(number).replace("0b", "")

            if len(binary) < length_of_nums:
                break





my_sol = Solution()

#2 ^3 = 8 subarrays
nums = [1,1,2]
print(my_sol.permuteUnique(nums))