class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = self.make_graph(numCourses, prerequisites)

        temp_visited = [False] * numCourses
        visited = [False] * numCourses
        result = []

        for i in range(0, numCourses):
            ans = self.visit(i, temp_visited, visited, graph, result)
            if not ans:
                return []

            if len(result) == numCourses:
                return result

    def visit(self, current, temp_visited, visited, graph, result):
        if visited[current]:
            return True

        if temp_visited[current]:
            return False

        #Temp mark current
        temp_visited[current] = True

        #visit its dependencoies
        neighbours = graph[current]
        for neighbour in neighbours:
            ans = self.visit(neighbour, temp_visited, visited, graph, result)
            if not ans:
                return False

        #remove temp mark
        temp_visited[current] = False

        #Mark current as permanent
        visited[current] = True

        #Add current to beginning of result
        result.insert(0, current)
        return True


    def make_graph(self, numCourses, prerequisites):
        graph = {}
        for i in range(0, numCourses):
            graph[i] = []

        # y depends on x => first do x then y => graph[y] = x
        for course in prerequisites:
            y = course[0]
            x = course[1]
            graph[y].append(x)

        return graph

my_sol = Solution()
#
# numCourses = 2
# prerequisites = [[1,0]]
# print(my_sol.findOrder(numCourses, prerequisites)) #[0,1]

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(my_sol.findOrder(numCourses, prerequisites)) #[0,1,2,3] or [0,2,1,3]

# numCourses = 2
# prerequisites = [[0,1],[1,0]]
# print(my_sol.findOrder(numCourses, prerequisites)) #[]
#
# pairs = [[3,0],[0,1]]
# print(my_sol.findOrder(4, pairs)) #[1, 0, 2, 3]

