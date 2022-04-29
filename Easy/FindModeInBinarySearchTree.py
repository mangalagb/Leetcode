#Given the root of a binary search tree (BST) with duplicates, return all the mode(s)
# (i.e., the most frequently occurred element) in it.

# If the tree has more than one mode, return them in any order.
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
#

from collections import defaultdict

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return 0
        self.key_map = defaultdict(int)
        self.do_inorder(root)

        max_count = max(self.key_map.values())
        result = [key for key, value in self.key_map.items() if value == max_count]
        return result

    def do_inorder(self, node):
        if not node:
            return

        self.key_map[node.val] += 1
        self.do_inorder(node.left)
        self.do_inorder(node.right)

    def makeTree(self):
        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(2)

        root.right = node1
        node1.left = node2
        return root

my_sol = Solution()

root = my_sol.makeTree()
print(my_sol.findMode(root)) #[2]

root1 = TreeNode(0)
print(my_sol.findMode(root1)) #[0]
