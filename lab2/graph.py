from collections import deque


class Graph:

    def __init__(self, edges, n):

        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


def bfs(graph, src, n):

    discovered = [False] * n
    discovered[src] = True

    q = deque()
    q.append((src, -1))

    while q:

        (v, parent) = q.popleft()

        for u in graph.adjList[v]:
            if not discovered[u]:
                discovered[u] = True
                q.append((u, v))
            elif u != parent:
                return True
    return False


if __name__ == '__main__':

    edges = []
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            edges.append(tuple(map(int, line.split())))

    n = len(edges)

    graph = Graph(edges, n)

    if bfs(graph, 0, n):
        with open('result.txt', 'w') as file:
            file.write('True')
    else:
        with open('result.txt', 'w') as file:
            file.write('False')
