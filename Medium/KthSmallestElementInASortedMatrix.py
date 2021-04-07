# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the
# kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

from heapq import *

class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        first_row = matrix[0]
        if not first_row:
            return

        #Add the first element of every row in the heap.
        #This is the smallest element in the row
        heap = []
        range_to_iterate = min(len(matrix), k)

        for i in range(range_to_iterate):
            row = matrix[i]
            num = row[0]
            element = [num, 0, row]
            heappush(heap, element)

        num_of_iterations = 0
        result = None
        while len(heap) > 0:
            popped_element = heappop(heap)
            col_num = popped_element[1]
            result = popped_element[0]
            row = popped_element[2]

            num_of_iterations += 1

            if num_of_iterations == k:
                break

            if col_num+1 < len(row):
                col_num += 1
                new_element = [row[col_num], col_num, row]
                heappush(heap, new_element)

        return result




my_sol = Solution()
matrix = [
   [1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]

#[1, 5, 9, 10, 11, 12, 13, 13, 15]
print(my_sol.kthSmallest(matrix, 5))
#
# for i in range(1,10):
#     print(my_sol.kthSmallest(matrix, i))
