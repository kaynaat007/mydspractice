

class DFS:

    def __init__(self, edges, n):

        self.edges = edges
        self.vertices = n
        self.visited = [0] * n

    def main(self):
        ans = []
        for u, v in self.edges:
            self.visited[v] = 1
        for i, v in enumerate(self.visited):
            if v == 0:
                ans.append(i)
        return ans


n = 6
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]


#
# n = 5
# edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]


#
n = 3
edges = [[1,2],[1,0],[0,2]]
#
# n = 5
# edges = [[1,3],[2,0],[2,3],[1,0],[4,1],[0,3]]

dfs = DFS(edges, n)
print(dfs.main())
