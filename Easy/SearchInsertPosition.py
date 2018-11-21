#Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted
# in order.

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) -1

        if len(nums) == 0:
            return 0
        elif target > nums[high]:
            return len(nums)
        elif target < nums[low]:
            return 0

        while True:
            if low > high:
                return low

            mid = low + (high-low)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1



mySolution = Solution()

nums1 = [1,3,5,6]
target1 = 5
print(mySolution.searchInsert(nums1, target1))

nums1 = [1,3,5,6]
target1 = 2
print(mySolution.searchInsert(nums1, target1))

nums1 = [1,3,5,6]
target1 = 7
print(mySolution.searchInsert(nums1, target1))

nums1 = [1,3,5,6]
target1 = 0
print(mySolution.searchInsert(nums1, target1))


nums1 = [1,3]
target1 = 2
print(mySolution.searchInsert(nums1, target1))
