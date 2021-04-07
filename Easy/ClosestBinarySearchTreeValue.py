# Given a non-empty binary search tree and a target value, find the value in
# the BST that is closest to the target.
#
# Note:
#
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.

# Definition for a binary tree node.
import sys


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return -1

        closest_node = None
        closest_val = sys.maxsize
        result = self.find_closest(root, target, closest_node, closest_val)
        return result

    def find_closest(self, node, target, closest_node, closest_val):
        if not node:
            return closest_node

        difference = abs(target - node.val)
        if difference < closest_val:
            closest_val = difference
            closest_node = node.val

        if target > node.val and node.right:
            return self.find_closest(node.right, target, closest_node, closest_val)
        elif target < node.val and node.left:
            return self.find_closest(node.left, target, closest_node, closest_val)

        return closest_node


    def make_tree(self):
        root = TreeNode(4)
        node1 = TreeNode(2)
        node2 = TreeNode(5)
        node3 = TreeNode(1)
        node4 = TreeNode(3)

        root.left = node1
        root.right = node2

        node1.left = node3
        node1.right = node4
        return root

    def make_tree1(self):
        root = TreeNode(1)
        node1 = TreeNode(2)

        root.right = node1
        return root

my_sol = Solution()

root = my_sol.make_tree()
target = 3.714286
print(my_sol.closestValue(root, target)) #4

root = my_sol.make_tree1()
target = 3.714286
print(my_sol.closestValue(root, target)) #2
