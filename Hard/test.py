from heapq import *

class MedianFinder:
    def __init__(self):
        self.left_heap = []
        self.right_heap = []

    def addNum(self, num):

        #But we cannot just push the item into right.
        #First push into left. Then pop the root of left
        #The push that into large
        heappush(self.left_heap, -num)
        element = heappop(self.left_heap)
        heappush(self.right_heap, element)

        length_of_left_heap = len(self.left_heap)
        length_of_right_heap = len(self.right_heap)



        #Pop element from top of min heap and put it on the left
        #after negating it. Since python does not have a max heap, we
        # negate the number ie, -10 > -3 in a min heap.
        if length_of_right_heap > length_of_left_heap:
            element = heappop(self.right_heap)
            element = -1 * element
            heappush(self.left_heap, element)

    def findMedian(self):
        length_of_max_heap = len(self.left_heap)
        length_of_min_heap = len(self.right_heap)
        median = None

        if length_of_max_heap == length_of_min_heap:
            element1 = self.right_heap[0]
            element2 = self.left_heap[0] * -1
            median = (element1 + element2) / 2.0
        else:
            median = float(self.right_heap[0])
        return median

median_finder = MedianFinder()
# median_finder.addNum(1)
# median_finder.addNum(2)
# print(median_finder.findMedian())
# median_finder.addNum(3)
# print(median_finder.findMedian())
# print("\n________________________")
#
# median_finder.addNum(2)
# median_finder.addNum(3)
# median_finder.addNum(4)
# print(median_finder.findMedian())
# print("\n________________________")

# median_finder.addNum(2)
# median_finder.addNum(3)
# print(median_finder.findMedian())
# print("\n________________________")

#[[],[-1],[],[-2],[],[-3],[],[-4],[],[-5],[]]
median_finder.addNum(-1)
print(median_finder.findMedian())

median_finder.addNum(-2)
print(median_finder.findMedian())

median_finder.addNum(-3)
print(median_finder.findMedian())

# median_finder.addNum(4)
# print(median_finder.findMedian())
print("\n________________________")


