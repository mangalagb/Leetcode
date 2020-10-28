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

        if not head:
            return None

        current = head
        previous = None
        duplicate_nodes = set()

        # Find duplicate nodes
        while current is not None:
            if not previous:
                previous = current
            elif previous.val != current.val:
                previous = current
            else:
                duplicate_nodes.add(current.val)
            current = current.next

        # Remove duplicate nodes
        current = head
        previous = None

        while current:
            if current.val in duplicate_nodes:
                duplicate_num = current.val
                while current and current.val == duplicate_num:
                    current = current.next

                if not current:
                    if previous:
                        previous.next = None
                    else:
                        head = None
                elif current and previous:
                    previous.next = current
                # head node is duplicate
                elif current and not previous:
                    head = current

            if current and current.val not in duplicate_nodes:
                previous = current
                current = current.next
        return head



    def create_list1(self):
        #1->1

        head = ListNode(1)
        node2 = ListNode(1)
        node3 = ListNode(3)

        head.next = node2
        node2.next = node3

        return head

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

head = my_sol.create_list1()
my_sol.deleteDuplicates(head)

# head = my_sol.create_list()
# my_sol.deleteDuplicates(head)
