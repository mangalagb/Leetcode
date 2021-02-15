#Given two binary trees original and cloned and given a reference to a node
# target in the original tree.

# The cloned tree is a copy of the original tree.
#
# Return a reference to the same node in the cloned tree.
#
# Note that you are not allowed to change any of the two trees or the target
# node and the answer must be a reference to a node in the cloned tree.
#
# Follow up: Solve the problem if repeated values on the tree are allowed.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        result_node = self.traverse_tree(original, cloned, target)
        return result_node

    def traverse_tree(self, node1, node2, target):
        if node1.val == target.val:
            result = self.check_tree(node1, node2)
            if result:
                return node2

        if node1.left:
            left_result = self.traverse_tree(node1.left, node2.left, target)
            if left_result:
                return left_result

        if node1.right:
            right_result = self.traverse_tree(node1.right, node2.right, target)
            if right_result:
                return right_result


    def check_tree(self, node1, node2):
        if node1.val != node2.val:
            return False

        if node1.left:
            left_result = self.check_tree(node1.left, node2.left)
            if not left_result:
                return False

        if node1.right:
            right_result = self.check_tree(node1.right, node2.right)
            if not right_result:
                return False
        return True


    def make_tree(self):
        root = TreeNode(7)
        node1 = TreeNode(4)
        node2 = TreeNode(3)
        node3 = TreeNode(6)
        node4 = TreeNode(19)

        root.left = node1
        root.right = node2
        node2.left = node3
        node2.right = node4
        return root

    def get_target(self, root):
        #3
        node = root.right
        return node


my_sol = Solution()

original = my_sol.make_tree()
cloned = my_sol.make_tree()
target = my_sol.get_target(original)

print(my_sol.getTargetCopy(original, cloned, target))

