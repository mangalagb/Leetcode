# We are given a binary tree (with root node root), a target node, and an integer value K.
#
# Return a list of the values of all nodes that have a distance K from the target node.
# The answer can be returned in any order.

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        if not root:
            return

        #Create a graph
        graph = {root.val: []}
        self.make_graph(root, graph)

        if K > len(graph):
            return []

        queue = []
        visited = [False] * len(graph)
        visited[target.val] = True

        target_children = graph[target.val]
        if K == 0:
            return [target.val]
        elif K == 1:
            return target_children
        else:
            queue.extend(target_children)

        result = []
        for node in queue:
            local_result = self.visit_node(node, graph, visited, 1, K)
            result.extend(local_result)
        return result

    def visit_node(self, current, graph, visited, counter, K):
        if counter == K:
            return [current]
        elif counter > K:
            return None

        children = graph[current]
        result = []
        visited[current] = True
        for child in children:
            if not visited[child]:
                ans = self.visit_node(child, graph, visited, counter+1, K)
                if ans:
                    result.extend(ans)
        return result


    def make_graph(self, current, nodes):
        if current.left:
            nodes[current.left.val] = [current.val]
            nodes[current.val].append(current.left.val)
            self.make_graph(current.left, nodes)

        if current.right:
            nodes[current.right.val] = [current.val]
            nodes[current.val].append(current.right.val)
            self.make_graph(current.right, nodes)

        return nodes


    def make_tree(self):
        root = TreeNode(3)
        node1 = TreeNode(5)
        node2 = TreeNode(1)
        node3 = TreeNode(6)
        node4 = TreeNode(2)
        node5 = TreeNode(0)
        node6 = TreeNode(8)
        node7 = TreeNode(7)
        node8 = TreeNode(4)

        root.left = node1
        root.right = node2
        node1.left = node3
        node1.right = node4
        node2.left = node5
        node2.right = node6
        node4.left = node7
        node4.right = node8
        return root

    def make_tree1(self):
        root = TreeNode(0)
        node1 = TreeNode(2)
        node2 = TreeNode(1)
        node3 = TreeNode(3)

        root.left = node1
        root.right = node2
        node2.left = node3
        return root


my_sol = Solution()

#root = my_sol.make_tree()
# target = TreeNode(5)
# K = 2
# print(my_sol.distanceK(root, target, K))

root = my_sol.make_tree1()
target = TreeNode(3)
K = 3
print(my_sol.distanceK(root, target, K))
