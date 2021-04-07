# Given the root of a binary tree, find the maximum value V for which
# there exist different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.
#
# A node A is an ancestor of B if either: any child of A is equal to B,
# or any child of A is an ancestor of B.

# Definition for a binary tree node.
import sys


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return
        self.max_value = 0
        self.traverse_path(root, root.val, root.val)
        return self.max_value

    def traverse_path(self, node, cur_min, cur_max):
        if not node:
            return

        val1 = abs(node.val - cur_min)
        val2 = abs(node.val - cur_max)
        self.max_value = max(self.max_value, val1, val2)

        cur_min = min(cur_min, node.val)
        cur_max = max(cur_max, node.val)

        self.traverse_path(node.left, cur_min, cur_max)
        self.traverse_path(node.right, cur_min, cur_max)


    def make_tree(self):
        root = TreeNode(8)
        node1 = TreeNode(3)
        node2 = TreeNode(10)
        node3 = TreeNode(1)
        node4 = TreeNode(6)
        node5 = TreeNode(4)
        node6 = TreeNode(7)
        node7 = TreeNode(14)
        node8 = TreeNode(13)

        root.left = node1
        root.right = node2

        node1.left = node3
        node1.right = node4
        node4.left = node5
        node4.right = node6
        node2.right = node7
        node7.left = node8
        return root

    def make_tree4(self):
        #[8,null,1,5,6,2,4,0,null,7,3]
        root = TreeNode(8)
        node1 = TreeNode(1)
        node2 = TreeNode(5)
        node3 = TreeNode(6)
        node4 = TreeNode(2)
        node5 = TreeNode(4)
        node6 = TreeNode(0)
        node7 = TreeNode(7)
        node8 = TreeNode(3)

        root.right = node1

        node1.left = node2
        node1.right = node3
        node2.left = node4
        node2.right = node5
        node4.left = node7
        node4.right = node8
        node3.left = node6
        return root

    def make_tree2(self):
        root = TreeNode(8)
        node1 = TreeNode(3)
        node2 = TreeNode(10)
        node3 = TreeNode(1)
        node4 = TreeNode(6)
        node5 = TreeNode(44)
        node6 = TreeNode(7)
        node7 = TreeNode(14)
        node8 = TreeNode(13)

        root.left = node1
        root.right = node2

        node1.left = node3
        node1.right = node4
        node4.left = node5
        node4.right = node6
        node2.right = node7
        node7.left = node8
        return root

    def make_tree1(self):
        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(0)
        node3 = TreeNode(3)

        root.right = node1
        node1.right = node2
        node2.left = node3
        return root

    def make_tree3(self):
        root = TreeNode(2)
        node1 = TreeNode(0)
        node2 = TreeNode(1)

        root.right = node1
        node1.left = node2
        return root

my_sol = Solution()

root = my_sol.make_tree()
print(my_sol.maxAncestorDiff(root)) #7

root = my_sol.make_tree1()
print(my_sol.maxAncestorDiff(root)) #3

root = my_sol.make_tree2()
print(my_sol.maxAncestorDiff(root)) #41

root = my_sol.make_tree3()
print(my_sol.maxAncestorDiff(root)) #2

root = my_sol.make_tree4()
print(my_sol.maxAncestorDiff(root)) #8
