from typing import List
from collections import defaultdict
from collections import deque

"""
a vertex is connected to itself 
converted given grid to adjacency list 
applied standard DFS 
Do not visit those vertices which are water 
"""


class DFS:

    def __init__(self, graph, m, n):

        self.total_vertices = m * n
        self.visited = [0] * self.total_vertices
        self.graph = graph
        self.cc = [-1] * self.total_vertices
        self.total_cc = 0


    def dfs(self, v, k):

        self.visited[v] = 1
        self.cc[v] = k

        for u in self.graph[v]:
            if self.visited[u] == 0:
                self.dfs(u, k)

    def main(self):

        k = 0

        for i in range(self.total_vertices):
            if self.visited[i] == 0 and self.graph[i]:
                self.dfs(i, k)
                k = k + 1

        self.total_cc = k


class BFS:
    def __init__(self, grid):

        self.color = {}
        self.grid = grid

    def bfs(self, i, j, m, n):

        q = deque([(i, j)])
        self.color[(i, j)] = 1  # gray
        while q:
            current_index_i, current_index_j = q.pop()

            if current_index_i - 1 >= 0 and grid[current_index_i - 1][current_index_j] == '1' and \
                     self.color.get((current_index_i - 1, current_index_j)) == 0:

                self.color[(current_index_i - 1, current_index_j)] = 1
                q.append((current_index_i - 1, current_index_j))

            if current_index_i + 1 <= m - 1 and grid[current_index_i + 1][current_index_j] == '1' and \
                    self.color.get((current_index_i + 1, current_index_j)) == 0:

                q.append((current_index_i + 1, current_index_j))
                self.color[(current_index_i + 1, current_index_j)] = 1

            if current_index_j - 1 >= 0 and grid[current_index_i][current_index_j - 1] == '1' and \
                     self.color.get((current_index_i, current_index_j - 1)) == 0:

                q.append((current_index_i, current_index_j - 1))
                self.color[(current_index_i, current_index_j - 1)] = 1

            if current_index_j + 1 <= n - 1 and grid[current_index_i][current_index_j + 1] == '1' and \
                    self.color.get((current_index_i, current_index_j + 1)) == 0:

                q.append((current_index_i, current_index_j + 1))
                self.color[(current_index_i, current_index_j + 1 )] = 1

            self.color[(current_index_i, current_index_j)] = 2  # black. done with this node.

    def main(self):

        m = len(self.grid)
        n = len(self.grid[0])

        for i in range(m):
            for j in range(n):
                self.color[(i, j)] = 0  # white

        k = 0
        for i in range(m):
            for j in range(n):
                if self.color[(i, j)] == 0 and self.grid[i][j] == '1':
                    self.bfs(i, j, m, n)
                    k += 1
        return k


def convert_into_adjacency_list(grid):

    m = len(grid)
    n = len(grid[0])
    graph = defaultdict(list)

    for i in range(m * n):
        graph[i] = []

    k = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                graph[k].append(k)
                if i - 1 >= 0 and grid[i-1][j] == '1':
                    graph[k].append(k-n)
                if i + 1 <= m-1 and grid[i+1][j] == '1':
                    graph[k].append(k+n)
                if j - 1 >= 0 and grid[i][j-1] == '1':
                    graph[k].append(k-1)
                if j + 1 <= n-1 and grid[i][j+1] == '1':
                    graph[k].append(k+1)
            k += 1
    return graph


def numIslands(grid: List[List[str]]) -> int:

    if not grid:
        return 0

    m = len(grid)
    n = len(grid[0])

    graph = convert_into_adjacency_list(grid)

    print(graph)

    dfs = DFS(graph, m, n)
    dfs.main()
    print(dfs.cc)
    return dfs.total_cc


def numIslandsBFS(grid: List[List[str]]) -> int:

    if not grid:
        return 0

    bfs = BFS(grid)
    return bfs.main()




# grid =  [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


#
# grid = [
#     ['1', '1', '1', '1'],
#     ['1', '1', '0', '1']
# ]


#
# grid = []

print(numIslandsBFS(grid))






