#represent binary tree in array

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def construct_binary_tree(self, nums):

        root = TreeNode(nums[0])

        i = 0
        depth = 1
        self.make_tree1(root, nums, i, depth)
        print("done")

    def make_tree1(self, node, nums, i, depth):
        left_node_index = (depth * i) + 1
        if left_node_index >= len(nums):
            return

        if nums[left_node_index]:
            left_node = TreeNode(nums[left_node_index])
            i += 1
            temp = depth
            self.make_tree1(left_node, nums, i, temp+1)
            node.left = left_node

        right_node_index = (depth * i) + 2
        if right_node_index >= len(nums):
            return

        if right_node_index < len(nums) and nums[right_node_index]:
            right_node = TreeNode(nums[right_node_index])
            i += 1
            self.make_tree1(right_node, nums, i, depth+1)
            node.right = right_node





    def make_tree(self, node, nums, i):

        left_node_index = (i*2) + 1
        right_node_index = (i*2) + 2
        left_node = None
        right_node = None

        if left_node_index >= len(nums) and right_node_index >= len(nums):
            return

        if 0 <= left_node_index < len(nums) and nums[left_node_index]:
            left_node = TreeNode(nums[left_node_index])
            node.left = left_node

        if 0 <= right_node_index < len(nums) and nums[right_node_index]:
            right_node = TreeNode(nums[right_node_index])
            node.right = right_node

        i += 1
        if left_node:
            self.make_tree(left_node, nums, i)
        if right_node:
            self.make_tree(right_node, nums, i)







array = [0,1,2,3,4,5,6,7,8]
my_sol = Solution()
my_sol.construct_binary_tree(array)