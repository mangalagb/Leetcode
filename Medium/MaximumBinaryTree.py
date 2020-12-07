#  Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
#
#     The root is the maximum number in the array.
#     The left subtree is the maximum tree constructed from left part subarray
#     divided by the maximum number.
#     The right subtree is the maximum tree constructed from right part subarray
#     divided by the maximum number.
#
# Construct the maximum tree by the given array and output the root node of this tree.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.root = None

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        self.construct_tree(nums, self.root)
        return self.root

    def construct_tree(self, nums, node):
        maximum_number = max(nums)
        maximum_index = nums.index(maximum_number)

        current = TreeNode(maximum_number)
        if not self.root:
            self.root = current

        left_tree = nums[:maximum_index]
        right_tree = nums[maximum_index+1:]

        if len(left_tree) > 0:
            current.left = self.construct_tree(left_tree, current)

        if len(right_tree) > 0:
            current.right = self.construct_tree(right_tree, current)

        return current

    def print_tree(self):
        if not self.root:
            print("Empty tree")
            return


my_sol = Solution()

nums = [3,2,1,6,0,5]
my_sol.constructMaximumBinaryTree(nums)
