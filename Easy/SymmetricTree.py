#Given a binary tree, check whether it is a mirror
# of itself (ie, symmetric around its center).

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        result = self.inOrderTraversal(root.left, root.right)
        return result


    def inOrderTraversal(self, left, right):
        if not left and not right:
            return True

        if not left or not right:
            return False

        if left.val == right.val:
            outer_pair = self.inOrderTraversal(left.left, right.right)
            inner_pair = self.inOrderTraversal(left.right, right.left)
            if outer_pair and inner_pair:
                return True

        return False



    def make_tree(self):
        nums = [1,2,2,3,4,4,3]

        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(3)
        node5 = TreeNode(4)
        node6 = TreeNode(4)

        root.left = node1
        root.right = node2

        node1.left = node3
        node1.right = node5
        node2.left = node6
        node2.right = node4
        return root

    def make_tree1(self):
        nums = [1,2,2,3,4,4,3]

        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(2)
        #node3 = TreeNode()
        node4 = TreeNode(2)
        node5 = TreeNode(2)

        root.left = node1
        root.right = node2
        node1.left = node4
        #node1.right = node3
        node2.left = node5
        return root


my_sol = Solution()

root = my_sol.make_tree()
print(my_sol.isSymmetric(root))
