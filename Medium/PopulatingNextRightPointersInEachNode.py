#You are given a perfect binary tree where all leaves are on the same level, and every
# parent has two children.
#Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.
#Initially, all next pointers are set to NULL.


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        current_depth = 0
        queue = [[root, current_depth]]

        while len(queue) > 0:
            neighbours = self.get_neighbours(queue, current_depth)
            current_depth += 1

            previous = None
            for neighbour in neighbours:
                # Set next pointer
                if not previous:
                    previous = neighbour
                else:
                    previous.next = neighbour
                    previous = neighbour

                # Push left and right child to queue
                if neighbour.left and neighbour.right:
                    queue.append([neighbour.left, current_depth])
                    queue.append([neighbour.right, current_depth])
        return root


    def get_neighbours(self, queue, depth):
        neighbours = []

        while len(queue) > 0 and queue[0][1] == depth:
            node = queue.pop(0)
            neighbours.append(node[0])
        return neighbours


    def make_tree(self):
        root = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)
        node7 = Node(7)

        root.left = node2
        root.right = node3
        node2.left = node4
        node2.right = node5
        node3.left = node6
        node3.right = node7
        return root

my_sol = Solution()

root = my_sol.make_tree()
my_sol.connect(root)
