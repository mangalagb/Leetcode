# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
#

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
        head = self.findSumOfLists(l1, l2)
        result = self.tallyCarry(head)
        return result


    def tallyCarry(self, head):
        reverse_head = self.reverseList(head)

        carry = None
        current = reverse_head
        previous = None
        while current:
            value = current.val
            if carry:
                value += 1
                carry = None

            units_digit = value % 10
            tens_digit = value // 10

            if tens_digit != 0:
                carry = 1
            current.val = units_digit
            previous = current
            current = current.next

        if carry:
            new_node = ListNode(1)
            previous.next = new_node

        #Reverse list again after calculating carry
        new_head = self.reverseList(reverse_head)
        return new_head


    def reverseList(self, head):
        current = head
        previous = None

        while current is not None:
            next = current.next
            current.next = previous

            previous = current
            current = next
        head = previous
        return head


    def findSumOfLists(self, l1, l2):
        l1_length = self.find_length_of_list(l1)
        l2_length = self.find_length_of_list(l2)

        difference_in_length = 0
        larger_list_current = None
        smaller_list_current = None
        if l1_length > l2_length:
            larger_list_current = l1
            smaller_list_current = l2
            difference_in_length = l1_length - l2_length
        elif l2_length > l1_length:
            larger_list_current = l2
            smaller_list_current = l1
            difference_in_length = l2_length - l1_length
        else:
            larger_list_current = l1
            smaller_list_current = l2
            difference_in_length = 0

        head3 = None
        previous = None
        while difference_in_length != 0:
            value = larger_list_current.val
            new_node = ListNode(value)

            if not head3:
                head3 = new_node
                previous = new_node
            else:
                previous.next = new_node
                previous = new_node
            difference_in_length -= 1
            larger_list_current = larger_list_current.next

        # add other values
        while larger_list_current is not None and smaller_list_current is not None:
            sum_of_digits = larger_list_current.val + smaller_list_current.val
            new_node = ListNode(sum_of_digits)

            if not head3:
                head3 = new_node
                previous = new_node
            else:
                previous.next = new_node
                previous = new_node
            larger_list_current = larger_list_current.next
            smaller_list_current = smaller_list_current.next

        return head3

    def find_length_of_list(self, l1):
        count = 0
        while l1 is not None:
            count += 1
            l1 = l1.next
        return count

    def create_2_lists(self):
        #(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
        head1 = ListNode(7)
        node2 = ListNode(2)
        node5 = ListNode(4)
        node6 = ListNode(3)

        head2 = ListNode(5)
        node3 = ListNode(6)
        node4 = ListNode(4)

        head1.next = node2
        node2.next = node5
        node5.next = node6

        head2.next = node3
        node3.next = node4

        return head1, head2

    def create_2_lists2(self):
        #(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
        head1 = ListNode(5)

        head2 = ListNode(5)
        return head1, head2

my_sol = Solution()

# l1, l2 = my_sol.create_2_lists()
# my_sol.addTwoNumbers(l1, l2)

l1, l2 = my_sol.create_2_lists2()
my_sol.addTwoNumbers(l1, l2)