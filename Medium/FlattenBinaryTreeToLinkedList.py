# Given a binary tree, flatten it to a linked list in-place.
#

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.do_flatten(root)


    def do_flatten(self, node):
        if not node:
            return
        elif not node.left and not node.right:
            return node

        left_tree = node.left
        right_tree = node.right
        node.left = None
        node.right = None

        left_result = self.do_flatten(left_tree)
        right_result = self.do_flatten(right_tree)

        if left_result:
            node.right = left_result

        current = node
        while current.right:
            current = current.right
        current.right = right_result
        return node


    def make_tree(self):
        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(3)
        node3 = TreeNode(4)
        node4 = TreeNode(5)
        node5 = TreeNode(6)

        root.left = node1
        root.right = node4

        node1.left = node2
        node1.right = node3

        node4.right = node5
        return root


my_sol = Solution()
root = my_sol.make_tree()
my_sol.flatten(root)