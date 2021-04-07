# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None

        root = self.build_tree_recursively(inorder, postorder)
        return root

    def build_tree_recursively(self, inorder, postorder):
        length_of_post_order = len(postorder)
        if length_of_post_order == 0:
            return

        node_value = postorder.pop(-1)
        index_of_node_in_inorder = inorder.index(node_value)

        node = TreeNode(node_value)
        left_nodes = inorder[:index_of_node_in_inorder]
        right_nodes = inorder[index_of_node_in_inorder+1:]

        if right_nodes:
            node.right = self.build_tree_recursively(right_nodes, postorder)

        if left_nodes:
            node.left = self.build_tree_recursively(left_nodes, postorder)

        return node


my_sol = Solution()

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
my_sol.buildTree(inorder, postorder)
