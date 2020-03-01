
class Solution(object):
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

    def do_BFS(self, adj_list):

        number_of_nodes = len(adj_list)
        visited = [False] * number_of_nodes

        queue = []
        root = 0

        #visit root
        queue.append(root)
        visited[root] = True
        print(root, sep= " ")

        while len(queue) > 0:
            node = queue.pop()
            visited[node] = True
            print(node, sep=" ")

            child_node = self.get_unvisited_nodes(node, adj_list, visited)
            if child_node != -1:
                queue.append(child_node)

    def get_unvisited_nodes(self, node, adj_list, visited):
        children = adj_list[node]
        for child in children:
            if not visited[child]:
                return child
        return -1




my_sol = Solution()
adj_list = my_sol.create_adj_list()
my_sol.do_BFS(adj_list)
