# Given the root of a binary tree, return the number of uni-value subtrees.
#
# A uni-value subtree means all nodes of the subtree have the same value.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.count = 0
        self.count_subtree(root)
        return self.count

    def count_subtree(self, node):
        if not node.left and not node.right:
            self.count += 1
            return True

        left_result = False
        if node.left:
            left_result = self.count_subtree(node.left)

        right_result = False
        if node.right:
            right_result = self.count_subtree(node.right)

        final_result = False
        if left_result and node.left.val == node.val:
            final_result = True

        if final_result and right_result and node.right.val == node.val:
            final_result = True

        if final_result:
            self.count += 1
            return True

        return False





    def make_tree(self):
        root = TreeNode(5)
        node1 = TreeNode(5)
        node2 = TreeNode(5)
        node3 = TreeNode(5)
        node4 = TreeNode(5)
        node5 = TreeNode(5)

        root.left = node1
        root.right = node2
        node1.left = node3
        node1.right = node4
        node2.right = node5

        return root

    def make_tree1(self):
        root = TreeNode(5)
        node1 = TreeNode(1)
        node2 = TreeNode(5)
        node3 = TreeNode(5)
        node4 = TreeNode(5)
        node5 = TreeNode(5)

        root.left = node1
        root.right = node2
        node1.left = node3
        node1.right = node4
        node2.right = node5

        return root

    def make_tree2(self):
        root = TreeNode(1)
        node1 = TreeNode(1)
        node2 = TreeNode(1)
        node3 = TreeNode(5)
        node4 = TreeNode(5)
        node5 = TreeNode(5)

        root.left = node1
        root.right = node2
        node1.left = node3
        node1.right = node4
        node2.right = node5

        return root

    def make_tree3(self):
        root = TreeNode(5)
        node1 = TreeNode(5)
        node2 = TreeNode(5)
        node3 = TreeNode(5)
        node4 = TreeNode(1)
        node5 = TreeNode(5)

        root.left = node1
        root.right = node2
        node1.left = node3
        node1.right = node4
        node2.right = node5

        return root

my_sol = Solution()

root = my_sol.make_tree1()
print(my_sol.countUnivalSubtrees(root)) #4
#
# root1 = my_sol.make_tree()
# print(my_sol.countUnivalSubtrees(root1)) #6
#
# root1 = my_sol.make_tree2()
# print(my_sol.countUnivalSubtrees(root1)) #3
#
# root1 = my_sol.make_tree3()
# print(my_sol.countUnivalSubtrees(root1)) #4

