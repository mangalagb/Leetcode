# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 1->2->3->3->4->4->5
        # 1->2->5
        print(head.val)

        indexes = []
        counter = 1

        current = head.next
        previous = head

        start = None
        end = None
        while current is not None:
            if current.val == previous.val and start is None:
                start = counter

            if current.val != previous.val and start is not None:
                indexes.append([start, counter])
                start = None

            counter += 1
            previous = current
            current = current.next

        print(indexes)






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
