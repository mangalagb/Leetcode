# Given a binary tree, imagine yourself standing on the right side
# of it, return the values of the nodes you can see ordered from top to bottom.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        result = self.do_BFS(root)
        return result

    def do_BFS(self, node):
        if not node:
            return

        depth_dict = {}
        queue = [[0, node]]

        while len(queue) > 0:
            element = queue.pop(0)
            depth = element[0]
            node = element[1]

            if depth not in depth_dict:
                depth_dict[depth] = node.val

            if node.right:
                queue.append([depth+1, node.right])
            if node.left:
                queue.append([depth+1, node.left])

        i = 0
        result = []
        while i in depth_dict:
            result.append(depth_dict[i])
            i += 1
        return result


    def make_tree(self):
        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(3)
        node3 = TreeNode(4)
        node4 = TreeNode(5)

        root.left = node1
        root.right = node2
        node1.right = node4
        node2.right = node3
        return root

    def make_tree1(self):
        #[1,2,3,4]
        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(3)
        node3 = TreeNode(4)

        root.left = node1
        root.right = node2

        node1.left = node3
        return root

my_sol = Solution()

root = my_sol.make_tree()
print(my_sol.rightSideView(root)) #[1, 3, 4]

root = my_sol.make_tree1()
print(my_sol.rightSideView(root)) #[1,3,4]
