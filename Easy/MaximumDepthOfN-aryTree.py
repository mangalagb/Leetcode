#Given a n-ary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node
# down to the farthest leaf node.
#
# Nary-Tree input serialization is represented in their level order traversal, each
# group of children is separated by the null value (See examples).

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        result = self.find_depth(root, 1)
        return result

    def find_depth(self, node, depth):
        if not node:
            return 0

        children = node.children
        max_children_depth = 0
        if children:
            for child in children:
                child_depth = self.find_depth(child, depth+1)
                max_children_depth = max(child_depth, max_children_depth)

        final_depth = max(max_children_depth, depth)
        return final_depth


    def build_tree(self):
        root = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)

        root.children = [node3, node2, node4]
        node3.children = [node5, node6]
        return root

my_sol = Solution()

root = my_sol.build_tree()
print(my_sol.maxDepth(root)) #3
