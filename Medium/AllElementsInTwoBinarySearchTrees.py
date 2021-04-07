# Given two binary search trees root1 and root2.
#
# Return a list containing all the integers from both trees sorted in ascending order.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        if not root1 and not root2:
            return []
        elif not root1:
            return self.get_single_list(root2)
        elif not root2:
            return self.get_single_list(root1)

        tree1 = self.get_single_list(root1)
        tree2 = self.get_single_list(root2)

        result = [-1] * (len(tree1) + len(tree2))

        i = 0
        j = 0
        counter = 0

        while True:
            if i < len(tree1) and j < len(tree2):
                if tree1[i] <= tree2[j]:
                    result[counter] = tree1[i]
                    i += 1
                else:
                    result[counter] = tree2[j]
                    j += 1
            elif i < len(tree1):
                result[counter] = tree1[i]
                i += 1
            elif j < len(tree2):
                result[counter] = tree2[j]
                j += 1
            else:
                break
            counter += 1
        return result

    def get_single_list(self, root):
        stack = []
        result = []

        current = root
        while current or len(stack) > 0:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop(-1)
            result.append(current.val)
            current = current.right
        return result


    def create_tree(self):
            root1 = TreeNode(2)
            node1 = TreeNode(1)
            node2 = TreeNode(4)

            root1.left = node1
            root1.right = node2

            root2 = TreeNode(1)
            node3 = TreeNode(0)
            node4 = TreeNode(3)

            root2.left = node3
            root2.right = node4
            return root1, root2

    def create_tree1(self):
            root1 = TreeNode(0)
            node1 = TreeNode(-10)
            node2 = TreeNode(10)

            root1.left = node1
            root1.right = node2

            root2 = TreeNode(5)
            node3 = TreeNode(1)
            node4 = TreeNode(7)
            node5 = TreeNode(0)
            node6 = TreeNode(2)

            root2.left = node3
            root2.right = node4
            node3.left = node5
            node3.right = node6
            return root1, root2

my_sol = Solution()

root1, root2 = my_sol.create_tree()
print(my_sol.getAllElements(root1, root2)) #[0,1,1,2,3,4]

root1, root2 = my_sol.create_tree1()
print(my_sol.getAllElements(root1, root2)) #[-10, 0, 0, 0, 0, 1, 2, 5, 7]
