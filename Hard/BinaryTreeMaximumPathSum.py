# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any node sequence from some
# starting node to any node in the tree along the parent-child connections.
# The path must contain at least one node and does not need to go through the root.

import sys

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.max_sum = -1 * sys.maxsize
        self.find_max(root)
        return self.max_sum


    def find_max(self, node):
        if not node:
            return 0

        left = self.find_max(node.left)
        right = self.find_max(node.right)

        #Do not include left sub tree
        if left < 0:
            left = 0

        # Do not include right sub tree
        #Include only current value
        if right < 0:
            right = 0

        include_sub_tree = node.val + left + right
        if include_sub_tree > self.max_sum:
            self.max_sum = include_sub_tree
        return node.val + max(left, right)

    def make_tree1(self):
        root = TreeNode(2)
        node1 = TreeNode(-1)

        root.left = node1
        return root

    def make_tree(self):
        root = TreeNode(-10)
        node1 = TreeNode(9)
        node2 = TreeNode(20)
        node3 = TreeNode(15)
        node4 = TreeNode(7)

        root.left = node1
        root.right = node2

        node2.left = node3
        node2.right = node4
        return root

my_sol = Solution()

root = my_sol.make_tree()
print(my_sol.maxPathSum(root)) #42

root = TreeNode(-3)
print(my_sol.maxPathSum(root)) #-3

root = my_sol.make_tree1()
print(my_sol.maxPathSum(root)) #2
