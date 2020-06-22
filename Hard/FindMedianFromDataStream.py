# Median is the middle value in an ordered integer list. If the size of
# the list is even, there is no middle value. So the median is the mean
# of the two middle value.
# For example,
#
# [2,3,4], the median is 3
#
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Design a data structure that supports the following two operations:
#
#     void addNum(int num) - Add a integer number from the data stream to
# the data structure.
#     double findMedian() - Return the median of all elements so far.

# We use 2 heaps - left and right. Left contains elements that are less than the effective median.
# And right contains elements greater than the current median.
# After processing an incoming element, the number of elements in heaps differ utmost by 1 element. When both heaps contain same number of elements, we pick average of heaps root data as effective median. When the heaps are not balanced, we select effective median from the root of heap containing more elements.

from heapq import *

class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        new_item = -heappushpop(large, num)
        heappush(small, new_item)
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0


median_finder = MedianFinder()
median_finder.addNum(1)
median_finder.addNum(2)
print(median_finder.findMedian()) # 1.5

median_finder.addNum(3)
print(median_finder.findMedian()) # 2