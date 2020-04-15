# You need to find the largest value in each row of a binary tree.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return

        node_dict = {}
        queue = [[root, 0]]

        while len(queue) > 0:
            element = queue.pop(0)
            node = element[0]
            depth = element[1]

            if depth not in node_dict:
                node_dict[depth] = [node.val]
            else:
                node_dict[depth].append(node.val)

            if node.left:
                queue.append([node.left, depth+1])

            if node.right:
                queue.append([node.right, depth+1])

        i = 0
        result = []
        while True:
            if i not in node_dict:
                break

            max_number = max(node_dict[i])
            result.append(max_number)
            i += 1
        return result



    def build_tree(self):
        root = TreeNode(1)
        node1 = TreeNode(3)
        node2 = TreeNode(2)
        node3 = TreeNode(5)
        node4 = TreeNode(3)
        node5 = TreeNode(9)

        root.left = node1
        root.right = node2

        node1.left = node3
        node1.right = node4

        node2.right = node5
        return root

my_sol = Solution()

root = my_sol.build_tree()
print(my_sol.largestValues(root))

