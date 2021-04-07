# #You are given a m x n 2D grid initialized with these three possible values.
#
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to
# represent INF as you may assume that the distance to a gate is less than 2147483647.

# Fill each empty room with the distance to its nearest gate. If it is
# impossible to reach a gate, it should be filled with INF.

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        queue = []
        seen = set()
        self.INF = 2147483647
        for i in range(0, len(rooms)):
            for j in range(0, len(rooms[0])):
                if rooms[i][j] == 0:
                    key = [i, j, 0]
                    queue.append(key)


        while len(queue) > 0:
            first = queue.pop(0)
            i = first[0]
            j = first[1]
            value = first[2]

            #Add to visited
            seen.add(tuple([i, j]))

            #Set value
            rooms[i][j] = value

            neighbours = self.get_neighbours(i, j, rooms)
            if len(neighbours) > 0:
                for neighbour in neighbours:
                    tup = tuple([neighbour[0], neighbour[1]])
                    if tup not in seen:
                        queue.append([neighbour[0], neighbour[1], value+1])
                        seen.add(tup)
        print(rooms)


    def get_neighbours(self, i , j, rooms):
        neighbours = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
        num_rows = len(rooms)
        num_cols = len(rooms[0])

        result = []
        for neighbour in neighbours:
            i = neighbour[0]
            j = neighbour[1]

            if 0 <= i < num_rows and 0 <= j < num_cols and rooms[i][j] == self.INF:
                result.append(neighbour)
        return result


my_sol = Solution()

max_size = 2147483647
matrix = [[max_size, -1, 0, max_size],
          [max_size, max_size, max_size, -1],
          [max_size, -1, max_size, -1],
          [0, -1, max_size, max_size]]
print(my_sol.wallsAndGates(matrix))

#  3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4


