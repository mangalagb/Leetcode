# A binary tree boundary is the set of nodes (no duplicates) denoting the union
# of the left boundary, leaves, and right boundary.
#
# The left boundary is the set of nodes on the path from the root to the
# left-most node. The right boundary is the set of nodes on the path from the root to the right-most node.
#
# The left-most node is the leaf node you reach when you always travel
# to the left subtree if it exists and the right subtree if it doesn't.
# The right-most node is defined in the same way except with left and right
# exchanged. Note that the root may be the left-most and/or right-most node.
#
# Given the root of a binary tree, return the values of its boundary in a
# counter-clockwise direction starting from the root.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        elif not root.left and not root.right:
            return [root.val]

        result = [root.val]
        self.get_left_boundary(root.left, result)
        self.get_leaves(root.left, result)
        self.get_leaves(root.right, result)
        self.get_right_boundary(root.right, result)

        return result


    def get_left_boundary(self, node, result):
        if not node or (not node.left and not node.right):
            return

        result.append(node.val)
        if node.left:
            self.get_left_boundary(node.left, result)
        elif node.right:
            self.get_left_boundary(node.right, result)


    def get_right_boundary(self, node, result):
        if not node or (not node.left and not node.right):
            return

        if node.right:
            self.get_right_boundary(node.right, result)
        elif node.left:
            self.get_right_boundary(node.left, result)

        result.append(node.val)


    def get_leaves(self, node, leaves):
        if not node:
            return

        if not node.left and not node.right:
            leaves.append(node.val)
            return

        self.get_leaves(node.left, leaves)
        self.get_leaves(node.right, leaves)



    def make_tree(self):
        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(3)
        node3 = TreeNode(4)
        node4 = TreeNode(5)
        node5 = TreeNode(6)
        node6 = TreeNode(7)
        node7 = TreeNode(8)
        node8 = TreeNode(9)
        node9 = TreeNode(10)

        root.left = node1
        root.right = node2

        node1.left = node3
        node1.right = node4
        node4.left = node6
        node4.right = node7

        node2.right = node5
        node5.left = node8
        node5.right = node9
        return root

    def make_tree1(self):
        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(3)
        node3 = TreeNode(4)

        root.right = node1
        node1.left = node2
        node1.right = node3
        return root

my_sol = Solution()

root = my_sol.make_tree1()
print(my_sol.boundaryOfBinaryTree(root)) #[1,3,4,2]

root = my_sol.make_tree()
print(my_sol.boundaryOfBinaryTree(root)) #[1,2,4,7,8,9,10,6,3]

