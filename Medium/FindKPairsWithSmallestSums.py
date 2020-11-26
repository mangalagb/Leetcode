# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
#
# Define a pair (u,v) which consists of one element from the first array and
# one element from the second array.
#
# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

import heapq


# def kSmallestPairs(self, nums1, nums2, k):
#     queue = []
#
#     def push(i, j):
#         if i < len(nums1) and j < len(nums2):
#             heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
#
#     push(0, 0)
#     pairs = []
#     while queue and len(pairs) < k:
#         _, i, j = heapq.heappop(queue)
#         pairs.append([nums1[i], nums2[j]])
#         push(i, j + 1)
#         if j == 0:
#             push(i + 1, 0)
#     return pairs

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        return heapq.nsmallest(k, ([u, v] for u in nums1 for v in nums2), key=sum)

my_sol = Solution()

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print(my_sol.kSmallestPairs(nums1, nums2, k)) #[[1,2],[1,4],[1,6]]

# nums1 = [1,1,2]
# nums2 = [1,2,3]
# k = 2
# print(my_sol.kSmallestPairs(nums1, nums2, k)) #[[1, 1], [1, 1]]
#
# nums1 = [1,1,2]
# nums2 = [1,2,3]
# k = 10
# print(my_sol.kSmallestPairs(nums1, nums2, k)) #[[1, 1], [1, 1]]
