# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the
# lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

# https://leetcode.com/problems/next-permutation/discuss/13994/Readable-code-without-confusing-ij-and-with-explanation


#SOLUTION

# 2,3,6,5,4,1
#
# Solution:
# Step1, from right to left, find the first number which not increase
# in a ascending order. In this case which is 3.
# Step2, here we can have two situations:
#
# We cannot find the number, all the numbers increasing in a ascending order.
# This means this permutation is the last permutation, we need to rotate back to
# the first permutation. So we reverse the whole array, for example, 6,5,4,3,2,1
# we turn it to 1,2,3,4,5,6.
#
# We can find the number, then the next step, we will start from right most to
# leftward, try to find the first number which is larger than 3, in this case it is 4.

# Then we swap 3 and 4, the list turn to 2,4,6,5,3,1.

# Last, we reverse numbers on the right of 4, we finally get 2,4,1,3,5,6.
#
# Time complexity is: O(3*n)=O(n).


class Solution(object):
    def nextPermutation(self, nums):
        if not nums or len(nums) == 1:
            return nums

        #Find the first element from the end that is not incresing
        index = -1
        for j in range(len(nums)-2, -1, -1):
            if nums[j] >= nums[j+1]:
                continue
            else:
                index = j
                break

        if index == -1:
            self.reverse_nums(nums, 0, len(nums)-1)
            return

        #Find the largest index number (from reverse)to the right which is greater than index
        special_num = nums[index]
        counter = len(nums)-1
        for i in range(len(nums)-1, index, -1):
            current = nums[i]
            if current > special_num:
                counter = i
                break

        #swap these 2
        temp = nums[counter]
        nums[counter] = nums[index]
        nums[index] = temp

        #Sort the right part in ascending order
        self.reverse_nums(nums, index+1, len(nums)-1)

    def reverse_nums(self, nums, i, j):
        while i < j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1


my_sol = Solution()

nums = [5,1,1]
my_sol.nextPermutation(nums) #[1,1,5]
print(nums)

# nums = [4,2,0,2,3,2,0]
# my_sol.nextPermutation(nums) #[4,2,0,3,0,2,2]
# print(nums)
#
# nums = [1,2,5,3]
# my_sol.nextPermutation(nums) #[1, 3, 2, 5]
# print(nums)
#
# nums = [1,2,3]
# my_sol.nextPermutation(nums) #[1, 3, 2]
# print(nums)
#
# nums = [2,3,1]
# my_sol.nextPermutation(nums) #[3,1,2]
# print(nums)
#
# nums = [3,2,1]
# my_sol.nextPermutation(nums) #[1,2,3]
# print(nums)
# #
# nums = [1,1,5]
# my_sol.nextPermutation(nums)#[1, 5, 1]
# print(nums)
