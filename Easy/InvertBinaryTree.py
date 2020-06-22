# Invert a binary tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        node = self.swap_tree(root)
        return node

    def swap_tree(self, current):
        if not current:
            return

        left = self.swap_tree(current.left)
        right = self.swap_tree(current.right)
        current.left = right
        current.right = left

        return current

    def make_tree(self):
        root = TreeNode(4)
        node2 = TreeNode(2)
        node3 = TreeNode(7)
        node4 = TreeNode(1)
        node5 = TreeNode(3)
        node6 = TreeNode(6)
        node7 = TreeNode(9)

        root.left = node2
        root.right = node3

        node2.left = node4
        node2.right = node5
        node3.left = node6
        node3.right = node7
        return root

my_sol = Solution()
root = my_sol.make_tree()
print(my_sol.invertTree(root))
