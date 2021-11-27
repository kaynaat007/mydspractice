from typing import List


class DFS:

    def __init__(self, graph):
        self.graph = graph
        self.vertices = len(graph)
        self.target = self.vertices - 1

    def run(self, v):

        paths = []
        if v == self.target:
            paths.append([v])
            return paths

        for w in self.graph[v]:
            E = self.run(w)
            for e in E:
                e.append(v)
                paths.append(e)
        return paths


def allPathsSourceTarget(graph: List[List[int]]):

    dfs = DFS(graph)
    paths = (dfs.run(0))
    answer = []
    for p in paths:
        answer.append(list(reversed(p)))
    return answer



# graph = [[1,2],[3],[3],[]]

graph = [[4,3,1],[3,2,4],[3],[4],[]]

# graph = [[1],[]]

# graph = [[1,2,3],[2],[3],[]]
#
# graph = [[1,3],[2],[3],[]]
#
# graph = [[1,2],[3],[3],[]]

print(allPathsSourceTarget(graph))



