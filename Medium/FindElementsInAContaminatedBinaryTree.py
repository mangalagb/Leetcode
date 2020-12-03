# Given a binary tree with the following rules:
#
#     root.val == 0
#     If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
#     If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
#
# Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.
#
# You need to first recover the binary tree and then implement the FindElements class:
#
#     FindElements(TreeNode* root) Initializes the object with a contamined binary tree,
#     you need to recover it first.
#     bool find(int target) Return if the target value exists in the recovered binary tree.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        if root is None:
            return

        self.root = root
        self.nodes = set()
        self.nodes.add(0)

        if self.root.val == -1:
            self.root.val = 0
        self.calculate_tree(self.root, 0)

    def calculate_tree(self, node, x):
        if node.left is not None:
            node.left.val = 2 * x + 1
            self.nodes.add(node.left.val)
            self.calculate_tree(node.left, node.left.val)

        if node.right is not None:
            node.right.val = 2 * x + 2
            self.nodes.add(node.right.val)
            self.calculate_tree(node.right, node.right.val)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        if target in self.nodes:
            return True
        else:
            return False

def make_tree1():
    root = TreeNode(-1)
    root.right = TreeNode(-1)
    return root

def make_tree2():
    root = TreeNode(-1)
    node1 = TreeNode(-1)
    node2 = TreeNode(-1)
    node3 = TreeNode(-1)
    node4 = TreeNode(-1)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    return root

def make_tree3():
    root = TreeNode(-1)
    node1 = TreeNode(-1)
    node2 = TreeNode(-1)
    node3 = TreeNode(-1)
    node4 = TreeNode(-1)

    root.right = node2
    node2.left = node3
    node3.left = node4
    return root

def make_tree4():
    root = TreeNode(-1)
    node1 = TreeNode(-1)
    node2 = TreeNode(-1)
    node3 = TreeNode(-1)
    node4 = TreeNode(-1)
    node5 = TreeNode(-1)

    root.left = node1
    root.right = node2
    node2.left = node3
    node2.right = node4
    node4.right = node5
    return root

# Your FindElements object will be instantiated and called as such:

root = make_tree4()
obj = FindElements(root)

print(obj.find(4))
print(obj.find(1))
print(obj.find(6))
