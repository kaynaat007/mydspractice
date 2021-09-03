from typing import List
from collections import deque
import math



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


class BFS:


    def __init__(self, graph):

        self.graph = graph
        self.vertices = len(self.graph)
        self.distances = [math.inf] * self.vertices
        self.pie = [-1] * self.vertices
        self.WHITE = 0
        self.GRAY = 1
        self.BLACK = 2
        self.color = [self.WHITE] * self.vertices
        self.cc = [0] * self.vertices

    def run(self, source, k):

        self.distances[source] = 0
        self.pie[source] = -1
        self.color[source] = self.GRAY
        self.cc[source] = k

        q = deque([source])
        while q:
            v = q.popleft()
            for i in range(self.vertices):
                if self.graph[v][i] == 1 and self.color[i] == self.WHITE:
                    self.color[i] = self.GRAY
                    self.distances[i] = self.distances[v] + 1
                    self.pie[i] = v
                    q.append(i)
            self.color[v] = self.BLACK
            self.cc[v] = k

    def main(self):

        k = 1
        for i in range(self.vertices):
            if self.color[i] == self.WHITE:
                self.run(i, k)
                k = k + 1

    def print(self):

        print('connected components', self.cc)
        print('distances', self.distances)
        print('color', self.color)
        print('parent', self.pie)


class UnionFind:
    """
    Union in O(1)
    Find in O(log(n))
    """

    def __init__(self, n):

        self.count = n
        self.n = n
        self.tree = []
        self.size = []
        for i in range(self.n):
            self.tree.append(i)
            self.size.append(1)

    def find_root(self, index):

        root = index
        while self.tree[index] != index:
            root = self.tree[index]
            index = root
        return root

    def find(self, index):

        root = self.find_root(index)

        while self.tree[index] != index: # another loop for path compression
            parent = self.tree[index]
            self.tree[index] = root
            index = parent

        return root

    def union(self, index1, index2):

        root1 = self.find(index1)
        root2 = self.find(index2)

        if self.size[index1] < self.size[index2]:
            self.tree[root1] = root2
            self.size[root2] += self.size[root1]
        else:
            self.tree[root2] = root1
            self.size[root1] += self.size[root2]

        self.count -= 1

    def components(self):
        components = set()
        for i in range(self.n):
            components.add(self.find(i))
        return components


def findCircleNum( M: List[List[int]]) -> int:
    """
    Union
    """
    n = len(M)
    u = UnionFind(n)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if i < j and M[i][j] == 1:
                u.union(i, j)
    return len(u.components())




M =  [[1,1,0],
 [1,1,0],
 [0,0,1]]

# M = [[1,1,0],
#  [1,1,1],
#  [0,1,1]]

# M  =  [[1,1,1],[1,1,1],[1,1,1]]

#
#
# M = [[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
#      [0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],
#      [0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],[1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],
#      [0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],[0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],
#      [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]]


def findCircleNumDFS( M: List[List[int]]) -> int:
    """
    Union
    """
    dfs = DFS(M)
    dfs.main()
    return max(dfs.cc)


def findCircleNumBFS( M: List[List[int]]) -> int:
    """
    Union
    """
    bfs = BFS(M)
    bfs.main()
    return max(bfs.cc)


# print(findCircleNumDFS(M))

# print(findCircleNum(M))
#
# dfs = DFS(M)
# dfs.main()
# dfs.print()
#

# bfs = BFS(M)
# bfs.main()
# bfs.print()


print(findCircleNumBFS(M))






