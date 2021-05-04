#Given a 2D grid consists of 0s (land) and 1s (water).  An island is a
# maximal 4-directionally connected group of 0s and a closed island is
# an island totally (all left, top, right, bottom) surrounded by 1s.

#Return the number of closed islands.

class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #Eliminate all corner 0s as they are not closed
        self.remove_border_regions(grid)

        #Do a DFS on the rest of water
        num_of_islands = 0
        row_len = len(grid)
        col_len = len(grid[0])
        for i in range(1, row_len-1):
            for j in range(1, col_len-1):
                if grid[i][j] == 0:
                    num_of_islands += 1
                    self.do_DFS(grid, i, j, "y")
        return num_of_islands

    def remove_border_regions(self, grid):
        row_len = len(grid)
        col_len = len(grid[0])

        for i in range(0, row_len):
            if grid[i][0] == 0:
                self.do_DFS(grid, i, 0, "x")

            if grid[i][col_len-1] == 0:
                self.do_DFS(grid, i, col_len-1, "x")

        for j in range(0, col_len):
            if grid[0][j] == 0:
                self.do_DFS(grid, 0, j, "x")

            if grid[row_len-1][j] == 0:
                self.do_DFS(grid, row_len-1, j, "x")

    def do_DFS(self, grid, row, col, symbol):
        stack = [[row, col]]

        while len(stack) > 0:
            top_element = stack[-1]
            row = top_element[0]
            col = top_element[1]

            #Mark current as visited
            grid[row][col] = symbol

            neighbour = self.find_unvisited_neighbour(grid, row, col)
            if len(neighbour) == 2:
                stack.append(neighbour)
            else:
                stack.pop()


    def find_unvisited_neighbour(self, grid, row, col):
        neighbours = [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]
        row_len = len(grid)
        col_len = len(grid[0])

        for neighbour in neighbours:
            i = neighbour[0]
            j = neighbour[1]

            if 1 <= i < row_len-1 and 1 <= j <col_len-1 and grid[i][j] == 0:
                return neighbour
        return []


my_sol = Solution()

grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
print(my_sol.closedIsland(grid)) #2

grid = [[0,0,1,0,0],
        [0,1,1,1,0],
        [0,1,0,1,0],
        [0,1,0,1,0]]
print(my_sol.closedIsland(grid)) #0

grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
print(my_sol.closedIsland(grid)) #2

grid = [[0,0,1,1,0,1,0,0,1,0],[1,1,0,1,1,0,1,1,1,0],[1,0,1,1,1,0,0,1,1,0],[0,1,1,0,0,0,0,1,0,1],
 [0,0,0,0,0,0,1,1,1,0],[0,1,0,1,0,1,0,1,1,1],[1,0,1,0,1,1,0,0,0,1],[1,1,1,1,1,1,0,0,0,0],
 [1,1,1,0,0,1,0,1,0,1],[1,1,1,0,1,1,0,1,1,0]]
print(my_sol.closedIsland(grid)) #5


