class Node:
    def __init__(self, val, key, nxt = None):
        self.val = val
        self.key = key
        self.nxt = nxt

class LRUCache(object):
    def __init__(self, capacity):
        self.dummy_head = Node(None, None)
        self.mru = self.dummy_head
        self.capacity = capacity
        self.current_capacity = 0
        self.cache = {}

    def print_list(self):
        current = self.dummy_head
        while current is not None:
            print(current.val, end =" ")
            current = current.nxt
        print("\n")


    def get(self, key):

        if key not in self.cache:
            return -1

        prev_node = self.cache[key]
        current_node = prev_node.nxt

        if not current_node:
            return -1

        if current_node.nxt is not None:
            self.cache[current_node.nxt.key] = self.cache[current_node.key]
            self.cache[current_node.key] = self.mru

        # move current node to end of list as it is most recently used
        self.mru.nxt = current_node
        self.mru = current_node

        prev_node.nxt = current_node.nxt
        current_node.nxt = None

        #Adjust cache
        return current_node.val

    def put(self, key, value):
        if key in self.cache:
            self.get(key)
            self.mru.val = value
            return


        current_node = Node(value, key)
        if self.current_capacity < self.capacity:
            self.current_capacity += 1

        else:
            # Remove from head
            node_to_be_removed = self.dummy_head.nxt
            self.dummy_head.nxt = self.dummy_head.nxt.nxt
            self.cache.pop(node_to_be_removed.key)

            #update reference
            if node_to_be_removed.nxt is not None:
                self.cache[node_to_be_removed.nxt.key] = self.dummy_head

        if self.mru.val is not None:
            self.cache[key] = self.mru
            self.mru.nxt = current_node
            self.mru = current_node
        else:
            self.mru = current_node
            self.dummy_head.nxt = self.mru
            self.cache[key] = self.dummy_head
        #self.print_list()











cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))

cache.put(3, 3)
print(cache.get(2))

cache.put(4, 4)
print(cache.get(1))

print(cache.get(3))
print(cache.get(4))

print("\n_________________________\n")
#1, -1, -1, 3, 4

# cache = LRUCache(1)
# cache.put(2,1)
# cache.get(2)
#
#
# print("\n_________________________\n")



cache = LRUCache(2)
print(cache.get(2))
cache.put(2,6)
print(cache.get(1))
cache.put(1,5)
cache.put(1,2)
print(cache.get(1))
print(cache.get(2))
print("\n_________________________\n")
#[-1,-1,,2,6]

cache = LRUCache(2)
cache.put(2,1)
cache.put(2,2)
print(cache.get(2))

print("\n_________________________\n")








