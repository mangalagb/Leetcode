#Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        values = set()

        #Traverse from p to root
        current = p
        while current is not None:
            values.add(current.val)
            current = current.parent

        #Traverse from q to root
        current = q
        while current is not None:
            if current.val in values:
                return current

            current = current.parent

        return None




    def make_tree(self):
        root = Node(3)
        root.parent = None

        node1 = Node(5)
        node1.parent = root

        node2 = Node(1)
        node2.parent = root

        node3 = Node(6)
        node3.parent = node1

        node4 = Node(2)
        node4.parent = node1

        node5 = Node(7)
        node5.parent = node4

        node6 = Node(4)
        node6.parent = node4

        node7 = Node(0)
        node7.parent = node2

        node8 = Node(8)
        node8.parent = node2

        root.left = node1
        root.right = node2

        node1.left = node3
        node1.right = node4

        node4.left = node5
        node4.right = node6
        node2.left = node7
        node2.right = node8

        return node1,node2

my_sol = Solution()

p,q = my_sol.make_tree()
ans = my_sol.lowestCommonAncestor(p,q)
if ans:
    print(ans.val) #3
