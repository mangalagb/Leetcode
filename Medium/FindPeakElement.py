class Solution(object):
    def findPeakElement(self, nums):

        length = len(nums)
        if length == 0:
            return -1
        elif length == 1:
            return 0

        low = 0
        high = length - 1

        while low <= high:
            mid = low + (high-low)//2

            left = mid - 1
            right = mid + 1

            if 0 <= left <= length-1 and 0 <= mid <= length-1 \
                    and 0 <= right <= length-1:

                if nums[left] < nums[mid] < nums[right]:
                    peak_index = right
                    right += 1
                    while right < length:
                        if nums[right] > nums[peak_index]:
                            peak_index = right
                            right += 1
                        else:
                            break
                    return peak_index
                elif nums[left] < nums[mid] and nums[mid] > nums[right]:
                    return mid
            elif 0 <= mid <= length-1 and 0 <= right <= length-1:
                if nums[right] > nums[mid]:
                    return right
                else:
                    return mid
            elif 0 <= left <= length-1 and 0 <= mid <= length-1:
                if nums[mid] > nums[left]:
                    return mid
                else:
                    return left

            high = mid - 1


my_sol = Solution()

nums = [1,2,1,3,5,6,4]
print(my_sol.findPeakElement(nums))

nums = [1,2,3,1]
print(my_sol.findPeakElement(nums))

nums = [1,2,1]
print(my_sol.findPeakElement(nums))

nums = [3,2,1]
print(my_sol.findPeakElement(nums))

nums = [3,4,3,2,1]
print(my_sol.findPeakElement(nums))

nums = [5,4,3,2,1]
print(my_sol.findPeakElement(nums))

nums = [3]
print(my_sol.findPeakElement(nums))