# Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k),
# where h is the height of the person and k is the number of people in front of this person who have a height greater
# than or equal to h. Write an algorithm to reconstruct the queue.
from operator import itemgetter


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        head = None
        people.sort(key=lambda k: (k[0], -k[1]))

        for person in reversed(people):
            count = 0
            index = person[1]
            current = head
            prev = None

            while count != index:
                if current:
                    prev = current
                    current = current.next
                else:
                    current = ListNode([])
                count += 1

            if not head:
                head = ListNode(person)
            elif current:
                new_node = ListNode(person)
                if prev:
                    prev.next = new_node
                else:
                    head = new_node
                new_node.next = current
            else:
                current = ListNode(person)
                if prev:
                    prev.next = current

        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


my_sol = Solution()

people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(my_sol.reconstructQueue(people))
