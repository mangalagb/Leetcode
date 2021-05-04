# #Given the root of a binary tree, return all duplicate subtrees.
#
# For each kind of duplicate subtrees, you only need to return the root node of any one of them.
#
# Two trees are duplicate if they have the same structure with the same node values.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.result = set()
        self.possible_trees = {}

        self.traverse_tree(root)
        return list(self.result)

    def traverse_tree(self, node):
        if not node:
            return "#"

        current_val =  self.traverse_tree(node.left) + ","+ str(node.val) + "," + self.traverse_tree(node.right)
        if current_val in self.possible_trees:
            self.result.add(self.possible_trees[current_val])
        else:
            self.possible_trees[current_val] = node

        return current_val


    def make_tree(self):
        root = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(2)
        node6 = TreeNode(4)
        node7 = TreeNode(4)

        root.left = node2
        root.right = node3

        node2.left = node4
        node3.left = node5
        node3.right = node6
        node5.left = node7
        return root

    def make_tree1(self):
        root = TreeNode(2)
        node2 = TreeNode(1)
        node3 = TreeNode(1)

        root.left = node2
        root.right = node3
        return root

    def make_tree2(self):
        root = TreeNode(2)
        node2 = TreeNode(2)
        node3 = TreeNode(2)
        node4 = TreeNode(3)
        node5 = TreeNode(3)

        root.left = node2
        root.right = node3

        node2.left = node4
        node3.left = node5
        return root


my_sol = Solution()

root1 = my_sol.make_tree()
print(my_sol.findDuplicateSubtrees(root1))
#
# root1 = my_sol.make_tree1()
# print(my_sol.findDuplicateSubtrees(root1))
#
# root1 = my_sol.make_tree2()
# print(my_sol.findDuplicateSubtrees(root1))
