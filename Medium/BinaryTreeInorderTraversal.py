# Given a binary tree, return the inorder traversal of its nodes' values.
# Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return

        stack = []
        result = []
        current = root
        while current or len(stack) > 0:

            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result


    def make_tree(self):
        root = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)

        root.right = node2
        node2.left = node3
        return root

my_sol = Solution()

root = my_sol.make_tree()
print(my_sol.inorderTraversal(root))