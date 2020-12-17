# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.
#
# You can think of the left and right pointers as synonymous to the predecessor
# and successor pointers in a doubly-linked list. For a circular doubly
# linked list, the predecessor of the first element is the last element,
# and the successor of the last element is the first element.
#
# We want to do the transformation in place. After the transformation,
# the left pointer of the tree node should point to its predecessor,
# and the right pointer should point to its successor. You should return
# the pointer to the smallest element of the linked list.

# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        self.head = None
        self.tail = None

        self.do_inorder(root)

        self.head.left = self.tail
        self.tail.right = self.head

        return self.head

    def do_inorder(self, current):
        if not current:
            return None

        #Recurse left
        self.do_inorder(current.left)

        #Add new elements to tail
        if self.tail:
            self.tail.right = current
            current.left = self.tail
        else:
            self.head = current

        self.tail = current

        self.do_inorder(current.right)


    def make_BST(self):
        root = Node(4)
        node1 = Node(2)
        node2 = Node(5)
        node3 = Node(1)
        node4 = Node(3)

        root.left = node1
        root.right = node2
        node1.left = node3
        node1.right = node4
        return root

    def make_BST1(self):
        root = Node(-1)
        node1 = Node(1)
        node2 = Node(9)

        root.right = node1
        node1.right = node2
        return root

    def make_BST2(self):
        root = Node(2)
        node2 = Node(3)

        root.right = node2
        return root

my_sol = Solution()

# root = my_sol.make_BST()
# my_sol.treeToDoublyList(root)
#
root = my_sol.make_BST1()
my_sol.treeToDoublyList(root)
#
# root = None
# my_sol.treeToDoublyList(root)
#
# root = Node(1)
# my_sol.treeToDoublyList(root)
#
# root = my_sol.make_BST2()
# my_sol.treeToDoublyList(root)
