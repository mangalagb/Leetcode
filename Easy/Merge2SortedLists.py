# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = None
        result_list = None
        lists_empty = False

        while not lists_empty:
            new_node = None
            if l1 is None and l2 is None:
                lists_empty = True
                break
            elif l1 is not None and l2 is not None:
                if l1.val <= l2.val:
                    new_node = ListNode(l1.val)
                    l1 = l1.next
                elif l2.val < l1.val:
                    new_node = ListNode(l2.val)
                    l2 = l2.next
            elif l1 is not None:
                new_node = ListNode(l1.val)
                l1 = l1.next
            elif l2 is not None:
                new_node = ListNode(l2.val)
                l2 = l2.next

            if not result:
                result = new_node
                result_list = new_node
            else:
                result_list.next = new_node
                result_list = new_node

        self.print_result(result)
        return result

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

