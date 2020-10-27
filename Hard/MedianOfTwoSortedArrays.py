# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.

from heapq import *

class Solution(object):
    # Left heap is max heap.
    # Right heap is min heap
    # Right heap can contain n+1 elements. Left heap must contain n elements.
    # 1) Insert new element to right by default. Since we have inserted to right, we now pop one
    #   from right and give it to left
    # 2) But now, left may conatin more than n elements. If so, pop from left and push to right
    # 3) if len(left) == len(right), median = Left[last] + Right[0] /2
    #    else, median = Large[0]

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Empty heaps
        left, right = [], []

        for element in nums1:
            self.insert_to_heap(element, left, right)

        for element in nums2:
            self.insert_to_heap(element, left, right)

        median = self.find_median(left, right)
        return median


    def find_median(self, left, right):
        median = 0
        if len(right) > len(left):
            median = right[0]
        else:
            left_element = -1 * left[0]
            right_element = right[0]
            median = (right_element + left_element) / 2
        return median


    def insert_to_heap(self, num, left, right):

        #Add to right and pop one to give to left
        popped_element = heappushpop(right, num)

        #Left heap is max heap
        popped_element = -1 * popped_element

        #Insert to leaf heap
        heappush(left, popped_element)

        #Check size of 2 heaps
        if len(left) > len(right):
            popped_element_for_right = heappop(left)

            #Remove the - sign
            popped_element_for_right = -1 * popped_element_for_right

            #Push to right
            heappush(right, popped_element_for_right)


my_sol = Solution()

nums1 = [1, 10]
nums2 = [5, 40]
print(my_sol.findMedianSortedArrays(nums1, nums2)) # 7.5

nums1 = [1,2]
nums2 = [3,4]
print(my_sol.findMedianSortedArrays(nums1, nums2)) # 2.5

nums1 = [0,0]
nums2 = [0,0]
print(my_sol.findMedianSortedArrays(nums1, nums2)) # 0.0

nums1 = []
nums2 = [1]
print(my_sol.findMedianSortedArrays(nums1, nums2)) # 1.0

nums1 = [2]
nums2 = []
print(my_sol.findMedianSortedArrays(nums1, nums2)) # 2.0
