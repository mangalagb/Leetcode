# Given a binary tree, we install cameras on the nodes of the tree.
#
# Each camera at a node can monitor its parent, itself, and its immediate children.
#
# Calculate the minimum number of cameras needed to monitor all nodes of the tree.
#
# 0 -> there is no camera at this node, and it's not monitored by camera at either of its children,
# which means neither of child nodes has camera.
# 1 -> there is no camera at this node; however, this node is monitored by at least 1
# of its children, which means at least 1 of its children has camera.
# -1 -> there is a camera at this node.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.camera = 0
        dfs_result = self.do_DFS(root)

        if dfs_result == 0:
            self.camera += 1
        return self.camera

    def do_DFS(self, node):
        # 0 -> if it is a leaf
        # 1 -> Has camera here
        # -1 -> No camera needed
        if not node:
            return -1
        elif not node.left and not node.right:
            return 0

        left_result = self.do_DFS(node.left)
        right_result = self.do_DFS(node.right)

        # If left or right is leaf, place camera here
        # Pass this info to parent so no need to place camera at parent
        if left_result == 0 or right_result == 0:
            self.camera += 1
            return 1

        # There is a camera just below which will monitor this node
        # So dont monitor parent
        if left_result == 1 or right_result == 1:
            return -1

        return 0



    def make_tree1(self):
        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(3)
        node3 = TreeNode(4)
        node4 = TreeNode(5)

        root.left = node1
        node1.left = node2
        node1.right = node3
        node2.left = node4
        return root

    def make_tree(self):
        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(3)
        node3 = TreeNode(4)

        root.left = node1
        node1.left = node2
        node1.right = node3
        return root

    def make_tree2(self):
        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(3)
        node3 = TreeNode(4)
        node4 = TreeNode(5)

        root.left = node1
        node1.left = node2
        node2.left = node3
        node3.right = node4
        return root

    def make_tree3(self):
        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(3)
        node3 = TreeNode(4)
        node4 = TreeNode(5)
        node5 = TreeNode(6)

        root.left = node1
        node1.left = node2
        node2.left = node3
        node3.right = node4
        node4.left = node5
        return root

    def make_tree5(self):
        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(3)
        node3 = TreeNode(4)
        node4 = TreeNode(5)
        node5 = TreeNode(6)

        root.left = node1
        root.right = node2

        node1.right = node3
        node3.right = node4
        node2.left = node5
        return root

    def make_tree4(self):
        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(3)
        node3 = TreeNode(4)

        root.right = node1
        node1.right = node2
        node2.right = node3
        return root

my_sol = Solution()

root = my_sol.make_tree()
print(my_sol.minCameraCover(root)) #1

root = my_sol.make_tree1()
print(my_sol.minCameraCover(root)) #2

root = my_sol.make_tree2()
print(my_sol.minCameraCover(root)) #2

root = my_sol.make_tree3()
print(my_sol.minCameraCover(root)) #2

root = my_sol.make_tree4()
print(my_sol.minCameraCover(root)) #2

root = my_sol.make_tree5()
print(my_sol.minCameraCover(root)) #2