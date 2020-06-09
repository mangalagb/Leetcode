# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated
# exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for
# those repeat numbers, k. For example, there won't be input like 3a or 2[4].

class TreeNode(object):
    def __init__(self, x = None):
        self.val = x
        self.left = None
        self.right = None

        
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        print("hello")

    def make_tree(self):
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



my_sol = Solution()

nodes = [1,2,3,4,5,6]
print(my_sol.make_tree(nodes))
