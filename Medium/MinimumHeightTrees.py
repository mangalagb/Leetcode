# For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then
# a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs).
# Given such a graph, write a function to find all the MHTs and return a list of their root labels.
#
# Format
# The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of
# undirected edges (each edge is a pair of labels).
#
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the
# same as [1, 0] and thus will not appear together in edges.

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = self.make_graph(n, edges)
        trees = {}

        for i in range(0, n):
            depth = self.do_BFS(i, graph)
            trees[i] = depth

        min_depth = min(trees.values())
        result = [k for k, v in trees.items() if v == min_depth]
        return result

    def make_graph(self, n, edges):
        graph = {}
        for i in range(0, n):
            graph[i] = []

        for edge in edges:
            x = edge[0]
            y = edge[1]

            graph[x].append(y)
            graph[y].append(x)

        return graph

    def do_BFS(self, current, graph):
        queue = []
        visited = [False] * len(graph)
        result = []

        # Visit root
        queue.append(current)
        depth = 0

        # visit other nodes
        while len(queue) > 0:
            node = queue.pop(0)
            result.append(node)
            visited[node] = True

            unvisited_children = self.find_unvisited_child(graph[node], visited)
            if len(unvisited_children) > 0:
                queue.extend(unvisited_children)
                depth += 1

        return depth

    def find_unvisited_child(self, children, visited):
        unvisited = []
        for child in children:
            if not visited[child]:
                unvisited.append(child)
        return unvisited


my_sol = Solution()

n = 4
edges = [[1, 0], [1, 2], [1, 3]]
print(my_sol.findMinHeightTrees(n, edges)) #[1]

n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
print(my_sol.findMinHeightTrees(n, edges)) #[3, 4]
