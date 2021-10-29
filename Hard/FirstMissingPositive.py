# Given an unsorted integer array nums, find the smallest missing positive integer.
#
# Follow up: Could you implement an algorithm that runs in O(n)
# time and uses constant extra space.?

# The first missing +ve number in array of size 1-> n will be between 1 to n
# or n+1

# set all nums less than 1 and greater than n to 0. Mark as invalid
# Then tag the indexs as visited

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        #Set all numbers out of range to n+1
        for i in range(0, n):
            num = nums[i]
            if 1 <= num <= n:
                continue
            else:
                nums[i] = n+1

        #Mark visited indexes
        for num in nums:
            num = abs(num)
            if num > n:
                continue

            index = num - 1

            #Make sure that index is non-negative
            # We want to avoid cases where element appears 2 times and we accidently mark it as unseen
            if nums[index] > 0:
                nums[index] *= -1

        #Find first non-negative index
        #It means that this index was never visited
        #Else return n+1
        for index in range(0, n):
            value = nums[index]
            if value > 0:
                return index + 1
        return n+1




my_sol = Solution()

nums = [1,2,0]
print(my_sol.firstMissingPositive(nums)) #3

nums = [3,4,-1,1]
print(my_sol.firstMissingPositive(nums)) #2

nums = [7, 8, 9, 11, 12]
print(my_sol.firstMissingPositive(nums)) #1
