# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
#
# To represent a cycle in the given linked list, we use an integer pos which represents
# the position (0-indexed) in the linked list where tail connects to. If pos is -1,
# then there is no cycle in the linked list.
# Note: Do not modify the linked list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        loop = self.hasCycle(head)
        slow = head
        if loop:
            while slow is not None and loop is not None:
                slow = slow.next
                loop = loop.next

                if slow.val == loop.val:
                    return slow


    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return None

        slow = head
        fast = head

        while slow is not None and fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return slow

        return None

    def create_list(self):
        head = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)

        head.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = head
        return head

my_sol = Solution()

head = my_sol.create_list()
my_node = my_sol.detectCycle(head)
if my_node:
    print(my_node.val)
else:
    print("None")