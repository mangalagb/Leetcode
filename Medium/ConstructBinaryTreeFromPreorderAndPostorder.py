# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None

        root = self.build_tree_recursively(preorder, inorder)
        return root

    def build_tree_recursively(self, preorder, inorder):
        node = preorder.pop(0)
        new_node = TreeNode(node)

        index_of_node = inorder.index(node)
        left_of_node = inorder[0:index_of_node]
        right_of_node = inorder[index_of_node+1 :]

        #recurse left
        if left_of_node:
            new_node.left = self.build_tree_recursively(preorder,
                                                    left_of_node)
        #recurse right
        if right_of_node:
            new_node.right = self.build_tree_recursively(preorder,
                                                        right_of_node)
        return new_node

my_sol = Solution()

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
my_sol.buildTree(preorder, inorder)

