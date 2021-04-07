#Given a sorted linked list, delete all duplicates such that each element appear only once.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        current = head
        previous = None
        duplicates_found = False

        while current is not None:
            if not previous:
                previous = current
            elif previous.val == current.val:
                duplicates_found = True
            elif previous.val != current.val:
                if duplicates_found:
                    previous.next = current
                    duplicates_found = False
                previous = current
            current = current.next

        # Delete last node which happens to be a duplicate
        if not current and duplicates_found:
            previous.next = None

        return head


    def create_list(self):
        #1->2->3->3->4->4->5

        head = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(3)
        node5 = ListNode(4)
        node6 = ListNode(4)
        node7 = ListNode(5)


        head.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node6
        node6.next = node7
        return head

my_sol = Solution()
head = my_sol.create_list()
my_sol.deleteDuplicates(head)
