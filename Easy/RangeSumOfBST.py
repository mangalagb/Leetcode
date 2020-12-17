# Given the root node of a binary search tree, return the sum of values
# of all nodes with a value in the range [low, high].

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0

        self.total_sum = 0
        self.find_sum(root, low, high)
        return self.total_sum

    def find_sum(self, node, low, high):
        if not node:
            return

        if low <= node.val <= high:
            self.total_sum += node.val

        if low < node.val:
            self.find_sum(node.left, low, high)
        if high > node.val:
            self.find_sum(node.right, low, high)


    def make_tree(self):
        root = TreeNode(10)
        node1 = TreeNode(5)
        node2 = TreeNode(15)
        node3 = TreeNode(3)
        node4 = TreeNode(7)
        node5 = TreeNode(18)

        root.left = node1
        root.right = node2

        node1.left = node3
        node1.right = node4
        node2.right = node5
        return root

    def make_tree1(self):
        root = TreeNode(10)
        node1 = TreeNode(5)
        node2 = TreeNode(15)
        node3 = TreeNode(3)
        node4 = TreeNode(7)
        node5 = TreeNode(18)
        node6 = TreeNode(13)
        node7 = TreeNode(1)
        node8 = TreeNode(6)

        root.left = node1
        root.right = node2

        node1.left = node3
        node1.right = node4
        node3.left = node7
        node4.left = node8
        node2.left = node6
        node2.right = node5

        return root



my_sol = Solution()
#
# low = 7
# high = 15
# root = my_sol.make_tree()
# print(my_sol.rangeSumBST(root, low, high)) #32

low = 6
high = 10
root = my_sol.make_tree1()
print(my_sol.rangeSumBST(root, low, high)) #23

