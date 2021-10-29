# #There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for
# room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room
# without having its key.
#
# When you visit a room, you may find a set of distinct keys in it. Each key
# has a number on it, denoting which room it unlocks, and you can take all of
# them with you to unlock the other rooms.
#
# Given an array rooms where rooms[i] is the set of keys that you can obtain
# if you visited room i, return true if you can visit all the rooms, or false otherwise.

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        adj_list = self.create_adj_list(rooms)
        result = self.do_DFS(adj_list)
        return result

    def do_DFS(self, adj_list):
        number_of_rooms = len(adj_list)
        visited = [False] * number_of_rooms

        stack = []
        stack.append(0)

        while len(stack) > 0:
            element = stack[-1]
            visited[element] = True

            unvisited_neighbour = self.find_unvisited_neighbour(adj_list[element], visited)
            if unvisited_neighbour:
                stack.append(unvisited_neighbour)
            else:
                stack.pop(-1)

        #Check if all rooms have been visited
        for visits in visited:
            if not visits:
                return False
        return True

    def find_unvisited_neighbour(self, neighbours, visited):
        for neighbour in neighbours:
            if not visited[neighbour]:
                return neighbour
        return None

    def create_adj_list(self, rooms):
        number_of_rooms = len(rooms)

        adj_list = {}
        for i in range(0, number_of_rooms):
            adj_list[i] = []

        for i in range(0, number_of_rooms):
            keys = rooms[i]
            adj_list[i].extend(keys)
        return adj_list


my_sol = Solution()

rooms = [[1],[2],[3],[]]
print(my_sol.canVisitAllRooms(rooms)) #true

rooms = [[1,3],[3,0,1],[2],[0]]
print(my_sol.canVisitAllRooms(rooms)) #false
