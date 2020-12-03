class Node():
    def __init__(self, key=0, value=0, previous=None, next=None):
        self.key = key
        self.value = value
        self.previous = previous
        self.next = next

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.max_capacity = capacity
        self.current_capacity = 0
        self.node_dict = {}

        #Double linked list
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.previous = self.head


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.node_dict:
            node = self.node_dict[key]
            result = node.value
            self.remove(node)
            self.add(node)
            return result
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        new_node = Node(key, value)

        if key in self.node_dict:
            self.remove(self.node_dict[key])

         #Remove least recently used (from tail)
        if self.current_capacity == self.max_capacity:
            self.remove(self.tail.previous)


        #Add to head
        self.add(new_node)
        self.node_dict[key] = new_node


    def add(self, node):
        prev_node = self.head
        next_node = self.head.next

        node.previous = prev_node
        prev_node.next = node

        node.next = next_node
        next_node.previous = node
        self.current_capacity += 1
        self.node_dict[node.key] = node


    def remove(self, node):
        prev_node = node.previous
        next_node = node.next

        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.previous = prev_node
        self.current_capacity -= 1
        self.node_dict.pop(node.key)

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
