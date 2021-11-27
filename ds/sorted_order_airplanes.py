from collections import defaultdict


class DFS:

    def __init__(self, graph, n):
        self.graph = graph
        self.n = n
        self.visited = {}
        for key in graph.keys():
            self.visited[key] = False
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
        for node in self.graph.keys():
            if not self.visited[node]:
                self.dfs(node)

    def get_sorted_output(self):
        return list(reversed(self.sorted_vertices))


if __name__ == '__main__':

    given_input = {
        "SFO": "EWR",
        "SJC": "LAX",
        "DFW": "SJC",
        "EWR": "OAK",
        "LAX": "SFO"
    }
    graph = defaultdict(list)
    for key, val in given_input.items():
        graph[key].append(val)
    n = len(graph.keys())
    dfs = DFS(graph, n)
    dfs.dfs_main()
    print(dfs.get_sorted_output())
