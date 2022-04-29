# #You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle).
# You can move up, down, left, or right from and to an empty cell in one step.
#
# Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right
# corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to
# find such walk return -1.
#
class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0

        #queue with length and k obstacles
        queue = [[0,0,0,k]]
        visited = set()
        visited.add((0,0))

        while len(queue) > 0:
            element = queue[0]
            row = element[0]
            col = element[1]
            length = element[2]
            remaining_obstacles = element[3]

            neighbours = self.find_neighbours(row,col, remaining_obstacles, visited, grid)

            if neighbours == -1:
                return length+1
            else:
                #Remove current node
                queue.pop(0)

                #Add neighbour to queue and add to visited
                for neighbour in neighbours:
                    i = neighbour[0]
                    j = neighbour[1]
                    remaining_obstacle = neighbour[2]

                    visited.add((i,j))
                    queue.append([i,j,length+1,remaining_obstacle])
        return -1


    def find_neighbours(self, i,j,remaining_obstacles,visited, grid):
        neighbours = [[i-1,j], [i+1,j], [i,j-1], [i,j+1]]
        row_len = len(grid)
        col_len = len(grid[0])
        result = []

        for neighbour in neighbours:
            i = neighbour[0]
            j = neighbour[1]
            if 0 <= i < row_len and 0 <= j < col_len:
                if (i,j) in visited:
                    continue

                elif i == row_len-1 and j == col_len-1:
                    return -1

                elif grid[i][j] == 0:
                    result.append([i,j, remaining_obstacles])

                elif grid[i][j] == 1:
                    if remaining_obstacles > 0:
                        result.append([i,j, remaining_obstacles-1])
        return result




my_sol = Solution()

# grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
# k = 1
# print(my_sol.shortestPath(grid, k))#6
#
# grid = [[0,1,1],[1,1,1],[1,0,0]]
# k = 1
# print(my_sol.shortestPath(grid, k))#-1

grid = [[0]]
k= 1
print(my_sol.shortestPath(grid, k))#0