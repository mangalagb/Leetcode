# You are given a binary tree in which each node contains an integer value.
#
# Find the number of paths that sum to a given value.
#
# The path does not need to start or end at the root or a leaf, but it must go downwards
# (traveling only from parent nodes to child nodes).
#
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

from collections import defaultdict

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        frequency = defaultdict(int)
        frequency[0] = 1
        result = self.find_paths(frequency, root, 0, sum)
        return result

    def find_paths(self, frequency, node, current_sum, target):
        if not node:
            return 0

        current_sum += node.val
        remaining_sum = current_sum - target

        count = 0
        if remaining_sum in frequency:
            count += frequency[remaining_sum]

        frequency[current_sum] += 1

        left_count = self.find_paths(frequency, node.left, current_sum, target)
        right_count = self.find_paths(frequency, node.right, current_sum, target)

        count += (left_count + right_count)

        # Remove 1 from the frequency since this path cannot be travelled again
        frequency[current_sum] -= 1
        return count


    def make_tree1(self):
        root = TreeNode(10)
        node1 = TreeNode(5)
        node2 = TreeNode(3)
        node3 = TreeNode(2)
        node4 = TreeNode(3)
        node5 = TreeNode(-2)

        node7 = TreeNode(1)
        node8 = TreeNode(-3)
        node9 = TreeNode(11)

        root.left = node1
        root.right = node8

        node1.left = node2
        node1.right = node3

        node2.left = node4
        node2.right = node5
        node3.right = node7

        node8.right = node9
        return root

my_sol = Solution()

root = my_sol.make_tree1()
print(my_sol.pathSum(root, 8))
