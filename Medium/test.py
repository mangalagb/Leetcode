def bstDistance(values, n, node1, node2):
    if node1 not in values or node2 not in values:
        return -1

    root = construct_tree(values)

    path1 = find_distance(root, node1, [])
    path2 = find_distance(root, node2, [])
    result1 = set(path1) - set(path2)
    result2 = set(path2) - set(path1)
    length_of_path = len(result1) + len(result2)
    return length_of_path


def find_distance(root, node1, path1):

    path1.append(root.data)
    if node1 == root.data:
        return path1

    if node1 <= root.data:
        return find_distance(root.left, node1, path1)
    elif node1 > root.data:
        return find_distance(root.right, node1, path1)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_helper(value, current_node):
    if value < current_node.data:
        if current_node.left is None:
            current_node.left = Node(value)
        else:
            insert_helper(value, current_node.left)

    elif value > current_node.data:
        if current_node.right is None:
            current_node.right = Node(value)
        else:
            insert_helper(value, current_node.right)

def construct_tree(values):
    if not values:
        return -1

    root = Node(values[0])

    values = values[1:len(values)]
    for value in values:
        insert_helper(value, root)

    return root



nums = [5,6,3,1,2,4]
n = 6
n1 = 2
n2 = 4

print(bstDistance(nums, n, n1, n2))
