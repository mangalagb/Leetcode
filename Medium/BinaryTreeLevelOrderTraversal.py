#Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        tree_dict = {}
        queue = [[root, 1]]

        while len(queue) > 0:
            elements = queue.pop(0)
            node = elements[0]
            depth = elements[1]

            if depth not in tree_dict:
                tree_dict[depth] = [node.val]
            else:
                tree_dict[depth].append(node.val)

            if node.left:
                queue.append([node.left, depth+1])

            if node.right:
                queue.append([node.right, depth+1])

        index = 1
        result = []
        while index in tree_dict:
            result.append(tree_dict[index])
            index += 1

        return result


    def make_tree(self):
        root = TreeNode(6)
        node1 = TreeNode(2)
        node2 = TreeNode(8)
        node3 = TreeNode(4)
        node4 = TreeNode(10)

        root.left = node1
        root.right = node2
        node1.right = node3
        node2.right = node4
        return root

my_sol = Solution()
root = my_sol.make_tree()
print(my_sol.levelOrder(root))
