# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        if not head:
            return

        current_node = head
        previous_node = None
        next_node = None

        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node

            previous_node = current_node
            current_node = next_node
        head = previous_node
        return head

    def createList(self):
        head = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)

        head.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        self.reverseList(head)

my_sol = Solution()

my_sol.createList()
