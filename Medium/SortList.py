# Given the head of a linked list, return the list after sorting it in ascending order.
#
# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        mid, prev = self.find_mid(head)

        #cut the connection between prev and mid
        #to split into 2 lists
        prev.next = None

        #1st list from head to prev
        #2nd list from mid to end
        left_head = self.sortList(head)
        right_head = self.sortList(mid)
        head = self.merge(left_head, right_head)
        return head

    def merge(self, l1, l2):
        new_head = ListNode(-1)
        current = new_head

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        while l1 is not None:
            current.next = l1
            l1 = l1.next
            current = current.next

        while l2 is not None:
            current.next = l2
            l2 = l2.next
            current = current.next

        return new_head.next

    def find_mid(self, head):
        if not head:
            return None

        slow = head
        fast = head
        prev = None

        while slow is not None and fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        return slow, prev

    def createList(self):
        head = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)

        head.next = node2
        node2.next = node3
        node3.next = node4
        return head

my_sol = Solution()

head = my_sol.createList()
result = my_sol.sortList(head)
print(result)
