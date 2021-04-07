#Given two arrays, write a function to compute their intersection.

class Solution(object):
    def MergeSort(self, nums, low, high):
        if low >= high:
            return

        mid = (high + low) // 2
        self.MergeSort(nums, low, mid)
        self.MergeSort(nums, mid+1, high)
        self.merge(nums, low, mid, high)

    def merge(self, nums, low, mid, high):
        left_array = nums[low:mid+1]
        right_array = nums[mid+1:high+1]

        left = 0
        right = 0
        counter = low

        # Copy smaller element from left array or right array
        while left < len(left_array) and right < len(right_array):
            if left_array[left] <= right_array[right]:
                nums[counter] = left_array[left]
                left += 1
            else:
                nums[counter] = right_array[right]
                right += 1
            counter += 1

        #Copy remaining elements of left array
        while left < len(left_array):
            nums[counter] = left_array[left]
            counter += 1
            left += 1

        # Copy remaining elements of right array
        while right < len(right_array):
            nums[counter] = right_array[right]
            counter += 1
            right += 1


my_sol = Solution()

nums = [4,2, 3, 1]
my_sol.MergeSort(nums, 0, len(nums)-1)
print(nums) #[1,2,3,4]

nums = [1,2,3,4]
my_sol.MergeSort(nums, 0, len(nums)-1)
print(nums) #[1,2,3,4]
