# Reverse a linked list from position m to n. Do it in one-pass.
#
# Note: 1 ≤ m ≤ n ≤ length of list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if n == 0 or not head or m == n:
            return head

        current = head
        previous = None
        count = 1
        reverses = n - m + 1

        while count < m:
            if not current:
                break
            previous = current
            current = current.next
            count += 1

        reversed_head = self.reverse_list(current, reverses)
        if previous:
            previous.next = reversed_head
        else:
            head = reversed_head

        return head

    def reverse_list(self, head, reverses):
        reversed_list_tail = None
        previous = None
        current = head

        count = reverses
        while count != 0 and current:
            if count == reverses:
                reversed_list_tail = current

            count -= 1
            next_node = current.next
            current.next = previous

            previous = current
            current = next_node

        head = previous

        #Append the rest of non reversed list
        while current:
            reversed_list_tail.next = current
            reversed_list_tail = current
            current = current.next

        return head


    def create_list(self):
        #1->2->3->4->5->NULL
        head = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)

        head.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        return head

my_sol = Solution()

head = my_sol.create_list()
m = 2
n = 4
my_sol.reverseBetween(head, m, n)
