# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

#The algorithm is as follows :
    # If node == null -> return 0
    # Check left subtree. If not balanced -> return -1
    # Check right subtree. If not balanced -> return -1
    # The absolute between heights of left and right subtrees. If it is greater than 1 -> return -1.
    # If the tree is balanced -> return height

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = self.find_depth(root)
        if result == -1:
            return False
        else:
            return True

    def find_depth(self, current):
        if not current:
            return 0

        ldepth = self.find_depth(current.left)
        if ldepth == -1:
            return -1

        rdepth = self.find_depth(current.right)
        if rdepth == -1:
            return -1

        height_difference = abs(ldepth - rdepth)
        if height_difference > 1:
            return -1

        return max(ldepth, rdepth) + 1

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
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(3)
        node5 = TreeNode(4)
        node6 = TreeNode(4)

        root.left = node1
        root.right = node2

        node1.left = node3
        node1.right = node4

        node3.left = node5
        node3.right = node6
        return root

my_sol = Solution()


root = my_sol.make_tree()
print(my_sol.isBalanced(root)) #True

root = my_sol.make_tree1()
print(my_sol.isBalanced(root)) #False
