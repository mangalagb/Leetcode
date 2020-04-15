#Given a linked list and a value x, partition it such that all nodes less than x come before nodes
# greater than or equal to x.

#You should preserve the original relative order of the nodes in each of the two partitions.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        node1 = None
        node2 = None
        left_head = None
        right_head = None

        current = head
        while current is not None:
            num = current.val

            if num < x:
                if node1 is None:
                    node1 = current
                    left_head = node1
                else:
                    node1.next = current
                    node1 = node1.next

            else:
                if node2 is None:
                    node2 = current
                    right_head = node2
                else:
                    node2.next = current
                    node2 = node2.next
            current = current.next

        if left_head is not None:
            node1.next = right_head
        else:
            left_head = right_head

        if right_head:
            node2.next = None
        return left_head


    def make_list(self):
        head = ListNode(1)
        node1 = ListNode(4)
        node2 = ListNode(3)
        node3 = ListNode(2)
        node4 = ListNode(5)
        node5 = ListNode(2)

        head.next = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        return head


my_sol = Solution()

x = 3
head = my_sol.make_list()
my_sol.partition(head, x)