# Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most
# twice and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array
# in-place with O(1) extra memory.
#
# It doesn't matter what you leave beyond the returned length.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length_of_array = len(nums)
        if length_of_array == 0 or length_of_array == 1:
            return length_of_array

        counter = 1
        prev = nums[0]
        position = 1

        for i in range(1, length_of_array):
            current = nums[i]
            if current == prev:
                if counter < 2:
                    counter += 1
                    nums[position] = current
                    position += 1
                elif counter == 2:
                    counter += 1
            else:
                nums[position] = current
                prev = current
                counter = 1
                position += 1
        return position


my_sol = Solution()

nums = [1,1,1,2,2,2,3,3]
print(my_sol.removeDuplicates(nums)) #6     #1,1,2,2,3,3
print(nums)

nums = [1,1,1,2,2,3]
print(my_sol.removeDuplicates(nums)) #5     #1, 1, 2, 2, 3
print(nums)

nums = [0,0,1,1,1,1,2,3,3]
print(my_sol.removeDuplicates(nums))  #7    # 0, 0, 1, 1, 2, 3, 3
print(nums)

nums = [1,2,3,4]
print(my_sol.removeDuplicates(nums))  #4    # 1,2,3,4
print(nums)
