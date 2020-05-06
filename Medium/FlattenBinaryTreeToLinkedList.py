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

        pre_order = self.do_preorder(root)
        current = root

        for i in range(1, len(pre_order)):
            current.left = None

            if current.right:
                current.right.val = pre_order[i]
            else:
                current.right = TreeNode(pre_order[i])
            current = current.right


    def do_preorder(self, root):
        preorder = []
        stack = []
        current = root
        while current or len(stack) > 0:
            while current:
                stack.append(current)
                preorder.append(current.val)
                current = current.left

            current = stack.pop()
            current = current.right
        return preorder


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