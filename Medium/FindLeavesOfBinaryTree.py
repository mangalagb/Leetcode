# #Given the root of a binary tree, collect a tree's nodes as if you were doing this:
#
# Collect all the leaf nodes.
# Remove all the leaf nodes.
# Repeat until the tree is empty.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        while root is not None:
            leaves = []
            self.remove_leaves(root, None, None, leaves)

            #it is a root node
            if len(leaves) == 0:
                leaves.append(root.val)
                root = None

            ans.append(leaves)


        return ans

    def remove_leaves(self, node, parent, isLeftChild, leaves):
        if not node:
            return

        #If node is a leaf
        if not node.left and not node.right:
            if isLeftChild is None:
                return

            if isLeftChild:
                parent.left = None
            else:
                parent.right = None
            leaves.append(node.val)


        if node.left:
            self.remove_leaves(node.left, node, True, leaves)

        if node.right:
            self.remove_leaves(node.right, node, False, leaves)

    def make_tree(self):
        root = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)


        root.left = node2
        root.right = node3
        node2.left = node4
        node2.right = node5

        return root

    def make_tree1(self):
        root = TreeNode(1)
        return root

my_sol = Solution()

root = my_sol.make_tree()
print(my_sol.findLeaves(root)) #[[4,5,3],[2],[1]]

root = my_sol.make_tree1()
print(my_sol.findLeaves(root)) #[[1]]
