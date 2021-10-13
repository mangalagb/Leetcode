#You are a hiker preparing for an upcoming hike. You are given heights,
# a 2D array of size rows x columns, where heights[row][col] represents
# the height of cell (row, col). You are situated in the top-left cell,
# (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1)
# (i.e., 0-indexed). You can move up, down, left, or right, and you wish to
# find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between two
# consecutive cells of the route.
#
# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
import sys


class Solution(object):
    def __init__(self):
        self.cost = sys.maxsize

    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        self.do_DFS(heights)
        return self.cost

    def do_DFS(self, heights):
        visited = set()
        stack = [[0,0]]

        while len(stack) > 0:
            top_of_stack = stack[-1]
            i = top_of_stack[0]
            j = top_of_stack[1]
            current = heights[i][j]
            visited.add((i,j))

            neighbour = self.find_neighbours(i, j, heights, visited)
            if neighbour:
                tuple = (neighbour[0], neighbour[1])
                visited.add(tuple)
                value_of_neighbour = heights[neighbour[0]][neighbour[1]]
                abs_cost = abs(current - value_of_neighbour)
                if value_of_neighbour <= self.cost:
                    self.cost = abs_cost
                    stack.append(neighbour)
            else:
                stack.pop(-1)

    def find_neighbours(self, row, col, heights, visited):
        row_len = len(heights)
        col_len = len(heights[0])

        neighbours = [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]
        for neighbour in neighbours:
            i = neighbour[0]
            j = neighbour[1]

            if i == row_len-1 and j == col_len-1:
                return None

            if 0 <= i < row_len and 0 <= j < col_len:
                if (i,j) not in visited:
                    return neighbour
        return None

my_sol = Solution()

heights = [[1,2,2],[3,8,2],[5,3,5]]
print(my_sol.minimumEffortPath(heights)) #2

