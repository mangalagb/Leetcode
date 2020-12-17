import heapq
from math import sqrt


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        my_heap = []
        heap_size = 0

        for point in points:
            current_distance = self.find_euclidian_distance(point)

            if heap_size < K:
                heapq.heappush(my_heap, [-current_distance, point])
                heap_size += 1
            else:
                max_in_heap = heapq.heappop(my_heap)
                max_distance = -max_in_heap[0]

                if current_distance > max_distance:
                    heapq.heappush(my_heap, max_in_heap)
                else:
                    heapq.heappush(my_heap, [-current_distance, point])

        #Find k minimum
        result = []
        while len(my_heap) > 0:
            max_in_heap = heapq.heappop(my_heap)
            result.append(max_in_heap[1])
        return result


    def find_euclidian_distance(self, point):
        x_coordiante = point[0]
        y_coordiante = point[1]

        dist = pow(x_coordiante,2) + pow(y_coordiante, 2)
        result = sqrt(dist)
        return result


my_sol = Solution()

points = [[1,3],[-2,2]]
K = 1
print(my_sol.kClosest(points, K)) # [[-2,2]]

points = [[3,3],[5,-1],[-2,4]]
K = 2
print(my_sol.kClosest(points, K)) # [[3,3],[-2,4]]
