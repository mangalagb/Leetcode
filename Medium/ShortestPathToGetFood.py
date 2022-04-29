# #You are starving and you want to eat food as quickly as possible. You want to find the shortest path to
# arrive at any food cell.
#
# You are given an m x n character matrix, grid, of these different types of cells:
#
# '*' is your location. There is exactly one '*' cell.
# '#' is a food cell. There may be multiple food cells.
# 'O' is free space, and you can travel through these cells.
# 'X' is an obstacle, and you cannot travel through these cells.
# You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.
#
# Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach
# food, return -1.
import sys


class Solution(object):
    def getFood(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #Find start
        start_i = -1
        start_j = -1
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == "*":
                    start_i = i
                    start_j = j
                    break

        #Queue for BFS
        queue = [[start_i, start_j, 0]]
        visited = set()
        visited.add((start_i,start_j))

        while len(queue) > 0:
            element = queue[0]
            row = element[0]
            col = element[1]
            length = element[2]

            neighbours = self.find_neighbours(row, col, grid, visited)
            #found food
            if neighbours == -1:
                food_len = length + 1
                return food_len
            else:
                queue.pop(0)
                for neighbour in neighbours:
                    queue.append([neighbour[0], neighbour[1], length+1])
                    visited.add((neighbour[0], neighbour[1]))

        return -1

    def find_neighbours(self, i, j, grid, visited):
        neighbours = [[i-1,j], [i+1, j], [i, j-1], [i,j+1]]
        row_len = len(grid)
        col_len = len(grid[0])
        result = []

        for neighbour in neighbours:
            row = neighbour[0]
            col = neighbour[1]

            if 0 <= row < row_len and 0 <= col < col_len:
                if (row,col) in visited:
                    continue

                if grid[row][col] == "O":
                    result.append([row,col])
                elif grid[row][col] == "#":
                    result = -1
                    break

        return result


my_sol = Solution()

grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
print(my_sol.getFood(grid))#3

grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
print(my_sol.getFood(grid))#-1

grid = [["X", "X", "X", "X", "X", "X", "X", "X"], ["X", "*", "O", "X", "O", "#", "O", "X"],
        ["X", "O", "O", "X", "O", "O", "X", "X"], ["X", "O", "O", "O", "O", "#", "O", "X"],
        ["X", "X", "X", "X", "X", "X", "X", "X"]]
print(my_sol.getFood(grid))#6
