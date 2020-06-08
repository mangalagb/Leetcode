# There are a total of n courses you have to take, labeled from 0 to n-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is
# expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take
# to finish all courses.
#
# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all
# courses, return an empty array.

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        if not prerequisites:
            result = [i for i in range(0, numCourses)]
            return result

        graph = self.construct_graph(numCourses, prerequisites)

        top_sort = []
        temp_visited = [False] * numCourses
        visited = [False] * numCourses

        # Visit every node in a loop
        for node in graph.keys():
            top_sort = self.topological_sort_helper(node, graph, top_sort,
                                                    visited, temp_visited,
                                                    numCourses)
            #Contains a cycle
            if not top_sort:
                return []

            if len(top_sort) == numCourses:
                return top_sort

        #Such an ordering is not possible
        return []

    def topological_sort_helper(self, node, graph, top_sort, visited,
                                temp_visited, numCourses):

        # The node is already visited
        if visited[node]:
            return top_sort

        # It is not a DAG. Contains a cycle
        if temp_visited[node]:
            return []

        #Visit node temporarily
        temp_visited[node] = True

        # Visit all its neighbours
        neighbours = graph[node]
        for neighbour in neighbours:
            top_sort = self.topological_sort_helper(neighbour, graph, top_sort, visited,
                                         temp_visited, numCourses)
            if not top_sort:
                return []

        # remove temp mark
        temp_visited[node] = False

        #Vist node permanently
        visited[node] = True

        #Add node to head of visited list
        top_sort.append(node)
        return top_sort

    def construct_graph(self, numCourses, prerequisites):
        graph = {}

        for i in range(0, numCourses):
            graph[i] = []

        #Each node n gets prepended to the output list L only after considering all other nodes which depend
        # on n (all descendants of n in the graph).

        for course in prerequisites:

            y = course[0]
            x = course[1]
            graph[y].append(x)


        return graph


my_sol = Solution()

# pairs = [[1,0]]
# print(my_sol.findOrder(2, pairs))

pairs = [[1,0],[2,0],[3,1],[3,2]]
print(my_sol.findOrder(4, pairs)) #[0,1,2,3] or [0,2,1,3]

pairs = [[1,0],[0,1]]
print(my_sol.findOrder(2, pairs)) #[]

pairs = [[3,0],[0,1]]
print(my_sol.findOrder(4, pairs)) #[1, 0, 2, 3]

numCourses = 2
prerequisites = [[1,0]]
print(my_sol.findOrder(numCourses, prerequisites)) #[0,1]
