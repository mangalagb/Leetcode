# Given a binary tree, find the length of the longest path where each node in the
# path has the same value.
# This path may or may not pass through the root.
#
# The length of path between two nodes is represented by the number of edges between them.

#SOLUTION
#at the end of each recursive loop, return the longest length using that node as the root so that
# the node's parent can potentially use it in its longest path computation.
#We also use an external variable longest that keeps track of the longest path seen so far.

#Similar to diameter of binary tree


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 0
        self.traverse_node(root, None)
        return self.longest


    def traverse_node(self, node, parent):
        if not node:
            return 0

        left = self.traverse_node(node.left, node.val)
        right = self.traverse_node(node.right, node.val)

        self.longest = max((left+right), self.longest)

        max_at_current = 0
        if node.val == parent:
            max_at_current = max(left, right) + 1
        return max_at_current


    def make_tree(self):
        root = TreeNode(5)
        node2 = TreeNode(5)
        node3 = TreeNode(5)
        node4 = TreeNode(4)
        node5 = TreeNode(1)
        node6 = TreeNode(1)

        root.right = node2
        root.left = node4
        node2.right = node3

        node4.left = node5
        node4.right = node6
        return root

    def make_tree2(self):
        root = TreeNode(1)
        node2 = TreeNode(1)
        node3 = TreeNode(1)
        node4 = TreeNode(1)
        node5 = TreeNode(1)
        node6 = TreeNode(1)
        node7 = TreeNode(1)

        root.right = node2
        node2.left = node3
        node2.right = node4

        node3.left = node5
        node3.right = node6
        node4.right = node7

        return root

    def make_tree1(self):
        root = TreeNode(1)
        node2 = TreeNode(4)
        node3 = TreeNode(5)
        node4 = TreeNode(5)
        node6 = TreeNode(4)
        node7 = TreeNode(4)

        root.right = node3
        root.left = node2

        node3.right = node4
        node2.left = node6
        node2.right = node7
        return root

my_sol = Solution()

root = my_sol.make_tree()
print(my_sol.longestUnivaluePath(root)) #2

root = my_sol.make_tree1()
print(my_sol.longestUnivaluePath(root)) #2

root = my_sol.make_tree2()
print(my_sol.longestUnivaluePath(root)) #4
