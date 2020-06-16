# Given a binary tree, determine if it is a complete binary tree.
#
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is
# completely filled, and all nodes in the last level are as far left as possible.
# It can have between 1 and 2h nodes inclusive at the last level h.
#
import sys

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        max_depth = self.find_max_depth_of_tree(root)
        number_of_nodes = 0
        for i in range(0, max_depth):
            number_of_nodes += 2 ** i

        number_of_nodes += 1

        #If the number of nodes is too high try to simplify the calculation
        if number_of_nodes > sys.maxsize:
            result = self.is_valid_tree(root)
            if not result:
                return False

        tree_array = [None] * number_of_nodes
        tree_array[1] = root.val
        value = self.construct_tree_array(root, tree_array, 1)
        if not value:
            return False

        is_complete = True
        null_value_seen = False

        # Find deviations
        for i in range(1, len(tree_array)):
            if tree_array[i] and null_value_seen:
                is_complete = False
                break

            if not tree_array[i]:
                null_value_seen = True
        return is_complete

    def is_valid_tree(self, node):
        if not node:
            return True

        left_child = node.left
        right_child = node.right

        if not left_child and right_child:
            return False

    def find_max_depth_of_tree(self, node):
        if not node:
            return 0

        ldepth = self.find_max_depth_of_tree(node.left)
        rdepth = self.find_max_depth_of_tree(node.right)

        if ldepth >= rdepth:
            return ldepth + 1
        else:
            return rdepth + 1

    def construct_tree_array(self, node, tree_array, i):
        if not node:
            return True

        left_child = node.left
        right_child = node.right

        if not left_child and right_child:
            return False

        if left_child or right_child:
            left_index = 2 * i
            right_index = (2 * i) + 1

            if left_child:
                tree_array[left_index] = left_child.val

            if right_child:
                tree_array[right_index] = right_child.val

            left_value = self.construct_tree_array(left_child, tree_array, left_index)
            right_value = self.construct_tree_array(right_child, tree_array, right_index)
            return left_value and right_value
        return True

    def make_tree(self, nums):
        nums.insert(0, None)

        root = self.construct_tree(nums, 1)
        return self.isCompleteTree(root)

    def construct_tree(self, nums, index):
        value = nums[index]
        if not value:
            return

        current_node = TreeNode(nums[index])

        left_child_index = 2 * index
        right_child_index = (2 * index) + 1

        if left_child_index < len(nums):
            current_node.left = self.construct_tree(nums, left_child_index)

        if right_child_index < len(nums):
            current_node.right = self.construct_tree(nums, right_child_index)

        return current_node





my_sol = Solution()

nodes = [1,2,3,4,5,6]
print(my_sol.make_tree(nodes))

# nodes = [1,2,3,5,None,7,8]
# print(my_sol.make_tree(nodes))
#
# nodes = [1,None,2,None,3,None,4,None,5,None,6,None,7,None,8,None,9,None,10,None,11,None,12,None,13,
#          None,14,None,15,None,16,None,17,None,18,None,19,None,20,None,21,None,22,None,23,None,24,None,
#          25,None,26,None,27,None,28,None,29,None,30,None,31,None,32,None,33,None,34,None,35,None,36,None,
#          37,None,38,None,39,None,40,None,41,None,42,None,43,None,44,None,45,None,46,None,47,None,48,None,
#          49,None,50,None,51,None,52,None,53,None,54,None,55,None,56,None,57,None,58,None,59,None,60,None,
#          61,None,62,None,63,None,64,None,65,None,66,None,67,None,68,None,69,None,70,None,71,None,72,None,
#          73,None,74,None,75,None,76,None,77,None,78,None,79,None,80,None,81,None,82,None,83,None,84,None,
#          85,None,86,None,87,None,88,None,89,None,90,None,91,None,92,None,93,None,94,None,95,None,96,None,
#          97,None,98,None,99,None,100,None]
# print(my_sol.make_tree(nodes))


