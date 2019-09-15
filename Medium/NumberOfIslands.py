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
        print(grid)


        num_of_islands = 0

        element_index = [0,0]






my_sol = Solution()

i1 = [[1,1,1,1,0],
[1,1,0,1,0],
[1,1,0,0,0],
[0,0,0,0,0]]

my_sol.numIslands(i1)