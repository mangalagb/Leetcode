#Given a binary tree, return the sum of values of its deepest leaves.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        queue = [[0, root]]
        deepest_leaves = {0: root.val}
        new_height = 0

        while len(queue) > 0:
            popped_element = queue.pop(0)
            height = popped_element[0]
            node = popped_element[1]

            neighbours = self.find_neighbours(node)
            if len(neighbours) > 0:
                new_height = height + 1

                for neighbour in neighbours:
                    queue.append([new_height, neighbour])
                    if new_height in deepest_leaves:
                        deepest_leaves[new_height] += neighbour.val
                    else:
                        deepest_leaves[new_height] = neighbour.val
                        deepest_leaves.pop(height)

        result = deepest_leaves[new_height]
        return result


    def find_neighbours(self, node):
        result = []
        if node.left:
            result.append(node.left)
        if node.right:
            result.append(node.right)
        return result


    def make_tree(self):
        root = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        node6 = TreeNode(6)
        node7 = TreeNode(7)
        node8 = TreeNode(8)

        root.left = node2
        root.right = node3
        node2.left = node4
        node2.right = node5
        node4.left = node7
        node3.right = node6
        node6.right = node8

        return root

my_sol = Solution()

root = my_sol.make_tree()
print(my_sol.deepestLeavesSum(root)) #15
