# Given an array of integers of size ‘n’.
# Our aim is to calculate the maximum sum possible for ‘k’
# consecutive elements in the array.


def find_sum(nums):
    sum = 0

    for i in range(0,k):
        sum += nums[i]

    max_sum = sum

    for i in range(k, len(nums)):
        sum += nums[i]
        sum -= nums[i-k]
        if sum > max_sum:
            max_sum = sum
    print(max_sum)




nums = [100, 200, 300, 400]
k = 2
find_sum(nums)
#Output : 700
