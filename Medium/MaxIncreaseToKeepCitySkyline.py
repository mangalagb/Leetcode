#In a 2 dimensional array grid, each value grid[i][j] represents the
# height of a building located there. We are allowed to increase the
# height of any number of buildings, by any amount (the amounts can be
# different for different buildings). Height 0 is considered to be a building as well.
#
# At the end, the "skyline" when viewed from all four directions of
# the grid, i.e. top, bottom, left, and right, must be the same as the
# skyline of the original grid. A city's skyline is the outer contour
# of the rectangles formed by all the buildings when viewed from a
# distance. See the following example.
#
# What is the maximum total sum that the height of the buildings can be increased?


class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.count = 0
        left_right_row_max, top_bottom_col_max = self.find_max_in_row_and_col(grid)
        self.increase_heights(grid, left_right_row_max, top_bottom_col_max)
        return self.count

    def increase_heights(self, grid, left_right_row_max, top_bottom_col_max):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                current = grid[i][j]

                row_max = left_right_row_max[i]
                col_max = top_bottom_col_max[j]

                if current < col_max and current < row_max:
                    new_height = min(row_max, col_max)
                    extra_height = new_height - current
                    self.count += extra_height
                    grid[i][j] = new_height
        #print(grid)

    def find_max_in_row_and_col(self, grid):
        row_len = len(grid)
        col_len = len(grid[0])

        left_right_row_max = [-1] * col_len
        top_bottom_col_max = [-1] * row_len

        for i in range(0, row_len):
            row_max = -1
            for j in range(0, col_len):
                if grid[i][j] > row_max:
                    row_max = grid[i][j]
            left_right_row_max[i] = row_max

        for j in range(0, col_len):
            col_max = -1
            for i in range(0, row_len):
                if grid[i][j] > col_max:
                    col_max = grid[i][j]
            top_bottom_col_max[j] = col_max

        return left_right_row_max, top_bottom_col_max



my_sol = Solution()

grid = [[3, 0, 8, 4],
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]
print(my_sol.maxIncreaseKeepingSkyline(grid))

            #[ [8, 4, 8, 7],
            # [7, 4, 7, 7],
            # [9, 4, 8, 7],
            # [3, 3, 3, 3] ]
