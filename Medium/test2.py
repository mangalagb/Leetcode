#You are a hiker preparing for an upcoming hike. You are given heights,
# a 2D array of size rows x columns, where heights[row][col] represents
# the height of cell (row, col). You are situated in the top-left cell,
# (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1)
# (i.e., 0-indexed). You can move up, down, left, or right, and you wish to
# find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between two
# consecutive cells of the route.
#
# Return the minimum effort required to travel from the top-left cell to the bottom-right
# cell.
import sys


class Solution(object):
    def __init__(self):
        self.all_paths = []

    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        start = (0,0)
        row_len = len(heights)-1
        col_len = len(heights[0])-1
        end = (row_len, col_len)
        path = [heights[0][0]]
        visited = set()
        visited.add(start)

        self.do_DFS(start, end, path, visited, heights)

        for path in self.all_paths:
            print(path)

    def do_DFS(self, start, end, path, visited, heights):
        if start[0] == end[0] and start[1] == end[1]:
            print("path found")
            self.all_paths.append(path)

        neighbour = self.find_neighbour(start, visited, heights)
        if neighbour is not None:
            neighbour_value = heights[neighbour[0]][neighbour[1]]

            #Add neighbour value to path
            path.append(neighbour_value)
            visited.add(neighbour)

            #Do a DFS of all neighbours till you reach end
            self.do_DFS(neighbour, end, path, visited, heights)

            #Bactrack and remove neighbour value from path to explore new paths
            path.pop(-1)
            visited.remove(neighbour)

    def find_neighbour(self, node, visited, heights):
        row = node[0]
        col = node[1]
        neighbours = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
        row_len = len(heights)
        col_len = len(heights[0])

        for neighbour in neighbours:
            i = neighbour[0]
            j = neighbour[1]
            if 0 <= i < row_len and 0 <= j < col_len:
                if neighbour not in visited:
                    return neighbour
        return None


my_sol = Solution()

heights = [[1,2,2],[3,8,2],[5,3,5]]
print(my_sol.minimumEffortPath(heights)) #2

