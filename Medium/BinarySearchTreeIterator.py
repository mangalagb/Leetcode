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

def create_tree():
    root = TreeNode(7)
    node1 = TreeNode(3)
    node2 = TreeNode(15)
    node3 = TreeNode(9)
    node4 = TreeNode(20)


    root.left = node1
    root.right = node2
    node2.left = node3
    node2.right = node4

    return root

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        if not root:
            self.smallest = None
            return

        self.stack = []
        current = root
        while current is not None:
            self.stack.append(current)
            current = current.left

        self.smallest = self.stack[-1]


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

        # Pop current
        current = self.smallest
        result = current.val
        self.stack.pop(-1)

        #New smallest
        right = current.right
        if right:
            while right:
                self.stack.append(right)
                right = right.left

        #update global smallest
        if len(self.stack) > 0:
            self.smallest = self.stack[-1]
        else:
            self.smallest = None

        return result


root = create_tree()
my_sol = BSTIterator(root)

nodes = []
while my_sol.hasNext():
    result = my_sol.next()
    if result:
        nodes.append(result)
print(nodes)

 #############################
root = None
my_sol = BSTIterator(root)

print(my_sol.hasNext())
