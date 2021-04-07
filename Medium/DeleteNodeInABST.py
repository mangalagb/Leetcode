# Given a root node reference of a BST and a key, delete the node with the given key in the BST.
# Return the root node reference (possibly updated) of the BST.
#
# Basically, the deletion can be divided into two stages:
#
#     Search for a node to remove.
#     If the node is found, delete the node.
#
# Note: Time complexity should be O(height of tree).

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            min_node = self.find_min(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, root.val)
        return root

    def find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def make_tree1(self):
        root = TreeNode(5)
        node1 = TreeNode(3)
        node2 = TreeNode(6)
        node3 = TreeNode(2)
        node4 = TreeNode(4)
        node5 = TreeNode(7)

        root.left = node1
        root.right = node2

        node1.left = node3
        node1.right = node4

        node2.right = node5
        return root

my_sol = Solution()

root = my_sol.make_tree1()
root = my_sol.deleteNode(root, 5)
print(root)
