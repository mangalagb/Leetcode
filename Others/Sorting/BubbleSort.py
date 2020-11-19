#Given two arrays, write a function to compute their intersection.

class Solution(object):
    def bubbleSort(self, nums):
        for i in range(0, len(nums)):
            elements_swapped = False

            # Last i elements are already in place
            for j in range(0, len(nums) - i - 1):
                if nums[j] > nums[j+1]:
                    temp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = temp
                    elements_swapped = True
            if not elements_swapped:
                break
        return nums




my_sol = Solution()

nums = [4,2, 3, 1]
print(my_sol.bubbleSort(nums)) #[1,2,3,4]

nums = [1,2,3,4]
print(my_sol.bubbleSort(nums)) #[1,2,3,4]
