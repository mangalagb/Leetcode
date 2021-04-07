# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
#
# k is a positive integer and is less than or equal to the length of the
# linked list. If the number of nodes is not a multiple of k then left-out
# nodes, in the end, should remain as it is.
#
# Follow up:
#
# Could you solve the problem in O(1) extra memory space?
# You may not alter the values in the list's nodes, only nodes itself may be changed.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        reverse_head = head

        current = head
        previous = None
        previous_list = None

        count = 0
        first_reverse = True

        while current:
            while current and count < k:
                previous = current
                current = current.next
                count += 1

            if count < k and not current:
                break

            #split list temporarily
            previous.next = None

            #Reverse list
            new_head, new_tail = self.reverse_list(reverse_head)

            #Patch up the reversed list to existing list
            if first_reverse:
                head = new_head
                first_reverse = False
            else:
                previous_list.next = new_head

            previous_list = new_tail
            new_tail.next = current
            reverse_head = current
            count = 0
        return head


    def reverse_list(self, head):
        new_tail = head

        current = head
        previous = None

        while current:
            next_node = current.next
            current.next = previous

            previous = current
            current = next_node
        new_head = previous
        return new_head, new_tail


    def make_list1(self):
        head = ListNode(1)
        node1 = ListNode(2)
        node2 = ListNode(3)
        node3 = ListNode(4)

        head.next = node1
        node1.next = node2
        node2.next = node3
        return head

    def make_list2(self):
        head = ListNode(1)
        node1 = ListNode(2)

        head.next = node1
        return head

    def make_list(self):
        head = ListNode(1)
        node1 = ListNode(2)
        node2 = ListNode(3)
        node3 = ListNode(4)
        node4 = ListNode(5)

        head.next = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4
        return head

my_sol = Solution()

head = my_sol.make_list()
k = 2
my_sol.reverseKGroup(head, k)

head = my_sol.make_list1()
k = 2
my_sol.reverseKGroup(head, k)

head = my_sol.make_list2()
k = 2
my_sol.reverseKGroup(head, k)
