#Given an array of integers and an integer k, you need to find the
# total number of continuous subarrays whose sum equals to k.

#The idea behind this approach is as follows: If the cumulative sum(represented by sum[i]sum[i] for sum up to i^{th}i th
#index) up to two indices is the same, the sum of the elements
# lying in between those indices is zero. Extending the same
# thought further, if the cumulative sum up to two indices, say
# ii and jj is at a difference of kk i.e. if sum[i] - sum[j] = ksum[i]−sum[j]=k,
# the sum of elements lying between indices ii and jj is kk.

#https://leetcode.com/problems/subarray-sum-equals-k/solution/

from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
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
print(my_sol.subarraySum(nums, k)) #55


nums = [1,1,1]
k = 2
print(my_sol.subarraySum(nums, k)) #2

nums = [3,3,3,3]
k = 6
print(my_sol.subarraySum(nums, k)) #3

nums = [1,2,3]
k = 3
print(my_sol.subarraySum(nums, k)) #2

nums = [1]
k = 1
print(my_sol.subarraySum(nums, k)) #1

nums = [1,2, 3]
k = 10
print(my_sol.subarraySum(nums, k)) #0

nums = [-1,-1,1]
k = 0
print(my_sol.subarraySum(nums, k)) #1
