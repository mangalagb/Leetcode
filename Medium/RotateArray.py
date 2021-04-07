# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
# Follow up:
#
# Try to come up as many solutions as you can, there are at least 3 different ways
# to solve this problem.
# Could you do it in-place with O(1) extra space?

#This approach is based on the fact that when we rotate the array k times,
# k%nk elements from the back end of the array come to the front and the rest
# of the elements from the front shift backwards.

# In this approach, we firstly reverse all the elements of the array.
# Then, reversing the first k elements followed by reversing the rest n-kn−k
# elements gives us the required result.
#
# Let n = 7 and k = 3
#
# Original List                   : 1 2 3 4 5 6 7
# After reversing all numbers     : 7 6 5 4 3 2 1
# After reversing first k numbers : 5 6 7 4 3 2 1
# After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        if k > len(nums):
            times_to_reverse = k % len(nums)
            for i in range(0, times_to_reverse):
                nums = self.rotate_array_by_1(nums)
            return


        #Reverse the entire array
        nums.reverse()

        #Reverse the first k elements
        i = 0
        j = k - 1
        while i < j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1

        #Reverse the remaining array
        i = k
        j = len(nums) - 1
        while i < j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1
        #print(nums)

    def rotate_array_by_1(self, nums):
        length_of_nums = len(nums)
        last_num = nums[length_of_nums-1]

        previous = None
        for i in range(0, length_of_nums):
            if previous is None:
                previous = nums[i]
                nums[i] = last_num
            else:
                temp = nums[i]
                nums[i] = previous
                previous = temp
        return nums


my_sol = Solution()

# nums = [1,2,3,4,5,6,7]
# k = 3
# my_sol.rotate(nums, k) #[5,6,7,1,2,3,4]
#
# nums = [-1,-100,3,99]
# k = 2
# my_sol.rotate(nums, k) #[3,99,-1,-100]
#
# nums = [2147483647,-2147483648,33,219,0]
# k = 4
# my_sol.rotate(nums, k) #[-2147483648, 33, 219, 0, 2147483647]
#
nums = [-1]
k = 2
my_sol.rotate(nums, k) #[-1]

nums = [1,2]
k = 3
my_sol.rotate(nums, k) #[2, 1]

