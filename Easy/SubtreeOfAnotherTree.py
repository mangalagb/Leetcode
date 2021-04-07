# Given two non-empty binary trees s and t, check whether tree t has exactly
# the same structure and node values with a subtree of s. A subtree of s is
# a tree consists of a node in s and all of this node's descendants. The tree
# s could also be considered as a subtree of itself.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not t:
            return True
        elif not s:
            return False

        result = self.traverse_larger_tree(s, t)
        return result


    def traverse_larger_tree(self, node1, node2):
        if node1.val == node2.val:
            result = self.match_subtree(node1, node2)
            if result:
                return True

        left_result = False
        if node1.left:
            left_result = self.traverse_larger_tree(node1.left, node2)
        if left_result:
            return True

        right_result = False
        if node1.right:
            right_result = self.traverse_larger_tree(node1.right, node2)
        return right_result



    def match_subtree(self, node1, node2):
        if not node1 and not node2:
            return True

        if node1.val != node2.val:
            return False

        if (node1.left and not node2.left) or (not node1.left and node2.left):
            return False

        if (node1.right and not node2.right) or (not node1.right and node2.right):
            return False

        left_result = self.match_subtree(node1.left, node2.left)
        right_result = self.match_subtree(node1.right, node2.right)
        return left_result and right_result


    def make_tree(self):
        root1 = TreeNode(3)
        node1 = TreeNode(4)
        node2 = TreeNode(5)
        node3 = TreeNode(1)
        node4 = TreeNode(2)
        node7 = TreeNode(2)

        root1.left = node1
        root1.right = node2
        node1.left = node3
        node1.right = node4
        node4.left = node7

        root2 = TreeNode(4)
        node5 = TreeNode(1)
        node6 = TreeNode(2)

        root2.left = node5
        root2.right = node6

        return root1, root2

my_sol = Solution()

root1, root2 = my_sol.make_tree()
print(my_sol.isSubtree(root1, root2)) #False
