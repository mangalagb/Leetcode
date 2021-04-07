# Given a list of non-negative numbers and a target integer k, write
# a function to check if the array has a continuous subarray of size at
# least 2 that sums up to a multiple of k, that is, sums up to n*k where
# n is also an integer.
import collections


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums or len(nums) < 2:
            return False

        index_dict = collections.defaultdict(int)
        # corner case: if the very first subarray with first two numbers
        # in array could form the result, we need to
        # put mod value 0 and index -1 to make it as a true case
        index_dict[0] = -1

        current_sum = 0
        k = abs(k)

        for i in range(0, len(nums)):
            current = nums[i]
            current_sum += current

            if k != 0:
                current_sum = current_sum % k

            if current_sum in index_dict:
                #subarray len must be greater than 2
                if i - index_dict[current_sum] > 1:
                    return True
            else:
                index_dict[current_sum] = i

        return False


my_sol = Solution()

nums = [0,1,0]
k = 0
print(my_sol.checkSubarraySum(nums, k)) #False

nums = [23,2,6,4,7]
k = 0
print(my_sol.checkSubarraySum(nums, k)) #False

nums = [23,2,4,6,7]
k = -6
print(my_sol.checkSubarraySum(nums, k)) #True

nums = [23, 2, 4, 6, 7]
k = 6
print(my_sol.checkSubarraySum(nums, k)) #True

nums = [23, 2, 6, 4, 7]
k=6
print(my_sol.checkSubarraySum(nums, k)) #True

nums = [10, 2, 9, 15]
k=4
print(my_sol.checkSubarraySum(nums, k)) #True

nums = [11, 2, 1, 13]
k=4
print(my_sol.checkSubarraySum(nums, k)) #True

nums = [2, 11, 2, 13]
k=4
print(my_sol.checkSubarraySum(nums, k)) #False

nums = [8]
k=4
print(my_sol.checkSubarraySum(nums, k)) #False

