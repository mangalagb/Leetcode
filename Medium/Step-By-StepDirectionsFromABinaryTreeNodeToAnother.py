# #You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n.
# You are also given an integer startValue representing the value of the start node s, and a different
# integer destValue representing the value of the destination node t.
#
# Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of
# such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates
# a specific direction:
#
# 'L' means to go from a node to its left child node.
# 'R' means to go from a node to its right child node.
# 'U' means to go from a node to its parent node.
# Return the step-by-step directions of the shortest path from node s to node t.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        if not root:
            return ""

        lca = self.find_lca(startValue, destValue, root)
        if lca is None:
            return ""

        left_path = []
        self.find_path_from_lca(lca, startValue, left_path)
        left_path_str = ""
        for direction in left_path:
            left_path_str = left_path_str + "U"

        right_path = []
        self.find_path_from_lca(lca, destValue, right_path)

        result = left_path_str + ''.join(right_path)
        return result



    def find_path_from_lca(self, node, value, path):
        if not node:
            return None

        if node.val == value:
            return True

        left = self.find_path_from_lca(node.left, value, path)
        if left:
            path.insert(0, "L")
            return True
        else:
            right = self.find_path_from_lca(node.right, value, path)
            if right:
                path.insert(0, "R")
                return True

        return False


    def find_lca(self, p, q, node):
        if not node:
            return None

        if node.val == p or node.val == q:
            return node

        left = self.find_lca(p,q, node.left)
        right = self.find_lca(p,q, node.right)

        if left and right:
            return node
        elif left:
            return left
        elif right:
            return right
        else:
            return None


    def make_tree(self):
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        node6 = TreeNode(6)

        node5.left = node1
        node1.left = node3
        node5.right = node2
        node2.left = node6
        node2.right = node4
        return node5

    def make_tree1(self):
        node1 = TreeNode(1)
        node2 = TreeNode(2)

        node2.left = node1
        return node2

my_sol = Solution()

root = my_sol.make_tree()
startValue = 3
destValue = 6
print(my_sol.getDirections(root, startValue, destValue))#"UURL"

root = my_sol.make_tree1()
startValue = 2
destValue = 1
print(my_sol.getDirections(root, startValue, destValue))#"L"
