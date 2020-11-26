#Given a binary tree root and a linked list with head as the first node.
#
# Return True if all the elements in the linked list starting from the head
# correspond to some downward path connected in the binary tree otherwise return False.
#
# In this context downward path means a path that starts at some node and goes downwards.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        if not head:
            return True

        if not root:
            return False

        elements = self.get_list_contents(head)
        result = self.do_DFS(elements, root)
        return result

    def do_DFS(self, elements, node):
        stack = [node]
        end = len(elements) - 1
        match_found = False
        visited = set()

        while len(stack) > 0:
            current = stack[-1]
            visited.add(current)
            neighbour = self.get_neighbour(current, visited)

            if neighbour is not None:
                stack.append(neighbour)
            else:
                if not match_found:
                    if current.val == elements[end]:
                        match_found = True
                        end -= 1
                else:
                    if current.val == elements[end]:
                        end -= 1
                        if end < 0:
                            return True
                    else:
                        match_found = False
                        end = len(elements) - 1
                stack.pop(-1)
        return False


    def get_neighbour(self, node, visited):
        if node.left and node.left not in visited:
            return node.left
        if node.right and node.right not in visited:
            return node.right
        return None


    def get_list_contents(self, head):
        elements = []
        current = head

        while current:
            elements.append(current.val)
            current = current.next
        return elements


    def make_tree(self):
        root = TreeNode(1)
        node1 = TreeNode(4)
        node2 = TreeNode(4)
        node3 = TreeNode(2)
        node4 = TreeNode(2)
        node5 = TreeNode(1)
        node6 = TreeNode(6)
        node7 = TreeNode(8)
        node8 = TreeNode(1)
        node9 = TreeNode(3)

        root.left = node1
        root.right = node2

        node1.right = node3
        node3.left = node5

        node2.left =node4
        node4.left = node6
        node4.right = node7
        node7.left = node8
        node7.right = node9
        return root

    def make_tree1(self):
        root = TreeNode(1)
        node1 = TreeNode(1)
        node2 = TreeNode(10)
        node3 = TreeNode(9)
        node4 = TreeNode(1)

        root.right = node1
        node1.left = node2
        node1.right = node4
        node2.left = node3
        return root

    def make_linked_list(self):
        # head = ListNode(4)
        # node1 = ListNode(2)
        # node2 = ListNode(8)
        #
        # head.next = node1
        # node1.next = node2
        # return head

        head = ListNode(1)
        node1 = ListNode(4)
        node2 = ListNode(2)
        node3 = ListNode(6)

        head.next = node1
        node1.next = node2
        node2.next = node3
        return head

    def make_linked_list1(self):
        head = ListNode(1)
        node1 = ListNode(10)

        head.next = node1
        return head


my_sol = Solution()

root = my_sol.make_tree()
head = my_sol.make_linked_list()
print(my_sol.isSubPath(head, root)) #True

# root = my_sol.make_tree1()
# head = my_sol.make_linked_list1()
# print(my_sol.isSubPath(head, root)) #True

