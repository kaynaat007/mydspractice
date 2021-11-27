class DFS:

    def __init__(self, graph):

        self.graph = graph
        self.n = len(graph)
        self.visited = [0] * self.n

    def run(self, v):

        self.visited[v] = 1
        for w in self.graph[v]:
            if self.visited[w] == 0:
                self.run(w)

    def main(self):

        self.run(0)
        for v in self.visited:
            if v == 0:
                return False
        return True


graph = [[1],[2],[3],[]]

graph = [[1,3],[3,0,1],[2],[0]]

dfs = DFS(graph)
print(dfs.main())