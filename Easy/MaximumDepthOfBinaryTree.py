# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):

        if not root:
            return 0
        depth = self.max_depth_helper(root, 1)
        #print(depth)
        return depth

    def max_depth_helper(self, node, count):
        if node is None:
            return count

        left_val = count
        right_val = count
        if node.left is not None:
            left_val = self.max_depth_helper(node.left, count+1)

        if node.right is not None:
            right_val = self.max_depth_helper(node.right, count+1)

        return max(left_val, right_val)


    def createTree(self):
        root = TreeNode(3)
        node1 = TreeNode(9)
        node2 = TreeNode(20)
        node3 = TreeNode(15)
        node4 = TreeNode(7)

        root.left = node1
        root.right = node2
        node2.left = node3
        node2.right = node4

        self.maxDepth(root)

my_sol = Solution()
my_sol.createTree()
