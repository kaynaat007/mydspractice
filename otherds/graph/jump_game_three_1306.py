from typing import List

class DFS:

    def __init__(self, graph, arr):

        self.graph = graph
        self.arr = arr
        self.found = False
        self.n = len(graph)
        self.visited = [0] * self.n

    def run(self, v):

        self.visited[v] = 1
        if self.arr[v] == 0:
            self.found = True
            return

        for w in self.graph[v]:
            if self.visited[w] == 0:
                self.run(w)


def canReach(arr: List[int], start: int) -> bool:

    n = len(arr)
    graph = [None] * n
    for i, e in enumerate(arr):
        if i - e >= 0:
            if graph[i] is None:
                graph[i] = [i-e]
            else:
                graph[i].append(i-e)
        if i + e <= n-1:
            if graph[i] is None:
                graph[i] = [i + e]
            else:
                graph[i].append(i + e)

    dfs = DFS(graph, arr)
    print(dfs.graph)
    dfs.run(start)
    return dfs.found


def canReachV2(A, i):
    if 0 <= i < len(A) and A[i] >= 0:
        A[i] = -A[i]
        return A[i] == 0 or canReach(A, i + A[i]) or canReach(A, i - A[i])
    return False


arr  = [4,2,3,0,3,1,2]
start =  5


# arr  = [4,2,3,0,3,1,2]
# start = 0

# arr = [3, 0, 2, 1, 2]
# start = 2

arr = [0]
start = 0

r = canReachV2(arr, start)
print(r)









