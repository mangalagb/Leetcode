# Design a data structure that follows the constraints of a Least
# Recently Used (LRU) cache.
#
# Implement the LRUCache class:
#
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists,
# otherwise return -1.
# void put(int key, int value) Update the value of the key if the
# key exists. Otherwise, add the key-value pair to the cache. If the
# number of keys exceeds the capacity from this operation, evict the
# least recently used key.
# Follow up:
# Could you do get and put in O(1) time complexity?

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.nxt = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dict:
            node = self.dict[key]
            self.__remove(node)
            self.__add(node)
            return node.value
        return -1

    def put(self, key, value):
        new_node = Node(key, value)
        if key in self.dict:
            self.__remove(self.dict[key])

        if len(self.dict) == self.capacity:
            node_to_remove = self.head.nxt
            self.__remove(node_to_remove)

        if len(self.dict) < self.capacity:
            self.__add(new_node)

    def __add(self, node):
        # Add to end of list
        previous = self.tail.prev
        previous.nxt = node

        self.tail.prev = node

        node.prev = previous
        node.nxt = self.tail

        self.dict[node.key] = node

    def __remove(self, node):
        previous = node.prev
        next = node.nxt
        if previous:
            previous.nxt = next
        if next:
            next.prev = previous
        del self.dict[node.key]




# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1), end=" ")

cache.put(3, 3)
print(cache.get(2), end=" ")

cache.put(4, 4)
print(cache.get(1), end=" ")

print(cache.get(3), end=" ")
print(cache.get(4), end=" ")

print("\n_________________________\n")
# 1, -1, -1, 3, 4

cache = LRUCache(1)
cache.put(2,1)
print(cache.get(2), end=" ")


print("\n_________________________\n")
#1

cache = LRUCache(2)
print(cache.get(2), end=" ")
cache.put(2,6)
print(cache.get(1), end=" ")
cache.put(1,5)
cache.put(1,2)
print(cache.get(1), end=" ")
print(cache.get(2), end=" ")
print("\n_________________________\n")
# #[-1,-1,,2,6]