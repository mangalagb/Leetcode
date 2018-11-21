
def findMin(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return nums[0]
        return search(nums, 0, len(nums)-1)


def search(nums, low, high):
    mid = low + (high-low)//2
    direction = None
    pivot_element = None

    if nums[low] > nums[mid] and nums[mid] < nums[high]:
        direction = "left"
    elif nums[high] < nums[mid] and nums[low] < nums[mid]:
        direction = "right"

    if direction is "left":
        high = mid
        return search(nums, low, high)
    elif direction is "right":
        low = mid
        return search(nums, low, high)
    else:
        if nums[low] < nums[high]:
            pivot_element = nums[low]
        else:
            pivot_element = nums[high]
        return pivot_element


nums = [4,5,6,7,0,1,2]
print(findMin(nums))
