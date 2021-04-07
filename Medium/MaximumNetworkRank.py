# #There is an infrastructure of n cities with some number of roads connecting
# these cities. Each roads[i] = [ai, bi] indicates that there is a
# bidirectional road between cities ai and bi.
#
# The network rank of two different cities is defined as the total
# number of directly connected roads to either city. If a road is
# directly connected to both cities, it is only counted once.
#
# The maximal network rank of the infrastructure is the maximum
# network rank of all pairs of different cities.
#
# Given the integer n and the array roads, return the maximal
# network rank of the entire infrastructure.

class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 0
        elif len(roads) == 0 or len(roads[0]) == 0:
            return 0

        adj_list = self.build_graph(n, roads)

        max_rank = 0
        for i in range(0, n):
            for j in range(i+1, n):
                rank = self.find_rank(i, j, adj_list)
                max_rank = max(max_rank, rank)
        return max_rank

    def find_rank(self, city1, city2, adj_list):
        rank1 = len(adj_list[city1])
        rank2 = len(adj_list[city2])

        total_rank = rank1 + rank2
        if city2 in adj_list[city1] or city1 in adj_list[city2]:
            total_rank -= 1

        if total_rank < 0:
            total_rank = 0
        return total_rank

    def build_graph(self, n, roads):
        adj_list = {}
        for i in range(0, n):
            adj_list[i] = []

        for road in roads:
            road1 = road[0]
            road2 = road[1]

            adj_list[road1].append(road2)
            adj_list[road2].append(road1)
        return adj_list


my_sol = Solution()

n = 4
roads = [[0,1],[0,3],[1,2],[1,3]]
print(my_sol.maximalNetworkRank(n, roads)) #4

n = 5
roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
print(my_sol.maximalNetworkRank(n, roads)) #5

n = 8
roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
print(my_sol.maximalNetworkRank(n, roads)) #5
