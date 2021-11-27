
class DFS:

    def __init__(self, graph, n):
        self.graph = graph
        self.n = n
        self.visited = [False for _ in range(n)]
        self.sorted_vertices = []

    def dfs(self, i):
        """
        """
        self.visited[i] = True
        for u in self.graph[i]:
            if not self.visited[u]:
                self.dfs(u)
        self.sorted_vertices.append(i)

    def dfs_main(self):
        """
        """
        for i in range(self.n):
            if not self.visited[i]:
                self.dfs(i)

    def get_sorted_output(self):
        return list(reversed(self.sorted_vertices))


graph = {

    0: [1],
    1: [2],
    2: [3],
    3: [4],
    4: [5],
    5: []
}
n = 6


graph = {

    0: [1, 3],
    1: [2],
    2: [3],
    3: []
}
n = 4


dfs = DFS(graph, n)
dfs.dfs_main()
print(dfs.get_sorted_output())







