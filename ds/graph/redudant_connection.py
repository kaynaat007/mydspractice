from collections import defaultdict
from typing import List


class DFS:
    # find a cycle in undirected graph and processing cycle to return
    # an edge of highest weight. weight of the edge in this case is just index number of the edge
    # in the given input array.

    def __init__(self, graph, edges):
        self.graph = graph
        self.n = len(self.graph)
        self.visited = [0] * (self.n + 1)
        self.parent = [-1] * (self.n + 1)
        self.edges = edges
        self.ans = None
        self.lock = True  # on finding a cycle, we do not reprocess it further.

    def print(self):
        print('graph', self.graph)
        print('edges', self.edges)
        print('parent', self.parent)

    def run(self, v):

        self.visited[v] = 1

        for w in self.graph[v]:
            if self.visited[w] == 0:
                self.parent[w] = v
                self.run(w)
            else:
                if self.lock and self.parent[v] != -1 and self.parent[v] != w and (v, w) in self.edges:
                    cycle_start = w
                    # print('cycle found. cycle is starting at vertex ', cycle_start)
                    max_weight = self.edges[(v, w)]
                    self.ans = (v, w)
                    while self.parent[v] != -1 and self.parent[v] != cycle_start:
                        w = self.parent[v]
                        weight = self.edges[(v, w)]
                        if weight > max_weight:
                            self.ans = (v, w)
                            max_weight = weight
                        v = w
                    if self.edges[(v, cycle_start)] > max_weight:
                        self.ans = (v, cycle_start)
                    self.lock = False


def findRedundantConnection(edges: List[List[int]]):

     graph = defaultdict(list)
     weight_function = {}
     for i, e in enumerate(edges):
         u, v = e
         weight_function[(u, v)] = i
         weight_function[(v, u)] = i
         graph[u].append(v)
         graph[v].append(u)

     dfs  = DFS(graph, weight_function)
     dfs.print()
     dfs.run(1)
     if dfs.ans[0] > dfs.ans[1]:
         return [dfs.ans[1], dfs.ans[0]]
     return [dfs.ans[0], dfs.ans[1]]


def findRedundantConnectionV2(edges):
    tree = ''.join(map(chr, range(1001)))
    for u, v in edges:
        if tree[u] == tree[v]:
            return [u, v]
        tree = tree.replace(tree[u], tree[v])


class UnionFind:
    """
    Union find solution to detect a cycle and return the edge causing thr cycle in first place
    """

    def __init__(self, n):
        self.n = n
        self.components = [0] * self.n
        for i in range(n):
            self.components[i] = i

    def find(self, u):

        while self.components[u] != u:
            u = self.components[u]
        return u

    def union(self, u, v):

        root1 = self.find(u)
        root2 = self.find(v)

        if root1 != root2:
            self.components[root1] = root2
        else:
            if u < v:
                return [u, v]
            return [v, u]
        return None


# edges = [[1,2], [1,3], [2,3]]
edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]

# edges = [[3,4],[1,2],[2,4],[3,5],[2,5]]

# edges = [[1,3],[1,2],[2,5],[3,4],[2,4]]
# print(findRedundantConnection(edges))


# uf = UnionFind(5)
# uf.union(0, 1)
# uf.union(2, 3)
# uf.union(1, 2)
# print(uf.components)


def findRedundantConnectionUnionFind(edges):
    uf = UnionFind(2000)
    for u, v in edges:
        ans = uf.union(u, v)
        if ans:
            return ans

print(findRedundantConnectionUnionFind(edges))