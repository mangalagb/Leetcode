# Given a 2d grid map of '1's (land) and '0's (water), count the number
# of islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges
# of the grid are all surrounded by water.
#

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num_of_islands = 0

        for row in range(0, len(grid)):
            for column in range(0, len(grid[0])):
                if grid[row][column] == "1":
                    num_of_islands += 1
                    self.do_DFS(grid, row, column)
        #print(num_of_islands)
        return num_of_islands

    def do_DFS(self, grid, row, column):
        stack = [[row, column]]
        row_length = len(grid)
        column_length = len(grid[0])

        while stack:
            # stack.peek()
            latest_element_on_stack = stack[-1]
            row = latest_element_on_stack[0]
            column = latest_element_on_stack[1]

            # Mark visited
            grid[row][column] = "x"

            neighbour = self.find_unvisited_land(grid, row, column, row_length, column_length)
            if len(neighbour) == 2:
                neighbour_row = neighbour[0]
                neighbour_column = neighbour[1]
                stack.append([neighbour_row, neighbour_column])
            else:
                stack.pop()

    def find_unvisited_land(self, grid, row, column, row_length, column_length):
        neighbours = [[row-1, column], [row+1, column], [row, column-1], [row, column+1]]

        for elements in neighbours:
            i = elements[0]
            j = elements[1]

            if 0 <= i < row_length and 0 <= j < column_length and grid[i][j] == "1":
                return [i, j]
        return []

my_sol = Solution()

# 1 1 1 1 0
# 1 1 0 1 0
# 1 1 0 0 0
# 0 0 0 0 0

t1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(my_sol.numIslands(t1))
