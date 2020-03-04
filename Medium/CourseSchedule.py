# There are a total of n courses you have to take, labeled from 0 to n-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to
#  first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        if not prerequisites:
            return True

        graph = self.construct_graph(prerequisites, numCourses)
        result = True

        # Initially all nodes are unvisited
        top_sort = []
        temp_visited = [False] * numCourses
        visited = [False] * numCourses

        for i in range(0, numCourses):
            result = self.visit(i, top_sort, visited, temp_visited,
                           graph)
            if not result:
                return False

            if len(top_sort) == numCourses:
                return True
        return True

    def construct_graph(self, prerequisites, numCourses):
        graph = {}

        for i in range(0, numCourses):
            graph[i] = []

        for prerequisite in prerequisites:
            first_course = prerequisite[0]
            second_course = prerequisite[1]

            graph[first_course].append(second_course)
        return graph

    def visit(self, node, top_sort, visited, temp_visited,
              graph):
        if visited[node]:
            return True

        if temp_visited[node]:
            return False


        # Mark node temporarily
        temp_visited[node] = True

        #Visit all its neighbours
        neighbours = graph[node]
        for neighbour in neighbours:
            result = self.visit(neighbour, top_sort, visited,
                                temp_visited, graph)
            if not result:
                return False

        # Mark node permanently
        visited[node] = True

        # Add node to head of list
        top_sort.insert(0, node)
        return True

my_sol = Solution()

pairs = [[1,0],[0,1]]
print(my_sol.canFinish(2, pairs))

pairs = [[1,0]]
print(my_sol.canFinish(2, pairs))

pairs = [[3,0],[0,1]]
print(my_sol.canFinish(4, pairs))

pairs = []
print(my_sol.canFinish(1, pairs))

