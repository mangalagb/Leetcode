# Definition for a binary tree node.
import sys


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        stack = []
        prev = None
        current = root

        first = None
        second = None

        while True:
            if current:
                stack.append(current)
                current = current.left

            elif len(stack) > 0:
                current = stack.pop()

                if prev and prev.val > current.val and not first:
                    first = prev

                if prev and prev.val > current.val and first:
                    second = current

                prev = current
                current = current.right

            else:
                break

        #Swap
        temp = first.val
        first.val = second.val
        second.val = temp


    def print_tree(self, node):
        if not node:
            return

        self.print_tree(node.left)
        print(node.val, sep=" ")
        self.print_tree(node.right)

    def make_tree(self):
        root = TreeNode(1)
        node2 = TreeNode(3)
        node3 = TreeNode(2)

        root.left = node2
        node2.right = node3
        return root

    def make_tree1(self):
        root = TreeNode(3)
        node2 = TreeNode(1)
        node3 = TreeNode(4)
        node4 = TreeNode(2)

        root.left = node2
        root.right = node3
        node3.left = node4
        return root

my_sol = Solution()

root = my_sol.make_tree1()
my_sol.recoverTree(root)
my_sol.print_tree(root)

root = my_sol.make_tree()
my_sol.recoverTree(root)
my_sol.print_tree(root)
