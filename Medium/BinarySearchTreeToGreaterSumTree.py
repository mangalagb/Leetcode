#Given the root of a Binary Search Tree (BST), convert it to a Greater
# Tree such that every key of the original BST is changed to the original
# key plus sum of all keys greater than the original key in BST.
#
# As a reminder, a binary search tree is a tree that satisfies these constraints:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Note: This question is the same as 538:
# https://leetcode.com/problems/convert-bst-to-greater-tree/

# we need to sum node.right + node.val + node.left
#This is reverse inorder

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.sum  = 0

    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return

        #Visit right first, then add root.val then visit left
        self.bstToGst(root.right)

        self.sum += root.val
        root.val = self.sum

        self.bstToGst(root.left)

        return root



    def create_tree(self):
        root = TreeNode(4)
        node1 = TreeNode(1)
        node2 = TreeNode(6)
        node3 = TreeNode(0)
        node4 = TreeNode(2)
        node5 = TreeNode(3)
        node6 = TreeNode(5)
        node7 = TreeNode(7)
        node8 = TreeNode(8)

        root.left = node1
        root.right = node2
        node1.left = node3
        node1.right = node4
        node4.right = node5

        node2.left = node6
        node2.right = node7
        node7.right = node8
        return root

    def create_tree1(self):
        root = TreeNode(0)
        node1 = TreeNode(1)
        root.right = node1
        return root

    def create_tree2(self):
        root = TreeNode(1)
        node1 = TreeNode(0)
        node2 = TreeNode(2)

        root.left = node1
        root.right = node2
        return root

    def create_tree3(self):
        root = TreeNode(3)
        node1 = TreeNode(2)
        node2 = TreeNode(4)
        node3 = TreeNode(1)

        root.left = node1
        root.right = node2
        node1.left = node3
        return root


my_sol = Solution()

# root = my_sol.create_tree()
# print(my_sol.bstToGst(root))

root = my_sol.create_tree1()
print(my_sol.bstToGst(root))
#
# root = my_sol.create_tree2()
# print(my_sol.bstToGst(root))
#
# root = my_sol.create_tree3()
# print(my_sol.bstToGst(root))
