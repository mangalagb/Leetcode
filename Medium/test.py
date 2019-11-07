# Definition for a binary tree node.
import sys

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        max_depth = self.find_max_depth_of_tree(root)
        number_of_nodes = 0
        for i in range(0, max_depth):
            number_of_nodes += 2 ** i

        number_of_nodes += 1

        #If the number of nodes is too high try to simplify the calculation
        if number_of_nodes > sys.maxsize:
            result = self.is_valid_tree(root)
            if not result:
                return False

        tree_array = [None] * (number_of_nodes)
        tree_array[1] = root.val
        value = self.construct_tree_array(root, tree_array, 1)
        if not value:
            return False

        is_complete = True
        null_value_seen = False

        # Find deviations
        for i in range(1, len(tree_array)):
            if tree_array[i] and null_value_seen:
                is_complete = False
                break

            if not tree_array[i]:
                null_value_seen = True
        return is_complete

    def is_valid_tree(self, node):
        if not node:
            return True

        left_child = node.left
        right_child = node.right

        if not left_child and right_child:
            return False

    def find_max_depth_of_tree(self, node):
        if not node:
            return 0

        ldepth = self.find_max_depth_of_tree(node.left)
        rdepth = self.find_max_depth_of_tree(node.right)

        if ldepth > rdepth:
            return ldepth + 1
        else:
            return rdepth + 1

    def construct_tree_array(self, node, tree_array, i):
        if not node:
            return True

        left_child = node.left
        right_child = node.right

        if not left_child and right_child:
            return False

        if left_child or right_child:
            left_index = 2 * i
            right_index = (2 * i) + 1

            if left_child:
                tree_array[left_index] = left_child.val

            if right_child:
                tree_array[right_index] = right_child.val

            left_value = self.construct_tree_array(left_child, tree_array, left_index)
            right_value = self.construct_tree_array(right_child, tree_array, right_index)
            return left_value and right_value
        return True


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line)

            ret = Solution().isCompleteTree(root)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()