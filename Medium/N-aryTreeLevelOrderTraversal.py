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
        if not root:
            return []

        node_dict = {}
        curr_depth = 0
        queue = [[curr_depth, root]]

        while len(queue) > 0:
            element = queue.pop()
            depth = element[0]
            node = element[1]

            if depth not in node_dict:
                node_dict[depth] = [node.val]
            else:
                node_dict[depth].append(node.val)

            children = node.children
            if children:
                depth += 1
                for child in children:
                    queue.append([depth, child])

        depth = 0
        result = []
        while True:
            if depth in node_dict:
                nodes = node_dict[depth]
                reversed_nodes = nodes[::-1]
                result.append(reversed_nodes)
                depth += 1
            else:
                break

        return result
            


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
print(my_sol.levelOrder(root))