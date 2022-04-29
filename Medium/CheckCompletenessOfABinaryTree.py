# Given a binary tree, determine if it is a complete binary tree.
#
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is
# completely filled, and all nodes in the last level are as far left as possible.

#When level-order traversal in a complete tree, after the last node, all nodes in the queue should be null.
#Otherwise, the tree is not complete.

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

        queue = [root]
        empty_node_seen = False

        while len(queue) > 0:
            node = queue.pop(0)

            if not node:
                empty_node_seen = True

            else:
                if empty_node_seen:
                    return False

                queue.append(node.left)
                queue.append(node.right)
        return True

    def make_tree(self):
        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(3)
        node3 = TreeNode(4)
        node4 = TreeNode(5)
        node5 = TreeNode(6)

        root.left = node1
        root.right = node2

        node1.left = node3
        node1.right = node4
        node2.left = node5
        return root

    def make_tree1(self):
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        node7 = TreeNode(7)

        node1.left = node2
        node1.right = node3

        node2.left = node4
        node2.right = node5
        node3.right = node7
        return node1


my_sol = Solution()

root = my_sol.make_tree()
print(my_sol.isCompleteTree(root)) #True

root = my_sol.make_tree1()
print(my_sol.isCompleteTree(root)) #False

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


