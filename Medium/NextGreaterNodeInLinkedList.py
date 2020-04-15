# We are given a linked list with head as the first node.
# Let's number the nodes in the list: node_1, node_2, node_3,... etc.
#
# Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val
# such that j > i, node_j.val > node_i.val, and j is the smallest possible choice.
# If such a j does not exist, the next larger value is 0.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        stack = []
        elements = []

        current = head
        counter = 0
        while current:
            value = current.val
            elements.append(0)

            if len(stack) == 0 or value < stack[0][0]:
                stack.insert(0, [value, counter])
            else:
                while len(stack) > 0 and value > stack[0][0]:
                    popped_element = stack.pop(0)
                    popped_index = popped_element[1]
                    elements[popped_index] = value
                stack.insert(0, [value, counter])

            counter += 1
            current = current.next
        return elements


    def make_list2(self):
        head = ListNode(2)
        node1 = ListNode(7)
        node2 = ListNode(4)
        node3 = ListNode(3)
        node4 = ListNode(5)

        head.next = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4
        return head

    def make_list3(self):
        n = [1,7,5,1,9,2,5,1]
        head = ListNode(1)
        node1 = ListNode(7)
        node2 = ListNode(5)
        node3 = ListNode(1)
        node4 = ListNode(9)
        node5 = ListNode(2)
        node6 = ListNode(5)
        node7 = ListNode(1)

        head.next = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node6
        node6.next = node7
        return head

    def make_list1(self):
        head = ListNode(2)
        node1 = ListNode(1)
        node2 = ListNode(5)

        head.next = node1
        node1.next = node2
        return head

my_sol = Solution()

head1 = my_sol.make_list1()
print(my_sol.nextLargerNodes(head1)) #[5, 5, 0]

head2 = my_sol.make_list2()
print(my_sol.nextLargerNodes(head2)) #[7, 0, 5, 5, 0]

head3 = my_sol.make_list3()
print(my_sol.nextLargerNodes(head3)) #[7,9,9,9,0,5,0,0]

