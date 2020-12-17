#There are N students in a class. Some of them are friends, while some
# are not. Their friendship is transitive in nature. For example, if A
# is a direct friend of B, and B is a direct friend of C, then A is an
# indirect friend of C. And we defined a friend circle is a group of
# students who are direct or indirect friends.

# Given a N*N matrix M representing the friend relationship between
# students in the class. If M[i][j] = 1, then the ith and jth students
# are direct friends with each other, otherwise not. And you have to
# output the total number of friend circles among all the students.

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        row_len = len(M)
        if not row_len:
            return 0
        col_len = len(M[0])
        if not col_len:
            return 0

        adj_list = self.build_graph(M)
        visited = [False] * len(adj_list)

        num_of_friends = 0
        for node in adj_list:
            if not visited[node]:
                self.do_DFS(node, adj_list, visited)
                num_of_friends += 1

        return num_of_friends


    def build_graph(self, M):
        adj_list = {}
        for i in range(0, len(M)):
            adj_list[i] = []

            for j in range(0, len(M[0])):
                if M[i][j] == 1 and i != j:
                    adj_list[i].append(j)
        return adj_list

    def do_DFS(self, node, adj_list, visited):
        stack = [node]

        while len(stack) > 0:
            element = stack[-1]
            visited[element] = True

            neighbour = self.get_neighbour(adj_list[element], visited)
            if neighbour:
                stack.append(neighbour)
            else:
                stack.pop()

    def get_neighbour(self, neighbours, visited):
        for neighbour in neighbours:
            if not visited[neighbour]:
                return neighbour
        return None


my_sol = Solution()

matrix = [[1,1,0],
 [1,1,0],
 [0,0,1]]
print(my_sol.findCircleNum(matrix)) #2

matrix = [[1,1,0],
 [1,1,1],
 [0,1,1]]
print(my_sol.findCircleNum(matrix)) #1

matrix = [
    [1,0,0,1],
    [0,1,1,0],
    [0,1,1,1],
    [1,0,1,1]]
print(my_sol.findCircleNum(matrix)) #1

