# Given a reference of a node in a connected undirected graph.
#
# Return a deep copy (clone) of the graph.
#
# Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.


# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        result = self.visit(node, {})
        return result

    def visit(self, node, visited):
        #If already prsent, return cloned node
        if node in visited:
            return visited[node]

        new_node = Node(node.val)
        visited[node] = new_node

        for neighbour in node.neighbors:
            cloned_neighbour_node = self.visit(neighbour, visited)
            new_node.neighbors.append(cloned_neighbour_node)
        return new_node



    def make_input_graph(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)

        node1.neighbors = [node2, node4]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node2, node4]
        node4.neighbors = [node1, node3]
        return node1


my_sol = Solution()

root = my_sol.make_input_graph()
ans = my_sol.cloneGraph(root)
