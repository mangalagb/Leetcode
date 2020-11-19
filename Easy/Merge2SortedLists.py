# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = current = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 or l2
        return head.next


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
l1.next = l2
l2.next = l3

my_sol.mergeTwoLists(list_node1, l1)

