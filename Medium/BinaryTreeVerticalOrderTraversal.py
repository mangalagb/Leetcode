# Given a binary tree, return the vertical order traversal
# of its nodes' values. (ie, from top to bottom, column by column).
#
# If two nodes are in the same row and column, the order should be from left to right.
import collections
import heapq

# Definition for a binary tree node.
from operator import itemgetter


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        depth_dict = {}

        #DO BFS
        queue = [[root, 0, 0]]
        while len(queue) > 0:
            element = queue.pop(0)
            x = element[1]
            y = element[2]
            node = element[0]
            node_val = node.val

            tup = tuple([x, y])
            if tup in depth_dict:
                depth_dict[tup].append(node.val)
            else:
                depth_dict[tup] = [node_val]

            if node.left:
                queue.append([node.left, x-1, y-1])

            if node.right:
                queue.append([node.right, x+1, y-1])

        #Sort the keys first by increasing x values
        # then by decreasing y values (left to right will mean a greater y will be on the left)

        sorted_keys = list(depth_dict.keys())
        sorted_keys.sort(key=itemgetter(1), reverse=True)

        #The sort with first preference should come last
        sorted_keys.sort(key=itemgetter(0))

        result = {}
        for key in sorted_keys:
            x = key[0]
            values = depth_dict[key]

            if x not in result:
                result[x] = values
            else:
                result[x].extend(values)

        return list(result.values())


    def make_tree(self):
        root = TreeNode(3)
        node1 = TreeNode(9)
        node2 = TreeNode(20)
        node3 = TreeNode(15)
        node4 = TreeNode(7)

        root.left = node1
        root.right = node2
        node2.left = node3
        node2.right = node4
        return root

    def make_tree1(self):
        root = TreeNode(3)
        node1 = TreeNode(9)
        node2 = TreeNode(8)
        node3 = TreeNode(4)
        node4 = TreeNode(0)
        node5 = TreeNode(1)
        node6 = TreeNode(7)

        root.left = node1
        root.right = node2

        node1.left = node3
        node1.right = node4
        node2.left = node5
        node2.right = node6
        return root

    def make_tree2(self):
        root = TreeNode(3)
        node1 = TreeNode(9)
        node2 = TreeNode(8)
        node3 = TreeNode(4)
        node4 = TreeNode(0)
        node5 = TreeNode(1)
        node6 = TreeNode(7)
        node7 = TreeNode(2)
        node8 = TreeNode(5)

        root.left = node1
        root.right = node2

        node1.left = node3
        node1.right = node4
        node4.right = node7
        node2.left = node5
        node2.right = node6
        node5.left = node8
        return root

my_sol = Solution()

root = my_sol.make_tree()
print(my_sol.verticalOrder(root)) #[[9], [3, 15], [20], [7]]

root = my_sol.make_tree1()
print(my_sol.verticalOrder(root)) #[[4], [9], [3, 0, 1], [8], [7]]

root = my_sol.make_tree2()
print(my_sol.verticalOrder(root)) #[[4], [9, 5], [3, 0, 1], [8, 2], [7]]
