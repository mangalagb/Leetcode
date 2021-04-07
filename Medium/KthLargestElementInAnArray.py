# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return -1
        elif k > len(nums):
            return -1

        max_nums = [-1*x for x in nums]

        #Construct heap
        heapq.heapify(max_nums)

        result = None
        for i in range(0, k):
            result = heapq.heappop(max_nums)
        return result * -1


my_sol = Solution()

nums = [3,2,1,5,6,4]
k = 2
print(my_sol.findKthLargest(nums, k)) #5

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(my_sol.findKthLargest(nums, k)) #4
