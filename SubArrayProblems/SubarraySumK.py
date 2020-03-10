#Given an array of integers and an integer k, you need to find the
# total number of continuous subarrays whose sum equals to k.

#Observe that we actually only care about results of sub sum instead of value of individual elements.
# input =[1,2,3] k=5
# input =[1,1,1,3] k=5
# input =[1,-1,1,2,3] k=5
#
# While we iterate though array and encounter value 3, all these examples will achieve sub sum=5=k.
# Thus for value 3, it only need previous sum of 2 no matter what it composed. Ex: [2], [1,1], [-1,1,2]

# We record required_sum as key and value will be the count of number of times the sum has appeared

# So, if currentSum - k is in the recorded array, at this point, subarray sum = k

from collections import defaultdict

class Solution(object):
    def subarraySum1(self, nums, k):
        if not nums:
            return

        current_sum = 0
        result = 0
        frequencies = defaultdict(int)
        frequencies[0] = 1

        for i in range(0, len(nums)):
            current_sum += nums[i]
            required_sum = current_sum - k

            # required + current = k
            # key = required_sum
            # value = num of times this sum has appeared
            if required_sum in frequencies:
                count_of_required_sum = frequencies[required_sum]
                result += count_of_required_sum

            # The current sum now becomes required sum
            frequencies[current_sum] += 1
        return result


my_sol = Solution()

nums = [0,0,0,0,0,0,0,0,0,0]
k = 0
print(my_sol.subarraySum1(nums, k)) #55

#
# nums = [1,1,1]
# k = 2
# print(my_sol.subarraySum(nums, k)) #2
#
# nums = [3,3,3,3]
# k = 6
# print(my_sol.subarraySum(nums, k)) #3

# nums = [1,2,3]
# k = 3
# print(my_sol.subarraySum(nums, k)) #2
#
# nums = [1]
# k = 1
# print(my_sol.subarraySum(nums, k)) #1
#
# nums = [1,2, 3]
# k = 10
# print(my_sol.subarraySum(nums, k)) #0
#
# nums = [-1,-1,1]
# k = 0
# print(my_sol.subarraySum(nums, k)) #1
