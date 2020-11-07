
class Solution(object):

    def do_BFS(self, adj_list):

        number_of_nodes = len(adj_list)
        visited = [False] * number_of_nodes

        queue = []
        root = 0

        # Add root to queue
        queue.append(root)

        while len(queue) > 0:
            node = queue.pop()
            visited[node] = True
            print(node, end=" ")

            unvisited_children = self.get_unvisited_nodes(adj_list[node], visited)
            if len(unvisited_children) > 0:
                queue.extend(unvisited_children)

    def get_unvisited_nodes(self, children, visited):
        #BFS should return all children since we are visiting tree level by level
        unvisited_children = []
        for child in children:
            if not visited[child]:
                unvisited_children.append(child)
        return unvisited_children

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
my_sol.do_BFS(adj_list)
