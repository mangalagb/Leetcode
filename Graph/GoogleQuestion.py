# Given an array of N unsorted real numbers, write an efficient algorithm (then code) to determine
# the number of pairs whose sum is less than or equal a given number x.
from collections import OrderedDict

class Solution(object):
    def findPairs(self, nums, target):
        if not nums:
            return

        frequency = OrderedDict()
        count = 0
        for current in nums:
            remaining = target - current

            for key, val in frequency.items():
                if key > remaining:
                    break
                count += frequency[key]

            if current in frequency:
                frequency[current] += 1
            else:
                frequency[current] = 1
            frequency = OrderedDict(sorted(frequency.items()))
        return count



my_sol = Solution()

nums = [1,2,3,6]
target = 5
print(my_sol.findPairs(nums, target))
