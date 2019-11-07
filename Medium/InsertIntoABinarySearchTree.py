# Given the root node of a binary search tree (BST) and a value to be inserted into
# the tree, insert the value into the BST. Return the root node of the BST after
# the insertion. It is guaranteed that the new value does not exist in the original BST.
#
# Note that there may exist multiple valid ways for the insertion, as long as the
# tree remains a BST after insertion. You can return any of them.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        self.insert_node(root, val)
        return root

    def insert_node(self, node, val):
        if val <= node.val:
            if node.left:
                self.insert_node(node.left, val)
            else:
                node.left = TreeNode(val)
        else:
            if node.right:
                self.insert_node(node.right, val)
            else:
                node.right = TreeNode(val)

    def buildTree(self):
        root = TreeNode(4)
        node1 = TreeNode(2)
        node2 = TreeNode(7)
        node3 = TreeNode(1)
        node4 = TreeNode(3)

        root.left = node1
        root.right = node2

        node1.left = node3
        node1.right = node4
        return root

my_sol = Solution()
root = my_sol.buildTree()
my_sol.insert_node(root, 5)

