# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of itself).”

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        if p.val == root.val or q.val == root.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        else:
            return None

    def make_tree(self):
        root = TreeNode(3)
        node1 = TreeNode(5)
        node2 = TreeNode(1)
        node3 = TreeNode(6)
        node4 = TreeNode(2)
        node5 = TreeNode(7)
        node6 = TreeNode(4)
        node7 = TreeNode(0)
        node8 = TreeNode(8)

        root.left = node1
        root.right = node2

        node1.left = node3
        node1.right = node4

        node4.left = node5
        node4.right = node6
        node2.left = node7
        node2.right = node8

        return root

my_sol = Solution()

root = my_sol.make_tree()
ans = my_sol.lowestCommonAncestor(root, TreeNode(5), TreeNode(4)) #5
if ans:
    print(ans.val)