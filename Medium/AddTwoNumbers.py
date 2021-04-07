# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head3 = None
        previous = None
        carry = None

        while l1 is not None or l2 is not None or carry is not None:
            digit1 = 0
            if l1 is not None:
                digit1 = l1.val
                l1 = l1.next

            digit2 = 0
            if l2 is not None:
                digit2 = l2.val
                l2 = l2.next

            sum_of_digits = 0

            # Add carry from previous step
            if carry is not None:
                sum_of_digits += carry
                carry = None

            sum_of_digits += (digit1 + digit2)

            unit_digit = sum_of_digits % 10
            tens_digit = sum_of_digits // 10

            # carry for next step
            if tens_digit != 0:
                carry = tens_digit
            else:
                carry = None

            # Create new node
            new_node = ListNode(unit_digit)
            if head3 is None:
                head3 = new_node
                previous = new_node
            else:
                previous.next = new_node
                previous = new_node

        return head3

    def create_2_lists(self):
        head1 = ListNode(2)
        node2 = ListNode(4)
        node5 = ListNode(3)

        head2 = ListNode(5)
        node3 = ListNode(6)
        node4 = ListNode(4)

        head1.next = node2
        node2.next = node5

        head2.next = node3
        node3.next = node4

        return head1, head2

my_sol = Solution()
l1, l2 = my_sol.create_2_lists()
my_sol.addTwoNumbers(l1, l2)

