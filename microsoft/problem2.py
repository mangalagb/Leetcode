# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, N):
    # write your code in Python 3.6
    if N ==0:
        return 0
    elif N == 1:
        return 0
    elif len(A) == 0 or len(B) == 0:
        return 0

    adj_list = build_graph(A, B, N)

    max_rank = 0
    for node in adj_list.keys():
        visited = [False] * N
        if not visited[node-1]:
            result = do_BFS(node, adj_list, visited)
            max_rank = max(max_rank, result)

    if max_rank == N:
        return max_rank
    else:
        max_rank -= 1
    return max_rank


def do_BFS(node, adj_list, visited):
    queue = set()
    queue.add(node)

    count = 0
    while len(queue) > 0:
        element = queue.pop()
        visited[element-1] = True

        neighbours = adj_list[element]
        for neighbour in neighbours:
            if not visited[neighbour-1]:
                queue.add(neighbour)

    count = 0
    for visit in visited:
        if visit:
            count += 1
    return count


def build_graph(A, B, N):
    adj_list = {}
    for i in range(1, N+1):
        adj_list[i] = []

    i = 0
    while i < len(A):
        first_city = A[i]
        second_city = B[i]

        adj_list[first_city].append(second_city)
        adj_list[second_city].append(first_city)
        i += 1
    return adj_list


# A = [1,2,3,3]
# B = [2,3,1,4]
# N = 4
#
# print(solution(A, B, N)) #4
#
# A = [1,2,4,5, 3]
# B = [2,3,5,6, 4]
# N = 6
# print(solution(A, B, N)) #5

A = [1,2,4,5]
B = [2,3,5,6]
N = 6
print(solution(A, B, N)) #2