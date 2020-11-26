# Given a singly linked list, determine if it is a palindrome.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or head.next is None:
            return True

        mid, previous = self.find_middle(head)
        previous.next = None
        reverse_head = self.reverse_list(mid)

        current1 = head
        current2 = reverse_head
        while current1 and current2:
            if current1.val != current2.val:
                return False
            current1 = current1.next
            current2 = current2.next
        return True


    def reverse_list(self, head):
        current = head
        previous = None
        next = None

        while current:
            next = current.next
            current.next = previous

            previous = current
            current = next
        head = previous
        return head

    def find_middle(self, head):
        slow = head
        fast = head
        previous = None

        while slow is not None and fast is not None and fast.next is not None:
            previous = slow
            slow = slow.next
            fast = fast.next.next
        return slow, previous

    def createList(self):
        head = ListNode(1)
        node2 = ListNode(2)

        head.next = node2
        return head

    def createList1(self):
        head = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(2)
        node4 = ListNode(1)

        head.next = node2
        node2.next = node3
        node3.next = node4
        return head

    def createList2(self):
        head = ListNode(1)
        node2 = ListNode(2)
        node5 = ListNode(5)
        node3 = ListNode(2)
        node4 = ListNode(1)

        head.next = node2
        node2.next = node5
        node5.next = node3
        node3.next = node4
        return head

my_sol = Solution()

head = my_sol.createList1()
print(my_sol.isPalindrome(head)) # True

head = my_sol.createList()
print(my_sol.isPalindrome(head)) # False

head = my_sol.createList2()
print(my_sol.isPalindrome(head)) #True