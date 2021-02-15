#Given a binary tree, return the sum of values of nodes with
# even-valued grandparent.  (A grandparent of a node is the parent of
# its parent, if it exists.)
#
# If there are no nodes with an even-valued grandparent, return 0.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.current_sum = 0

        self.find_sum(root, None, None)
        return self.current_sum

    def find_sum(self, node, parent, grand_parent):
        if not node:
            return

        if parent and grand_parent and grand_parent.val % 2 == 0:
            self.current_sum += node.val

        if not parent:
            parent = node
        else:
            grand_parent = parent
            parent = node

        self.find_sum(node.left, parent, grand_parent)
        self.find_sum(node.right, parent, grand_parent)


    def make_tree(self):
        root = TreeNode(6)
        node1 = TreeNode(7)
        node2 = TreeNode(8)
        node3 = TreeNode(2)
        node4 = TreeNode(7)
        node5 = TreeNode(9)
        node6 = TreeNode(1)
        node7 = TreeNode(4)
        node8 = TreeNode(1)
        node9 = TreeNode(3)
        node10 = TreeNode(5)

        root.left = node1
        root.right = node2

        node1.left = node3
        node1.right = node4
        node3.left = node5
        node4.left = node6
        node4.right = node7
        node2.left = node8
        node2.right = node9
        node9.right = node10
        return root


my_sol = Solution()

root = my_sol.make_tree()
print(my_sol.sumEvenGrandparent(root)) #18

