# Given a binary tree, you need to compute the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two
# nodes in a tree. This path may or may not pass through the root.

# To this point, we are clear about one thing. To find the diameter of a tree, we need to process
# the left and right sub-tree first. This implies that using a post-order traversal may be
# helpful here. It makes sure that we traverse the left and right sub-tree before moving to the root.
#
# Here is an image showing maximum depth of each of the nodes in the tree. The diameter
# of the tree is the maximum value of (left_depth + right_depth) among each of the nodes.

# https://studyalgorithms.com/tree/diameter-of-a-binary-tree/
import sys


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.diameter = -1 * sys.maxsize
        self.find_diameter(root)
        return self.diameter

    def find_diameter(self, node):
        if not node:
            return 0

        left = self.find_diameter(node.left)
        right = self.find_diameter(node.right)

        self.diameter = max(self.diameter, left+right)

        max_current = max(left, right) + 1
        return max_current


    def make_tree(self):
        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(3)
        node3 = TreeNode(4)
        node4 = TreeNode(5)

        root.left = node1
        root.right = node2

        node1.left = node3
        node1.right = node4
        return root

my_sol = Solution()

root = my_sol.make_tree()
print(my_sol.diameterOfBinaryTree(root)) #3
