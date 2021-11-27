"""
back edge
cross edge
forward edge
Tree edge
"""

class DFS:
    """
    Graph is adjacency List
    """

    def __init__(self, graph, v):
        self.graph = graph
        self.vertices = v

        self.visited = [0] * self.vertices
        self.time = 0
        self.arr = [0] * self.vertices
        self.dep = [0] * self.vertices
        self.cc = [0] * self.vertices
        self.cycle = False

    def run(self, v, k, parent):

        if self.cycle:
            return

        self.time += 1
        self.arr[v] = self.time
        self.visited[v] = 1
        self.cc[v] = k

        for i in self.graph[v]:
                if self.visited[i] == 0:  # if vertex i is not visited
                    self.run(i, k, v)
                else:  # if vertex i is already visited
                    if i != parent:
                        self.cycle = True
                        return

        self.time += 1
        self.dep[v] = self.time

    def main(self):

        k = 1
        for i in range(self.vertices):
            if self.visited[i] == 0:
                self.run(i, k, None)
                k = k + 1

    def is_cycle(self):

        self.main()
        return self.cycle


M = [
    [1],
    [0]
]

M = [
    [1],
    [0, 2],
    [1, 3],
    [0, 2]
]

dfs = DFS(M, 4)
print(dfs.is_cycle())


