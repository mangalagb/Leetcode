#  A linked list is given such that each node contains an additional
# random pointer which could point to any node in the list or null.
# Return a deep copy of the list.

# Definition for singly-linked list with a random pointer.

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):

    def __init__(self, head = None):
        self.head = None

    def copyRandomList(self, head):

        self.create_list(head)
        print("created list")

        if self.head is None:
            return

        current = self.head
        visited_nodes = {}
        while current is not None:

            current_node = RandomListNode(current.label)
            new_next_node = None
            new_random_node = None
            if current.next is not None:
                new_next_node = RandomListNode(current.next.label)
            if current.random is not None:
                new_random_node = RandomListNode(current.random.label)


            if current_node.label not in visited_nodes:
                visited_nodes[current_node.label] = current_node


            if new_next_node is not None:
                if new_next_node.label in visited_nodes:
                    new_next_node = visited_nodes.get(new_next_node.label)
                    current_node.next = new_next_node
                else:
                    current_node.next = new_next_node
                    visited_nodes[new_next_node.label] = new_next_node

            if new_random_node is not None:
                if new_random_node.label in visited_nodes:
                    new_random_node = visited_nodes.get(new_random_node.label)
                    current_node.random = new_random_node
                else:
                    current_node.random = new_random_node
                    visited_nodes[new_random_node.label] = new_random_node
            visited_nodes[current_node.label] = current_node

            current = current.next






    def create_list(self, head):
        self.head = head
        node1 = RandomListNode(7)
        node2 = RandomListNode(-2)

        self.head.next = node1
        node1.next = node2

        self.head.random = node2
        node1.random = self.head

    def print_list(self):
        current = self.head

        if current is None:
            print("Empty list")
            return

        while current is not None:
            print(current.label,)
            current = current.next

        print("\n____________________________________\n")



head = RandomListNode(4)

my_sol = Solution()
my_sol.copyRandomList(head)
