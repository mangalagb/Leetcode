# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
#
# Define a pair (u,v) which consists of one element from the first array and
# one element from the second array.
#
# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

# First, we take the first k elements of nums1 and paired with nums2[0] as the
# starting pairs so that we have (0,0), (1,0), (2,0),.....(k-1,0) in the heap.

#Each time after we pick the pair with min sum, we put the new pair
# with the second index +1. ie, pick (0,0), we put back (0,1). Therefore,
# the heap alway maintains at most min(k, len(nums1)) elements.

import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []

        my_heap = []
        pairs = []

        #Push first k elements of nums1 and only first element of nums2
        #heap now has k elements or all valid numbers from nums1
        temp = 0
        i = 0
        while i < len(nums1) and temp < k:
            num = nums1[i] + nums2[0]
            heapq.heappush(my_heap, [num, temp, i, 0])
            i += 1
            temp += 1

        #start popping
        count = 0
        while len(my_heap) > 0 and count < k:
            element = heapq.heappop(my_heap)
            i = element[2]
            j = element[3]

            pairs.append([nums1[i], nums2[j]])
            count += 1

            if j+1 < len(nums2):
                num = nums1[i] + nums2[j+1]
                heapq.heappush(my_heap, [num, temp, i, j+1])
                temp += 1

        return pairs


my_sol = Solution()

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print(my_sol.kSmallestPairs(nums1, nums2, k)) #[[1,2],[1,4],[1,6]]

nums1 = [1,1,2]
nums2 = [1,2,3]
k = 2
print(my_sol.kSmallestPairs(nums1, nums2, k)) #[[1, 1], [1, 1]]

nums1 = [1,1,2]
nums2 = [1,2,3]
k = 10
print(my_sol.kSmallestPairs(nums1, nums2, k)) #[[1,1],[1,1],[2,1],[1,2],[1,2],[2,2],[1,3],[1,3],[2,3]]
