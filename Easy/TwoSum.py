#Given an array of integers, return indices of the two numbers such that
# they add up to a specific target.
#You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

def quicksort(nums, low, high):
    i = low
    j = high

    pivot_element = nums[low + (high-low)//2]

    while i <= j:
        while nums[i] < pivot_element:
            i += 1

        while nums[j] > pivot_element:
            j -= 1

        if i <= j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1

    if i <= high:
        quicksort(nums, i, high)
    if low <= j:
        quicksort(nums, low, j)


def two_sums_brute_force(nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return [-1]


def two_sums(nums, target):
    nums_dict = {}

    for index in range(0, len(nums)):
        num = nums[index]
        complement = target - num

        if num in nums_dict.keys():
            return [nums_dict[num], index]
        else:
            nums_dict[complement] = index
    return [-1]


#nums = [8, 2, 9, 18, -6, -16, 102]
nums = [2, 7, 11, 15]
print(two_sums(nums, 22))
#print(two_sums(nums, -14))