# Given a binary tree root and an integer target, delete all the leaf nodes with value target.
#
# Note that once you delete a leaf node with value target, if it's parent node
# becomes a leaf node and has the value target, it should also be deleted
# (you need to continue doing that until you can't).

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        if not root:
            return None

        self.delete_leaf(root, None, target)

        # Delete root
        if not root.left and not root.right and root.val == target:
            return None
        else:
            return root


    def delete_leaf(self, node, parent, target):
        if not node:
            return

        if node.left:
            self.delete_leaf(node.left, node, target)

        if node.right:
            self.delete_leaf(node.right, node, target)

        # Delete current node
        if not node.left and not node.right and node.val == target:
            self.delete_target_node(node, parent)

    def delete_target_node(self, node, parent):
        if parent:
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None


    def create_tree(self):
        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(3)
        node3 = TreeNode(2)
        node4 = TreeNode(2)
        node5 = TreeNode(4)

        root.left = node1
        root.right = node2

        node1.left = node3
        node2.left = node4
        node2.right = node5
        return root


    def create_tree1(self):
        root = TreeNode(1)
        node1 = TreeNode(1)
        node2 = TreeNode(1)

        root.left = node1
        root.right = node2
        return root

my_sol = Solution()

# root = my_sol.create_tree()
# my_sol.removeLeafNodes(root, 2)

root = my_sol.create_tree1()
my_sol.removeLeafNodes(root, 1)
