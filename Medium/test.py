class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visited = [False] * numCourses
        temp_visited = [False] * numCourses
        graph = self.build_graph(prerequisites, numCourses)
        top_sort = []

        if len(graph) == 0:
            return True

        result = False
        for i in range(0, numCourses):
            result = self.visit(i, visited, temp_visited, graph, top_sort)
            if not result:
                result = False
                break
        return result

    def build_graph(self, prerequisites, num_of_courses):
        graph = {}
        for num in range(0, num_of_courses):
            graph[num] = []

        for prerequisite in prerequisites:
            class_with_dependency = prerequisite[1]
            class_with_no_dependency = prerequisite[0]
            graph[class_with_dependency].append(class_with_no_dependency)

        return graph


    def visit(self, i, visited, temp_visited, graph, top_sort):
        if visited[i]:
            return True

        if temp_visited[i]:
            return False

        temp_visited[i] = True
        children = graph[i]
        for child in children:
            result = self.visit(child, visited, temp_visited, graph, top_sort)
            if not result:
                return result

        visited[i] = True
        top_sort.insert(0, i)
        return True

my_sol = Solution()

prerequisites = [[1,0]]
num_of_courses = 2
print(my_sol.canFinish(num_of_courses, prerequisites))

num_of_courses = 2
prerequisites = [[1,0],[0,1]]
print(my_sol.canFinish(num_of_courses, prerequisites))

num_of_courses = 1
prerequisites = []
print(my_sol.canFinish(num_of_courses, prerequisites))

num_of_courses = 3
prerequisites = [[1,0]]
print(my_sol.canFinish(num_of_courses, prerequisites))