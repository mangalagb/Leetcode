# Given a binary tree, return the vertical order traversal of its nodes values.
#
# For each node at position (X, Y), its left and right children respectively will
# be at positions (X-1, Y-1) and (X+1, Y-1).
#
# Running a vertical line from X = -infinity to X = +infinity, whenever the vertical
# line touches some nodes, we report the values of the nodes in order from top to
# bottom (decreasing Y coordinates).
#
# If two nodes have the same position, then the value of the node that is reported
# first is the value that is smaller.
#
# Return an list of non-empty reports in order of X coordinate.  Every report will
# have a list of values of nodes.

# Definition for a binary tree node.
import collections
import heapq

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        my_heap = []
        self.do_traversal(root, 0, 0, my_heap)
        answer = self.compute_result(my_heap)
        return answer

    def compute_result(self, my_heap):
        result = collections.OrderedDict()

        while len(my_heap) > 0:
            element = heapq.heappop(my_heap)
            x = element[0]
            y = element[1]
            value = element[2]

            if x not in result:
                result[x] = [value]
            else:
                result[x].append(value)

        answer = []
        for key, element in result.items():
            answer.append(element)
        return answer

    def do_traversal(self, node, x, y, my_heap):
        if not node:
            return

        values = [x, -y, node.val]
        heapq.heappush(my_heap, values)

        if node.left:
            self.do_traversal(node.left, x - 1, y - 1, my_heap)

        if node.right:
            self.do_traversal(node.right, x + 1, y - 1, my_heap)

    def make_tree(self):
        root = TreeNode(3)
        node1 = TreeNode(9)
        node2 = TreeNode(20)
        node3 = TreeNode(15)
        node4 = TreeNode(7)

        root.left = node1
        root.right = node2

        node2.left = node3
        node2.right = node4
        return root

    def make_tree1(self):
        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(3)
        node3 = TreeNode(4)
        node4 = TreeNode(5)
        node5 = TreeNode(6)
        node6 = TreeNode(7)

        root.left = node1
        root.right = node2

        node1.left = node3
        node1.right = node4

        node2.left = node5
        node2.right = node6
        return root

    def make_tree2(self):
        root = TreeNode(0)
        node1 = TreeNode(8)
        node2 = TreeNode(1)
        node3 = TreeNode(3)
        node4 = TreeNode(2)
        node5 = TreeNode(4)
        node6 = TreeNode(5)
        node7 = TreeNode(6)
        node8 = TreeNode(7)

        root.left = node1
        root.right = node2

        node2.left = node3
        node2.right = node4
        node3.right = node5
        node5.left = node7
        node5.right = node8
        node4.left = node6

        return root

my_sol = Solution()

root = my_sol.make_tree()
print(my_sol.verticalTraversal(root)) # [[9],[3,15],[20],[7]]

root = my_sol.make_tree1()
print(my_sol.verticalTraversal(root)) # [4],[2],[1,5,6],[3],[7]]

root = my_sol.make_tree2()
print(my_sol.verticalTraversal(root)) # [[8],[0,3,6],[1,4,5],[2,7]]

