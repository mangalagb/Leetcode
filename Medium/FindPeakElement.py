# A peak element is an element that is greater than its neighbors.
#
# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak
# element and return its index.
#
# The array may contain multiple peaks, in that case return the index
# to any one of the peaks is fine.
#
# You may imagine that nums[-1] = nums[n] = -∞.

class Solution(object):
    def findPeakElement(self, nums):

        length = len(nums)
        if length == 0:
            return -1
        elif length == 1:
            return 0

        i = 0
        #special case for first element
        if i+1 < length and nums[i] > nums[i+1]:
            return i

        # special case for last element
        j = length - 1
        if j-1 >= 0 and nums[j] > nums[j-1]:
            return j

        # increasing stack
        stack = [nums[0]]
        i = 1
        while i < length:
            current = nums[i]
            next_elem = None
            if i+1 < length:
                next_elem = nums[i+1]

            if current > stack[-1]:
                stack.append(current)

                if next_elem and current > next_elem:
                    return i
            i += 1
        return -1


my_sol = Solution()

nums = [2,1]
print(my_sol.findPeakElement(nums)) # 0

nums = [1,2,1,3,5,6,4]
print(my_sol.findPeakElement(nums)) # 1 or 5

nums = [1,2,3,1]
print(my_sol.findPeakElement(nums)) #2

nums = [1,2,1]
print(my_sol.findPeakElement(nums)) #1

nums = [3,2,1]
print(my_sol.findPeakElement(nums)) #0

nums = [3,4,3,2,1]
print(my_sol.findPeakElement(nums)) #1

nums = [5,4,3,2,1]
print(my_sol.findPeakElement(nums)) #0

nums = [3]
print(my_sol.findPeakElement(nums)) #0