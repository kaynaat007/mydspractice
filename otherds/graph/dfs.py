"""
DFS on a directed graph produces

a DFS tree rooted at source vertex

back edges
cross edges
forward edge
tree edges

"""

class DFS:

    def __init__(self, graph):
        self.graph = graph
        self.vertices = len(self.graph)

        self.visited = [0] * self.vertices
        self.time = 0
        self.arr = [0] * self.vertices
        self.dep = [0] * self.vertices
        self.cc = [0] * self.vertices

    def run(self, v, k):

        self.time += 1
        self.arr[v] = self.time
        self.visited[v] = 1
        self.cc[v] = k

        for i in range(self.vertices):
            if self.graph[v][i] == 1:
                if self.visited[i] == 0:
                    self.run(i, k)
        self.time += 1
        self.dep[v] = self.time

    def main(self):

        k = 1
        for i in range(self.vertices):
            if self.visited[i] == 0:
                self.run(i, k)
                k = k + 1

    def print(self):

        print(self.cc)


M = [[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],
     [0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],[1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],
     [0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],[0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]]

dfs = DFS(M)
dfs.main()
dfs.print()
