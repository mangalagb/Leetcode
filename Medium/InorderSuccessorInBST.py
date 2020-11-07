# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
#
# The successor of a node p is the node with the smallest key greater than p.val.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        stack = []
        current = root
        target_node_found = False

        while current or len(stack) > 0:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop(-1)
            if target_node_found:
                return current

            if current.val == p.val:
                target_node_found = True

            current = current.right

        if target_node_found:
            return None



    def make_tree(self):
        root = TreeNode(2)
        node2 = TreeNode(1)
        node3 = TreeNode(3)

        root.left = node2
        root.right = node3
        return root

    def make_tree1(self):
        root = TreeNode(5)
        node2 = TreeNode(3)
        node3 = TreeNode(6)
        node4 = TreeNode(2)
        node5 = TreeNode(4)
        node6 = TreeNode(1)

        root.left = node2
        root.right = node3

        node2.left = node4
        node2.right = node5
        node4.left = node6

        return root

my_sol = Solution()

root = my_sol.make_tree()
result = my_sol.inorderSuccessor(root, TreeNode(1))
if result:
    print(result.val)
else:
    print(result)

root = my_sol.make_tree1()
result = my_sol.inorderSuccessor(root, TreeNode(6))
if result:
    print(result.val)
else:
    print(result)

