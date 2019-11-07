# Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.
#
# In one move, we may choose two adjacent nodes and move one coin from one node to another.
# (The move may be from parent to child, or from child to parent.)
#
# Return the number of moves required to make every node have exactly one coin.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        stack.append(root.val)

        while stack:
            print("empty")
            stack.pop()

        print("done")









my_sol = Solution()

t1 = [3,0,0]
tt1 = TreeNode(t1[0])
my_sol.distributeCoins(tt1)