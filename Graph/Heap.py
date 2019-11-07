import sys

# Definition of a heap.
class Heap(object):
    def __init__(self, max_capacity):
        #Max elements in a heap must be fixed
        self.capacity = max_capacity
        self.size = 0

        #1 extra space for sentinel
        self.elements = [None] * (self.capacity + 1)

        #Sentinel element
        self.elements[0] = -1 * sys.maxsize

    def is_full(self):
        if self.size == self.capacity:
            return True
        return False

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def insert(self, value):
        if self.is_full():
            print("Heap full. Error")
            return

        i = self.size + 1
        while self.elements[i//2] > value:
            self.elements[i] = self.elements[i//2]
            i //= 2

        self.elements[i] = value
        self.size += 1

    def delete_min(self):
        if self.is_empty():
            print("Heap empty. Error")
            return

        min_element = self.elements[1]
        last_element = self.elements[self.size]
        self.elements[self.size] = None

        i = 1
        while i*2 <= self.size:

            #Find if left or right child is smaller
            child = i*2

            if child +1 < self.size:
                if self.elements[child] > self.elements[child+1]:
                    child += 1

            #Percolate down the hole from the root from removing the minimum element
            if last_element > self.elements[child]:
                self.elements[i] = self.elements[child]
            else:
                break
            i = child

        self.elements[i] = last_element
        self.size -= 1
        return min_element

    def print_heap(self):
        print(self.elements)


my_heap = Heap(13)

my_heap.insert(13)
my_heap.insert(14)
my_heap.insert(16)
my_heap.insert(19)
my_heap.insert(21)
my_heap.insert(19)
my_heap.insert(68)
my_heap.insert(65)
my_heap.insert(26)
my_heap.insert(32)
my_heap.insert(31)

my_heap.print_heap()
print(my_heap.delete_min())
my_heap.print_heap()
