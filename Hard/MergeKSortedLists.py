# You are given an array of k linked-lists lists, each linked-list is sorted in
# ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.

#When you put the objects (i.e. tuples) into heap, it will take the first attribute in the object
# (in this case is key) to compare. If a tie happens,
# the heap will use the next attribute (i.e. value_1) and so on.

import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        my_heap = []
        empty_list_count = 0
        i = 0

        for head in lists:
            if head:
                # store value and node in heap.
                # since values can be equal we use a random counter so as not to confuse heap
                heapq.heappush(my_heap, (head.val, i, head))
                i += 1
            else:
                empty_list_count += 1

        if empty_list_count == len(lists):
            return None

        # New linkedlist
        new_head = ListNode(-1)
        new_current = new_head

        while len(my_heap) > 0:
            popped_element = heapq.heappop(my_heap)
            popped_value = popped_element[0]
            popped_node = popped_element[2]

            # Insert into new linked list
            new_node = ListNode(popped_value)
            new_current.next = new_node
            new_current = new_node

            # Replace the popped element with its next element
            next_element = popped_node.next
            if next_element:
                heapq.heappush(my_heap, (next_element.val, i, next_element))
                i += 1

        return new_head.next

    def make_lists(self):
        head1 = ListNode(1)
        node1 = ListNode(4)
        node2 = ListNode(5)
        head1.next = node1
        node1.next = node2

        head2 = ListNode(1)
        node3 = ListNode(3)
        node4 = ListNode(4)
        head2.next = node3
        node3.next = node4

        head3 = ListNode(2)
        node5 = ListNode(6)
        head3.next = node5

        lists = [head1, head2, head3]
        return lists



my_sol = Solution()

lists = my_sol.make_lists()
print(my_sol.mergeKLists(lists))

lists = []
print(my_sol.mergeKLists(lists))

lists = [None]
print(my_sol.mergeKLists(lists))

lists = [None,ListNode(1)]
print(my_sol.mergeKLists(lists))
