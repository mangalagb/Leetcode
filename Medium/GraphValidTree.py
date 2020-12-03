# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes),
# write a function to check whether these edges make up a valid tree.

#According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices
# are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”

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

        result = self.do_BFS(root, graph, parent_dict)
        return result


    def do_BFS(self, node, graph, parent_dict):
        queue = [node]

        # Visit root
        visited = [False] * len(graph)

        while len(queue) > 0:
            element = queue.pop(0)
            visited[element] = True

            neighbours = graph[element]
            for neighbour in neighbours:
                if neighbour == parent_dict[element]:
                    continue

                if visited[neighbour]:
                    return False
                else:
                    queue.append(neighbour)
                    parent_dict[neighbour] = element

        for value in visited:
            if not value:
                return False
        return True


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

n = 5
edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
print(my_sol.validTree(n, edges)) #False

n = 2
edges = [[1,0]]
print(my_sol.validTree(n, edges)) #True

n = 3
edges = [[1,0],[2,0]]
print(my_sol.validTree(n, edges)) #True
