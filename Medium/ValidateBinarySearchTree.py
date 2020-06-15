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
    def isValidBST(self, root):
        """
        :type numbers: node values
        :rtype: bool
        """

        stack = []
        current = root
        prev = None

        while True:
            if current is not None:
                stack.append(current)
                current = current.left

            elif stack:
                current = stack.pop()
                # print(current.val, end=" ")

                # check valid BST
                if prev and prev.val >= current.val:
                    return False
                else:
                    prev = current

                current = current.right

            else:
                break
        return True

    def make_tree(self):
        root = TreeNode(2)
        node1 = TreeNode(1)
        node2 = TreeNode(3)

        root.left = node1
        root.right = node2
        return root

my_sol = Solution()

root = my_sol.make_tree()
print(my_sol.isValidBST(root))
