# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in
# the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary search tree.
# There is no restriction on how your serialization/deserialization algorithm
# should work. You just need to ensure that a binary search tree can be
# serialized to a string and this string can be deserialized to the original
# tree structure.
#
# The encoded string should be as compact as possible.
#
# Note: Do not use class member/global/static variables to store states.
# Your serialize and deserialize algorithms should be stateless.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "X"

        left_tree = self.serialize(root.left)
        right_tree = self.serialize(root.right)

        current_str = str(root.val) + "," + left_tree + "," + right_tree
        return current_str

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        queue = data.split(",")
        return self.deserialize_helper(queue)

    def deserialize_helper(self, queue):
        node_val = queue.pop(0)
        if node_val == "X":
            return

        node = TreeNode(int(node_val))
        node.left = self.deserialize_helper(queue)
        node.right = self.deserialize_helper(queue)
        return node

    def make_tree(self):
        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(3)
        node3 = TreeNode(4)
        node4 = TreeNode(5)
        node5 = TreeNode(7)

        root.left = node1
        root.right = node2

        node1.left = node3
        # node1.right = node4
        #
        # node2.right = node5
        return root


# Your Codec object will be instantiated and called as such:
codec = Codec()
root = codec.make_tree()

serial = codec.serialize(root)
print(serial)
#print(codec.deserialize(serial))
