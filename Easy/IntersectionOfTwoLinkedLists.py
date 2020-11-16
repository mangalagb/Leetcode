#Write a program to find the node at which the intersection of two singly linked lists begins.
# listA = [4, 1, 8, 4, 5], listB = [5, 6, 1, 8, 4, 5]
# A + B = [4, 1, 8, 4, 5, 5, 6, 1, 8, 4, 5]
# B + A = [5, 6, 1, 8, 4, 5, 4, 1, 8, 4, 5]
# so in the end they will intersect

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        current_A = headA
        current_B = headB
        merge_A = False
        merge_B = False
        result = None

        while current_A and current_B:
            if current_A == current_B:
                result = current_A
                break

            current_A = current_A.next
            current_B = current_B.next

            if not current_A and not merge_A:
                current_A = headB
                merge_A = True

            if not current_B and not merge_B:
                current_B = headA
                merge_B = True
        return result


    def create_2_lists(self):
        #listA = [4, 1, 8, 4, 5], listB = [5, 6, 1, 8, 4, 5]
        #A + B = [4, 1, 8, 4, 5, 5, 6, 1, 8, 4, 5]
        #B + A = [5, 6, 1, 8, 4, 5, 4, 1, 8, 4, 5]
        head1 = ListNode(4)
        node2 = ListNode(1)

        head2 = ListNode(5)
        node3 = ListNode(6)
        node4 = ListNode(1)

        node5 = ListNode(8)
        node6 = ListNode(4)
        node7 = ListNode(5)

        head1.next = node2
        node2.next = node5

        head2.next = node3
        node3.next = node4
        node4.next = node5

        node5.next = node6
        node6.next = node7
        return head1, head2

my_sol = Solution()

head1, head2 = my_sol.create_2_lists()
result = my_sol.getIntersectionNode(head1, head2)
if result:
    print(result.val)
