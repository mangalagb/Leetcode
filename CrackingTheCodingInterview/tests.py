# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummy = ListNode(0)
        current = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l1:
            current.next = l1

        if l2:
            current.next = l2

        head = dummy.next
        return head

    def print_result(self, result: ListNode):
        while result is not None:
            print(result.val, end=" ")
            result = result.next
        print("\n_____________________________________________\n")

my_sol = Solution()

list_node1 = ListNode(1)
list_node2 = ListNode(2)
list_node3 = ListNode(4)
list_node1.next = list_node2
list_node2.next = list_node3

l1 = ListNode(1)
l2 = ListNode(3)
l3 = ListNode(4)
l4 = ListNode(100)
l1.next = l2
l2.next = l3
l3.next = l4

new_head = my_sol.mergeTwoLists(list_node1, l1)
my_sol.print_result(new_head)


