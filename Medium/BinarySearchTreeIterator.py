# Implement an iterator over a binary search tree (BST). Your iterator will be
# initialized with the root node of a BST.
#
# Calling next() will return the next smallest number in the BST.
#
# Note: next() and hasNext() should run in average O(1) time and uses O(h)
# memory, where h is the height of the tree.

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x = None):
        self.val = x
        self.left = None
        self.right = None

    def create_tree(self):
        root = TreeNode(8)
        node1 = TreeNode(3)
        node2 = TreeNode(1)
        node3 = TreeNode(6)
        node4 = TreeNode(10)
        node5 = TreeNode(14)
        node6 = TreeNode(13)

        root.left = node1
        root.right = node4

        node1.left = node2
        node1.right = node3

        node4.right = node5
        node5.left = node6
        return root

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.smallest = root
        self.parent = None

        current = root
        while current.left is not None:
            self.parent = current
            current = current.left

        self.smallest = current


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.smallest is not None:
            return True
        else:
            return False


    def next(self):
        """
        :rtype: int
        """
        value = self.smallest

        if self.parent is not None:
            self.smallest = self.parent

        return value




tree_node = TreeNode()
root = tree_node.create_tree()

i = BSTIterator(root)
v = []

while i.hasNext():
    v.append(i.next())

