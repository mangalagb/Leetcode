# Given a binary tree, you need to compute the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two
# nodes in a tree. This path may or may not pass through the root.

# To this point, we are clear about one thing. To find the diameter of a tree, we need to process
# the left and right sub-tree first. This implies that using a post-order traversal may be
# helpful here. It makes sure that we traverse the left and right sub-tree before moving to the root.
#
# Here is an image showing maximum depth of each of the nodes in the tree. The diameter
# of the tree is the maximum value of (left_depth + right_depth) among each of the nodes.

# https://studyalgorithms.com/tree/diameter-of-a-binary-tree/

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        depth_map = {}
        stack = [root]
        max_diameter = 0

        while len(stack) > 0:
            current = stack[-1]

            if current.left and current.left not in depth_map:
                stack.append(current.left)
            elif current.right and current.right not in depth_map:
                stack.append(current.right)
            else:
                # Process the root, once left and right sub-tree have been processed
                stack.pop()

                ldepth = depth_map.get(current.left, 0)
                rdepth = depth_map.get(current.right, 0)

                #max height of tree at current
                max_height = 1 + max(ldepth, rdepth)
                depth_map[current] = max_height

                #max path length max(left_tree, right_tree, current diameter)
                max_diameter = max(ldepth + rdepth, max_diameter)
        return max_diameter


    def make_tree(self):
        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(3)
        node3 = TreeNode(4)
        node4 = TreeNode(5)

        root.left = node1
        root.right = node2

        node1.left = node3
        node1.right = node4
        return root

my_sol = Solution()

root = my_sol.make_tree()
print(my_sol.diameterOfBinaryTree(root)) #3
