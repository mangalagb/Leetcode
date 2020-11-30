# In a given grid, each cell can have one of three values:
#
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a
# rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has
# a fresh orange.  If this is impossible, return -1 instead.

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = []
        minute = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i,j, minute])

        max_minutes = 0
        while len(queue) > 0:
            element = queue.pop(0)
            row = element[0]
            col = element[1]
            minute = element[2]

            #Mark maximum minuts
            max_minutes = max(max_minutes, minute)

            #Mark current as rotten
            grid[row][col] = 2

            neighbours = self.get_neighbour_fresh_orange(row, col, minute+1, grid)
            queue.extend(neighbours)

        #Check if any fresh oranges are left after the BFS
        if self.fresh_oranges_left(grid):
            return -1
        else:
            return max_minutes


    def get_neighbour_fresh_orange(self, row, col, minute, grid):
        neighbours = [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]
        unvisited = []

        for neighbour in neighbours:
            i = neighbour[0]
            j = neighbour[1]

            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                unvisited.append([i, j, minute])

                #Temp marking
                grid[i][j] = "X"
        return unvisited


    def fresh_oranges_left(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    return True
        return False

my_sol = Solution()

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(my_sol.orangesRotting(grid)) #4

grid = [[2,1,1],[0,1,1],[1,0,1]]
print(my_sol.orangesRotting(grid)) #-1

grid = [[0,2]]
print(my_sol.orangesRotting(grid)) #0

grid = [[2,2],[1,1],[0,0],[2,0]]
print(my_sol.orangesRotting(grid)) #1
