# Return the root node of a binary search tree that matches the given preorder traversal.
#
# (Recall that a binary search tree is a binary tree where for every node, any descendant
# of node.left has a value < node.val, and any descendant of node.right has a value > node.val.
# Also recall that a preorder traversal displays the value of the node first, then
# traverses node.left, then traverses node.right.)
#
# It's guaranteed that for the given test cases there is always possible to find a
# binary search tree with the given requirements.

# SOLUTION
# First item in preorder list is the root to be considered.
# For next item in preorder list, there are 2 cases to consider:
# If value is less than last item in stack, it is the left child of last item.
# If value is greater than last item in stack, pop it.
# The last popped item will be the parent and the item will be the right child of the parent.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root = self.make_tree(preorder[0], preorder)
        return root

    def make_tree(self, value, preorder):
        if len(preorder) == 0:
            return
        elif len(preorder) == 1:
            return TreeNode(preorder[0])

        i = 1
        while i < len(preorder):
            if preorder[i] > value:
                break
            i += 1

        left = preorder[1:i]
        right = preorder[i:]

        node = TreeNode(value)
        if left:
            node.left = self.make_tree(left[0], left)
        if right:
            node.right = self.make_tree(right[0], right)
        return node


my_sol = Solution()

nums = [8,5,1,7,10,12]
my_sol.bstFromPreorder(nums)

nums = [4,2]
my_sol.bstFromPreorder(nums)
