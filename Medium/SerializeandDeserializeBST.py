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
        result = self.serialize_tree(root)
        return result

    def serialize_tree(self, node):
        if not node:
            return "X"

        result = str(node.val)
        if not node.left and not node.right:
            return result

        if node.left and node.right:
            left_string = self.serialize_tree(node.left)
            right_string = self.serialize_tree(node.right)
            result += "," + left_string + "," + right_string
        elif


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        elements = data.split(",")
        elements.insert(0, None)

        if len(elements) == 1 or elements[1] == "X":
            return None

        root = self.deseriailize_helper(1, elements)
        return root


    def deseriailize_helper(self, index, elements):
        length_of_elements = len(elements) - 1

        if index > length_of_elements:
            return

        if elements[index] == "X":
            return
        else:
            node = TreeNode(int(elements[index]))

            left_index = 2 * index
            right_index = (2 * index) + 1

            if left_index < length_of_elements:
                node.left = self.deseriailize_helper(left_index, elements)

            if right_index < length_of_elements:
                node.right = self.deseriailize_helper(right_index, elements)

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
