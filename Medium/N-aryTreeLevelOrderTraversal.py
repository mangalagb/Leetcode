# Given an n-ary tree, return the level order traversal of its nodes' values.
#
# Nary-Tree input serialization is represented in their level order traversal, each group of
# children is separated by the null value (See examples).

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        print(root.val)
        node_dict = {}

        queue = [[0, root]]

        while len(queue) > 0:
            element = queue.pop(0)
            depth = element[0]
            node = element[1]

            if depth not in node_dict:
                node_dict[depth] = [node.val]
            else:
                node_dict[depth].append(node.val)

            


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
my_sol.levelOrder(root)