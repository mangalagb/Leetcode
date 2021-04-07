# Given a complete binary tree, count the number of nodes.
#
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled,
# and all nodes in the last level are as far left as possible. It can have between 1 and 2h
# nodes inclusive at the last level h.

# Definition for a binary tree node.
#

#     A fully completed tree has node number: count = 2 ^ depth - 1
#     for example: [1,2,3]
#     depth is 2
#     count = (2 ^ 2 )- 1 = 3
#     Compare left height and right height, if equal, use the formula, otherwise recurvisely
#     search left and right at next level. The search pattern is very similar to
#     binary search, the difference of heights ethier exsits in left side, or right side.
#     Due to the reason stated in point 3, the time complexity is h ^ 2,
#     there is h times for each level, and h times for calculating height at each level

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left_depth = self.get_left_depth(root)
        right_depth = self.get_right_depth(root)

        if left_depth == right_depth:
            return (2 ** left_depth) -1

        number_of_nodes = 1 + self.countNodes(root.left) + self.countNodes(root.right)
        return number_of_nodes

    def get_left_depth(self, node):
        depth = 0
        while node:
            depth += 1
            node = node.left
        return depth

    def get_right_depth(self, node):
        depth = 0
        while node:
            depth += 1
            node = node.right
        return depth


    def make_tree(self):
        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(3)
        node3 = TreeNode(4)
        node4 = TreeNode(5)
        node5 = TreeNode(6)

        root.left = node1
        root.right = node2

        node1.left = node3
        node1.right = node4

        node2.left = node5
        return root


my_sol = Solution()
root = my_sol.make_tree()
print(my_sol.countNodes(root))
