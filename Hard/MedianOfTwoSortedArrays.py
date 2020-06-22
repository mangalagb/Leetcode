# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.

import heapq
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        left = []
        right = []

        for element in nums1:
            print("yo")



my_sol = Solution()

nums1 = [1, 10]
nums2 = [5, 40]
my_sol.findMedianSortedArrays(nums1, nums2)