# Given a sorted array nums, remove the duplicates in-place such that each element
# appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this
# by modifying the input array in-place with O(1) extra memory.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size_of_list = len(nums)
        if size_of_list == 0 or size_of_list == 1:
            return size_of_list

        position = 1
        prev_number = nums[0]
        for i in range(1,len(nums)):
            num = nums[i]
            if num != prev_number:
                nums[position] = num
                prev_number = num
                position += 1

        # print(nums)
        # print(position)
        return position

my_sol = Solution()
l1 = [1,1,1,2]
l2 = [0,0,1,1,1,2,2,3,3,4]
l3 = [0,0,1,1,2,2]
l4 = [1,2,3,4,5]
l5 = []
l6 = [8]

my_sol.removeDuplicates(l1)
my_sol.removeDuplicates(l2)
my_sol.removeDuplicates(l3)
my_sol.removeDuplicates(l4)
my_sol.removeDuplicates(l5)
my_sol.removeDuplicates(l6)
