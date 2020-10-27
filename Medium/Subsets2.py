# Given a collection of integers that might contain duplicates, nums,
# return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = self.subsets(nums)
        result = []

        for subset in subsets:
            sorted_subset = sorted(subset)
            if sorted_subset not in result:
                result.append(sorted_subset)

        return result

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

# nums = [1,2,2]
# print(my_sol.subsetsWithDup(nums))

nums = [4,4,4,1,4]
print(my_sol.subsetsWithDup(nums))

