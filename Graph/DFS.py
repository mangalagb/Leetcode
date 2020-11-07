
class Solution(object):

    def do_DFS(self, adj_list):

        number_of_nodes = len(adj_list)
        visited = [False] * number_of_nodes

        root = 0

        # Stack's top is at index 0. so, pop will be at index 0
        stack = [0]

        while len(stack) > 0:
            # stack.peek()
            top_element = stack[0]
            visited[top_element] = True

            # Visit the children of node first
            unvisited_child = self.get_unvisited_node(adj_list[top_element], visited)

            if unvisited_child:
                stack.insert(0, unvisited_child)
            else:
                print(top_element)
                stack.pop(0)


    def get_unvisited_node(self, children, visited):
        # Since it is DFS, visit only one child at a time in depth
        for child in children:
            if not visited[child]:
                return child
        return None

    def create_adj_list(self):
        adj_list = {}

        for i in range(0, 7):
            adj_list[i] = []

        adj_list[0].append(1)

        adj_list[1].append(0)
        adj_list[1].append(2)

        adj_list[2].append(1)
        adj_list[2].append(4)
        adj_list[2].append(5)

        adj_list[4].append(2)

        adj_list[5].append(2)

        adj_list[3].append(0)
        return adj_list

my_sol = Solution()
adj_list = my_sol.create_adj_list()
my_sol.do_DFS(adj_list)
