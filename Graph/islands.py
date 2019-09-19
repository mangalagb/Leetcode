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

        #Initialize visited array
        visited = []
        for i in range(0, len(grid)):
            row = []
            for j in range(0, len(grid[0])):
                row.append(False)
            visited.append(row)

        for row in range(0, len(grid)):
            for column in range(0, len(grid[0])):
                if grid[row][column] == 1 and visited[row][column] is False:
                    num_of_islands += 1
                    self.do_DFS(grid, row, column, visited)
        print(num_of_islands)

    def do_DFS(self, grid, row, column, visited):
        stack = [[row, column]]
        visited[row][column] = True
        row_length = len(grid)
        column_length = len(grid[0])

        while len(stack) > 0:
            latest_element_on_stack = stack[len(stack)-1]
            row = latest_element_on_stack[0]
            column = latest_element_on_stack[1]

            neighbour = self.find_unvisited_land(visited, row, column, row_length, column_length)
            if len(neighbour) == 2:
                visited[neighbour[0]][neighbour[1]] = True
                stack.append([neighbour[0], neighbour[1]])
            else:
                stack.pop()

    def find_unvisited_land(self, visited, row, column, row_length, column_length):
        rows_to_check = [row-1, row+1]
        columns_to_check = [column-1, column+1]

        for i in rows_to_check:
            for j in columns_to_check:
                if 0 <= i < row_length and 0 <= j < column_length and visited[i][j] is False:
                    return [i , j]

        return []

my_sol = Solution()

# 1 1 1 1 0
# 1 1 0 1 0
# 1 1 0 0 0
# 0 0 0 0 0

i1 = [[1,1,1,1,0],
[1,1,0,1,0],
[1,1,0,0,0],
[0,0,0,0,0]]

i2 = [[1,1,0,0,0],
[1,1,0,0,0],
[0,0,1,0,0],
[0,0,0,1,1]]

i3 = [[1,1,0,0,0],
[0,0,0,0,0],
[0,0,1,0,0],
[0,0,0,0,1]]

my_sol.numIslands(i1)
# my_sol.numIslands(i2)
# my_sol.numIslands(i3)
