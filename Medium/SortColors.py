# Given an array with n objects colored red, white or blue, sort them in-place so
# that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: You are not suppose to use the library's sort function for this problem.

#https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation

#This is a dutch partitioning problem. We are classifying the array into four groups:
# red, white, unclassified, and blue.
# Initially we group all elements into unclassified. We iterate from the
# beginning as long as the white pointer is less than the blue pointer.

#If the white pointer is red (nums[white] == 0), we swap with the red
# pointer and move both white and red pointer forward. If the pointer is
# white (nums[white] == 1), the element is already in correct place, so we
# don't have to swap, just move the white pointer forward. If the white
# pointer is blue, we swap with the latest unclassified element.

class Solution:
    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
        return nums

my_solution = Solution()

nums = [0, 1, 0, 1, 2]
print(my_solution.sortColors(nums)) #[0, 0, 1, 1, 2]

nums = [0,2,0,1,0,2,2,2]
print(my_solution.sortColors(nums)) #[0, 0, 0, 1, 2, 2, 2, 2]

nums = [2,0,2,1,1,0]
print(my_solution.sortColors(nums)) #[0, 0, 2, 1, 2, 2]

nums = [2, 0, 1]
print(my_solution.sortColors(nums)) #[0, 1, 2]
