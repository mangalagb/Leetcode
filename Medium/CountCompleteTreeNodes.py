# Given a complete binary tree, count the number of nodes.
#
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled,
# and all nodes in the last level are as far left as possible. It can have between 1 and 2h
# nodes inclusive at the last level h.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        current = root
        stack = []
        inorder = []

        while current or len(stack) != 0:
            while current:
                stack.append(current)
                current = current.left

            node = stack.pop()
            inorder.append(node.val)
            current = node.right

        return len(inorder)


    def make_tree(self):
        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(3)
        node3 = TreeNode(4)
        node4 = TreeNode(5)
        node5 = TreeNode(6)

        root.left = node1
        root.right = node2

        node1.left = node3
        node1.right = node4

        node2.left = node5
        return root


my_sol = Solution()
root = my_sol.make_tree()
my_sol.countNodes(root)
