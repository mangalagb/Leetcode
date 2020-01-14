# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
#     The left subtree of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, numbers):
        """
        :type numbers: node values
        :rtype: bool
        """

        if not numbers:
            return False

        root = TreeNode(numbers[0])

        self.construct_BST(root, numbers[1:])

    def construct_BST(self, root, numbers):
        print("yo")



        return True

my_sol = Solution()

n1 = [2,1,3]
print(my_sol.isValidBST(n1))
