class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        if not prerequisites:
            result = [i for i in range(0, numCourses)]
            return result

        graph = self.construct_graph(numCourses, prerequisites)

        top_sort = []
        visited = []
        temp_visited = []

        for i in range(0, numCourses):
            visited.append(False)
            temp_visited.append(False)

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

        #Vist node permanently
        visited[node] = True

        #Add node to head of visited list
        top_sort.insert(0, node)
        return top_sort

    def construct_graph(self, numCourses, prerequisites):
        graph = {}

        for i in range(0, numCourses):
            graph[i] = []

        for prerequisite in prerequisites:
            first_course = prerequisite[1]
            second_course = prerequisite[0]

            values = graph[first_course]
            values.append(second_course)
            graph[first_course] = values
        return graph


my_sol = Solution()

# pairs = [[1,0]]
# print(my_sol.findOrder(2, pairs))
#
# pairs = [[1,0],[2,0],[3,1],[3,2]]
# print(my_sol.findOrder(4, pairs))

# pairs = [[1,0],[0,1]]
# print(my_sol.findOrder(2, pairs))

# pairs = [[3,0],[0,1]]
# print(my_sol.findOrder(4, pairs))
