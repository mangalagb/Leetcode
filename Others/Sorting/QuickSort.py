#Given two arrays, write a function to compute their intersection.

class Solution(object):
    def QuickSort(self, nums, start, end):
        if start >= end:
            return

        p = self.partition(nums, start, end)
        self.QuickSort(nums, start, p-1)
        self.QuickSort(nums, p+1, end)


    def partition(self, nums, start, end):
        pivot = nums[start]

        low = start+1
        high = end

        while True:
            while low <= high and nums[low] <= pivot:
                low += 1

            while low <= high and nums[high] >= pivot:
                high -= 1

            if low <= high:
                temp = nums[low]
                nums[low] = nums[high]
                nums[high] = temp
            else:
                break

        temp = nums[start]
        nums[start] = nums[high]
        nums[high] = temp
        return high




my_sol = Solution()

nums = [4,2, 3, 1]
my_sol.QuickSort(nums, 0, len(nums) - 1)
print(nums) #[1,2,3,4]

nums = [1,2,3,4]
my_sol.QuickSort(nums, 0, len(nums) - 1)
print(nums) #[1,2,3,4]
