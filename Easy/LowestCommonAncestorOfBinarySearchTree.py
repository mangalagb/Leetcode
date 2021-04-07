# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined
# between two nodes p and q as the lowest node in T that has both p and q
# as descendants (where we allow a node to be a descendant of itself).”

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
        if root is None:
            return None

        result = self.find_lca(root, p, q, root.val)
        return result

    def find_lca(self, node, p, q, lca):
        if node is None:
            return None
        elif node.val == p.val or node.val == q.val:
            return node

        left_result = None
        right_result= None
        if p.val < node.val and q.val < node.val:
            left_result = self.find_lca(node.left, p,q, lca)
        elif p.val > node.val and q.val > node.val:
            right_result = self.find_lca(node.right, p, q, lca)
        else:
            left_result = self.find_lca(node.left, p,q, lca)
            right_result = self.find_lca(node.right, p, q, lca)

        if left_result and right_result:
            return node
        elif not left_result:
            return right_result
        else:
            return left_result

    def make_tree(self):
        root = TreeNode(6)
        node1 = TreeNode(2)
        node2 = TreeNode(0)
        node3 = TreeNode(4)
        node4 = TreeNode(3)
        node5 = TreeNode(5)
        node6 = TreeNode(8)
        node7 = TreeNode(7)
        node8 = TreeNode(9)

        root.left = node1
        root.right = node6

        node1.left = node2
        node1.right = node3

        node3.left = node4
        node3.right = node5

        node6.left = node7
        node6.right = node8
        return root

my_sol = Solution()
root = my_sol.make_tree()

ans = my_sol.lowestCommonAncestor(root, TreeNode(2), TreeNode(8))
if not ans:
    print("null")
else:
    print(ans.val)

ans = my_sol.lowestCommonAncestor(root, TreeNode(2), TreeNode(6))
if not ans:
    print("null")
else:
    print(ans.val)

ans = my_sol.lowestCommonAncestor(root, TreeNode(2), TreeNode(4))
if not ans:
    print("null")
else:
    print(ans.val)


