#Given a linked list, remove the n-th node from the end of list and
# return its head in a single pass.


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def insert(self, data):
        if self.head.data is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = Node(data)

    def print_list(self):
        if self.head is None:
            print("Empty list")
            return

        print("\n")
        current = self.head
        while current is not None:
            print(current.data, end= ' ')
            current = current.next


def initialize_list():
    my_list = LinkedList()
    my_list.insert(10)
    my_list.insert(20)
    my_list.insert(30)
    my_list.insert(40)
    my_list.insert(50)
    return my_list


def find_nth_from_last_again(n, head):
    counter = 0

    slow = None
    fast = head

    while fast.next is not None:
        counter += 1
        if counter == n:
            slow = head
        fast = fast.next

        if slow is not None and counter != n:
            slow = slow.next

    #Remove head
    if fast is not None and counter == n-1 and slow is None:
        head = head.next
    else:
        slow.next = slow.next.next
    return head


my_list = initialize_list()
my_list.print_list()
find_nth_from_last_again(2, my_list.head)
my_list.print_list()

