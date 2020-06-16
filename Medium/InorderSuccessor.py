# Write an algorithm to find the ‘next’ node (e.g., in-order successor) of a given node in
# a binary search tree where each node has a link to its parent.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, parent=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class Solution(object):
    def inorderSuccessor(self, root, node):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if not node.left and not node.right:
            parent = node.parent
            if parent.left == node:
                return parent
            else:
                return parent.parent

        if node.right:
            min_node = self.find_min(node.right)
            return min_node

    def find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def make_tree1(self):
        root = TreeNode(5, None)
        node1 = TreeNode(3, root)
        node2 = TreeNode(6, root)
        node3 = TreeNode(2, node1)
        node4 = TreeNode(4, node1)
        node5 = TreeNode(7, node2)

        root.left = node1
        root.right = node2

        node1.left = node3
        node1.right = node4

        node2.right = node5
        return [root, node1]

my_sol = Solution()

[root, node] = my_sol.make_tree1()

current = my_sol.inorderSuccessor(root, node)
if current:
    print(current.val)
else:
    print("None")

current = my_sol.inorderSuccessor(root, current)
if current:
    print(current.val)
else:
    print("None")

current = my_sol.inorderSuccessor(root, current)
if current:
    print(current.val)
else:
    print("None")
