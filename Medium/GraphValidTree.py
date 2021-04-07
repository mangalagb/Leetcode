# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes),
# write a function to check whether these edges make up a valid tree.

#According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices
# are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”

#https://leetcode.com/problems/graph-valid-tree/discuss/69046/Python-solution-with-detailed-explanation
#SOLUTION
# When we iterate through the neighbours of a node, we ignore
# the "parent" node as otherwise it'll be detected as a trivial cycle
# A -> B -> A(ignore B's parent A in B's neighbours)

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        graph = self.build_adjacency_list(n, edges)
        root = 0
        parent_dict = {0: -1}

        adj_list = self.build_adjacency_list(n, edges)
        visited = [False] * n

        #Check cycle
        has_cycle = self.has_cycle(0, -1, adj_list, visited)
        if has_cycle:
            return False

        #Check if all nodes were visited
        all_nodes_visited = True
        for value in visited:
            if not value:
                all_nodes_visited = False
                break
        return all_nodes_visited

    def has_cycle(self, current, parent, adj_list, visited):
        visited[current] = True

        neighbours = adj_list[current]
        for neighbour in neighbours:
            if not visited[neighbour]:
                result = self.has_cycle(neighbour, current, adj_list, visited)
                if result:
                    return True
            else:
                if visited[neighbour] and parent != current:
                    return True
        return False


    def build_adjacency_list(self, n, edges):
        adj = {}
        for i in range(0, n):
            adj[i] = []

        for edge in edges:
            i = edge[0]
            j = edge[1]

            adj[i].append(j)
            adj[j].append(i)
        return adj



my_sol = Solution()

n = 5
edges = [[0,1], [0,2], [0,3], [1,4]]
print(my_sol.validTree(n, edges)) #True
#
# n = 5
# edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# print(my_sol.validTree(n, edges)) #False
#
# n = 2
# edges = [[1,0]]
# print(my_sol.validTree(n, edges)) #True
#
# n = 3
# edges = [[1,0],[2,0]]
# print(my_sol.validTree(n, edges)) #True
