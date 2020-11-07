# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes),
# write a function to check whether these edges make up a valid tree.

#According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices
# are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if n == 1:
            return True

        adj_list = self.build_adjacency_list(n, edges)
        result = self.do_DFS(0, n, adj_list)


    def do_DFS(self,node, n, adj_list):
        visited = [False] * n
        stack = [node]

        while len(stack) > 0:
            top_element = stack[0]
            unvisited_neighbour = self.find_unvisited_neighbour(adj_list[top_element], visited)

            if unvisited_neighbour != -1:
                stack.insert(0, unvisited_neighbour)
            else:
                stack.pop(0)

    def find_unvisited_neighbour(self, neighbours, visited):
        for neighbour in neighbours:
            if not visited[neighbour]:
                return neighbour
        return -1




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

# n = 5
# edges = [[0,1], [0,2], [0,3], [1,4]]
# print(my_sol.validTree(n, edges)) #True
#
# n = 5
# edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# print(my_sol.validTree(n, edges)) #False

n = 2
edges = [[1,0]]
print(my_sol.validTree(n, edges)) #True
#
# n = 3
# edges = [[1,0],[2,0]]
# print(my_sol.validTree(n, edges)) #True
