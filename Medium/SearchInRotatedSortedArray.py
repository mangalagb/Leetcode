# Suppose an array sorted in ascending order is rotated at some
# pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array
# return its index, otherwise return -1.

def search(nums, target):
    low = 0
    high = len(nums) -1
    mid = low + (high-low)//2
    pivot_index = find_pivot(nums, low, high)
    print(nums)

    #Call search
    result = binary_search(nums, target, pivot_index)
    return result


def find_pivot(nums, low, high):
    direction = None
    pivot_index = -1
    mid = low + (high-low) //2

    if nums[low] < nums[mid] and nums[high] < nums[mid]:
        direction = "right"
    elif nums[low] > nums[mid] and nums[high] > nums[mid]:
        direction = "left"

    if direction is "right":
        low = mid
        return find_pivot(nums, low, high)
    elif direction is "left":
        high = mid
        return find_pivot(nums, low, high)
    else:
        if nums[high] < nums[low]:
            pivot_index = high
        else:
            pivot_index = low
        return pivot_index


def binary_search(nums, target, pivot_index):
    low = 0
    high = len(nums) -1
    length = len(nums)

    while low <= high:
        mid = low + (high - low)//2
        real_mid = (mid + pivot_index) % length

        if nums[real_mid] == target:
            return real_mid

        if nums[real_mid] < target:
            low = mid + 1
        else:
            high = mid -1

    return -1






#nums = [0,1,2,4,5,6,7]
#nums = [1,2,4,5,6,7,0]
#nums = [2,4,5,6,7,0,1]
#nums = [4,5,6,7,0,1,2]
#nums = [5,6,7,0,1,2,4]
#nums = [6,7,0,1,2,4,5]
nums = [7,0,1,2,4,5,6]


target = 4
print(search(nums, target))
