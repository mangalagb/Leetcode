# Given a binary tree, find the length of the longest path where each node in the path has the same value.
# This path may or may not pass through the root.
#
# The length of path between two nodes is represented by the number of edges between them.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        print("yo")

    def traverse_node(self, current, previous, count):
        if not previous:
            previous = current.value
        elif current.value == previous:
            count += 1

        left_count = 0
        right_count = 0






    def make_tree(self):
        # root = TreeNode(5)
        # node2 = TreeNode(5)
        # node3 = TreeNode(5)
        # node4 = TreeNode(4)
        # node5 = TreeNode(1)
        # node6 = TreeNode(1)
        #
        # root.right = node2
        # root.left = node4
        # node2.right = node3
        #
        # node4.left = node5
        # node4.right = node6

        root = TreeNode(4)
        node2 = TreeNode(4)
        node3 = TreeNode(4)


        root.right = node2
        root.left = node3
        return root

my_sol = Solution()
root = my_sol.make_tree()

print(my_sol.longestUnivaluePath(root))
