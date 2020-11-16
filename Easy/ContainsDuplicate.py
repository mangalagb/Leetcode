#Given an array of integers, find if the array contains any duplicates.

#Your function should return true if any value appears at least twice in the
# array, and it should return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        unique_nums = set()
        for num in nums:
            if num not in unique_nums:
                unique_nums.add(num)
            else:
                return True
        return False



my_sol = Solution()

nums = [1,2,3,1]
print(my_sol.containsDuplicate(nums)) #True